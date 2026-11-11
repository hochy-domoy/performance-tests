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

open_debit_card_account_request = {
    "userId": create_user_response_data['user']['id']
}
open_debit_card_account_response = httpx.post("http://localhost:8003/api/v1/accounts/open-debit-card-account",
                                          json=open_debit_card_account_request)
open_debit_card_account_response_data = open_debit_card_account_response.json()

issue_virtual_card_request = {
  "userId": create_user_response_data['user']['id'],
  "accountId": open_debit_card_account_response_data['account']['id']
}
issue_virtual_card_response = httpx.post("http://localhost:8003/api/v1/cards/issue-virtual-card",
                                          json=issue_virtual_card_request)
issue_virtual_card_response_data = issue_virtual_card_response.json()

print(issue_virtual_card_response_data)
print(issue_virtual_card_response.status_code)