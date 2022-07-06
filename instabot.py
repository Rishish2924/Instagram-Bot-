from getpass import getpass 
from time import sleep
from instabot import Bot
from os import remove
my_bot = Bot()

  #introduction to app 

print("--Welcome To Instabot CLI Application--")
sleep(2)
print("setting up the connecting with htts://WWW.instagram.com/",end="")
for i in range(3):
    sleep(1)
    print(',',end="")
print()
sleep(2)
print("Connection Established!")

#login user

username = input("username: ")
password = getpass(prompt="password:")
my_bot.login(username = username , password = password) 
print(F"--{username} LOGGEDIN SUCCESSFULLY,--")

#Operation to perform

while True:
  print("Choose suitable option:")
  print("""1. Follow user\n2.Unfollow user\n3.Send message user\n4.Exit the app""")
  print("Enter option you choose",end="")
  n=int(input())
  if n==1:
    user=input("enter username")
    my_bot.follow(user)
    print(F"{user} FOLLOWED.--+")
  elif n==2:
    user=input("enter username")
    my_bot.Unfollow(user)
    print(F"{user} UNFOLLOWED.--")
  elif n==3:
    user=input("enter username:")
    message=input("message you want to send:")
    my_bot.send_message(message,user)
    print(F"--MESSAGE SUCCESFULLY SENT TO {user}.--")
  elif n==4:
    my_bot.logout()
    print("looging out the user",end="")
    for i in range(3):
        sleep(1)
        print('.',end="")
        print()
        sleep(2)
        print("Connection ended!")
        print("logged out succesfully")
        break

else:
    print("Wrong input,Choose again")
remove('./config')
