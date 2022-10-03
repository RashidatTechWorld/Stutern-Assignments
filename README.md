# Stutern-Assignments
# Introduction to RDBMs
# # # # # script 1
# # # #import sqlite3
import sqlite3

# # # check
print("Sqlite imported successfully")

# # # # #create or connect to a connection
conn = sqlite3.connect("SGA_1_3_learners.db")

# # # #check
print("Connection created successfully") ; print(type(conn))

# # # #create a cursor object
cursor = conn.cursor()

# #cursor check
print("Cursor created successfully \n", type(cursor))
cursor.execute(
    """
    CREATE TABLE SGA_1_3_learners (
        first_name text,
        last_name text,
        email_address text,
        course text
    )
    """
)

# # # check that table was created successfully
print("Students table created successfully")
# #insert multiple records
SGA_1_3_learners_list = [
    ("Awoniran", "Omowunmi", "mowunmi@gmail.com", "Data Science"),
    ("Aishat", "Abass", "abass67@stutern.com", "Data Science"),
    ("Babajide", "Adesugba", "champtalks@stutern.com", "Data Science"),
    ("Sikiru", "Rashidat", "goldrashy@gmail.com","Data Science"),
    ("Amure", "Faith","faithamu@stutern.com","Data Science"),
    ("Olorunnishola","Deborah","debbyrise@gmail.com", "Data Science"),
    ("Ekeocha","Prince","princewill@stutern.com","Data Science"),
    ("Ibrahim","Kafayat","kaffygold@gmail.com", "Data Science"),
    ("Awiya","Cynthia","cyny@gmail.com","Data Science"),
    ("Ogungbile","Stephen","stevo@stutern.com","Data Science"),
    ("Awonaike", "Tawakalitu","naike@stutern.com","Data science"),
    ("Afolabi", "Ade", "afolade@stutern.com", "Data Science"),
    ("Jubril", "Ramotalahi","ramotubril@gmail.com","data science"),
    ("Ezenonwu","Joyce","joyful@gmail","Data Science"),
    ("Adeoti","Mariam","maryamadae@stutern.com","Data Science"),
    ("Umar","Binta","bintaumar@gmail.com","Data Science"),
    ("Akpanowo", "Esther","esthergrace@stutern.com", "Data Science")
]

cursor.executemany(
"""
INSERT INTO SGA_1_3_learners 
VALUES(?, ?, ?, ?)
""",

SGA_1_3_learners_list

)
# #check
# print("Inserted multiple records at once")



# #querying the data
cursor.execute(
    """
    SELECT * FROM SGA_1_3_learners 
    """
)
# print("Query created successfully")

items = cursor.fetchall()

# format outputs to display in a tabular form
print("first_name"+ "\tlast_name"+ "\temail_address" "\t\t\tCourse \n" f"{'.' * 100}")

#loop through the items
for item in items:
    first_name, last_name, email_address, course = item
    print(f"{first_name:16}{last_name:16}{email_address:16}\t\t{course}")
