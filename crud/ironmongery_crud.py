#Import the file connection
from databases.connection import get_connection

def get_all_products():
    #Make the connection with database.
    connection = get_connection()
    if not connection:
        return {"Error": "Can't connected with database."}
    
    try:
        #Create a cursor (Is important) with dictionary=True because this brings the table in a list.
        cursor = connection.cursor(dictionary=True)

        #Make the consult to this function and execute.
        query = "SELECT * FROM productos"
        cursor.execute(query)

        #We saved everything the cursos brought and return.
        products = cursor.fetchall()
        return products
    
    except Exception as Exc:
        print(f"Error: {Exc}")
        return {"Error": str(Exc)}
    
    #Finally, close the connection with database
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'connection' in locals() and connection:
            connection.close()

#This function getting products with ID
def get_one_product(id_product:int):
    #Connect with database
    connection = get_connection()
    if not connection:
        return {"Error": "Can't connected with database."}
    try:
        #Create the cursor
        cursor = connection.cursor()

        #Make query and execute the query
        query = "SELECT * FROM productos WHERE id = %s"

        #Create the tupla
        id = (
            id_product,
        )

        cursor.execute(query, id)

        #Safe the list
        products = cursor.fetchall()
        return products
    
    except Exception as Exc:
        return {"Error": "Error to consult.", "detail": str(Exc)}
    
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'connection' in locals() and connection:
            connection.close()

def create_product(iron_data: dict):
    connection = get_connection()
    if not connection:
        return {"Error": "Can't connected with database."}
    try:
        cursor = connection.cursor()

        #Create the query
        query = "INSERT INTO productos (nombre, precio_costo, precio_venta, cantidad_actual, stock_minimo_alerta) VALUES (%s,%s,%s,%s,%s)"
        
        values = (
            iron_data["nombre"],
            iron_data["precio_costo"],
            iron_data["precio_venta"],
            iron_data["cantidad_actual"],
            iron_data["stock_minimo_alerta"]
        )

        cursor.execute(query, values)

        #Safe changes
        connection.commit()

        return {"success":"successful", "message":"The insert was successful"}
    
    except Exception as Exc:
        return {"Error": "Error to consult.", "detail": str(Exc)}
    
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'connection' in locals() and connection:
            connection.close()

def update_product_crud(iron_id: int, iron_price_cost: float, iron_price_sale: float, iron_amount: int):
    connection = get_connection()
    if not connection:
        return {"Error": "Can't connected with database."}
    
    try:
        cursor = connection.cursor()

        #Create the query
        query = "UPDATE productos SET precio_costo = %s, precio_venta = %s, cantidad_actual = %s WHERE id = %s"
        
        values = (
            iron_price_cost,
            iron_price_sale,
            iron_amount,
            iron_id
        )

        cursor.execute(query, values)

        connection.commit()

        return {"status": "Successful", "message": "Update was successful"}
    
    except Exception as Exc:
        return {"Error": "Error to update.", "detail": str(Exc)}
    
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'connection' in locals() and connection:
            connection.close()

def delete_product_crud(iron_id: int):
    connection = get_connection()
    if not connection:
        return {"Error": "Can't connected with database."}
    
    try:
        cursor = connection.cursor()

        query = "DELETE FROM productos WHERE id = %s"

        value = (
            iron_id,
        )

        cursor.execute(query, value)

        connection.commit()

        return {"status": "Success", "message": "Delete successful."}
    
    except Exception as Exc:
        return {"Error": "Error to delete.", "detail": str(Exc)}
    
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'connection' in locals() and connection:
            connection.close()

def get_low_amount():
    connection = get_connection()
    if not connection:
        return {"Error": "Can't connected with database."}
    
    try:
        cursor = connection.cursor(dictionary= True)

        query = "SELECT * FROM productos WHERE cantidad_actual <= stock_minimo_alerta"

        cursor.execute(query)

        alert = cursor.fetchall()
        return alert

    except Exception as Exc:
        return {"Error": "Error to query.", "detail": str(Exc)}
    
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'connection' in locals() and connection:
            connection.close()


#This function serves for check that the ID really exist.
def check_iron_exists(iron_id: int) -> bool:
    connection = get_connection()
    if not connection:
        return {"Error": "Was error when connected with database."}
    
    try:
        cursor = connection.cursor()

        #This serves for find the ID specific.
        query = "SELECT COUNT(*) FROM productos WHERE id = %s"
        cursor.execute(query, (iron_id,))

        (exists,) = cursor.fetchone()

        return exists > 0
    
    except Exception as Exc:
        print(f"Error: {Exc}")
        return False
    
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'connection' in locals() and connection:
            connection.close()