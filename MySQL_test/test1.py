# from getpass import getpass
#
# import mysql
# from mysql.connector import connect, errorcode
#
# # try:
# #     with connect(
# #         host="77.222.54.50",
# #         user="root",
# #         password="DBlexizli@",
# #     ) as connection:
# #         print(connection)
# # except Error as e:
# #     print(e)
# try:
#     cnx = mysql.connector.connect(user='root', password='DBlexizli@', host='77.222.54.50',
#                                   port='10000', database='swwcomru')
# except mysql.connector.Error as err:
#     if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#         print("Something is wrong with your user name or password")
#     elif err.errno == errorcode.ER_BAD_DB_ERROR:
#         print("Database does not exist")
#     else:
#         print(err)
# else:
#     cnx.close()
#
# print("Done")
import mysql
import pymysql
from mysql.connector import connect, errorcode
from config import host, user, password, database

try:
    connection = mysql.connector.connect(
        host=host,
        user=user,
        passwd=password
    )
    print("Connection to MySQL DB successful")
except Exception as e:
    print(f"The error '{e}' occurred")

# try:
#     connection = pymysql.connect(
#         host=host,
#         # port=33036,
#         # user=user,
#         # password=password,
#         # database=database,
#         # cursorclass=pymysql.cursors.DictCursor
#     )
#     print("Connected...")
#
# except Exception as ex:
#     print("Connection refused...")
#     print(ex)
