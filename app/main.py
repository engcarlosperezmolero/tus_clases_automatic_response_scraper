import os
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException


options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--user-agent=""Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36""')
driver = webdriver.Chrome('chromedriver', options=options)


user_tus_clases = os.getenv("TUS_CLASES_USER")
password_tus_clases = os.getenv("TUS_CLASES_PASSWORD")
user_gmail = os.getenv("GMAIL_USER")
password_gmail = os.getenv("GMAIL_PASSWORD")

if None in [user_tus_clases, password_tus_clases, user_gmail, password_gmail]:
  raise ValueError("Environments variables are not valid.")
  

def send_notifying_mail(names: list = None, mail_user: str = "", mail_password: str = "") -> None:
    """sends a mail notifying me the persons that have received the automatic message."""
    if names == None or (len(names) == 0):
        return None

    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    message = f"Subject: TUS CLASES MENSAJE AUTOMATICO\n\nFollowing people ({len(names)}) have received the message: {', '.join(u)}."
    s.starttls()
    s.login(mail_user, mail_password)
    s.sendmail(mail_user, mail_user, message)
    s.quit()





cuerpo_mensaje_automatizado = "Hola %nombre%, este es un mensaje automatizado. En caso de que necesites una respuesta inmediata me"\
                              " puedes escribir a mi WhatsApp: +5491122510584"
nombres_nuevos = []
driver.get("https://www.tusclases.com.ar/area-profesores/messaging")
time.sleep(2)
driver.set_window_size(4096, 2160)
# driver.save_screenshot("screenshot_tusclases_0.png")

try:
    input_email = driver.find_element(by=By.XPATH, value="/html/body/div[2]/form/div[3]/div/div/div/div[2]/div[2]/div[1]/div[2]/div/div/div[1]/input")
    input_password = driver.find_element(by=By.XPATH, value="/html/body/div[2]/form/div[3]/div/div/div/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/input")
    input_email.send_keys(credentials.tus_clases_user)
    input_password.send_keys(credentials.tus_clases_password + Keys.ENTER)
    time.sleep(2)
    # driver.save_screenshot("screenshot_tusclases_1.png")

except NoSuchElementException as e:
    print(f"La sesion ya fue iniciada. Procediendo a enviar los mensajes automatizados.")
finally:
    mensajes_no_leidos = driver.find_elements(by=By.XPATH, value="/html/body/div[2]/form/div[3]/div/div/div/div[1]/div[3]/*[@class='rc unread']")
    mensajes = driver.find_elements(by=By.XPATH, value="/html/body/div[2]/form/div[3]/div/div/div/div[1]/div[3]/*[contains(@class, 'rc')]")

    if len(mensajes_no_leidos) == 0:
        for num_mensaje, mensaje in enumerate(mensajes):
            # solo itera los 5 primeros mensajes
            if num_mensaje == 5:
                break
                
            mensaje.click()
            time.sleep(2)
            nombre = driver.find_element(by=By.XPATH, value="/html/body/div[2]/form/div[3]/div/div/div/div[2]/div[1]/div[1]/div[3]/div").get_attribute("innerHTML").strip().split(" ")[0]
            mensajes_enviados_por_mi = driver.find_elements(by=By.XPATH, value="/html/body/div[2]/form/div[3]/div/div/div/div[2]/div[3]/*[contains(@class, 'conb me')]/*[@class='lin']")
            texto_total_enviado = " | ".join([mensaje.get_attribute("innerHTML") for mensaje in mensajes_enviados_por_mi])

            if len(mensajes_enviados_por_mi) == 0 or "+5491122510584" not in texto_total_enviado:
                text_area = driver.find_element(by=By.XPATH, value="/html/body/div[2]/form/div[3]/div/div/div/div[2]/div[4]/div/div[1]/div/textarea")
                text_area.send_keys(cuerpo_mensaje_automatizado.replace("%nombre%", nombre) + Keys.TAB + Keys.ENTER)
                print(f"El mensaje fue enviado a {nombre}.")
                nombres_nuevos.append(nombre)

    else:
        for mensaje_no_leido in mensajes_no_leidos:
            mensaje_no_leido.click()
            time.sleep(2)
            nombre = driver.find_element(by=By.XPATH, value="/html/body/div[2]/form/div[3]/div/div/div/div[2]/div[1]/div[1]/div[3]/div").get_attribute("innerHTML").strip().split(" ")[0]
            text_area = driver.find_element(by=By.XPATH, value="/html/body/div[2]/form/div[3]/div/div/div/div[2]/div[4]/div/div[1]/div/textarea")
            text_area.send_keys(cuerpo_mensaje_automatizado.replace("%nombre%", nombre) + Keys.TAB + Keys.ENTER)
            print(f"El mensaje fue enviado a {nombre}.")
            nombres_nuevos.append(nombre)


    send_notifying_mail(nombres_nuevos, user_gmail, password_gmail)
    print("Sucess running all the code!")
