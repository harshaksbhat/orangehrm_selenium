from pages.login_page import Login_Page


def test_login(driver,config):
    # Create login page object
    login_page=Login_Page(driver,config)
    
    #Open Webpage using the url in config JSON
    login_page.get_url()

    #Enter login Credentials, take values from config Json using fixture
    login_page.enter_username(config["username"])
    login_page.enter_password(config["password"])
    
    #Click Login
    login_page.click_login()
