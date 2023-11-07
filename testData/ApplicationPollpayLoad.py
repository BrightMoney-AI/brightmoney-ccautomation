import json
null = None

def pollAppPayLoad(context,buid):
    response_json = context.response.json()
    context.pid = response_json['data']['application']['pid']
    body = {
        "meta": {
       "bm_request_id": "01c00add-2f6b-4ff5-a6b3-0f5240e7e9b9",
       "bm_session_id": "01c00add-2f6b-4ff5-a6b3-0f5240e7e9b9",
       "app_version": "123",
       "client_source": "akshat_local_host",
       "bright_uid": buid
   },
        "data": {
            "application_pid": context.pid
        }
    }
    return body


def pollPayloadWithWrongPayload(context,buid):
    response_json = context.response.json()
    context.pid = response_json['data']['application']['pid']
    body = {
        "meta": {
       "bm_request_id": "01c00add-2f6b-4ff5-a6b3-0f5240e7e9b9",
       "bm_session_id": "01c00add-2f6b-4ff5-a6b3-0f5240e7e9b9",
       "app_version": "123",
       "client_source": "akshat_local_host",
       "bright_uid": buid
   },
        "data": {
            "application_pid": context.pid + '7dgdh'
        }
    }
    return body

def pollPayloadWithNullPayload(context,buid):
    response_json = context.response.json()
    context.pid = response_json['data']['application']['pid']
    body = {
        "meta": {
       "bm_request_id": "01c00add-2f6b-4ff5-a6b3-0f5240e7e9b9",
       "bm_session_id": "01c00add-2f6b-4ff5-a6b3-0f5240e7e9b9",
       "app_version": "123",
       "client_source": "akshat_local_host",
       "bright_uid": buid
   },
        "data": {
            "application_pid": null
        }
    }
    return body


def pollPayloadWithEmptyMetaPayload(context,buid):
    response_json = context.response.json()
    context.pid = response_json['data']['application']['pid']
    body = {
        "meta": {
       
   },
        "data": {
            "application_pid": context.pid
        }
    }
    return body





    