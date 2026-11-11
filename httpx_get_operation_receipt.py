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

open_credit_account_request = {
    "userId": create_user_response_data['user']['id']
}
open_credit_account_response = httpx.post("http://localhost:8003/api/v1/accounts/open-credit-card-account",
                                          json=open_credit_account_request)
open_credit_account_response_data = open_credit_account_response.json()

make_purchase_operation_request = {
    "status": "IN_PROGRESS",
    "amount": 77.99,
    "cardId": open_credit_account_response_data['account']['cards'][0]['id'],
    "accountId": open_credit_account_response_data['account']['id'],
    "category": "taxi"
}
make_purchase_operation_response = httpx.post("http://localhost:8003/api/v1/operations/make-purchase-operation",
                                              json=make_purchase_operation_request)
make_purchase_operation_response_data = make_purchase_operation_response.json()

get_operation_receipt_response = httpx.get("http://localhost:8003/api/v1/operations/operation-receipt/"
                                           f"{make_purchase_operation_response_data['operation']['id']}")
get_operation_receipt_response_data = get_operation_receipt_response.json()

print(f"Get operation receipt data: {get_operation_receipt_response_data}")
print(f"Get operation receipt status code: {get_operation_receipt_response.status_code}")
