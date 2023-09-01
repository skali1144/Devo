from time import sleep
print("The Username is Linux and the password is root")
for i in range(3):
    u=input("Enter the account Username.")
    l=input("Enter the password.")
    if u == 'Linux' and l == 'root':
        sleep(3)
        print("sorry to keep you waiting but it is reading the password to check if it is correct or wrong...")
        sleep(13)
        print("Thank you for waiting and you Gained Full Access.")
        sleep(1)
        print("Now run devo.sh with ./devo.sh or bash devo.sh, before running them write chmod +x devo.sh. :) thank you for installiong my tool.")        
        break
    else:
        print("Wrong password or username!")
        print("Please Try Again")
else:
    print(1)
    print("Sorry you can't try again... :(")