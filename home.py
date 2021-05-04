"""
http://practice.automationtesting.in/
Home page
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

# ============================== Home: добавление комментария
with webdriver.Chrome() as driver:
    driver.maximize_window()

    driver.get('http://practice.automationtesting.in/')

    driver.execute_script('window.scrollBy(0, 300);')

    selenium_ruby_book = driver.find_element(By.CSS_SELECTOR, '#text-22-sub_row_1-0-2-0-0 h3')
    selenium_ruby_book.click()

    reviews_tab = driver.find_element(By.CSS_SELECTOR, '#product-160 li.reviews_tab > a')
    reviews_tab.click()

    rating_5_stars = driver.find_element(By.CSS_SELECTOR, '#commentform a.star-5')
    rating_5_stars.click()

    review_fld = driver.find_element(By.ID, 'comment')
    review_fld.send_keys('Nice book!')

    name_fld = driver.find_element(By.ID, 'author')
    name_fld.send_keys('Anonymous User')

    email_fld = driver.find_element(By.ID, 'email')
    email_fld.send_keys('anon@email.xyz')

    submit_btn = driver.find_element(By.ID, 'submit')
    submit_btn.click()
