from tabulate import tabulate

import mysql.connector
try:
        mydb = mysql.connector.connect(host = 'localhost',user = 'root' ,password = '',database = 'ksebdb')
except mysql.connector.Error as e:
        print("MySql error",e)
mycursor = mydb.cursor()
while True:
    print("select an option from the menu")
    print("""             1. add consumer
             2. search consumer
             3. delete a consumer
             4. update the consumer
             5. view all consmer
             6. generate bill
             7. view bill
             8. Exit""")
    choice =int(input("Enter your option : "))
    if choice==1:
        print("add consumer selected")
        consumer_id = int(input("Enter the consumer id: "))
        name = input("enter the name :")
        phone = input("Enter the phone number : ")
        place = input("Enter the address : ")
        email = input("Enter the email id : ")
        sql = "INSERT INTO `consumer`(`consumer_id`, `consumer_name`, `consumer_phone`, `consumer_place`, `consumer_email`) VALUES (%s,%s,%s,%s,%s)"
        data =(consumer_id,name,phone,place,email)
        mycursor.execute(sql,data)
        mydb.commit()
    elif choice==8:
        break