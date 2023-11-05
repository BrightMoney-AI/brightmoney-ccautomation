import json
null = None

def createAccountpayLoad(context,buid):
    response_json = context.response.json()
    context.pid = response_json['data']['application']['pid']
    body = {
        "meta": {
       "bm_request_id": "01c00add-2f6b-4ff5-a6b3-0f5240e7e9b9",
       "bm_session_id": "01c00add-2f6b-4ff5-a6b3-0f5240e7e9b9",
       "app_version": "123",
       "client_source": "asif_local_host",
       "bright_uid": buid
   },
        "data": {
            "auth_signals": {
                "fingerprint": [],
                "authStatement": "I have reviewed the Bright line of credit agreement and, if approved, agree to the terms and conditions and the Bright credit line agreement. I authorize Bright to obtain my consumer report and understand my credit bureau file will show this as a hard inquiry."
            },
            "loan_version": "v1",
            "application_pid": context.pid
        }

    }
    return body


