import mysql.connector as c
con=c.connect(host="localhost",user="root",password="root",database="lib")
cur=con.cursor()
cur.execute(f"select status from books2 where bid=1;")
dis2=cur.fetchall()
for i in dis2:
    for x in i:
        print(x)
