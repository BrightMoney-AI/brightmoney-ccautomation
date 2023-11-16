import psycopg2, requests, random, allure
from behave import *
from utilities.configuration import *
from utilities.resources import *
from utilities.dbConnection import *
from testData.SubmitApplicationpayLoad import *
from testData.usmPayLoad import *



def getEligibleBrightUID(context):
    try:
        phone_num = "+19876543210"
        context.conn = getConnection("usm")
        context.cur = context.conn.cursor()
        while(is_number_exist(context, phone_num)):
                phone_num = '+1' + str(random.randint(200, 999)) + str(random.randint(100, 999)) + str(random.randint(1000, 9999))
        
        usmurl = "https://gateway-dev.brightmoney.co/api/v1/users/usm/signin/"
        usmheaders = {"Content-Type": "application/json"}
        add_allure_step("Adding Phone Number: " + str(phone_num))
        context.usmresponse = requests.post(usmurl, json = usm_SigninPayLoad(phone_num) , headers = usmheaders, )
        add_allure_step("USM Response code: "+ str(context.usmresponse.status_code))
        if context.usmresponse.status_code == 200:
            context.brightuid = get_bright_uid(context, phone_num)
            add_allure_step("Bright uid got through Phone Number: " + str(context.brightuid))
        else:
            allure.attach("USM endpoint returns: "+ str(context.usmresponse.status_code) + ", Not 200", allure.attachment_type.TEXT)
        if context.conn is not None:
            context.conn.close()       
    except (Exception, psycopg2.DatabaseError) as error:
        add_allure_step(str(error))
    finally:
        if context.conn is not None:
            context.conn.close()
    

#for definition
def is_number_exist(context, PHONE_NUMBER):
    try :         
        context.cur.execute("SELECT bright_user_id FROM bm_users_userprofile WHERE primary_phonenum = %s;",(str(PHONE_NUMBER),))
        bright_user_id = context.cur.fetchone() 
        add_allure_step("Bright user id is  = " + str(bright_user_id))
        if bright_user_id != None:            
            return True                
        else:
            return False       
    except (Exception, psycopg2.DatabaseError) as error:
        add_allure_step(str(error))
    return False

def get_bright_uid(context, PHONE_NUMBER):
    try :   
        context.cur.execute("SELECT bright_user_id FROM bm_users_userprofile WHERE primary_phonenum = %s;",(str(PHONE_NUMBER),))
        bright_user_id = context.cur.fetchone()[0]       
        if bright_user_id != None:            
            context.cur.execute("SELECT bright_uid FROM bm_users_brightuser WHERE id =%s;",(str(bright_user_id),))          
            bright_uid = context.cur.fetchone()[0]
            return bright_uid
        else:
            return False               
    except (Exception, psycopg2.DatabaseError) as error:
        add_allure_step(str(error))
    return False

