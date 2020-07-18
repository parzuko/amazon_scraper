import time
from configs import(
    get_web_driver_options,
    get_chrome_driver,
    set_ignore_certificate_error,
    set_browser_as_incognito,
    NAME,
    CURRENCY,
    FILTERS,
    BASE_URL,
    DIRECTORY
    )

class GenerateReport():
    def __init__(self):
        pass



class AmazonAPI():
    def __init__(self, search_term, filters, base_url, currency):
        self.base_url = base_url
        self.search_term = search_term
        options = get_web_driver_options()
        set_browser_as_incognito(options)
        set_browser_as_incognito(options)
        self.driver = get_chrome_driver(options)
        self.currency = currency
        self.price_filter = f"&rh=p_36{filters['min']}00-{filters['max']}00"

    def run(self):
        print("Starting Script......")
        print(f"Looking for {self.search_term} products...")
        links = self.get_products_links()
        time.sleep(3)

        self.driver.quit()

    def get_products_links(self):
        self.driver.get(self.base_url)
        element = self.driver.find_element_by_class_name("nav-input")
        element.send_keys(self.search_term)
        element.send_keys(Keys.ENTER)
        time.sleep(2)



if __name__ == '__main__':
    print("HELo")
    amazon = AmazonAPI(NAME, FILTERS, BASE_URL, CURRENCY)
    amazon.run()