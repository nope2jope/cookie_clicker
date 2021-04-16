from selenium import webdriver
import time


class Puppet:
    def __init__(self, path, link, wait_time):
        self.driver = webdriver.Chrome(executable_path=path)
        self.price_list = []
        # this wait is a time.sleep function to give the driver some breathing room
        # and ensure elements are findable/clickable
        self.wait = wait_time
        # class opens game upon being called, but could just as easily be broken out to a separate call
        self.driver.get(link)

    def price_check(self):
        price_data = self.driver.find_elements_by_css_selector('#store div b')
        # the price data from above is presented as a list of strings, reformatted below along the hyphen
        for i in range(len(price_data) - 1):
            # purchase names
            y = price_data[i].text.split(' -')[0]
            # purchase prices
            x = price_data[i].text.split('- ')[1]
            # another step in reformatting variable, plus changing type to int
            if ',' in x:
                x = int(x.replace(',', ''))
            else:
                x = int(x)
            self.price_list.append({'name': y, 'price': x})
        return self.price_list

    def check_wallet(self):
        money = self.driver.find_element_by_id('money').text
        if ',' in money:
            money = int(money.replace(',', ''))
        else:
            money = int(money)
        return money

    def pause_n_click(self):
        prices = self.price_check()
        current_funds = self.check_wallet()

        # any nonpurchasable options removed from the options
        for choice in prices[:]:
            if choice['price'] > current_funds:
                prices.remove(choice)

        # find and click the most expensive (last) entry in list
        click_this = prices[-1]['name']
        self.driver.find_element_by_id(f'buy{click_this}').click()

        # confirm selection, give the driver a break
        time.sleep(self.wait)

    def slam_cookie(self):
        # make dough?
        cookie = self.driver.find_element_by_id('cookie')
        cookie.click()

    def set_timer(self):
        # sets increment between price-checks, etc.
        cooldown = time.time() + self.wait
        return cooldown
