from pages.dashboard_page import Dashboard


def test_dashboard(driver,config):
    dashboard=Dashboard(driver,config)
    dashboard.get_url()
    dashboard.login(config["username"],config["password"])
 
    assert dashboard.title_iscorrect()
    assert dashboard.myinfo_visible()
    assert dashboard.dashboard_visible()