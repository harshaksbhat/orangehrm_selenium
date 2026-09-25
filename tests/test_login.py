from pages.login_page import Login_Page

def test_login(driver):
# Create login page object
    login_page=Login_Page(driver)
    # Open Url
    login_page.get_url()

    #Enter login Credentials
    
    login_page.enter_username("admin")
    login_page.enter_password("admin123")
    #Click Login
    login_page.click_login()
