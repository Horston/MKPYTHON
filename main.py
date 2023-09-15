from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


#Переменная смысловой нагрузки для определения ХромДрайвера настроек
options = webdriver.ChromeOptions()


options.add_argument("--disable-blink-features=AutomationControlled")


#Фоновый режим
options.headless = True

#Переменная где мы используем именно ХромДрайвер из библиотеки
driver = webdriver.Chrome(
    options=options
)

try:
    #
    print("Готово")
    driver.get('https://vk.com')
    time.sleep(15)

    #Принт для вывода информации. переменную для ввода данных, мы создаем для логической цепочки
    print("вводим логин")
    login_input = driver.find_element(By.ID, 'index_email')
    login_input.clear()
    login_input.send_keys("Пишем Логин")
    login_input.send_keys(Keys.ENTER)
    time.sleep(15)

    #переменная для поиска по имени пароль
    password_input = driver.find_element(By.NAME, 'password')
    password_input.clear()
    password_input.send_keys("Пишем Пароль")
    password_input.send_keys(Keys.ENTER)
    time.sleep(25)

except Exception as ex:
    print(ex)

#
finally:
    driver.close()
    driver.quit()
