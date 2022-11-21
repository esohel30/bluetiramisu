import sqlite3
 
# connecting to the database
connection = sqlite3.connect("gfg.db")
 
# cursor
crsr = connection.cursor()
 
# SQL command to insert the data in the table
sql_command = """INSERT INTO emp VALUES (23, "Rishabh",\
"Bansal", "M", "2014-03-28");"""

crsr.execute(sql_command)
 
# another SQL command to insert the data in the table
sql_command = """INSERT INTO emp VALUES (1, "Bill", "Gates",\
"M", "1980-10-28");"""
crsr.execute(sql_command)

connection.commit()
 
# close the connection
connection.close()
