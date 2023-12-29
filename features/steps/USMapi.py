import requests, psycopg2, pdb
from behave import *
from utilities.configuration import *
from utilities.resources import *
from utilities.dbConnection import *
# from testData.payLoad import *
from testData.dynamicPayLoad import *
from testData.SubmitApplicationpayLoad import *
from testData.ApplicationPollpayLoad import *
from testData.CreateAccountpayLoad  import *
from testData.TransactionSubmitpayLoad  import *
from testData.SecurityDepositpayLoad  import *
from features.automationCode.usm import *
from testdata import *
from testData.usmPayLoad import *
import time
import random


@given('payload required for signin API')
def step_impl(context):
    context.headers = {"Content-Type": "application/json"}

    context.url = getConfig()[env]['endpoint'] + ApiResources.usmSignIn
    context.phone_num = '+1'+str(random.randint(10000000000,100000000000))
    while(is_number_exist(context,context.phone_num)):
        context.phone_num = '+1'+str(random.randint(10000000000,100000000000))
    context.payLoad = usm_SigninPayLoad(context.phone_num)

@given('negative payload for signin API')
def step_impl(context):
    context.headers = {"Content-Type": "application/json"}
    context.url = getConfig()[env]['endpoint'] + ApiResources.usmSignIn
    context.phone_num = '+1'+str(random.randint(10000000000,100000000000))
    while(is_number_exist(context,context.phone_num)):
        context.phone_num = '+1'+str(random.randint(10000000000,100000000000))
    context.payLoad = usm_SigninPayLoadNegative(context.phone_num)


@when('postAPI method is executed')
def step_impl(context):
    context.response = requests.post(context.url, json=context.payLoad , headers=context.headers, )

@then('validate response code should be 200')
def step_impl(context):
    assert context.response.status_code == 200, f"Assertion failed: Actual:{context.response.status_code} ::: Expected:{200}"
    
@then('validate respone code should be 400')
def step_impl(context):
    assert context.response.status_code == 400, f"Assertion failed: Actual:{context.response.status_code} ::: Expected:{400}"

@then('access or refresh token or bright_uid is not null')
def step_impl(context):
    response_json = context.response.json()
    context.access = response_json['data']['action_data']['access']
    context.refresh = response_json['data']['action_data']['refresh']
    context.buid = response_json['data']['action_data']['bright_uid']
    assert context.access is not null
    assert context.refresh is not null
    assert context.buid is not null

@then('action name is correct')
def step_impl(context):
    response_json = context.response.json()
    context.action = response_json['data']['action']
    assert context.action == 'ENABLE_APP_PIN_ACTION', "Assertion failed"

@then('response contain event_name field')
def step_impl(context):
    response_json = context.response.json()
    context.emptyfield = response_json['data']['event_name']
    assert context.emptyfield is not null

@Given('payload for app pin enabel')
def step_impl(context):
    context.AppPinheaders = {"Content-Type": "application/json",
                       "Authorization":"Bearer "+context.access}
    context.AppPinurl = getConfig()[env]['endpoint'] + ApiResources.appPin
    context.AppPinpayLoad = usm_appPinPayload()

@when('app pin enable is hit')
def step_impl(context):
    context.AppPinresponse = requests.post(context.AppPinurl, json=context.AppPinpayLoad , headers=context.AppPinheaders, )

@given('previous API is hit in sequence')
def step_impl(context):

    context.phone_num = '+1'+str(random.randint(10000000000,100000000000))
    while(is_number_exist(context,context.phone_num)):
        context.phone_num = '+1'+str(random.randint(10000000000,100000000000))
    context.payLoad = usm_SigninPayLoad(context.phone_num)

    context.headers = {"Content-Type": "application/json"}
    context.url = getConfig()[env]['endpoint'] + ApiResources.usmSignIn
    context.response = requests.post(context.url, json=context.payLoad , headers=context.headers, )
    context.access = context.response.json()['data']['action_data']['access']

@Then('validate action name and pii data type')
def step_impl(context):
    assert context.AppPinresponse.json()['data']['action'] =='COLLECT_PII_ACTION'


