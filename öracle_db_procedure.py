#!/usr/bin/python
#!/usr/bin/python
	
import cx_Oracle

#set variables
OraUid="admin"       #Oracle User  
OraPwd="myadmin "    #Oracle password
OraService="localhost:1521/ORCL"    #Oracle Service name From Tnsnames.ora file

# Open database connection
db = cx_Oracle.connect(OraUid + "/" + OraPwd + "@" + OraService)

cid = 1
rep_date = date(2015,09,20)

# prepare a cursor object using cursor() method
cursor = db.cursor()
cur_var = cursor.var(cx_Oracle.CURSOR)

try:
   # Call procedure
   l_query = my_cursor.callproc('sp_procedure', (cid,rep_date,l_cur))
   l_results = l_query[2]

   for row in l_results:
		print row
   # Column Specs
   for row in l_results.description:
        print row

except:
   print "Error: unable to fecth data"

# disconnect from server
db.close()