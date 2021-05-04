"""
http://practice.automationtesting.in/
Registration login
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

# ============================== Registration login: регистрация аккаунта
with webdriver.Chrome() as driver:
    driver.maximize_window()

    driver.get('http://practice.automationtesting.in/')

    my_account_item = driver.find_element(By.CSS_SELECTOR, '#menu-item-50 > a')
    my_account_item.click()

    register_email_fld = driver.find_element(By.ID, 'reg_email')
    register_email_fld.send_keys('anon@email.xyz')

    register_password_fld = driver.find_element(By.ID, 'reg_password')
    register_password_fld.send_keys('t#d67Q$jiV')

    register_btn = driver.find_element(By.CSS_SELECTOR, 'div.u-column2.col-2 input.woocommerce-Button.button')
    register_btn.click()

# ============================== Registration login: логин в систему
with webdriver.Chrome() as driver:
    driver.maximize_window()

    driver.get('http://practice.automationtesting.in/')

    my_account_item = driver.find_element(By.CSS_SELECTOR, '#menu-item-50 > a')
    my_account_item.click()

    login_email_fld = driver.find_element(By.ID, 'username')
    login_email_fld.send_keys('anon@email.xyz')

    login_password_fld = driver.find_element(By.ID, 'password')
    login_password_fld.send_keys('t#d67Q$jiV')

    login_btn = driver.find_element(By.CSS_SELECTOR, 'div.u-column1.col-1 input.woocommerce-Button.button')
    login_btn.click()
