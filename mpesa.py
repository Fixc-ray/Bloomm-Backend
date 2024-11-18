import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime
from config import CONSUMER_KEY, CONSUMER_SECRET, BUSINESS_SHORT_CODE


def get_access_token():
    """Generate an access token for authenticating with the M-Pesa API."""
    url = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    response = requests.get(url, auth=HTTPBasicAuth(CONSUMER_KEY, CONSUMER_SECRET))
    response.raise_for_status()
    return response.json().get('access_token')


def send_money_to_phone(phone_number, amount):
    """Send money to a phone number using M-Pesa's B2C API."""
    access_token = get_access_token()

    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    payload = {
        "InitiatorName": "YourInitiatorName",
        "SecurityCredential": "base64_encoded_credential",
        "CommandID": "BusinessPayment",
        "Amount": amount,
        "PartyA": "600000",
        "PartyB": phone_number,
        "Remarks": "Product payment",  
        "QueueTimeOutURL": "https://your_domain.com/timeout", 
        "ResultURL": "https://your_domain.com/result",
        "Occasion": "ProductPurchase"
    }

    print("M-Pesa Payload:", payload)

    url = 'https://sandbox.safaricom.co.ke/mpesa/b2c/v1/paymentrequest'
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        
        print("M-Pesa Response Status:", response.status_code)
        print("M-Pesa Response Content:", response.text)

        response.raise_for_status()

        return response.json()
    
    except requests.exceptions.RequestException as e:
        print("Request to M-Pesa failed:", e)
        raise e
    except Exception as e:
        print("General error in send_money_to_phone:", e)
        raise e
