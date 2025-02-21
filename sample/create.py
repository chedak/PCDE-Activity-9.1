import mysql.connector  

cnx = mysql.connector.connect(user='root', 
    password='Today#31%Otugi78',
    host='127.0.0.1',
    database='education',
    auth_plugin='mysql_native_password')

college = input('Enter college name: ')
students = input('Enter student population: ')
city = input('Enter city: ')
region = input('Enter region: ')
country = input('Enter country: ')

cursor = cnx.cursor()
query = (f'INSERT INTO `Colleges` (Name, Students, City, Region, Country) VALUES ("{college}", {students}, "{city}", "{region}", "{country}")')
cursor.execute(query)

query = ("SELECT * FROM Colleges")
cursor.execute(query)

# print all the cells of all the rows
for row in cursor.fetchall():
    print(row)

cursor.close()
cnx.close()

