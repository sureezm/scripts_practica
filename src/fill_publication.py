import mysql.connector
from mysql.connector import Error
from dataframe_publications import pubs

#database connection
try:
    connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        db='ref_rank' 
    )

    if connection.is_connected():
        #QUERY
        cursor=connection.cursor()
        cursor.executemany("""INSERT INTO publication (ID, title, doi) VALUES (%s, %s, %s)""",pubs)

        
        if(len(pubs) == cursor.rowcount):
            connection.commit()
            print("{} rows inserted.".format(len(pubs)))

except Error as ex:
    print("Error during connection: {}".format(ex))

finally:
    if connection.is_connected():
            connection.close()
            print("Connection closed.")




    