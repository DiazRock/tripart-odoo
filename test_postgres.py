import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="odoo_data", 
   user='diazrock', 
   password='1234', 
   host='127.0.0.1', 
   port= '5433'
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Executing an MYSQL function using the execute() method
cursor.execute("select version()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print("Connection established to: ",data)

#Closing the connection
conn.close()
