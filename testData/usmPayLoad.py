def usm_SigninPayLoadNegative(phnum):

    body = {
        "meta": {
            "bm_request_id": "068f1313-87ff-436a-a9fa-477c754085b4",
            "app_version": "1.33-v430",
            "client_source": "ios",
            "bm_session_id": "4c6a421e-a00c-11ea-be57-0ace1771e734"
        },
        "data": {
            "event_name": "",
            "event_data": {
                "referral_code": "651E0B",
                "funnel_variation": "4",
                "presell_version": "v2",
                "segment_anonymous_id": "some_id",
                "bm_request_id": "5041681c-e9fa-4a0a-9591-05e1c4ccbe27",
                "client_source": "ios",
                "phone_number":phnum,
                "phone_uid": "RmaQbdJVeCZ1FGml9CNRK6YNzzx2",
                "apns_token": "5714758AEEBE9761C994874ACFA457A265F9074661BF2AF82E890F27BB7F267C",
                "fcm_token": "fcm_token_trial_anshul",
                "extra_params": {"credit_builder_funnel_exp_v1": "1", "tof_experiment": "treatment3","cb_eligible_product_exp":"treatment2"},
                "utm": {"utm_ad": "528330201547", "utm_campaign": "13436129417", "utm_adset": "127188548790", "utm_keyword": "bright%20money", "utm_source": "gtp", "utm_medium": "gsb"},
                "id_token": "eyJhbGciOiJSUzI1NiIsImtpZCI6IjBiYWJiMjI0NDBkYTAzMmM1ZDAwNDJjZGFhOWQyODVjZjhkMjAyYzQiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vYnJpZ2h0Y2FwaXRhbGFwcCIsImF1ZCI6ImJyaWdodGNhcGl0YWxhcHAiLCJhdXRoX3RpbWUiOjE1ODc0NDA3NzMsInVzZXJfaWQiOiI2NXQ5SXBqREJRYnpVNmlYZEpkUklpMHJwSTAzIiwic3ViIjoiNjV0OUlwakRCUWJ6VTZpWGRKZFJJaTBycEkwMyIsImlhdCI6MTU4NzU2NjI0OSwiZXhwIjoxNTg3NTY5ODQ5LCJwaG9uZV9udW1iZXIiOiIrMTgzMTIzNDc5ODQiLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7InBob25lIjpbIisxODMxMjM0Nzk4NCJdfSwic2lnbl9pbl9wcm92aWRlciI6InBob25lIn19.EwZ9DjUkw5667Bhx2fGdlWzNw1iPkEeK18FCWKgQbY23t2ZVNXVGZR2NUSPeLzuD05zRXxN84s8CHETH6rfNdvyT3HTEUr_2EmhyTpUIn9mdKPcDVts4G2Qxs9GmSz2A-knboI29c3ND-j4FqfdGlvSoqlPpJBySed4wHACkToHUfA54ZZLMccz2ueSl4tl9FLyYo7BjSXaGDBMVGmJANacxlF5uMFv5ajL-MTlZO3aS_EA5MGkwdpnkqqvzM8o-AV7HDHDQnNmenynApPvGkN1odQ_0kLff4UUepxzQtDhFL3CyUpIl5KQEjEm-snNXqi3wjBwFkymki5ivyLW81A",
                "auth_signals": {
                    "fingerprint": {}, 
                    "authStatement": "I here by agrees to TnC"
                }
            }
        }  
    }
    return body



def usm_SigninPayLoad(phnum):
    body = {
        "meta": {
            "bm_request_id": "068f1313-87ff-436a-a9fa-477c754085b4",
            "app_version": "1.33-v430",
            "client_source": "ios",
            "bm_session_id": "4c6a421e-a00c-11ea-be57-0ace1771e734"
        },
        "data": {
            "event_name": "LOGIN_EVENT",
            "event_data": {
                "referral_code": "651E0B",
                "funnel_variation": "4",
                "presell_version": "v2",
                "segment_anonymous_id": "some_id",
                "bm_request_id": "5041681c-e9fa-4a0a-9591-05e1c4ccbe27",
                "client_source": "ios",
                "phone_number":phnum,
                "phone_uid": "RmaQbdJVeCZ1FGml9CNRK6YNzzx2",
                "apns_token": "5714758AEEBE9761C994874ACFA457A265F9074661BF2AF82E890F27BB7F267C",
                "fcm_token": "fcm_token_trial_anshul",
                "extra_params": {"credit_builder_funnel_exp_v1": "1", "tof_experiment": "treatment3","cb_eligible_product_exp":"treatment2"},
                "utm": {"utm_ad": "528330201547", "utm_campaign": "13436129417", "utm_adset": "127188548790", "utm_keyword": "bright%20money", "utm_source": "gtp", "utm_medium": "gsb"},
                "id_token": "eyJhbGciOiJSUzI1NiIsImtpZCI6IjBiYWJiMjI0NDBkYTAzMmM1ZDAwNDJjZGFhOWQyODVjZjhkMjAyYzQiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vYnJpZ2h0Y2FwaXRhbGFwcCIsImF1ZCI6ImJyaWdodGNhcGl0YWxhcHAiLCJhdXRoX3RpbWUiOjE1ODc0NDA3NzMsInVzZXJfaWQiOiI2NXQ5SXBqREJRYnpVNmlYZEpkUklpMHJwSTAzIiwic3ViIjoiNjV0OUlwakRCUWJ6VTZpWGRKZFJJaTBycEkwMyIsImlhdCI6MTU4NzU2NjI0OSwiZXhwIjoxNTg3NTY5ODQ5LCJwaG9uZV9udW1iZXIiOiIrMTgzMTIzNDc5ODQiLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7InBob25lIjpbIisxODMxMjM0Nzk4NCJdfSwic2lnbl9pbl9wcm92aWRlciI6InBob25lIn19.EwZ9DjUkw5667Bhx2fGdlWzNw1iPkEeK18FCWKgQbY23t2ZVNXVGZR2NUSPeLzuD05zRXxN84s8CHETH6rfNdvyT3HTEUr_2EmhyTpUIn9mdKPcDVts4G2Qxs9GmSz2A-knboI29c3ND-j4FqfdGlvSoqlPpJBySed4wHACkToHUfA54ZZLMccz2ueSl4tl9FLyYo7BjSXaGDBMVGmJANacxlF5uMFv5ajL-MTlZO3aS_EA5MGkwdpnkqqvzM8o-AV7HDHDQnNmenynApPvGkN1odQ_0kLff4UUepxzQtDhFL3CyUpIl5KQEjEm-snNXqi3wjBwFkymki5ivyLW81A",
                "auth_signals": {
                    "fingerprint": {}, 
                    "authStatement": "I here by agrees to TnC"
                }
            }
        }  
    }
    return body

def usm_appPinPayload():
    body={
    "meta": {
        "bm_request_id": "068f1313-87ff-436a-a9fa-477c754085b4",
        "app_version": "1.9-v51",
        "client_source": "ios",
        "bm_session_id": "4c6a421e-a00c-11ea-be57-0ace1771e734"
    },
    "data": {
        "event_name": "APP_PIN_ENABLED_EVENT",
        "event_data": {}
    }
    }
    return body

