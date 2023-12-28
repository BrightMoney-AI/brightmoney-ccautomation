import pdb
import requests


def submitAppDynamicPayLoad(context, buid):
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



def dynamic_post_request(url, payload_data):
    try:
        response = requests.post(url, json=payload_data)
        response.raise_for_status()  # Check for HTTP status code errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

# Define the base URL for your API endpoint
base_url = "https://api.example.com/"

# Read the data from the Excel file into a DataFrame
df = pdb.read_excel("payload_data.xlsx")

# Define the keys in your payload
keys_to_change = ["key1", "key2", "nested_key1", "nested_key2", "key5", "key6", "nested_key3", "nested_key4"]

# Iterate through the sets of dynamic values
for i in range(1, len(df.columns)//2 + 1):
    dynamic_values = [f"Set{i}_Value1", f"Set{i}_Value2"]
    
    # Create a function to recursively update the payload
    def update_payload(payload, keys, values):
        if isinstance(payload, dict):
            for key, value in payload.items():
                if key in keys:
                    payload[key] = values[keys.index(key)]
                elif isinstance(value, dict):
                    update_payload(value, keys, values)
    
    # Update the payload with the current set of dynamic values
    payload = {
        "dictionary1": {
            "key1": "value1",
            "key2": "value2",
            "key3": "value3",
            "key4": {
                "nested_key1": "nested_value1",
                "nested_key2": "nested_value2"
            }
        },
        "dictionary2": {
            "key5": "value5",
            "key6": "value6",
            "key7": {
                "nested_key3": "nested_value3",
                "nested_key4": "nested_value4"
            }
        }
    }
    
    update_payload(payload, keys_to_change, dynamic_values)
    
    # Send the modified payload in the POST request for testing
    print(f"Testing with Set{i} of dynamic values...")
    response_data = dynamic_post_request(base_url, payload)
    
    if response_data is not None:
        # Process the response data here
        print(f"Response: {response_data}")
    else:
        print(f"Failed to test with Set{i} of dynamic values")