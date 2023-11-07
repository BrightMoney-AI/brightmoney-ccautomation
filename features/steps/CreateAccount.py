
import requests, psycopg2, random
from behave import *
from utilities.configuration import *
from utilities.resources import *
from utilities.dbConnection import *
from testData.SubmitApplicationpayLoad import *
from testData.ApplicationPollpayLoad import *
from testData.CreateAccountpayLoad  import *
from features.automationCode.usm import *
from testdata import *
import time



@given('the payload req with empty pid with rest same')
def step_impl_payload_with_complete_data(context):
    context.headers = {"Content-Type": "application/json"}
    context.url = getConfig()[env]['endpoint'] + ApiResources.createAccount
    context.buid = context.brightuid
    context.payLoad = createpayLoadWithEmptyPid(context, context.buid)


@given('the payload req with empty auth signal with rest same')
def step_impl_payload_with_complete_data(context):
    context.headers = {"Content-Type": "application/json"}
    context.url = getConfig()[env]['endpoint'] + ApiResources.createAccount
    context.buid = context.brightuid
    context.payLoad = createpayLoadWithEmptyAuthSignal(context, context.buid)  


@given('the payload req with empty bright uid with rest same')
def step_impl_payload_with_complete_data(context):
    context.headers = {"Content-Type": "application/json"}
    context.url = getConfig()[env]['endpoint'] + ApiResources.createAccount
    context.buid = context.brightuid
    context.payLoad = createpayLoadWithEmptyBuid(context, context.buid) 

@given('the payload req with empty meta data with rest same')
def step_impl_payload_with_complete_data(context):
    context.headers = {"Content-Type": "application/json"}
    context.url = getConfig()[env]['endpoint'] + ApiResources.createAccount
    context.buid = context.brightuid
    context.payLoad = createpayLoadWithEmptyMeta(context, context.buid) 
