import psycopg2, requests, random, allure
from behave import *
from utilities.configuration import *
from utilities.resources import *
from utilities.dbConnection import *
from testData.SubmitApplicationpayLoad import *
from testData.usmPayLoad import *




def getEligibleBrightUID(context):
    try:
        conn = getConnection("test")
        cur = conn.cursor()
        query = 'SELECT * FROM "Usm_Automation" ORDER BY "created_at" DESC LIMIT 50'
        # cur.execute("SELECT BrightUid FROM Usm_Automation WHERE BrightUid = '68fa7bfa-1b4b-4fdb-8b7d-3d5fd2944e98' ORDER BY created_at DESC LIMIT 1;")
        cur.execute(query)
        context.brightuid  = cur.fetchone()[1]
        print("Bright uid got through USM: " + str(context.brightuid))
        add_allure_step("Bright uid got through Phone Number: " + str(context.brightuid))    
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error" + error)
        add_allure_step(str(error))   
    

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

