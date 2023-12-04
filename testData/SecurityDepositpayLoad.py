def securityDepositPayload(context,buid,pgr_id,acc_pid):
    body = {
        
     "meta": {
        "bm_request_id": "01c00add-2f6b-4ff5-a6b3-0f5240e7e9b9",
        "bm_session_id": "01c00add-2f6b-4ff5-a6b3-0f5240e7e9b9",
        "app_version": "123",
        "client_source": "asif_local_host",
        "bright_uid": buid
    },
    "data": {
        "account_pid":acc_pid,
        "pull_account_pid": pgr_id,
        "amount":20,
        "transaction_type": "CC_SECURITY_DEPOSIT"
    }
    }
    return body