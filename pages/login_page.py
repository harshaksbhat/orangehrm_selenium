from selenium.webdriver.common.by import By
from pages.get_page import Get_Page

class Login_Page(Get_Page):
    username=(By.XPATH,"//input[@name='username']")
    password=(By.XPATH,"//input[@name='password']")
    login_button=(By.XPATH,"//button[@type='submit']")
    
    # def __init__(self,driver):
    #     self.driver=driver

    def enter_username(self,username):
        self.driver.find_element(*self.username).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(*self.password).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()