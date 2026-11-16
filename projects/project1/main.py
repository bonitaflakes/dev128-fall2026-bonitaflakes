# Starting file for Project 1
# Heshy Bosshart, 11/15/2026, DEV 128

#import the sqlite3 database module
import sqlite3

print("Welcome to the Tea Shop employee database\n")

#Create a connection to the database file
conn = sqlite3.connect('mydatabase.db')
#Cursor that will be used to use through the database
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS user;")
#create table 
cursor.execute("""CREATE TABLE user(first_name TEXT, last_name TEXT, email TEXT, phone_number TEXT, street_address TEXT, city TEXT, state TEXT, zip_code TEXT)""")
#Create some records of data
cursor.execute("INSERT INTO user VALUES (\"Kitty\", \"Cat\", \"kittycat@teashop.com\", \"111-222-3333\", \"12345 Main Street\", \"Malibu\", \"CA\", \"98589\")")
cursor.execute("INSERT INTO user VALUES (\"Fido\", \"Pup\", \"Fidopup@teashop.com\", \"222-333-4444\", \"54321 Main Street\", \"Los Angeles\", \"CA\", \"98581\")")
cursor.execute("INSERT INTO user VALUES (\"Dorothy\", \"Perkins\", \"dorothyperkins@teashop.com\", \"333-444-5555\", \"6789 Side Street\", \"Cresent city\", \"CA\", \"98500\")")
cursor.execute("INSERT INTO user VALUES (\"Waldo\", \"Ishere\", \"waldoishere@teashop.com\", \"444-555-6666\", \"1111 found you Street\", \"Los Angeles\", \"CA\", \"98581\")")
cursor.execute("INSERT INTO user VALUES (\"Pikachu\", \"Isarat\", \"pikachuisarat@teashop.com\", \"555-666-7777\", \"6767 cornhole avenue\", \"Marinebay\", \"CA\", \"98469\")")

#query the table and include the rowid primarykey value
cursor.execute("SELECT rowid, first_name, last_name, email, phone_number, street_address, city, state, zip_code FROM user")
#storing results on query to a list called users
users = cursor.fetchall()
#loop through results of query
for this_user in users:
    print(this_user[0], this_user[1], this_user[2], this_user[3],this_user[4], this_user[5])
#Save the updates to the database
conn.commit()
#Close the connection
conn.close()    