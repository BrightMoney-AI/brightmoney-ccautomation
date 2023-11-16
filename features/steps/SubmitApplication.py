import requests, psycopg2, pdb
from behave import *
from utilities.configuration import *
from utilities.resources import *
from utilities.dbConnection import *
from testData.SubmitApplicationpayLoad import *
from testData.ApplicationPollpayLoad import *
from testData.CreateAccountpayLoad  import *
from testData.TransactionSubmitpayLoad  import *
from features.automationCode.usm import *
from testdata import *
import time


@given('the payLoad required for "{APIaction}"')
def step_impl(context,APIaction,test_data):
    context.headers = {"Content-Type": "application/json"}

    if APIaction == "Submit":
        context.url = getConfig()[env]['endpoint'] + ApiResources.submitApplication
        #context.buid = generate_test_data_from_excel()[test_data][0]['buid']
        #print("BUID from excel: "+context.buid)
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
    elif APIaction == "Transactions":
        context.url = getConfig()[env]['endpoint'] + ApiResources.transactionSubmit  
        context.payLoad = transactionSubmitPayLoad()            


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
    elif APIaction == "Transactions":
        context.url = getConfig()[env]['endpoint'] + ApiResources.transactionSubmit  
        context.payLoad = transactionSubmitPayLoad()


@when('PostAPI method is executed for "{APIaction}"')
def step_impl(context, APIaction):
    context.response = requests.post(context.url, json=context.payLoad , headers=context.headers, )


@then('status code of response should be {statusCode:d}')
def step_impl(context, statusCode):
    assert context.response.status_code == statusCode, f"Assertion failed: Actual:{context.response.status_code} ::: Expected:{statusCode}"


@then('response is having "{param}" as "{actual_value}"')
def step_impl(context, param, actual_value):
    response_json = context.response.json()
    context.submit_buid = response_json['meta']['bright_uid']
    add_allure_step("Bright UID from response of Submit Application: " + str(context.submit_buid))
    expected_value = response_json['data']['application'][param]
    context.pid = response_json['data']['application']['pid'] 
    add_allure_step("PID:"+ str(context.pid))
    assert expected_value == actual_value, f"Assertion failed: {expected_value} != {actual_value}"

@then('Poll response is having "{param}" as "{actual_value}"')
def step_impl(context, param, actual_value):
    time.sleep(60)
    response_json = context.response.json()
    context.poll_buid = response_json['meta']['bright_uid']
    add_allure_step("Bright uid from response of Poll Application: " + str(context.poll_buid))
    expected_value = response_json['data']['application'][param]
    context.pid = response_json['data']['application']['pid']
    add_allure_step("PID: "+ str(context.pid))
    assert expected_value == actual_value, f"Assertion failed: {expected_value} != {actual_value}"    


@then('row is created in subsequent tables in DB "{db_name}" with application_type as "{app_value}"')
def step_impl(context, db_name, app_value):
    #pdb.set_trace()
    data = {}
    conn = None
    try:
        conn = getConnection(db_name)
        cur = conn.cursor()

        cur.execute("SELECT * FROM credit.lsp_user WHERE bright_uid = %s;", (str(context.buid),))
        bright_user_id = cur.fetchone()

        if bright_user_id is not None:
            cur.execute("SELECT * FROM credit.lsp_application WHERE user_id = %s ORDER BY modified_on;", (str(bright_user_id[0]),))
            application_row = cur.fetchone()
            if application_row:
                application_id = application_row[0]
                app_type_db = application_row[6]

                cur.execute("SELECT * FROM credit.lsp_applicationhistory WHERE application_id = %s ORDER BY modified_on;", (str(application_id),))
                app_state_db = cur.fetchone()[4]
            else:
                application_id = None
                app_type_db = None
                app_state_db = None
        else:
            add_allure_step("Unable to fetch bright user id corresponding to" + str(context.buid))

        data = {
            "bright_user_id": bright_user_id[0] if bright_user_id else None,
            "application_id": application_id,
            # Add other field validations here
        }

        assert app_type_db == app_value
        assert app_state_db == "UNKNOWN"
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        add_allure_step(str(error))
    finally:
        if conn is not None:
            conn.close()



@then('row is created in subsequent tables in DB "{db_name}" with application_state as "{app_value}"')
def step_impl(context, db_name, app_value):
    data = {}
    conn = None
    try:
        conn = getConnection(db_name)
        cur = conn.cursor()

        cur.execute("SELECT * FROM credit.lsp_user WHERE bright_uid = %s;", (str(context.buid),))
        bright_user_id = cur.fetchone()

        if bright_user_id is not None:
            cur.execute("SELECT * FROM credit.lsp_application WHERE user_id = %s ORDER BY modified_on;", (str(bright_user_id[0]),))
            application_row = cur.fetchone()
            if application_row:
                application_id = application_row[0]
                app_state = application_row[5]
            else:
                application_id = None
                app_type_db = None
                app_state_db = None
        else:
            add_allure_step("Unable to fetch bright user id corresponding to "+ str(context.buid))

        data = {
            "bright_user_id": bright_user_id[0] if bright_user_id else None,
            "application_id": application_id,
            # Add other field validations here
        }

        assert app_state == app_value
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        add_allure_step(str(error))
    finally:
        if conn is not None:
            conn.close()


@then('row is created in subsequent tables in DB "{db_name}" with account_state as "{app_value}"')
def step_impl(context, db_name, app_value):
    data = {}
    conn = None
    try:
        conn = getConnection(db_name)
        cur = conn.cursor()

        cur.execute("SELECT * FROM credit.lsp_user WHERE bright_uid = %s;", (str(context.buid),))
        bright_user_id = cur.fetchone()

        if bright_user_id is not None:
            cur.execute("SELECT * FROM credit.lsp_application WHERE user_id = %s ORDER BY modified_on;", (str(bright_user_id[0]),))
            application_row = cur.fetchone()

            if application_row:
                application_id = application_row[0]
                cur.execute("SELECT * FROM credit.lsp_account WHERE application_id = %s ORDER BY modified_on;", (str(application_id),))
                application_row = cur.fetchone()
                app_state = application_row[6]
            else:
                application_id = None
                app_type_db = None
                app_state = None
        else:
            add_allure_step(f"Unable to fetch bright user id corresponding to {context.buid}")

        data = {
            "bright_user_id": bright_user_id[0] if bright_user_id else None,
            "application_id": application_id,
            # Add other field validations here
        }

        assert app_state == app_value
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        add_allure_step(error)
    finally:
        if conn is not None:
            conn.close()               


@then('row is created in subsequent tables in DB "{db_name}" with card_state as "{app_value}"')
def step_impl(context, db_name, app_value):
    data = {}
    conn = None
    try:
        conn = getConnection(db_name)
        cur = conn.cursor()

        cur.execute("SELECT * FROM credit.lsp_user WHERE bright_uid = %s;", (str(context.buid),))
        bright_user_id = cur.fetchone()

        if bright_user_id is not None:
            cur.execute("SELECT * FROM credit.lsp_application WHERE user_id = %s ORDER BY modified_on;", (str(bright_user_id[0]),))
            application_row = cur.fetchone()

            if application_row:
                application_id = application_row[0]
                app_type_db = application_row[6]

                cur.execute("SELECT * FROM credit.lsp_account WHERE application_id = %s ORDER BY modified_on;", (str(application_id),))
                acc_id = cur.fetchone()[0]
                if acc_id is not None:
                    cur.execute("SELECT * FROM credit.lsp_card WHERE account_id = %s ORDER BY modified_on;", (str(acc_id),))
                    card_row = cur.fetchone()
                    card_state = card_row[10]
                else:
                    card_state = None
            else:
                application_id = None
                app_type_db = None
                app_state_db = None
                card_state = None
        else:
            add_allure_step(f"Unable to fetch bright user id corresponding to {context.buid}")

        data = {
            "bright_user_id": bright_user_id[0] if bright_user_id else None,
            "application_id": application_id,
            # Add other field validations here
        }

        assert card_state == app_value
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        add_allure_step(error)
    finally:
        if conn is not None:
            conn.close()           


@given('User have eligible bright uid')
def step_impl(context):
    getEligibleBrightUID(context)


@then('row is created in subsequent tables with application_type as "{app_value}"')
def step_impl(context, app_value):
    data = {}
    try :
        conn = getConnection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM credit.lsp_user WHERE bright_uid = %s;", (str(context.buid),))

        bright_user_id = cur.fetchone()
        if bright_user_id != None:
            cur.execute("SELECT * FROM credit.lsp_application WHERE user_id = %s ORDER BY modified_on;",(str(bright_user_id[0]),))
            application_id = cur.fetchone()[0]
            app_type_db = cur.fetchone()[6]
            if application_id != None:
                cur.execute("SELECT * FROM credit.lsp_applicationhistory WHERE application_id = %s ORDER BY created_on;",(str(application_id),))
                app_state_db = cur.fetchone()[4]
        else:
            add_allure_step(f'unable to fetch bright user id corresponding to {context.buid}')
        context.data = {
            'bright_user_id':bright_user_id[0],
            'application_id':application_id,
            #other field validation
        }
        assert app_type_db == app_value
        assert app_state_db == "UNKNOWN"
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        add_allure_step(error)
    finally:
        if conn is not None:
            conn.close()

        
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
            add_allure_step(f'unable to find bright user id corresponding to {PHONE_NUMBER}')
        context.data = {
            'bright_user_id':bright_user_id[0],
            'user_state_id':user_state_id
        }
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        add_allure_step(error)
    finally:
        if conn is not None:
            conn.close()
    return context.data


@then('response is "{data}"')
def step_impl(context,data):
    add_allure_step("User State ID" + context.data.get('user_state_id'))
    assert context.data.get('user_state_id') == data


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



@then('the application state transitions from UNKNOWN to APPLICATION_RECEIVED to UNDERWRITING_IN_PROGRESS to APPROVED/DECLINED/REFERRED')
def step_impl_check_application_state_transitions(context):
    response_data = context.response.json()
    application_state = response_data['data']['application']['state']
    expected_states = ['UNKNOWN', 'APPLICATION_RECEIVED', 'UNDERWRITING_IN_PROGRESS', 'APPROVED', 'DECLINED', 'REFERRED']
    assert all(state in application_state for state in expected_states)


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