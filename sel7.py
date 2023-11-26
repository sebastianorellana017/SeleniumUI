from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver #permite guardar la instancia del navegador como argumento
        self.url = 'https://opencart.abstracta.us/index.php?route=account/login'
        self.email_locator = (By.ID, 'input-email') #label 1
        self.password_locator = (By.ID, 'input-password') #label 2
        self.login_button_locator = (By.XPATH, '//*[@id="content"]/div/div[2]/div/form/input') #boton formulario login

    def open(self):
        self.driver.get(self.url)

    def login(self, email, password):
        email_input = self.driver.find_element(*self.email_locator) #localizar label email
        email_input.clear()  # Limpiar el campo de correo electrónico para asegurarse de que esté vacío
        email_input.send_keys(email)

        password_input = self.driver.find_element(*self.password_locator) #localizar label password
        password_input.clear()  # Limpiar el campo de contraseña para asegurarse de que esté vacío
        password_input.send_keys(password)

        self.driver.find_element(*self.login_button_locator).click()

class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_input_locator = (By.XPATH, '//*[@id="search"]/input') #parase en la barra de busqueda
        self.search_button_locator = (By.XPATH, '//*[@id="search"]/span/button/i') #Boton de la barra de busqueda
        self.add_to_cart_button_locator = (By.XPATH, '//*[@id="content"]/div[3]/div/div/div[2]/div[2]/button[1]/span')  #Agregar producto al carrito de compras

    def search_product(self, product_name):
        search_input = self.driver.find_element(*self.search_input_locator)
        search_input.clear()  
        search_input.send_keys(product_name)
        self.driver.find_element(*self.search_button_locator).click()

    def add_product_to_cart(self):
        try:
            add_to_cart_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.add_to_cart_button_locator)
            )
            add_to_cart_button.click()
            print("Producto agregado exitosamente.")
        except TimeoutException:
            print("El botón 'Agregar al carrito' no está presente después de la búsqueda.")

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_link_locator = (By.XPATH, '//*[@id="cart-total"]')      #view carrito chico
        self.view_cart_link_locator = (By.XPATH, '//*[@id="cart"]/ul/li[2]/div/p/a[1]/strong')     #view label buton para ir al carrito completo
        self.remove_product_locator = (By.XPATH, '//*[@id="content"]/form/div/table/tbody/tr/td[4]/div/span/button[2]/i')  #acceder al boton de remover producto
        self.continue_page_locator = (By.XPATH,'//*[@id="content"]/div/div/a')  #acceder al boton continuar

    def view_cart(self):
        self.driver.find_element(*self.cart_link_locator).click()

    def view_cart_contents(self):
        self.driver.find_element(*self.view_cart_link_locator).click()

    def remove_product(self):
        try:
            remove_product_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.remove_product_locator) #localizacion del boton
            )
            remove_product_button.click()
            print("Producto Removido exitosamente.")
        except TimeoutException:
            print("El botón 'Remover producto del carrito' no está presente.")

    def continue_page(self):
        try:
            continue_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.continue_page_locator) #localizacion del boton
            )
            continue_button.click()
            print("Redirigiendose a la pagina principal exitosamente.")
        except TimeoutException:
            print("El botón 'Continuar' no está presente.")

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.page_home_locator = (By.XPATH, '//*[@id="cart"]/button') #boton del carrito chico
    
    def page_home(self):
        try:
            home_button = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located(self.page_home_locator)
            )
            home_button.click() #viewcart
            print("Comprobando que el carrito esta vacio despues de haber terminado el flujo")
        except TimeoutException:
            print("El botón 'Carrito pequeno' no está presente.")

# Crea una instancia del navegador Chrome
driver = webdriver.Chrome()

# Crear instancias de los Page Objects model (clases)
login_page = LoginPage(driver)
search_page = SearchPage(driver)
cart_page = CartPage(driver)
home_page = HomePage(driver)

# Maximizar ventana
driver.maximize_window()
time.sleep(4) 

# Abrir la página de inicio de sesión y realizar el login
login_page.open()
time.sleep(4) 
login_page.login('rock@rock.cl', 'pass123')
time.sleep(4) 

# Buscar un producto y agregarlo al carrito
search_page.search_product('Iphone')
time.sleep(4)  

search_page.add_product_to_cart()
time.sleep(4)  

# Realizar acciones en el carrito
cart_page.view_cart()
time.sleep(4)  

cart_page.view_cart_contents()
time.sleep(4)  

cart_page.remove_product()
time.sleep(4)  

cart_page.continue_page()
time.sleep(4)

# Revisar la página principal y comprobar carro vacío
home_page.page_home()

# Espera un tiempo breve para que puedas ver lo que está sucediendo
time.sleep(6)

# Cierra el navegador
driver.quit()

