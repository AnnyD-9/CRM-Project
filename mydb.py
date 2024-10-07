import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    password='anukulad',

)

# prepare cursor object

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE crm_company")

print("All Done")