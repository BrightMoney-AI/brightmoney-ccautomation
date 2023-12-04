import requests, psycopg2, random
from behave import *
from utilities.configuration import *
from utilities.resources import *
from utilities.dbConnection import *
from testData.ApplicationPollpayLoad import *
from features.automationCode.usm import *
from testdata import *



@given('the payLoad required for poll "{APIaction}" with eligible buid')
def step_impl(context, APIaction):
    context.headers = {"Content-Type": "application/json"}

    if APIaction == "Poll":
        context.url = getConfig()[env]['endpoint'] + ApiResources.pollApplication
        context.buid = context.brightuid
        context.payLoad = pollAppPayLoad(context, context.buid , context.pid)            


@given('the payload req for "{Poll}" with wrong application id')
def step_impl_payload_with_complete_data(context,Poll):
    context.headers = {"Content-Type": "application/json"}
    context.url = getConfig()[env]['endpoint'] + ApiResources.pollApplication
    context.buid = context.brightuid
    context.payLoad = pollPayloadWithWrongPayload(context, context.buid)   


@given('the payload req for "{Poll}" with null application id')
def step_impl_payload_with_complete_data(context,Poll):
    context.headers = {"Content-Type": "application/json"}
    context.url = getConfig()[env]['endpoint'] + ApiResources.pollApplication
    context.buid = context.brightuid
    context.payLoad = pollPayloadWithNullPayload(context, context.buid)            


@given('the payload req for "{Poll}" with empty meta data')
def step_impl_payload_with_complete_data(context,Poll):
    context.headers = {"Content-Type": "application/json"}
    context.url = getConfig()[env]['endpoint'] + ApiResources.pollApplication
    context.buid = context.brightuid
    context.payLoad = pollPayloadWithEmptyMetaPayload(context, context.buid)       