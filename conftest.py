import pytest
from pathlib import Path
from selenium import webdriver
import json

#Code to Store Reports in /reports folder
REPORT_DIR = Path(__file__).parent / "reports"


def get_next_report_number():
    REPORT_DIR.mkdir(exist_ok=True)

    existing_reports = list(REPORT_DIR.glob("report-*.html"))

    if not existing_reports:
        return 1

    numbers = []

    for report in existing_reports:
        try:
            number = int(report.stem.split("-")[1])
            numbers.append(number)
        except (IndexError, ValueError):
            pass

    return max(numbers, default=0) + 1


def pytest_configure(config):
    report_number = get_next_report_number()
    report_path = REPORT_DIR / f"report-{report_number}.html"

    config.option.htmlpath = str(report_path)

#Fixture for setup and teardown
@pytest.fixture
def driver():
    driver = webdriver.Chrome()

    try:
        driver.maximize_window()
        driver.implicitly_wait(5)
        yield driver
    finally:
        driver.quit()

#Fixture to load json data from config folder
@pytest.fixture
def config():
    config_path=Path(__file__).parent /"config" / "config.json"

    with open(config_path,"r") as file:
        return json.load(file)