# importing module
import cx_Oracle

# Create a table in Oracle database
try:
    # conexion = cx_Oracle.connect(
    # user= 'system',
    # password= 'oracle',
    # dsn = 'localhost/xe')
    
	con = cx_Oracle.connect('system/oracle@localhost:49161/xe')
	print(con.version)

	# Now execute the sqlquery
	cursor = con.cursor()

	# Creating a table employee
	cursor.execute("create table employee2(empid integer primary key, name varchar2(30), salary number(10, 2))")

	print("Table Created successfully")

except cx_Oracle.DatabaseError as e:
	print("There is a problem with Oracle", e)

# by writing finally if any error occurs
# then also we can close the all database operation
finally:
	if cursor:
		cursor.close()
	if con:
		con.close()
