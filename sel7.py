from selenium import webdriver
import time

# Crea una instancia del navegador Chrome
driver = webdriver.Chrome()

# URL de la página web que deseas abrir
url = 'https://www.twitch.tv/rakyz'

# Abre la página web en el navegador
driver.get(url)

# Cierra el navegador después de un tiempo (por ejemplo, después de 5 segundos)
#driver.implicitly_wait(20)
#driver.quit()

# Añade una pausa de 10 segundos antes de cerrar la ventana del navegador
time.sleep(500)

# Cierra el navegador al finalizar el script
driver.quit()
