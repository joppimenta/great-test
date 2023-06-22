from selenium import webdriver
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from time import sleep
import pyautogui
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.organizze.com.br/')
driver.maximize_window()

begin_button = driver.find_element(By.XPATH, "//a[@href='https://auth.organizze.com.br/cadastro']")
begin_button.click()

WebDriverWait(driver, 60).until(expected_conditions.text_to_be_present_in_element((By.XPATH, "/html/body/section/div/h1"), "Crie sua conta como quiser"))

email_field = driver.find_element(By.ID, "email")
email_field.send_keys("joaopedropimenta2@gmail.com")

password_field = driver.find_element(By.ID, "password")
password_field.send_keys("abcd1234")

password_confirmation_field = driver.find_element(By.ID, "repeatPassword")
password_confirmation_field.send_keys("abcd1234")

terms_checkbox = driver.find_element(By.XPATH, "//*[@id='termsOfuse']")
terms_checkbox.click()

confirmation_button = driver.find_element(By.XPATH, "/html/body/section/div/form/button")
confirmation_button.click()