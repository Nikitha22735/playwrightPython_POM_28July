import sqlite3
import pytest


def fetchArtist(connection,sqlQuery):
    # connection = sqlite3.connect(r"C:\Users\Nikitha\AppData\Roaming\DBeaverData\workspace6\.metadata\sample-database-sqlite-1\Chinook.db")
    # try:
        script = connection.cursor()
        script.execute(sqlQuery)
        # print(script.fetchall())
        # print(script.fetchone())
        # print(script.fetchmany(3))
        results = script.fetchall()
        # print(script.description)
        return results
        # assert len(results)==347
        # print(len(results))
    # finally:
    #     connection.close()

# def fetchAll(connection,sqlQuery):
    
#     # try:
#         script = connection.cursor()
#         script.execute(sqlQuery)
#         # print(script.fetchall())
#         # print(script.fetchone())
#         # print(script.fetchmany(3))
#         results = script.fetchall()
#         print(script.description)
#         # assert len(results)==347
#         # print(len(results))
#     # finally:
    #     connection.close()

# @pytest.mark.db
def test_sql():
        connection = sqlite3.connect(r"C:\Users\Nikitha\AppData\Roaming\DBeaverData\workspace6\.metadata\sample-database-sqlite-1\Chinook.db")
        try:
           result= fetchArtist(connection,"select *  from Album WHERE  ArtistId = 2") 
           assert len(result)==3
        finally:
            connection.close()


# //////////////////////////////////mySql///////////////////////////////////

# pip install mysql-connector-python
def fetchArtist(connection,sqlQuery):
    connection = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="Chinook"
    )
    try:
        script = connection.cursor()
        script.execute(sqlQuery)
        print(script.fetchall())
        print(script.fetchone())
        print(script.fetchmany(3))
        results = script.fetchall()
        print(script.description)
        assert len(results)==347
        print(len(results))
    finally:
        connection.close()

# //////////////////////////////////oracle///////////////////////////////////

# pip install oracledb
def fetchArtist(connection,sqlQuery):
    connection = oracledb.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="Chinook"
    )
    try:
        script = connection.cursor()
        script.execute(sqlQuery)
        print(script.fetchall())
        print(script.fetchone())
        print(script.fetchmany(3))
        results = script.fetchall()
        print(script.description)
        assert len(results)==347
        print(len(results))
    finally:
        connection.close()
               

# //////////////////////////////////postgress///////////////////////////////////          
        
# pip install pycopg2-binary
def fetchArtist(connection,sqlQuery):
    connection = pycopg2.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="Chinook",
        port=5432
    )
    try:
        script = connection.cursor()
        script.execute(sqlQuery)
        print(script.fetchall())
        print(script.fetchone())
        print(script.fetchmany(3))
        results = script.fetchall()
        print(script.description)
        assert len(results)==347
        print(len(results))
    finally:
        connection.close()

# //////////////////////////////////snowflake///////////////////////////////////          
        
# pip install snowflake-connector-python
def fetchArtist(connection,sqlQuery):
    connection = snowflake.connector.connect(
        user='your_username',
        password='your_password',
        host='your_account.snowflakecomputing.com',
        port = 443,
        warehouse='your_warehouse',
        database='Chinook',
        schema='public',
        role='your_role',
        authenticator='snowflake'
    )
    try:
        script = connection.cursor()
        script.execute(sqlQuery)
        print(script.fetchall())
        print(script.fetchone())
        print(script.fetchmany(3))
        results = script.fetchall()
        print(script.description)
        assert len(results)==347
        print(len(results))
    finally:
        connection.close()
