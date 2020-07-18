from selenium import webdriver

DIRECTORY = 'reports'
NAME = 'PS4'
CURRENCY = '₹'
MIN_PRICE = '10000'
MAX_PRICE = '40000'
FILTERS = {
    'min' : MIN_PRICE,
    'max' : MAX_PRICE
}
BASE_URL = "http://www.amazon.in/"

def get_chrome_driver(options):
    return webdriver.Chrome(chrome_options =options)

def get_web_driver_options():
    return webdriver.ChromeOptions()

def set_ignore_certificate_error(options):
    options.add_argument('--ignore-certicate-errors')

def set_browser_as_incognito(options):
    options.add_argument('--incongito')
