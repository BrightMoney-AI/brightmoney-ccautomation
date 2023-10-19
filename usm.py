import psycopg2
from utilities.configurations import *



def is_number_exist(PHONE_NUMBER):
    try :   
        conn = getConnection()
        cur = conn.cursor()
        cur.execute("SELECT bright_user_id FROM bm_users_userprofile WHERE primary_phonenum = %s;",(str(PHONE_NUMBER),))
        bright_user_id = cur.fetchone() 
        print("Bright user id is  = ",bright_user_id[0])
        if bright_user_id != None:            
            return True                
        else:
            return False       
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return False

def get_bright_uid(PHONE_NUMBER):
    try :   
        conn = getConnection()
        print("hi")
        cur = conn.cursor()
        cur.execute("SELECT bright_user_id FROM bm_users_userprofile WHERE primary_phonenum = %s;",(str(PHONE_NUMBER),))
        bright_user_id = cur.fetchone()[0]
        # print(type(bright_user_id))
        if bright_user_id != None:            
            cur.execute("SELECT bright_uid FROM bm_users_brightuser WHERE id =%s;",(str(bright_user_id),))          
            bright_uid = cur.fetchone()[0]
            print(type(bright_uid))
            return bright_uid
        else:
            return False       
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return False