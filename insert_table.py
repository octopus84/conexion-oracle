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

	#con.autocommit = True
	# Inserting a record into table employee
	cursor.execute('insert into employee values(10001,\'Rahul\',50000.50)')

	# commit() to make changes reflect in the database
	con.commit()
	print('Record inserted successfully')

except cx_Oracle.DatabaseError as e:
	print("There is a problem with Oracle", e)

# by writing finally if any error occurs
# then also we can close the all database operation
finally:
	if cursor:
		cursor.close()
	if con:
		con.close()