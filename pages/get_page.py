from selenium.webdriver.support.ui import WebDriverWait

class GetPage:
    # Initalise Driver and Configuration from conftest in init method
    def __init__(self,driver,config):
        self.driver=driver
        self.wait=WebDriverWait(driver,10)
        self.config =config
        
    #Get Function to open test URL
    def get_url(self):
        self.driver.get(self.config["url"])
  