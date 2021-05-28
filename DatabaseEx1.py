# creating connection to mysql
import mysql.connector as sql
con=sql.connect(user="root",host="localhost",port=8080,passwd="Lava", auth_plugin="mysql_native_password")
if con.is_connected():
    print("Connected")
else:
    print("not connected")
con.close()
if con.is_connected():
    print("Connection is not closed")
else:
    print("Connection is closed")
