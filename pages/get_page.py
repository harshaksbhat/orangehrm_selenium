from selenium.webdriver.support.ui import WebDriverWait

class Get_Page:
    url="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,10)

    def get_url(self):
        self.driver.get(self.url)
  