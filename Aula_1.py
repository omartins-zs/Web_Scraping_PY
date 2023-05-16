# Instalando Bibliotecas e Dependencias

# Instalando o Selenium
!pip install selenium

# Atualizando o Ubuntu para executar corretamento o apt-install
!apt-get update

# Instalando o ChromeDrive e Trazendo ele para a Pasta Local
!apt install chromium-chromedriver

!cp /usr/lib/chromium-browser/chromedriver /usr/bin
import sys
sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')