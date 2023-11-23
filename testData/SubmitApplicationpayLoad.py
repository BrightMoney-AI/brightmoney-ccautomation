import json
null = None
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


# Be(Payload ,payload)
# function(params,parmas)
# return response
# FE show/accept


def submitAppMissingPayLoad(context, buid):
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
                "income": "",
                "questions": {
                    "occupation": "Retired"
                }
            }
        }
    }
    return body

def submitAppIncorrectLoanVersionPayLoad(context, buid):
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
            "loan_version": "",
            "application_data": {
                "income": 50000,
                "questions": {
                    "occupation": "Retired"
                }
            }
        }
    }
    return body

def submitAppPayLoadWithLargeIncome(context, buid):
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
                "income": 5800000000000000000000000,
                "questions": {
                    "occupation": "Retired"
                }
            }
        }
    }
    return body
    
def submitAppPayLoadWithMissingMeta(context, buid):
    body = {
        "meta": {
            "bm_request_id": "01c00add-2f6b-4ff5-a6b3-0f5240e7e9b9",
            "bm_session_id": "01c00add-2f6b-4ff5-a6b3-0f5240e7e9b9",
            "app_version": "123",
            "client_source": "akshat_local_host",
            # "bright_uid": buid
        },
        "data": {
            "product": "CREDIT_CARD_SECURED_V1",
            "auth_signals": {
                "fingerprint": [],
                "authStatement": "I have reviewed the Bright line of credit agreement and, if approved, agree to the terms and conditions and the Bright credit line agreement. I authorize Bright to obtain my consumer report and understand my credit bureau file will show this as a hard inquiry."
            },
            "loan_version": "v1",
            "application_data": {
                "income": 5800000000000000000000000,
                "questions": {
                    "occupation": "Retired"
                }
            }
        }
    }
    return body   

def submitAppPayLoadWithmissingApplicationData(context, buid):
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
                # "income": 5800000000000000000000000,
                # "questions": {
                #     "occupation": "Retired"
                # }
            }
        }
    }
    return body      

def submitAppPayLoadWithnullApplicationData(context, buid):
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
                "income": null,
                "questions": {
                    "occupation": null
                }
            }
        }
    }
    return body

def submitAppPayLoadWithMissingAuthData(context, buid):
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
                "authStatement": ""
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

def submitAppPayLoadWithIncorrectProductData(context, buid):
    body = {
        "meta": {
            "bm_request_id": "01c00add-2f6b-4ff5-a6b3-0f5240e7e9b9",
            "bm_session_id": "01c00add-2f6b-4ff5-a6b3-0f5240e7e9b9",
            "app_version": "123",
            "client_source": "akshat_local_host",
            "bright_uid": buid
        },
        "data": {
            "product": "CREDIT",
            "auth_signals": {
                "fingerprint": [],
                "authStatement": ""
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


import json
null = None
def submitAppPayLoadWithMissingIncome(context, buid):
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
                "questions": {
                    "occupation": "Retired"
                }
            }
        }
    }
    return body

def submitAppPayLoadWithNullLoanVersion(context, buid):
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
            "loan_version": null,
            "application_data": {
                "income": 58000,
                "questions": {
                    "occupation": "Retired"
                }
            }
        }
    }
    return body    

def createAccPollPayLoad(context , buid):
    body = {
        "meta": {
                "bm_request_id": "01c00add-2f6b-4ff5-a6b3-0f5240e7e9b9",
                "bm_session_id": "01c00add-2f6b-4ff5-a6b3-0f5240e7e9b9",
                "app_version": "123",
                "client_source": "akshat_local_host",
                "bright_uid": buid
            },
        "data": {
                "application_pid": "942d751d-9728-4b87-9bde-f634fc411836"
            }
    }
    return body

def createAccPayLoad(context,buid):
    body = {
        "meta": {
            "bm_request_id": "01c00add-2f6b-4ff5-a6b3-0f5240e7e9b9",
            "bm_session_id": "01c00add-2f6b-4ff5-a6b3-0f5240e7e9b9",
            "app_version": "123",
            "client_source": "akshat_local_host",
            "bright_uid": buid
        },
        "data": {
            "auth_signals": {
                "fingerprint": [],
                "authStatement": "I have reviewed the Bright line of credit agreement and, if approved, agree to the terms and conditions and the Bright credit line agreement. I authorize Bright to obtain my consumer report and understand my credit bureau file will show this as a hard inquiry."
            },
            "loan_version": "v1",
            "application_pid": "942d751d-9728-4b87-9bde-f634fc411836"
        }
    }
    return body

def activateCardPayLoad(context,buid):
    body = {
        "meta": {
                "bm_request_id": "01c00add-2f6b-4ff5-a6b3-0f5240e7e9b9",
                "bm_session_id": "01c00add-2f6b-4ff5-a6b3-0f5240e7e9b9",
                "app_version": "123",
                "client_source": "akshat_local_host",
                "bright_uid": buid
            },
        "data": {
                "cvv": "123",
                "dob": "2023-09-12",
                "card_pid": "40ac44cf-ccc4-4de1-936c-03838b0268cc"
            }
    }
    return body

def blockCardPayLoad(context,buid):
    body = {

        "meta": {
                "bm_request_id": "01c00add-2f6b-4ff5-a6b3-0f5240e7e9b9",
                "bm_session_id": "01c00add-2f6b-4ff5-a6b3-0f5240e7e9b9",
                "app_version": "123",
                "client_source": "akshat_local_host",
                "bright_uid": buid
            },
        "data": {
                "cvv": "123",
                "dob": "2023-09-12",
                "card_pid": "01c00add-2f6b-4ff5-a6b3-0f5240e7e9b9"
            }
        
    }
    return body


def securityDepositPayload(context,buid):
    body = {
        
     "meta": {
        "bm_request_id": "01c00add-2f6b-4ff5-a6b3-0f5240e7e9b9",
        "bm_session_id": "01c00add-2f6b-4ff5-a6b3-0f5240e7e9b9",
        "app_version": "123",
        "client_source": "asif_local_host",
        "bright_uid": "347810c5-7531-4617-904c-cff14e44e8f0"
    },
    "data": {
        "account_pid": "32b2ae21-92d3-41b9-b07d-7b01ab0be756",
        "pull_account_pid": "34066068-cfb3-4bf2-a3cb-55c224c21995",
        "amount":20,
        "transaction_type": "CC_SECURITY_DEPOSIT"
    }
    }


def transactionSubmitPayLoad(context,buid):
    body = {

        "meta": {
        "bm_session_id": "c0f8e120-911f-4c3c-8793-85641070851c",
        "bm_request_id": "033e22ff-1ae0-47ef-a68e-465d1d888241",
        "client_source": "bci_fe"
        },
    "data": {
            "bright_uid": "d1f8e220-911f-4c3c-8793-85641171850d",
            "account_pid": "799d112e-205a-41c8-82f4-409b1f5bfe5f",
            "external_reference_id":"799d112e-205a-41c8-82f4-409b1f5bfe5f",
            "transaction_type":"PAYMENT",
            "pull_accounts": {
            "CHECKING_ACCOUNT_PID": 1
        }
            }
        
    }
    return body

