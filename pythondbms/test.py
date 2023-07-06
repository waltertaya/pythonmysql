import mysql.connector
myconn = mysql.connector.connect(host = "localhost", user = " ", passwd = "password")
cur = myconn.cursor()
n = 1
while n != 0:
    command = input("Enter your command: ")
    try:
        dbs = cur.execute(command)
        for x in cur:
            print(x)
    except:
        myconn.rollback()
    myconn.close()
