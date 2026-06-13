from databases.connection import get_connection

def check_user_credentials(username: str, password: str):
    connection = get_connection()
    if not connection:
        return {"Error": "Can't connected with database."}
    
    try:
        #Create a cursor
        cursor = connection.cursor()

        query = "SELECT * FROM usuarios WHERE username = %s AND password_hash = %s"

        value = (
            username,
            password
        )

        cursor.execute(query, value)

        products = cursor.fetchall()
        return products
    
    except Exception as Exc:
        return {"Error": "Error to consult.", "detail": str(Exc)}
    
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'connection' in locals() and connection:
            connection.close()