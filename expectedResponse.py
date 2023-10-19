import json

def submitResponse(context, userid):
    submitResponse = {
    "meta": {
        "bm_request_id": "01c00add-2f6b-4ff5-a6b3-0f5240e7e9b9",
        "bm_session_id": "01c00add-2f6b-4ff5-a6b3-0f5240e7e9b9",
        "app_version": "123",
        "client_source": "akshat_local_host",
        "bright_uid": "f26800c5-7539-4417-900c-cff52e38e2f6"
    },
    "data": {
        "application": {
            "id": 984,
            "created_on": "2023-10-18T07:25:51.960401",
            "modified_on": "2023-10-18T07:25:54.911387",
            "pid": "519835b8-0da4-4c7c-a452-be3bae9e5fc5",
            "application_date": "2023-10-18",
            "application_state": "WAITING_ON_USER_RESPONSE_ON_AGREEMENT",
            "application_type": "CREDIT_CARD_SECURED_APPLICATION_V1",
            "originator": "BCI",
            "application_data": {
                "income": 58000.0,
                "questions": {
                    "occupation": "Retired"
                }
            },
            "loan_parameters": {
                "apr": 19.5,
                "credit_line": 6000,
                "max_permissible_apr": 29.99
            },
            "approval_details": {
                "apr": 19.5,
                "reasons": [
                    {
                        "param 1": "comment 1"
                    },
                    {
                        "param 2": "comment 2"
                    }
                ],
                "strategy": [
                    "MINIFI_STRICT_STRATEGY_V0"
                ],
                "d2ch_risk": "medium",
                "originator": "BCI",
                "eligibility": "APPROVED",
                "line_amount": 6000,
                "max_permissible_apr": 29.99,
                "refi_funnel_treatment": "legacy"
            },
            "system_rejection_details": None,
            "data_update_details": None,
            "referred_details": None,
            "refer_meta": None,
            "application_meta": None,
            "credit_soft_pull_done": False,
            "credit_hard_pull_done": False,
            "notified_for_approval_on": "2023-10-18T07:25:54.856018",
            "expires_on": "2023-11-17T00:00:00",
            "e_signed_on": None,
            "cool_off_till": None,
            "loan_version": "v1",
            "user": userid,
            "submission_auth": 6857,
            "agreement_auth": None,
            "agreement": 757,
            "notice": None
        },
    "eligibility": "APPROVED",
    "origination_fee": 0.0,
    "min_monthly_payment": 278,
    "d2ch_risk": "medium"
    }   
}
    return submitResponse
