# Hacking the Fender
# The Fender, a notorious computer hacker and general villain of the people, has compromised several top-secret passwords including your own. Your mission, should you choose to accept it, is threefold. You must acquire access to The Fender‘s systems, you must update his "passwords.csv" file to scramble the secret data. The last thing you need to do is add the signature of Slash Null, a different hacker whose nefarious deeds could be very conveniently halted by The Fender if they viewed Slash Null as a threat.

import csv
import json

#Reading in the Passwords
compromised_users = []
with open("passwords.csv", "r") as password_file:
  password_csv = csv.DictReader(password_file)
  for line in password_csv:
    password_row = line["Password"]
    compromised_users.append(line["Username"])

with open("compromised_users.txt", "w") as compromised_user_file:
    for user in compromised_users:
        compromised_user_file.write(user + "\n")

#Notifying the Boss
with open("boss_message.json", "w") as boss_message:
  boss_message_dict = {"recipient": "The Boss", "message": "Mission Success"}
  json.dump(boss_message_dict, boss_message)

#Scrambling the Password
with open("new_passwords.csv", "w") as new_passwords_obj:
  slash_null_sig = """
   _  _     ___   __  ____             
  / )( \   / __) /  \(_  _)            
  ) \/ (  ( (_ \(  O ) )(              
  \____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
  / )( \ / _\  / __)(  / )(  __)(    \ 
  ) __ (/    \( (__  )  (  ) _)  ) D ( 
  \_)(_/\_/\_/ \___)(__\_)(____)(____/ 
          ____  __     __   ____  _  _ 
  ___   / ___)(  )   / _\ / ___)/ )( \
  (___)  \___ \/ (_/\/    \\___ \) __ (
        (____/\____/\_/\_/(____/\_)(_/
  __ _  _  _  __    __                
  (  ( \/ )( \(  )  (  )               
  /    /) \/ (/ (_/\/ (_/\             
  \_)__)\____/\____/\____/
  """
  new_passwords_obj.write(slash_null_sig)
