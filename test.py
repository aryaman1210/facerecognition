import mysql.connector as con
connect=con.connect(host="localhost",password="12345678",user="root",database="aryaman")
cursor=connect.cursor()
query= """insert into data
values("Nishq","/Users/aryamanbhardwaj/Desktop/project/python/Nishq.jpg");
"""
cursor.execute(query)
connect.commit()


