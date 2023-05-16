# Configuração do Web Driver

# Utilizando o WebDriver do Selenium
from selenium import webdriver

# Instanciando o Objeto ChromeOptions
options = webdriver.ChromeOptions()

# Passando algumas opções para esse ChromeOptions
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Criação do WebDriver do Chrome
wd_Chrome = webdriver.Chrome('chromedriver',options=options)