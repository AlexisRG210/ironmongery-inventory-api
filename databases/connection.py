#Import this librery to connect with database
import mysql.connector

def get_connection():
    #Make a try to avoid any mistake
    try:
        #Create variable that contains the connection
        db_connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "ferreteria_db"
        )

        #This if ensures that the connection is successful
        if db_connection.is_connected():
            print("Connection Successful.")
        
        return db_connection

    except mysql.connector.Error as Error:
        print(f"Error: {Error}")
        return None