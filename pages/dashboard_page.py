from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from selenium.webdriver.support import expected_conditions as EC


class Dashboard(LoginPage):

    my_info = (By.XPATH, "//span[normalize-space()='My Info']")
    dashboard = (By.XPATH, "//span[normalize-space()='Dashboard']")

    def title_iscorrect(self):
        return self.driver.title == "OrangeHRM"

    def myinfo_visible(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.my_info)
        ).is_displayed()

    def dashboard_visible(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.dashboard)
        ).is_displayed()
