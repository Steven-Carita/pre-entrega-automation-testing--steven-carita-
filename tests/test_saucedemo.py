from utils.helpers import login
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Automatizacion de Login  

def test_login(driver): 
    login(driver, "standard_user", "secret_sauce")
    
    assert "inventory.html" in driver.current_url 
    
    title = driver.find_element(By.CLASS_NAME, "title").text
    assert title == "Products"     
    

#Automatizacion de Navegación y Verificacion del Catalogo
    
def test_catalogo_products(driver):
    login(driver, "standard_user", "secret_sauce")
    
    menu = driver.find_element(By.ID, "react-burger-menu-btn")
    assert menu.is_displayed()        
    
    filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")
    assert filtro.is_displayed()
    
    assert "inventory.html" in driver.current_url 
    
    productos = driver.find_elements(By.CSS_SELECTOR, "[data-test='inventory-item']")
    assert len(productos) > 0     
    
    nombre = productos[0].find_element(By.CLASS_NAME, "inventory_item_name").text   
    assert nombre == "Sauce Labs Backpack"
    
#Automatizacion de Interaccion con Productos
    
def test_agregar_producto_al_carrito(driver):
    login(driver, "standard_user", "secret_sauce")
    wait = WebDriverWait(driver, 12)
    
    
    nombre_producto = driver.find_element(By.CLASS_NAME, "inventory_item_name").text

    
    btn_agregar= wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Add to cart')]"))
    )
    btn_agregar.click() 
    
    
    #validar contador 
    
    badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert badge.text == "1"                
    
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()    
    
    #validar productos en el carrito
    
    producto_carrito = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert producto_carrito == nombre_producto
    