from crud.ironmongery_crud import (
    check_iron_exists, 
    get_all_products, 
    get_one_product, 
    create_product, 
    update_product_crud, 
    delete_product_crud,
    get_low_amount
)
from fastapi import HTTPException, FastAPI #Specialized libraries
from pydantic import BaseModel

class IronSchema(BaseModel):
    nombre: str
    precio_costo: float
    precio_venta: float
    cantidad_actual: int
    stock_minimo_alerta: int

app = FastAPI()
#This is the root and links the function below
@app.get("/")
def inicio():
    return {"message": "Welcome to the Ironmongery API Core."}

#Get all products of database
@app.get("/iron")
def get_all():
    result = get_all_products()
    
    if isinstance(result, dict) and "Error" in result:
        raise HTTPException(status_code=500, detail=result["Error"])
    
    if not result:
        raise HTTPException(status_code=404, detail="No products found")
    
    return result

@app.get("/iron/alerts")
def get_alerts_stock():
    result = get_low_amount()
    if isinstance(result, dict) and "Error" in result:
        raise HTTPException(status_code="500", detail=result["Error"])
    return result

#Get only a product
@app.get("/iron/{id}")
def get_one(id:int):
    if not check_iron_exists(id):
        raise HTTPException(status_code="404", detail="No products found.")
    
    result = get_one_product(id)
    if not result:
        return {"Error":"No get product"}
    else:
        print("Get the product success.")
        return result
    
#Register a product
@app.post("/iron")
def register_products(item: IronSchema):
    #Convert data to dictionary
    dict_product = item.model_dump()

    result = create_product(dict_product)
    return result

@app.put("/iron")
def update_product_main(iron_id:int, iron_price_cost:float, iron_price_sale:float, iron_amount:int):
    if not check_iron_exists(iron_id):
        raise HTTPException(status_code=404, detail="Component not exists.")
    
    result = update_product_crud(iron_id, iron_price_cost, iron_price_sale, iron_amount)
    return result

@app.delete("/iron/{iron_id}")
def delete_product_main(iron_id:int):
    if not check_iron_exists(iron_id):
        raise HTTPException(status_code="404", detail="Component not exists")
    
    result = delete_product_crud(iron_id)
    return result