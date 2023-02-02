# from tinder_token.phone import TinderTokenPhoneV2
#
# phone = TinderTokenPhoneV2()
#
# def sample_phone(phone_number: str) -> str:
#     phone.send_otp_code(phone_number)
#     otp_code = input('code: ')
#
#     refresh_token = phone.get_refresh_token(otp_code, phone_number)
#     return phone.get_tinder_token(refresh_token)
#

from tinderapi import Scavenger
import json

ACCOUNT = json.loads(open('account.json', 'r').read())

scavenger = Scavenger('Photos', ACCOUNT['telegram_bot_access_token'], ACCOUNT['chat_id'])
