import requests
import json

def checkingConnect(phone_num):

    headers = {        
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Content-Length": ""
    }
    
    payload = {
        "meta": {
            "bm_request_id": "4d2906d9-3488-452f-997e-13ae03c2380e",
            "bm_session_id": "aa38c848-ff23-48fc-9f27-d6edbe400c9b",
            "app_version": "1.33-v430",
            "client_source": "ios",
            "client_source_meta": "ios", 
            "major_version": "1.0", 
            "minor_version": "0"      
        },
        "data": {
        "event_data": {
          "utm": {
            
          },
          "email": {
            
          },
          "fb_data": {
            
          },
          "id_token": "eyJhbGciOiJSUzI1NiIsImtpZCI6ImRjNGQwMGJjM2NiZWE4YjU0NTMzMWQxZjFjOTZmZDRlNjdjNTFlODkiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vYnJpZ2h0Y2FwaXRhbGFwcC1kZXYiLCJhdWQiOiJicmlnaHRjYXBpdGFsYXBwLWRldiIsImF1dGhfdGltZSI6MTYyMzY1MTAyMCwidXNlcl9pZCI6InZtZDBPMDZncFRiQ3drR2NFSldteTdQa2RqcjEiLCJzdWIiOiJ2bWQwTzA2Z3BUYkN3a0djRUpXbXk3UGtkanIxIiwiaWF0IjoxNjIzNjUxMDIwLCJleHAiOjE2MjM2NTQ2MjAsInBob25lX251bWJlciI6IisxMjQ1MjY1NDIzNiIsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnsicGhvbmUiOlsiKzEyNDUyNjU0MjM2Il19LCJzaWduX2luX3Byb3ZpZGVyIjoicGhvbmUifX0.Vrb7nP6AmhkyAGkEg9pkyLqVBsrBCA_GcGsh4QimDEsdz9d0fVgDPaJYO6w3YmJCmVWf6id_PXs9JLuf7AXMzHTH8FjEJ95os7V839l8naErm23XMh-pHKYM7lRaqAJywotkFaK__mRjsROMUlOOnBA4MgnqWuoV57iXg-27rkfatpBof4BDWiJAjlOgb8RBYYQcGjYga1_c4fjpesm57Z06koyWUtyQZKDVZ-TAJUhraw7VAbnPecHA48fcSjidDAvQ_qlYJZseW7104PXaemZs0UrSVhJsJK40FsNAVrWyBZLRyLG9UCwIk7gX4ReliDINUbIQl6kCHMFeLyIprw",
          "fcm_token": "d_97JvvYS5Ww464ESQgQdi:APA91bEQTFG0bxOxKPWiLPyykfRmk6KWazjVlq5iZNEOKtOwHMLzzCsDWyqOleKT6x2cTsCEJYjAaMC2xrQUtEbLig_DxL9QDY49j1Nfls59chKi4VdK1cZI1qAefUPJV4LYufHR3nVA",
          "phone_uid": "vmd0O06gpTbCwkGcEJWmy7Pkdjr1",
          "apns_token": None,
          "auth_signals": {
            
          },
          "phone_number": phone_num,
          "presell_version": "v2",
          "funnel_variation": "",
          "segment_anonymous_id": "3a3994d8-c3e0-4c00-b09c-859ec3578e37",
          "pre_sell_lottie_shown": False,
          "extra_params": {
            "credit_builder_funnel_exp_v1": "1",
            "tof_experiment": "treatment3",
            "cb_eligible_product_exp": "treatment2"
          },
          
        },
        "event_name": "LOGIN_EVENT"
      }


    }
    response = requests.request("POST", 'https://gateway-dev.brightmoney.co/api/v1/users/usm/signin/' , headers=headers, data=json.dumps(payload))  
    result = response.json()
    access_code = result['data']['action_data']['access']

    headers = {
        "Authorization":'Bearer ' + access_code,
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Content-Length": ""
    }
    payload = {
        "meta": {
            "bm_request_id": "4d2906d9-3488-452f-997e-13ae03c2380e",
            "bm_session_id": "aa38c848-ff23-48fc-9f27-d6edbe400c9b",
            "app_version": "1.33-v430",
            "client_source": "ios",
            "client_source_meta": "ios", 
            "major_version": "1.0", 
            "minor_version": "0"      
        },

        "data": {
        "event_name": "APP_PIN_ENABLED_EVENT",
        "event_data": {}
        }


    }
    response = requests.request("POST",url= "https://gateway-dev.brightmoney.co/api/v1/users/usm/trigger/",headers=headers,data=json.dumps(payload))
    result = response.json()
    # print(result)

    payload={

        "meta": {
            "bm_request_id": "4d2906d9-3488-452f-997e-13ae03c2380e",
            "bm_session_id": "aa38c848-ff23-48fc-9f27-d6edbe400c9b",
            "app_version": "1.33-v430",
            "client_source": "ios",
            "client_source_meta": "ios", 
            "major_version": "1.0", 
            "minor_version": "0"      
        },

        "data": {
        "event_name": "ADD_ACCOUNT_EVENT",
        "event_data": {
        "linking_for": "CHECKING",
        "linking_flow": "ADD",
        "flow_type": "ONBOARDING"
        }
    }

    }
    response = requests.request("POST",url= "https://gateway-dev.brightmoney.co/api/v1/users/usm/trigger/",headers=headers,data=json.dumps(payload))
    result = response.json()
    linking_session_id=result['data']['action_data']['linking_session_id']
    

    payload={

        "meta": {
            "bm_request_id": "4d2906d9-3488-452f-997e-13ae03c2380e",
            "bm_session_id": "aa38c848-ff23-48fc-9f27-d6edbe400c9b",
            "app_version": "1.33-v430",
            "client_source": "ios",
            "client_source_meta": "ios", 
            "major_version": "1.0", 
            "minor_version": "0"      
        },

        "data": {
        "event_name": "ACCOUNT_LINKING_TRIGGER_EVENT",
        "event_data": {
            "alsm_event_name": "SEARCH_SELECTION_REQUIRED_EVENT",
            "alsm_event_data": {
            "mfa_type": None,
            "eventName": "OPEN",
            "timestamp": "2021-07-26T17:55:06.095Z",
            "view_name": "CONSENT",
            "error_code": None,
            "error_type": None,
            "request_id": None,
            "exit_status": None,
            "error_message": None,
            "linking_client": "PLAID",
            "linking_session_id": linking_session_id,
            "institution_search_query": "Citi"
            }
        }
        }
    }
    response = requests.request("POST",url= "https://gateway-dev.brightmoney.co/api/v1/users/usm/trigger/",headers=headers,data=json.dumps(payload))
    result = response.json()
    # print(result)

    payload={

        "meta": {
            "bm_request_id": "4d2906d9-3488-452f-997e-13ae03c2380e",
            "bm_session_id": "aa38c848-ff23-48fc-9f27-d6edbe400c9b",
            "app_version": "1.33-v430",
            "client_source": "ios",
            "client_source_meta": "ios", 
            "major_version": "1.0", 
            "minor_version": "0"      
        },


        "data": {
        "event_name": "ACCOUNT_LINKING_TRIGGER_EVENT",
        "event_data": {
            "alsm_event_name": "SELECT_INSTITUTION_EVENT",
            "alsm_event_data": {
            "linking_client": "PLAID",
            "dynamic_provider_selected": "PLAID",
            "eventName": "OPEN",
            "error_code": None,
            "error_message": None,
            "error_type": None,
            "exit_status": None,
            "institution_search_query": None,
            "institution_id": "ins_114298",
            "institution_name": "Opportunity Bank of Montana - Personal",
            "linking_session_id": linking_session_id,
            "mfa_type": None,
            "view_name": "CONSENT",
            "request_id": None,
            "timestamp": "2021-07-26T17:55:06.095Z"
            }
        }
        }
    }

    response = requests.request("POST",url= "https://gateway-dev.brightmoney.co/api/v1/users/usm/trigger/",headers=headers,data=json.dumps(payload))
    result = response.json()
    # print(result)

    payload={

        "meta": {
            "bm_request_id": "4d2906d9-3488-452f-997e-13ae03c2380e",
            "bm_session_id": "aa38c848-ff23-48fc-9f27-d6edbe400c9b",
            "app_version": "1.33-v430",
            "client_source": "ios",
            "client_source_meta": "ios", 
            "major_version": "1.0", 
            "minor_version": "0"      
        },

        "data": {
        "event_name": "ACCOUNT_LINKING_TRIGGER_EVENT",
        "event_data": {
            "alsm_event_name": "SELECT_INSTITUTION_EVENT",
            "alsm_event_data": {
            "linking_client": "PLAID",
            "dynamic_provider_selected": "PLAID",
            "eventName": "OPEN",
            "error_code": None,
            "error_message": None,
            "error_type": None,
            "exit_status": None,
            "institution_search_query": None,
            "institution_id": "ins_114298",
            "institution_name": "Opportunity Bank of Montana - Personal",
            "linking_session_id": linking_session_id,
            "mfa_type": None,
            "view_name": "CONSENT",
            "request_id": None,
            "timestamp": "2021-07-26T17:55:06.095Z"
            }
        }
        }
    }

    response = requests.request("POST",url= "https://gateway-dev.brightmoney.co/api/v1/users/usm/trigger/",headers=headers,data=json.dumps(payload))
    result = response.json()
    # print(result)

    payload={

        "meta": {
            "bm_request_id": "4d2906d9-3488-452f-997e-13ae03c2380e",
            "bm_session_id": "aa38c848-ff23-48fc-9f27-d6edbe400c9b",
            "app_version": "1.33-v430",
            "client_source": "ios",
            "client_source_meta": "ios", 
            "major_version": "1.0", 
            "minor_version": "0"      
        },

        "data": {
        "event_name": "ACCOUNT_LINKING_TRIGGER_EVENT",
        "event_data": {
            "alsm_event_name": "SUBMITTED_CREDENTIALS_EVENT",
            "alsm_event_data": {
            "linking_client": "PLAID",
            "eventName": "SUBMIT_CREDENTIALS",
            "error_code": None,
            "error_message": None,
            "error_type": None,
            "exit_status": None,
            "institution_search_query": None,
            "institution_id": "ins_114298",
            "institution_name": "Opportunity Bank of Montana - Personal",
            "linking_session_id": linking_session_id,
            "mfa_type": None,
            "view_name": "CONSENT",
            "request_id": "9lgQLqPXBZy2DX4",
            "timestamp": "2021-07-26T17:55:06.095Z",
            "credentials": {
                "fi_username": "",
                "fi_password": ""
            }
            }
        }
        }
    }

    response = requests.request("POST",url= "https://gateway-dev.brightmoney.co/api/v1/users/usm/trigger/",headers=headers,data=json.dumps(payload))
    result = response.json()
    # print(result)

    payload={

        "meta": {
            "bm_request_id": "4d2906d9-3488-452f-997e-13ae03c2380e",
            "bm_session_id": "aa38c848-ff23-48fc-9f27-d6edbe400c9b",
            "app_version": "1.33-v430",
            "client_source": "ios",
            "client_source_meta": "ios", 
            "major_version": "1.0", 
            "minor_version": "0"      
        },

        "data": {
        "event_name": "ACCOUNT_LINKING_TRIGGER_EVENT",
        "event_data": {
            "alsm_event_name": "MFA_ENTERED_EVENT",
            "alsm_event_data": {
            "linking_client": "PLAID",
            "eventName": "SUBMIT_MFA",
            "error_code": None,
            "error_message": None,
            "error_type": None,
            "exit_status": None,
            "institution_search_query": None,
            "institution_id": "ins_114298",
            "institution_name": "Opportunity Bank of Montana - Personal",
            "linking_session_id": linking_session_id,
            "mfa_type": "code",
            "view_name": "CONSENT",
            "request_id": "9lgQLqPXBZy2DX4",
            "timestamp": "2021-07-26T17:55:06.095Z",
            "credentials": {
                "fi_username": "",
                "fi_password": ""
            }
            }
        }
        }
    }

    response = requests.request("POST",url= "https://gateway-dev.brightmoney.co/api/v1/users/usm/trigger/",headers=headers,data=json.dumps(payload))
    result = response.json()
    # print(result)

    payload={

        "credentials": {
            "username": "user_good",
            "password": "pass_good"
        },
        "initial_products": [
            "transactions"
        ],
        "institution_id": "ins_114298",
        "display_language": "en",
        "options": {
            "webhook": "https://hydra-dev-4.brightmoney.co/api/v0/plaid/webhook/"
        },
        "public_key": "b566e5e558542013455f5cb2f1fc15"
        
    }

    response = requests.request("POST",url="https://sandbox.plaid.com/link/item/create",headers=headers,data=json.dumps(payload))
    result = response.json()
    public_token=result['public_token']


    payload={

        "meta": {
            "bm_request_id": "4d2906d9-3488-452f-997e-13ae03c2380e",
            "bm_session_id": "aa38c848-ff23-48fc-9f27-d6edbe400c9b",
            "app_version": "1.33-v430",
            "client_source": "ios",
            "client_source_meta": "ios", 
            "major_version": "1.0", 
            "minor_version": "0"      
        },

        "data": {
        "event_name": "ACCOUNT_LINKING_TRIGGER_EVENT",
        "event_data": {
            "alsm_event_name": "LINKING_SUCCESS_EVENT",
            "alsm_event_data": {
            "response": {
                "institution": {
                "name": "",
                "institution_id": ""
                },
                "account": {
                "id": None,
                "name": None,
                "type": None,
                "subtype": None,
                "mask": None
                },
                "account_id": None,
                "accounts": [
                {
                    "id": "QrgK6l5mndsxEqrbb5KrfvJJyzP5qjfkqwepk",
                    "name": "Plaid Savin",
                    "mask": "1110",
                    "type": "depository",
                    "subtype": "savings"
                },
                {
                    "id": "egQo3L51ZGuPM5l66jelU7WWoLK4yXsMorkLF",
                    "name": "Plaid Checkin",
                    "mask": "0001",
                    "type": "depository",
                    "subtype": "checking"
                }
                ],
                "linking_session_id": linking_session_id,
                "public_token": public_token,
                "link_token": ""
            },
            "linking_client": "PLAID",
            "linking_session_id": linking_session_id
            }
        }
        }
    }

    response = requests.request("POST",url="https://gateway-dev.brightmoney.co/api/v1/users/usm/trigger/",headers=headers,data=json.dumps(payload))
    result = response.json()
    # print(result)

    payload={

        "meta": {
            "bm_request_id": "4d2906d9-3488-452f-997e-13ae03c2380e",
            "bm_session_id": "aa38c848-ff23-48fc-9f27-d6edbe400c9b",
            "app_version": "1.33-v430",
            "client_source": "ios",
            "client_source_meta": "ios", 
            "major_version": "1.0", 
            "minor_version": "0"      
        },
        

        "data": {
        "event_data": {
            "flow_type": "ONBOARDING",
            "linking_for": "CHECKING",
            "linking_flow": "ADD",
            "linking_session_pid": linking_session_id
        },
        "event_name": "LINKING_SESSION_SUCCEEDED_EVENT"
        }
    }

    response = requests.request("POST",url="https://gateway-dev.brightmoney.co/api/v1/users/usm/trigger/",headers=headers,data=json.dumps(payload))
    result = response.json()
    print(response.status_code())
    # print('here result :' , result)
    return result['data']['action']

def validateAccountConnect(phone_number):
    while(checkingConnect(phone_number)!='CHOOSE_CHECKING_ACCOUNTS_ACTION'):
        checkingConnect(phone_number)
