import requests
from behave import *
from payLoad import *
from expectedResponse import *
from utilities.resources import *
from utilities.configurations import *
from usm import *
import psycopg2, random



@given('the payLoad required for "{APIaction}"')
def step_impl(context,APIaction):
    context.headers = {"Content-Type": "application/json"}

    if APIaction == "Submit":
        context.url = getConfig()[env]['endpoint'] + ApiResources.submitApplication
        context.payLoad = submitAppPayLoad()
    elif APIaction == "Create":
        context.url = getConfig()[env]['endpoint'] + ApiResources.createAccount
        context.payLoad = createAccPayLoad()
    elif APIaction == "Activate":
        context.url = getConfig()[env]['endpoint'] + ApiResources.activateCard
        context.payLoad = activateCardPayLoad()
    elif APIaction == "Block":
        context.url = getConfig()[env]['endpoint'] + ApiResources.blockCard  
        context.payLoad = blockCardPayLoad()     

    


@when('PostAPI method is executed for "{APIaction}"')
def step_impl(context, APIaction):
    context.response = requests.post(context.url, json=context.payLoad , headers=context.headers, )
    print("POST is executed for "+APIaction)


@then('status code of response should be {statusCode:d}')
def step_impl(context,statusCode):
    print(context.response.status_code)
    assert context.response.status_code == statusCode


@then('response is having "{param}" as "{value}"')
def step_impl(context, param, value):
    #assert context.response == submitResponse()    
    #print(context.response.json())
    response_json = context.response.json()
    print("Print")
    context.buid = response_json['meta']['bright_uid']
    print(context.buid)
    assert response_json['data'][param] == value

@then('row is created in subsequent tables with application_type as "{app_value}"')
def step_impl(context, app_value):
    data = {}
    try :   
        conn = getConnection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM lsp_user WHERE bright_uid = %s;",(context.buid,))
        bright_user_id = cur.fetchone()
        if bright_user_id != None:                      
            cur.execute("SELECT * FROM lsp_application WHERE user_id = %s ORDER BY modified_on",(bright_user_id[0],))
            application_id = cur.fetchone()[0]    
            app_type_db = cur.fetchone()[6]
            if application_id != None:  
                cur.execute("SELECT * FROM lsp_applicationhistory WHERE application_id = %s ORDER BY created_on",(application_id),)   
                app_state_db = cur.fetchone()[4]             
        else:
            print(f'unable to fetch bright user id corresponding to {context.buid}')
        context.data = {
            'bright_user_id':bright_user_id[0],
            'application_id':application_id,
            #other field validation 
        }
        assert app_type_db == app_value
        assert app_state_db == "UNKNOWN"
        print(context.data)


        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
  
    




#For example
@given('the payLoad details with "{buids}" for "{APIaction}"')
def step_impl(context,buid,APIact):
    context.url = getConfig()['API']['endpoint'] + ApiResources.submitApplication
    context.headers = {"Content-Type": "application/json"}
    for buid in ApiResources.buids:
        context.payLoad = varSubmitPayload(buid, APIact)


@given('get_user_profile with "{PHONE_NUMBER}"')
def get_user_profile(context,PHONE_NUMBER):    
    data = {}
    try :   
        conn = getConnection()
        cur = conn.cursor()
        cur.execute("SELECT bright_user_id FROM bm_users_userprofile WHERE primary_phonenum = %s;",(PHONE_NUMBER,))
        bright_user_id = cur.fetchone()
        if bright_user_id != None:            
            cur.execute("SELECT id FROM bm_users_userstate WHERE user_id = %s;",(bright_user_id[0],))
            user_state_id = cur.fetchone()[0]                  
        else:
            print(f'unable to find bright user id corresponding to {PHONE_NUMBER}')
        context.data = {
            'bright_user_id':bright_user_id[0],
            'user_state_id':user_state_id
        }
        print(context.data)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return context.data

@then('response is "{data}"')
def step_impl(context,data):
    print(context.data)
    assert context.data.get('user_state_id') == data


@given('Eligible bright uid')
def step_impl(context):
    phone_num = "+19876543210"
    while(is_number_exist(phone_num)):
            phone_num = '+1' + str(random.randint(200, 999)) + str(random.randint(100, 999)) + str(random.randint(1000, 9999))
    usmurl = "https://gateway-dev.brightmoney.co/api/v1/users/usm/signin/"
    context.response = requests.post(usmurl, json=usm_SigninPayLoad(phone_num) , headers=context.headers, )



@given('the payload req for "{apiAction}" application')
def step_impl(context, apiAction):
     context.headers = {"Content-Type": "application/json"}
     if apiAction == "Submit":
        context.url = getConfig()[env]['endpoint'] + ApiResources.submitApplication
        context.payLoad = varSubmitPayload(context.buid)

@when('Post API is sent')
def step_impl(context, apiAction):
    pass



