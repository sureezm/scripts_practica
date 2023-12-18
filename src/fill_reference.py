import mysql.connector
from mysql.connector import Error
from dataframe_references import refs

#database connection
try:
    connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        db='ref_db' 
    )

    if connection.is_connected():
        #QUERY
        cursor=connection.cursor()
        cursor.executemany("""INSERT INTO reference_exp (PUBID, RID, title_exp) VALUES (%s, %s, %s)""",refs)
        connection.commit()

        print(len(refs))
        print(cursor.rowcount)
        
        if(len(refs) == cursor.rowcount):
            connection.commit()
            print("{} rows inserted.".format(len(refs)))

except Error as ex:
    print("Error during connection: {}".format(ex))

finally:
    if connection.is_connected():
            connection.close()
            print("Connection closed.")




    