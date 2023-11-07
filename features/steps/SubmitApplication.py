import requests, psycopg2, random
from behave import *
from utilities.configuration import *
from utilities.resources import *
from utilities.dbConnection import *
from testData.payLoad import *
from testData.dynamicPayLoad import *
from testData.SubmitApplicationpayLoad import *
from testData.ApplicationPollpayLoad import *
from testData.CreateAccountpayLoad  import *
from features.automationCode.usm import *
from testdata import *
import time


@given('the payLoad required for "{APIaction}"')
def step_impl(context,APIaction,test_data):
    context.headers = {"Content-Type": "application/json"}

    if APIaction == "Submit":
        context.url = getConfig()[env]['endpoint'] + ApiResources.submitApplication
        context.buid = generate_test_data_from_excel()[test_data][0]['buid']
        print(context.buid)
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
    elif APIaction=="Poll":
         context.url = getConfig()[env]['endpoint'] + ApiResources.pollApplication
         context.buid = context.brightuid
         context.payLoad = pollAppPayLoad(context,context.buid)
    elif APIaction == "Create":
        context.buid = context.brightuid
        context.url = getConfig()[env]['endpoint'] + ApiResources.createAccount
        context.payLoad = createAccountpayLoad(context,context.buid)
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
    context.pid = response_json['data']['application']['pid']
    print(context.pid + " pid")
    assert expected_value == actual_value, f"Assertion failed: {expected_value} != {actual_value}"

@then('Poll response is having "{param}" as "{actual_value}"')
def step_impl(context, param, actual_value):
    time.sleep(60)
    response_json = context.response.json()
    print(response_json)
    context.poll_buid = response_json['meta']['bright_uid']
    print("Bright uid from response of Poll Application: " + context.poll_buid)
    expected_value = response_json['data']['application'][param]
    context.pid = response_json['data']['application']['pid']
    print(context.pid + " pid")
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



@then('row is created in subsequent tables in DB "{db_name}" with application_state as "{app_value}"')
def step_impl(context, db_name, app_value):
    data = {}
    try :   
        conn = getConnection(db_name)
        cur = conn.cursor()
        
        cur.execute("SELECT * FROM lsp_user WHERE bright_uid = %s", context.buid)
        bright_user_id = cur.fetchone()
        if bright_user_id != None:                      
            cur.execute("SELECT * FROM lsp_application WHERE user_id = %s ORDER BY modified_on", bright_user_id[0])
            application_id = cur.fetchone()[0]    
            app_type_db = cur.fetchone()[6]
            if application_id != None:  
                cur.execute("SELECT * FROM lsp_applicationhistory WHERE application_id = %s ORDER BY modified_on", application_id)   
                app_state_db = cur.fetchone()[5]             
        else:
            print(f'unable to fetch bright user id corresponding to {context.buid}')
        context.data = {
            'bright_user_id':bright_user_id[0],
            'application_id':application_id,
            #other field validation 
        }
        assert app_type_db == app_value
        print(context.data)


        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

@then('row is created in subsequent tables in DB "{db_name}" with account_state as "{app_value}"')
def step_impl(context, db_name, app_value):
    data = {}
    try :   
        conn = getConnection(db_name)
        cur = conn.cursor()
        
        cur.execute("SELECT * FROM lsp_user WHERE bright_uid = %s", context.buid)
        bright_user_id = cur.fetchone()
        if bright_user_id != None:                      
            cur.execute("SELECT * FROM lsp_application WHERE user_id = %s ORDER BY modified_on", bright_user_id[0])
            application_id = cur.fetchone()[0]    
            app_type_db = cur.fetchone()[6]
            if application_id != None:  
                cur.execute("SELECT * FROM lsp_application WHERE application_id = %s ORDER BY modified_on", application_id)   
                app_state_db = cur.fetchone()[5]    

        else:
            print(f'unable to fetch bright user id corresponding to {context.buid}')
        context.data = {
            'bright_user_id':bright_user_id[0],
            'application_id':application_id,
            #other field validation 
        }
        assert app_type_db == app_value
        print(context.data)


        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()            

@then('row is created in subsequent tables in DB "{db_name}" with card_state as "{app_value}"')
def step_impl(context, db_name, app_value):
    data = {}
    try :   
        conn = getConnection(db_name)
        cur = conn.cursor()
        
        cur.execute("SELECT * FROM lsp_user WHERE bright_uid = %s", context.buid)
        bright_user_id = cur.fetchone()
        if bright_user_id != None:                      
            cur.execute("SELECT * FROM lsp_application WHERE user_id = %s ORDER BY modified_on", bright_user_id[0])
            application_id = cur.fetchone()[0]    
            app_type_db = cur.fetchone()[6]
            if application_id != None:  
                cur.execute("SELECT * FROM lsp_application WHERE application_id = %s ORDER BY modified_on", application_id)   
                app_state_db = cur.fetchone()[5]
                acc_id=cur.fetchone()[0]
                if  acc_id!=None:
                    cur.execute("SELECT * FROM lsp_card WHERE account_id = %s ORDER BY modified_on", acc_id) 
                    card_state = cur.fetchone()[10]


        else:
            print(f'unable to fetch bright user id corresponding to {context.buid}')
        context.data = {
            'bright_user_id':bright_user_id[0],
            'application_id':application_id,
            #other field validation 
        }
        assert card_state == app_value
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







# @then('response is having "{param}" as "{value}"')
# def step_impl(context, param, value):
#     #assert context.response == submitResponse()
#     #print(context.response.json())
#     response_json = context.response.json()
#     print("Print")
#     context.buid = response_json['meta']['bright_uid']
#     print(context.buid)
#     assert response_json['data'][param] == value


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
# @given('the payLoad details with "{buids}" for "{APIaction}"')
# def step_impl(context,buid,APIact):
#     context.url = getConfig()['API']['endpoint'] + ApiResources.submitApplication
#     context.headers = {"Content-Type": "application/json"}
#     for buid in ApiResources.buids:
#         context.payLoad = varSubmitPayload(buid, APIact)

        
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
    context.conn = getConnection("usm")
    context.cur = context.conn.cursor()
    while(is_number_exist(context , phone_num)):
            phone_num = '+1' + str(random.randint(200, 999)) + str(random.randint(100, 999)) + str(random.randint(1000, 9999))
    usmurl = "https://gateway-dev.brightmoney.co/api/v1/users/usm/signin/"
    usmheaders = {"Content-Type": "application/json"}
  
    context.response = requests.post(usmurl, json=usm_SigninPayLoad(phone_num) , headers=usmheaders)
# @given('the payload req for "{apiAction}" application')



@when('Post API is sent')
def step_impl(context, apiAction):
    pass



@given('the payload req for "{Submit}" with a missing required field')
def step_impl_payload_with_complete_data(context,Submit):
    context.headers = {"Content-Type": "application/json"}
    context.url = getConfig()[env]['endpoint'] + ApiResources.submitApplication
    context.buid = context.brightuid
    context.payLoad = submitAppMissingPayLoad(context, context.buid)   




@given('the payload req for "{Submit}" application with an Missing loan version')
def step_impl_payload_with_incorrect_data(context,Submit):
    context.headers = {"Content-Type": "application/json"}
    context.url = getConfig()[env]['endpoint'] + ApiResources.submitApplication
    context.buid = context.brightuid
    context.payLoad = submitAppIncorrectLoanVersionPayLoad(context, context.buid)   

@given('the payload req for "{Submit}" application with a large income value')
def step_impl_payload_with_large_data(context,Submit):
    context.headers = {"Content-Type": "application/json"}
    context.url = getConfig()[env]['endpoint'] + ApiResources.submitApplication
    context.buid = context.brightuid
    context.payLoad = submitAppPayLoadWithLargeIncome(context, context.buid)         

@given('the payload req for "{Submit}" application with missing meta information')
def step_impl_payload_with_missing_meta_data(context,Submit):
    context.headers = {"Content-Type": "application/json"}
    context.url = getConfig()[env]['endpoint'] + ApiResources.submitApplication
    context.buid = context.brightuid
    context.payLoad = submitAppPayLoadWithMissingMeta(context, context.buid)  

@given('the payload req for "{Submit}" application with missing application data')
def step_impl_payload_with_missing_meta_data(context,Submit):
    context.headers = {"Content-Type": "application/json"}
    context.url = getConfig()[env]['endpoint'] + ApiResources.submitApplication
    context.buid = context.brightuid
    context.payLoad = submitAppPayLoadWithmissingApplicationData(context, context.buid)  


@given('the payload req for "{Submit}" application with null values')
def step_impl_payload_with_missing_meta_data(context,Submit):
    context.headers = {"Content-Type": "application/json"}
    context.url = getConfig()[env]['endpoint'] + ApiResources.submitApplication
    context.buid = context.brightuid
    context.payLoad = submitAppPayLoadWithnullApplicationData(context, context.buid)  

@given('the payload req for "{Submit}" application with empty auth signals')
def step_impl_payload_with_missing_auth_data(context,Submit):
    context.headers = {"Content-Type": "application/json"}
    context.url = getConfig()[env]['endpoint'] + ApiResources.submitApplication
    context.buid = context.brightuid
    context.payLoad = submitAppPayLoadWithMissingAuthData(context, context.buid)  


@given('the payload req for "{Submit}" application with a large income value and complete data')
def step_impl_payload_with_large_data(context,Submit):
    context.headers = {"Content-Type": "application/json"}
    context.url = getConfig()[env]['endpoint'] + ApiResources.submitApplication
    context.buid = context.brightuid
    context.payLoad = submitAppPayLoadWithLargeIncome(context, context.buid)  

@given('the payload req for "{Submit}" application with an invalid product')
def step_impl_payload_with_large_data(context,Submit):
    context.headers = {"Content-Type": "application/json"}
    context.url = getConfig()[env]['endpoint'] + ApiResources.submitApplication
    context.buid = context.brightuid
    context.payLoad = submitAppPayLoadWithIncorrectProductData(context, context.buid)      


@given('the payload req for "{Submit}" application with missing income information')
def step_impl_payload_with_large_data(context,Submit):
    context.headers = {"Content-Type": "application/json"}
    context.url = getConfig()[env]['endpoint'] + ApiResources.submitApplication
    context.buid = context.brightuid
    context.payLoad = submitAppPayLoadWithMissingIncome(context, context.buid)   

@given('the payload req for "{Submit}" application with null loan version')
def step_impl_payload_with_large_data(context,Submit):
    context.headers = {"Content-Type": "application/json"}
    context.url = getConfig()[env]['endpoint'] + ApiResources.submitApplication
    context.buid = context.brightuid
    context.payLoad = submitAppPayLoadWithNullLoanVersion(context, context.buid)   

@then('the response status code should be 200')
def step_impl_check_response_status_200(context):
    assert context.response.status_code == 200


@then('the application state transitions from UNKNOWN to APPLICATION_RECEIVED to UNDERWRITING_IN_PROGRESS to APPROVED/DECLINED/REFERRED')
def step_impl_check_application_state_transitions(context):
    response_data = context.response.json()
    application_state = response_data['data']['application']['state']
    expected_states = ['UNKNOWN', 'APPLICATION_RECEIVED', 'UNDERWRITING_IN_PROGRESS', 'APPROVED', 'DECLINED', 'REFERRED']
    assert all(state in application_state for state in expected_states)


@then('the response status code should be 400')
def step_impl_check_response_status_400(context):
    assert context.response.status_code == 400



@then('the application state transitions from APPLICATION_RECEIVED to UNDERWRITING_IN_PROGRESS')
def step_impl_check_application_state_transitions_2(context):
    response_data = context.response.json()
    application_state = response_data['data']['application']['state']
    expected_states = ['APPLICATION_RECEIVED', 'UNDERWRITING_IN_PROGRESS']
    assert all(state in application_state for state in expected_states)


@then('the application state transitions from UNDERWRITING_IN_PROGRESS to APPROVED or DECLINED or REFERRED')
def step_impl_check_application_state_transitions_3(context):
    response_data = context.response.json()
    application_state = response_data['data']['application']['state']
    expected_states = ['UNDERWRITING_IN_PROGRESS', 'APPROVED', 'DECLINED', 'REFERRED']
    assert any(state in application_state for state in expected_states)


@then('the application state remains UNKNOWN')
def step_impl_check_application_state_unknown(context):
    response_data = context.response.json()
    application_state = response_data['data']['application']['state']
    assert application_state == 'UNKNOWN'


@then('the application state transitions to UNKNOWN')
def step_impl_check_application_state_transitions_unknown(context):
    response_data = context.response.json()
    application_state = response_data['data']['application']['state']
    assert application_state == 'UNKNOWN'


@then('the application state transitions from UNKNOWN to APPLICATION_RECEIVED to UNDERWRITING_IN_PROGRESS to APPROVED or DECLINED or REFERRED')
def step_impl_check_application_state_transitions_complete(context):
    response_data = context.response.json()
    application_state = response_data['data']['application']['state']
    expected_states = ['UNKNOWN', 'APPLICATION_RECEIVED', 'UNDERWRITING_IN_PROGRESS', 'APPROVED', 'DECLINED', 'REFERRED']
    assert any(state in application_state for state in expected_states)    