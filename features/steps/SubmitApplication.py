import requests, psycopg2, configparser
from behave import *
from utilities.configuration import *
from utilities.resources import *
from utilities.dbConnection import *
from testData.payLoad import *



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
def step_impl(context, statusCode):
    print(context.response.status_code)
    assert context.response.status_code == statusCode


@then('response is having "{param}" as "{actual_value}"')
def step_impl(context, param, actual_value):
    response_json = context.response.json()
    print(response_json)
    context.buid = response_json['meta']['bright_uid']
    print(context.buid)
    expected_value = response_json['data'][param]
    print(expected_value)
    assert expected_value == actual_value, f"Assertion failed: {expected_value} != {actual_value}"


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
                cur.execute("SELECT * FROM lsp_applicationhistory WHERE application_id = %s ORDER BY modified_on",(application_id),)   
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