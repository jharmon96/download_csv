import settings
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pathlib import Path

home = str(Path.home())


# starts google chrome in either headless (export) or standard (import) mode.

def initialize_browser():
    chromeOptions = webdriver.ChromeOptions()
    prefs = {"download.default_directory": settings.source_path + r"\unanet_AQC_imu\reference_files"}
    chromeOptions.add_experimental_option("prefs", prefs)
    # chromeOptions.add_argument("--headless")
    caps = DesiredCapabilities().CHROME
    # caps["pageLoadStrategy"] = "normal"  #  complete
    caps["pageLoadStrategy"] = "none"  # interactive
    chromeDriver = settings.source_path + r'\unanet_AQC_imu\python\driver\chromedriver.exe'
    settings.driver = webdriver.Chrome(desired_capabilities=caps, executable_path=chromeDriver,
                                       chrome_options=chromeOptions)


# logs into the browser with credentials provided in settings.py

def login():
    wait = WebDriverWait(settings.driver, 10)
    settings.driver.get(settings.URL + "/login")
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#username')))
    id_box = settings.driver.find_element_by_name('username')
    id_box.send_keys(settings.username)

    pass_box = settings.driver.find_element_by_name('password')
    pass_box.send_keys(settings.password)

    login_button = settings.driver.find_element_by_name('button_ok')
    login_button.click()
