import requests, psycopg2, random
from behave import *
from utilities.configuration import *
from utilities.resources import *
from utilities.dbConnection import *
from testData.payLoad import *
from testData.dynamicPayLoad import *
from features.automationCode.usm import *



@given('the payLoad required for "{APIaction}"')
def step_impl(context,APIaction):
    context.headers = {"Content-Type": "application/json"}

    if APIaction == "Submit":
        context.url = getConfig()[env]['endpoint'] + ApiResources.submitApplication
        context.buid = "f16800c5-7539-4617-900c-cff64e44e2f6"
        context.payLoad = submitAppPayLoad(context, context.buid)     
    elif APIaction == "Create":
        context.url = getConfig()[env]['endpoint'] + ApiResources.createAccount
        context.payLoad = createAccPayLoad()
    elif APIaction == "Activate":
        context.url = getConfig()[env]['endpoint'] + ApiResources.activateCard
        context.payLoad = activateCardPayLoad()
    elif APIaction == "Block":
        context.url = getConfig()[env]['endpoint'] + ApiResources.blockCard  
        context.payLoad = blockCardPayLoad()     


@given('the payLoad required for "{APIaction}" with eligible buid')
def step_impl(context, APIaction):
    context.headers = {"Content-Type": "application/json"}

    if APIaction == "Submit":
        context.url = getConfig()[env]['endpoint'] + ApiResources.submitApplication
        context.buid = context.brightuid
        context.payLoad = submitAppPayLoad(context, context.buid)     
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
    #print("POST is executed for "+APIaction)


@when('PostAPI method is executed for "{APIaction}" with dynamic data')
def step_impl(context, APIaction):
    context.headers = {"Content-Type": "application/json"}
    context.url = getConfig()[env]['endpoint'] + ApiResources.submitApplication
    context.payLoad = submitAppDynamicPayLoad(context, context.buid)
    context.response = requests.post(context.url, json=context.payLoad , headers=context.headers, )
    #print("POST is executed for "+APIaction)

@then('status code of response should be {statusCode:d}')
def step_impl(context, statusCode):
    print(context.response.status_code)
    assert context.response.status_code == statusCode


@then('response is having "{param}" as "{actual_value}"')
def step_impl(context, param, actual_value):
    response_json = context.response.json()
    print(response_json)
    context.submit_buid = response_json['meta']['bright_uid']
    print("Bright uid from response of Submit Application: " + context.submit_buid)
    expected_value = response_json['data']['application'][param]
    print(expected_value)
    assert expected_value == actual_value, f"Assertion failed: {expected_value} != {actual_value}"


@then('row is created in subsequent tables in DB "{db_name}" with application_type as "{app_value}"')
def step_impl(context, db_name, app_value):
    data = {}
    try :   
        conn = getConnection(db_name)
        cur = conn.cursor()
        #cur.execute("UPDATE credit_eligibilitydata SET bright_uid = %s WHERE pid = f3b68ab3-4afa-4ade-be93-b2bcd9c347c7", context.buid)
        
        cur.execute("SELECT * FROM lsp_user WHERE bright_uid = %s", context.buid)
        bright_user_id = cur.fetchone()
        if bright_user_id != None:                      
            cur.execute("SELECT * FROM lsp_application WHERE user_id = %s ORDER BY modified_on", bright_user_id[0])
            application_id = cur.fetchone()[0]    
            app_type_db = cur.fetchone()[6]
            if application_id != None:  
                cur.execute("SELECT * FROM lsp_applicationhistory WHERE application_id = %s ORDER BY modified_on", application_id)   
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


@given('User have eligible bright uid')
def step_impl(context):
    getEligibleBrightUID(context)