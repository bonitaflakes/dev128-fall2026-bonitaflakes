# Starting file for Project 1
# Heshy Bosshart, 11/15/2026, DEV 128

#import the sqlite3 database module
import sqlite3

def setup_db(conn):
    cursor= conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS user;")
    #create table 
    cursor.execute("""CREATE TABLE IF NOT EXISTS user(first_name TEXT, last_name TEXT, email TEXT, phone_number TEXT, street_address TEXT, city TEXT, state TEXT, zip_code TEXT)""")
    #Create some records of data
    cursor.execute("INSERT INTO user VALUES (\"Kitty\", \"Cat\", \"kittycat@teashop.com\", \"111-222-3333\", \"12345 Main Street\", \"Malibu\", \"CA\", \"98589\")"
                   )
    cursor.execute("INSERT INTO user VALUES (\"Fido\", \"Pup\", \"Fidopup@teashop.com\", \"222-333-4444\", \"54321 Main Street\", \"Los Angeles\", \"CA\", \"98581\")"
                   )
    cursor.execute("INSERT INTO user VALUES (\"Dorothy\", \"Perkins\", \"dorothyperkins@teashop.com\", \"333-444-5555\", \"6789 Side Street\", \"Cresent city\", \"CA\", \"98500\")"
                   )
    cursor.execute("INSERT INTO user VALUES (\"Waldo\", \"Ishere\", \"waldoishere@teashop.com\", \"444-555-6666\", \"1111 found you Street\", \"Los Angeles\", \"CA\", \"98581\")"
                   )
    cursor.execute("INSERT INTO user VALUES (\"Pikachu\", \"Isarat\", \"pikachuisarat@teashop.com\", \"555-666-7777\", \"6767 cornhole avenue\", \"Marinebay\", \"CA\", \"98469\")"
                   )
    conn.commit()

def list_names(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT rowid, first_name, last_name FROM user")
    users = cursor.fetchall()
    for this_user in users:
          print(this_user[0], this_user[1], this_user[2])
    #This print code was an AI suggestion. It wouldnt print otherwise.      
    print() 
                  

def list_contact_info(conn):
    #Cursor that will be used to use through the database
    cursor = conn.cursor()
    #query the table and include the rowid primarykey value
    cursor.execute("SELECT rowid, first_name, last_name, email, phone_number FROM user")
    #storing results on query to a list called users
    users = cursor.fetchall()
    #loop through results of query
    for this_user in users:
        print(this_user[0], this_user[1], this_user[2], this_user[3],this_user[4])
    #This print code was an AI suggestion. It wouldnt print otherwise    
        print()

def list_location(conn):
   cursor = conn.cursor()
   cursor.execute(
      "SELECT rowid, first_name, last_name, street_address, city, state, zip_code FROM user"
      )
   users = cursor.fetchall()
   for this_user in users:
    print(
        this_user[0],
        this_user[1],
        this_user[2],
        this_user[3],
        this_user[4],
        this_user[5],
        this_user[6],
      )  
#The print code below was an AI suggestion. It wouldn't print otherwise.     
    print()

def add_user(conn):
    first = input ("Enter first name: ")
    last = input  ("Enter last name: ")
    email = input ("enter email address: ")
    phone_number = input ("Enter phone number: ")
    street = input ("Enter street address: ")
    city = input ("Enter city: ")
    state = input ("Enter state: ")
    zip_code = input ("Enter zip code: ")

    cursor = conn.cursor()
    cursor.execute(
       "Insert into user values (?,?,?,?,?,?,?,?)",
       (first, last, email, phone_number, street, city, state, zip_code))
    conn.commit()
    print(f"\n {first} {last} has been added to the database!\n")
   
def menu():
    #options for 3 reports, 1 add new user and exit program
    print("* * * * Tea Shop database program * * * *")
    print("\nChoose from the options below: ")
    print("Option '1' List all Names") 
    print("Option '2' List Names, Phone and Email")
    print("Option '3' List Names and Location ")
    print("Option '4' Add A New User")
    print("Option '5' Exit the Program") 
          
#Function that will show Menu 
def main():
  print("Welcome to the Tea Shop employee database\n")

  #Create a connection to the database file
conn = sqlite3.connect('mydatabase.db')
setup_db(conn)
  
while True:
    menu() 
    choice = input("Select your option ").strip()
    print()
    if choice == "1":
     list_names(conn)
    elif choice == "2":
      list_contact_info(conn)
    elif choice == "3":
      list_location(conn)
    elif choice == "4":
      add_user(conn)
    elif choice == "5":
      break
    else:
        print("Invalid option! Please try again.")

    input("Press enter to return to the menu\n")    
#Save the updates to the database
conn.commit()
#Close the connection
conn.close() 
# Goodbye message           
print("Thanks for using the Tea Shop database")   

if __name__ == "__main__":
    main()