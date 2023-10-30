def submitAppPayLoad(context, buid):
    body = {
        "meta": {
            "bm_request_id": "01c00add-2f6b-4ff5-a6b3-0f5240e7e9b9",
            "bm_session_id": "01c00add-2f6b-4ff5-a6b3-0f5240e7e9b9",
            "app_version": "123",
            "client_source": "akshat_local_host",
            "bright_uid": buid
        },
        "data": {
            "product": "CREDIT_CARD_SECURED_V1",
            "auth_signals": {
                "fingerprint": [],
                "authStatement": "I have reviewed the Bright line of credit agreement and, if approved, agree to the terms and conditions and the Bright credit line agreement. I authorize Bright to obtain my consumer report and understand my credit bureau file will show this as a hard inquiry."
            },
            "loan_version": "v1",
            "application_data": {
                "income": 58000,
                "questions": {
                    "occupation": "Retired"
                }
            }
        }
    }
    return body

def createAccPayLoad():
    body = {

    }
    return body

def activateCardPayLoad():
    body = {
        
    }
    return body

def blockCardPayLoad():
    body = {
        
    }
    return body