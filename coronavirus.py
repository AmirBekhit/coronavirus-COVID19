
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import re
from datetime import datetime
import smtplib
"""installing chromedriver :https://chromedriver.chromium.org/getting-started
then testing it on the terminal by typing (chromedriver)
installing selenium"""


class Coronavirus():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def get_data(self):
        # try:
        self.driver.get('https://www.worldometers.info/coronavirus/')
        table = self.driver.find_element_by_id('main_table_countries')
        country_element = table.find_element_by_xpath(
            "//td[contains(., 'China')]")
        row = country_element.find_element_by_xpath("./..")
        data = row.text.split(" ")
        total_cases = data[1]
        new_cases = data[2]
        total_deaths = data[3]
        new_deaths = data[4]
        active_cases = data[5]
        total_recovered = data[6]
        serious_critical = data[7]

        print("Country: " + country_element.text)
        print("Total cases: " + total_cases)
        print("New cases: " + new_cases)
        print("Total deaths: " + total_deaths)
        print("New deaths: " + new_deaths)
        print("Active cases: " + active_cases)
        print("Total recovered: " + total_recovered)
        print("Serious, critical cases: " + serious_critical)

        send_mail(country_element.text, total_cases, new_cases, total_deaths,
                  new_deaths, active_cases, total_recovered, serious_critical)
        print('Hey Email has been sent!')
        self.driver.close()
        # except:
        #     print('Something went wrong!')
        #     self.driver.quit()


def send_mail(country_element, total_cases, new_cases, total_deaths, new_deaths, active_cases, total_recovered, serious_critical):

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('bekdevelopment@gmail.com', 'iowbzvsuhsyvcpgu')

    subject = 'Coronavirus stats in your country today!'

    body = 'Today in ' + country_element + '\
            \nThere is new data on coronavirus:\
            \nTotal cases: ' + total_cases + '\
            \nNew cases: ' + new_cases + '\
            \nTotal deaths: ' + total_deaths + '\
            \nNew deaths: ' + new_deaths + '\
            \nActive cases: ' + active_cases + '\
            \nTotal recovered: ' + total_recovered + '\
            \nSerious, critical cases: ' + serious_critical + '\
            \nCheck the link: https://www.worldometers.info/coronavirus/'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'bekdevelopment@gmail.com',
        'amir.bekhit@outlook.com',
        msg
    )
    server.quit()


bot = Coronavirus()
bot.get_data()
