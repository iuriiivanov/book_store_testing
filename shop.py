"""
http://practice.automationtesting.in/
Shop
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

# ============================== Shop: отображение страницы товара
with webdriver.Chrome() as driver:
    driver.maximize_window()
    wait = WebDriverWait(driver, 5)

    driver.get('http://practice.automationtesting.in/')

    my_account_item = driver.find_element(By.CSS_SELECTOR, '#menu-item-50 > a')
    my_account_item.click()

    login_email_fld = driver.find_element(By.ID, 'username')
    login_email_fld.send_keys('anon@email.xyz')

    login_password_fld = driver.find_element(By.ID, 'password')
    login_password_fld.send_keys('t#d67Q$jiV')

    login_btn = driver.find_element(By.CSS_SELECTOR, 'div.u-column1.col-1 input.woocommerce-Button.button')
    login_btn.click()

    shop_item = driver.find_element(By.CSS_SELECTOR, '#menu-item-40 > a')
    shop_item.click()

    book = driver.find_element(By.CSS_SELECTOR, 'li.post-181 h3')
    book.click()

    book_title = driver.find_element(By.CSS_SELECTOR, '#product-181 h1')
    assert "HTML5 Forms" in book_title.text

# ============================== Shop: количество товаров в категории
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

    shop_item = driver.find_element(By.CSS_SELECTOR, '#menu-item-40 > a')
    shop_item.click()

    html_category_item = driver.find_element(By.CSS_SELECTOR, 'li.cat-item.cat-item-19 > a')
    html_category_item.click()

    html_category_amount = driver.find_elements(By.CSS_SELECTOR, '#content > ul > li')
    assert len(html_category_amount) == 3

# ============================== Shop: сортировка товаров
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

    shop_item = driver.find_element(By.CSS_SELECTOR, '#menu-item-40 > a')
    shop_item.click()

    order_by_select = Select(driver.find_element(By.CSS_SELECTOR, '#content > form > select'))
    assert order_by_select.first_selected_option.get_attribute('value') == 'menu_order'
    order_by_select.select_by_value('price-desc')
    order_by_select = Select(driver.find_element(By.CSS_SELECTOR, '#content > form > select'))
    assert order_by_select.first_selected_option.get_attribute('value') == 'price-desc'

# ============================== Shop: отображение, скидка товара
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

    shop_item = driver.find_element(By.CSS_SELECTOR, '#menu-item-40 > a')
    shop_item.click()

    book_title = driver.find_element(By.CSS_SELECTOR, 'li.post-169 h3')
    book_title.click()

    book_old_price = driver.find_element(By.CSS_SELECTOR, 'del span')
    assert book_old_price.text == '₹600.00'

    book_new_price = driver.find_element(By.CSS_SELECTOR, 'ins span')
    assert book_new_price.text == '₹450.00'

    book_cover = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#product-169 img')))
    book_cover.click()

    book_cover_preview_close_btn = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'div.pp_details > a')))
    book_cover_preview_close_btn.click()

# ============================== Shop: проверка цены в корзине
with webdriver.Chrome() as driver:
    driver.maximize_window()

    driver.get('http://practice.automationtesting.in/')

    shop_item = driver.find_element(By.CSS_SELECTOR, '#menu-item-40 > a')
    shop_item.click()

    add_to_basket_btn = driver.find_element(By.CSS_SELECTOR, 'li.post-182 .ajax_add_to_cart')
    add_to_basket_btn.click()

    time.sleep(3)

    basket_items_amount = driver.find_element(By.CLASS_NAME, 'cartcontents')
    assert basket_items_amount.text == '1 Item'

    basket_items_price = driver.find_element(By.CSS_SELECTOR, '#wpmenucartli span.amount')
    assert basket_items_price.text == '₹180.00'

    basket_btn = driver.find_element(By.ID, 'wpmenucartli')
    basket_btn.click()

    wait.until(ec.text_to_be_present_in_element((By.CSS_SELECTOR, 'tr.cart-subtotal > td > span'), '₹180.00'))

    wait.until(ec.text_to_be_present_in_element((By.CSS_SELECTOR, 'tr.order-total > td > strong > span'), '₹189.00'))

# ============================== Shop: работа в корзине
with webdriver.Chrome() as driver:
    driver.maximize_window()

    driver.get('http://practice.automationtesting.in/')

    shop_item = driver.find_element(By.CSS_SELECTOR, '#menu-item-40 > a')
    shop_item.click()

    driver.execute_script('window.scrollBy(0, 300);')

    time.sleep(2)

    add_book1_to_basket_btn = driver.find_element(By.CSS_SELECTOR, 'li.post-182 .ajax_add_to_cart')
    add_book1_to_basket_btn.click()

    time.sleep(1)

    add_book2_to_basket_btn = driver.find_element(By.CSS_SELECTOR, 'li.post-180 .ajax_add_to_cart')
    add_book2_to_basket_btn.click()

    basket_btn = driver.find_element(By.ID, 'wpmenucartli')
    basket_btn.click()

    basket_book1_del_btn = driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(1) > td.product-remove > a')
    basket_book1_del_btn.click()

    time.sleep(3)

    basket_del_undo_btn = driver.find_element(By.CSS_SELECTOR, '.woocommerce-message > a')
    basket_del_undo_btn.click()

    basket_book2_quantity_fld = driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(1) td.product-quantity input')
    basket_book2_quantity_fld.clear()
    basket_book2_quantity_fld.send_keys('3')

    time.sleep(3)

    basket_update_btn = driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(3) > td > input.button')
    basket_update_btn.click()

    assert basket_book2_quantity_fld.get_attribute('value') == '3'

    time.sleep(3)

    basket_apply_coupon_btn = driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(3) > td > div > input.button')
    basket_apply_coupon_btn.click()

    enter_a_coupon_code_msg = wait.until(ec.text_to_be_present_in_element(
        (By.CSS_SELECTOR, 'div.woocommerce > ul > li'), 'Please enter a coupon code.'))

# ============================== Shop: покупка товара
with webdriver.Chrome() as driver:
    driver.maximize_window()

    driver.get('http://practice.automationtesting.in/')

    shop_item = driver.find_element(By.CSS_SELECTOR, '#menu-item-40 > a')
    shop_item.click()

    driver.execute_script('window.scrollBy(0, 300);')

    add_book1_to_basket_btn = driver.find_element(By.CSS_SELECTOR, 'li.post-182 .ajax_add_to_cart')
    add_book1_to_basket_btn.click()

    time.sleep(2)

    basket_btn = driver.find_element(By.ID, 'wpmenucartli')
    basket_btn.click()

    proceed_to_checkout_btn = wait.until(ec.element_to_be_clickable(
        (By.CSS_SELECTOR, '.woocommerce > div > div > div > a')))
    proceed_to_checkout_btn.click()

    billing_first_name_fld = driver.find_element(By.ID, 'billing_first_name')
    wait.until(ec.visibility_of(billing_first_name_fld))
    billing_first_name_fld.send_keys('John')

    billing_last_name_fld = driver.find_element(By.ID, 'billing_last_name')
    billing_last_name_fld.send_keys('Doe')

    billing_email_fld = driver.find_element(By.ID, 'billing_email')
    billing_email_fld.send_keys('john_doe@email.xyz')

    billing_phone_fld = driver.find_element(By.ID, 'billing_phone')
    billing_phone_fld.send_keys('+1322223322')

    country_expand_select = driver.find_element(By.CSS_SELECTOR, '#s2id_billing_country > a > span.select2-arrow > b')
    country_expand_select.click()
    country_enter_text_select = driver.find_element(By.ID, 's2id_autogen1_search')
    country_enter_text_select.send_keys('Russia')
    country_pick_select = driver.find_element(By.ID, 'select2-results-1')
    country_pick_select.click()

    billing_address_1_fld = driver.find_element(By.ID, 'billing_address_1')
    billing_address_1_fld.send_keys('Basseynaya Street, 21')

    billing_city_fld = driver.find_element(By.ID, 'billing_city')
    billing_city_fld.send_keys('Sankt-Peterburg')

    billing_state_fld = driver.find_element(By.ID, 'billing_state')
    billing_state_fld.send_keys('Russia')

    billing_postcode_fld = driver.find_element(By.ID, 'billing_postcode')
    billing_postcode_fld.send_keys('196191')

    driver.execute_script('window.scrollBy(0, 300);')

    check_payments_chkbox = driver.find_element(By.ID, 'payment_method_cheque')
    check_payments_chkbox.click()

    place_order_btn = driver.find_element(By.ID, 'place_order')
    place_order_btn.click()

    wait.until(ec.text_to_be_present_in_element(
        (By.CSS_SELECTOR, 'p.woocommerce-thankyou-order-received'), 'Thank you. Your order has been received.'))

    wait.until(ec.text_to_be_present_in_element(
        (By.CSS_SELECTOR, 'li.method > strong'), 'Check Payments'))
