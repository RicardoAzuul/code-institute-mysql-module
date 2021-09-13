import os
import datetime
import pymysql

# Get username from Cloud9 workspace
# (modify this variable if running on another environment)
username = os.getenv('C9_USER')

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')

try:
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        # sql = "SELECT * FROM Artist;"
        # cursor.execute(sql)
        # result = cursor.fetchall()
        # print(result)
        # sql = "SELECT * FROM Genre;"
        # cursor.execute(sql)
        # for row in cursor:
        #     print(row)
        # cursor.execute(""" CREATE TABLE IF NOT EXISTS
        #                Friends(name char(20), age int, DOB datetime);""")
        # row = ("Bob", 21, "1190-02-06 23:04:56")
        # cursor.execute("INSERT INTO Friends VALUES (%s, %s, %s);", row)
        # connection.commit()
        # rows = [("Hank", 21, "1990-02-06 23:04:56"),
        #         ("Jim", 56, "1955-05-09 13:12:45"),
        #         ("Fred", 100, "1911-09-10 12:34:56")]
        # cursor.executemany("INSERT INTO Friends VALUES (%s, %s, %s);", rows)
        # connection.commit()
        # cursor.execute("UPDATE Friends SET age = 22 WHERE name = 'Bob';")
        # connection.commit()
        # cursor.execute("UPDATE Friends SET age = %s WHERE name = %s;",
        #        (23, 'Bob'))
        # connection.commit()
        # rows = [(36, "Hank"),
        #  (65, "Jim"),
        #  (121, "Fred")]
        # cursor.executemany("UPDATE Friends SET age = %s WHERE name = %s;", rows)
        # connection.commit()
        # cursor.execute("DELETE FROM Friends WHERE name = 'Bob';")
        # connection.commit()
        # cursor.execute("DELETE FROM Friends WHERE name = %s;", 'Fred')
        # connection.commit()
        # cursor.executemany("DELETE FROM Friends WHERE name = %s;", ['Hank', 'Jim'])
        # connection.commit()
        # names = ['Jim', 'Fred']
        # cursor.execute("DELETE FROM Friends WHERE name in (%s, %s)", names)
        # connection.commit()
        list_of_names = ['Hank', 'Hank', 'Jim', 'Fred']
        format_strings = ','.join(['%s']*len(list_of_names))
        cursor.execute("DELETE FROM Friends WHERE name in ({});".format(format_strings), list_of_names)
        connection.commit()
finally:
    # Close the connection, regardless of whether or not the above was successful
    connection.close()
