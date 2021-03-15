from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver_path = '/Users/Jope/Development/chromedriver'

driver = webdriver.Chrome(executable_path=driver_path)

driver.get('https://orteil.dashnet.org/experiments/cookie/')

cookie = driver.find_element_by_id('cookie')


def price_check():
    price_data = driver.find_elements_by_css_selector('#store div b')
    price_list = []
    for i in range(len(price_data) - 1):
        y = price_data[i].text.split(' -')[0]
        x = price_data[i].text.split('- ')[1]
        if ',' in x:
            x = int(x.replace(',', ''))
        else:
            x = int(x)
        price_list.append({'name': y, 'price': x})
    return price_list

def check_wallet():
    money = driver.find_element_by_id('money').text
    if ',' in money:
        money = int(money.replace(',', ''))
    else:
        money = int(money)
    return(money)

def pause_n_click():
    prices = price_check()
    current_funds = check_wallet()

    for choice in prices[:]:
        if choice['price'] > current_funds:
            prices.remove(choice)

    click_this = prices[-1]['name']
    driver.find_element_by_id(f'buy{click_this}').click()
    time.sleep(2)

def set_timer():
    cooldown = time.time() + 5
    return cooldown

def total_run():
    runtime = time.time() + 20
    return runtime


game_on = True

cooldown = set_timer()
runtime = total_run()

while game_on:
    cookie.click()

    if runtime < time.time():
        print("time's up!")
        print(check_wallet())
        driver.close()
        game_on = False
    elif cooldown < time.time():
        try:
            pause_n_click()
            cooldown = set_timer()
        finally:
            continue








