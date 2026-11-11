import httpx

import time

create_user_request = {
    "email": f"user.{time.time()}@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
}
create_user_response = httpx.post("http://localhost:8003/api/v1/users", json=create_user_request)
create_user_response_data = create_user_response.json()

open_credit_card_account_request = {
    "userId": create_user_response_data['user']['id']
}
open_credit_card_account_response = httpx.post("http://localhost:8003/api/v1/accounts/open-credit-card-account",
                                               json=open_credit_card_account_request)
open_credit_card_account_response_data = open_credit_card_account_response.json()

get_tariff_document_response = httpx.get(
    f"http://localhost:8003/api/v1/documents/tariff-document/{open_credit_card_account_response_data['account']['id']}")
get_tariff_document_response_data = get_tariff_document_response.json()

print(f"Get tariff document: {get_tariff_document_response_data}")
print(f"Get tariff document status code: {get_tariff_document_response.status_code}")

get_tariff_contract_response = httpx.get(
    f"http://localhost:8003/api/v1/documents/contract-document/{open_credit_card_account_response_data['account']['id']}")
get_tariff_contract_response_data = get_tariff_contract_response.json()

print(f"Get contract document: {get_tariff_contract_response_data}")
print(f"Get contract document status code: {get_tariff_contract_response.status_code}")
