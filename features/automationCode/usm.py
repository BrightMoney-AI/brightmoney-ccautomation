import psycopg2, requests, random, allure
from behave import *
from utilities.configuration import *
from utilities.resources import *
from utilities.dbConnection import *
from testData.payLoad import *
from testData.usmPayLoad import *



#for steps
def getEligibleBrightUID(context):
    try:
        phone_num = "+19876543210"
        context.conn = getConnection("usm")
        context.cur = context.conn.cursor()
        while(is_number_exist(context, phone_num)):
                phone_num = '+1' + str(random.randint(200, 999)) + str(random.randint(100, 999)) + str(random.randint(1000, 9999))
        
        usmurl = "https://gateway-dev.brightmoney.co/api/v1/users/usm/signin/"
        usmheaders = {"Content-Type": "application/json"}
        with allure.step("Adding Phone Number"):
            print("Phone Num:" + phone_num)
            context.usmresponse = requests.post(usmurl, json = usm_SigninPayLoad(phone_num) , headers = usmheaders, )
        print("USM Response code: "+ str(context.usmresponse.status_code))
        if context.usmresponse.status_code == 200:
            context.brightuid = get_bright_uid(context, phone_num)
            print("Bright uid got through Phone Number: " + context.brightuid)
        else:
            with allure.step("Get bright uid from USM"):
                allure.attach("USM endpoint returns: "+ str(context.usmresponse.status_code) + ", Not 200", allure.attachment_type.TEXT)
        
        if context.conn is not None:
            context.conn.close()
    
        with allure.step("Updating credit_eligibilitydata to make buid eligible"):
            pid = "f3b68ab3-4afa-4ade-be93-b2bcd9c347c7"
            conn = getConnection("payments")
            cur = conn.cursor()
            cur.execute("UPDATE credit.credit_eligibilitydata SET bright_uid = %s WHERE pid = %s;", (context.brightuid, pid,))
            conn.close()
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if context.conn is not None:
            context.conn.close()
    

#for definition
def is_number_exist(context, PHONE_NUMBER):
    try :         
        context.cur.execute("SELECT bright_user_id FROM bm_users_userprofile WHERE primary_phonenum = %s;",(str(PHONE_NUMBER),))
        bright_user_id = context.cur.fetchone() 
        print("Bright user id is  = ",bright_user_id)
        if bright_user_id != None:            
            return True                
        else:
            return False       
        #cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    # finally:
    #     if conn is not None:
    #         conn.close()
    return False

def get_bright_uid(context, PHONE_NUMBER):
    try :       
        context.cur.execute("SELECT bright_user_id FROM bm_users_userprofile WHERE primary_phonenum = %s;",(str(PHONE_NUMBER),))
        bright_user_id = context.cur.fetchone()[0]       
        if bright_user_id != None:            
            context.cur.execute("SELECT bright_uid FROM bm_users_brightuser WHERE id =%s;",(str(bright_user_id),))          
            bright_uid = context.cur.fetchone()[0]
            print(type(bright_uid))
            return bright_uid
        else:
            return False       
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    # finally:
    #     if conn is not None:
    #         conn.close()
    return False

