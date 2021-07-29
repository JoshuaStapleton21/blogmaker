## this code is for checking that a payment has been made
from square.client import Client
from datetime import datetime, timezone
from dateutil import parser
import os
from dotenv import load_dotenv
load_dotenv()

def check_client_payment(email):
  # need to use the production application token
  api_key = os.getenv("SQUARE_API_KEY")
  client = Client(
      access_token=api_key,
  )

  customers_result = client.customers.search_customers(
      body = {
      "limit": 1,
      "query": {
        "filter": {
          "creation_source": {
            "values": [
              "THIRD_PARTY"
            ],
            "rule": "INCLUDE"
          },
          "email_address": {
            "fuzzy": email # find user by email address
          }
        },
        "sort": {
          "field": "CREATED_AT",
          "order": "ASC"
        }
      }
    }
  )

  # first find the customer ID and created_at time
  customer_id_from_user = ""
  if customers_result.is_success():
      print(customers_result.body)
      customer_id_from_user = customers_result.body["customers"][0]["id"]
      payment_time_rfc3339 = customers_result.body["customers"][0]["created_at"]
      print(customer_id_from_user) # get id
      payment_time = parser.parse(payment_time_rfc3339)
      
      
  elif customers_result.is_error():
      # print(customers_result.errors)
      print("Customer email not found")
      return -1

  # next find the payment which has the same payment time
  payments_result = client.payments.list_payments(begin_time = payment_time_rfc3339)

  if payments_result.is_success():
      print(payments_result.body)
      amount = payments_result.body["payments"][0]["amount_money"]["amount"]
      # print(amount)

      local_time = datetime.now(timezone.utc).astimezone()
      now = local_time.isoformat()
      now = parser.parse(now)

      # check if the payments are more than a month apart
      num_months = (now.year - payment_time.year) * 12 + (now.month - payment_time.month)
      tier = 0
      if num_months < 1:
        if amount == 1299:
          tier = 1
          print("detected tier 1 subscription")
        elif amount == 1999:
          tier = 2
          print("detected tier 2 subscription")
        elif amount == 2999:
          tier = 3
          print("detected tier 3 subscription")
        elif amount == 5999:
          tier = 4
          print("detected tier 4 subscription")
        else:
          tier = -1
          print("Payment was found but the amount is incorrect")
        
        return tier

      else:
        print("Payment is outdated. Needs to have been completed at most 1 month ago.")
        return -1

  elif payments_result.is_error():
    print(payments_result.errors)
    return -1