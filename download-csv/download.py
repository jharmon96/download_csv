import time
import settings
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Used in case of export
output_file = []


# Navigates to the proper pages where changes are to be made / information is to be read, then kicks off the Import /
# Export function

def navigate():
    # Navigates to the URL for the given Expense Type, then clicks the edit pencil for the given Project Type
    wait = WebDriverWait(settings.driver, 20)
    # Wait until dashboard appears (AKA successful login) before navigating to shared report
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#body > table > tbody > tr > td.reports')))
    webPage = settings.URL + "/reports/financials/general_ledger/detail/report?runFrom=S_165"
    settings.driver.get(webPage)
    # Wait until the download CSV button appears, click it, then wait 25 seconds for it to download
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#nav-links-top > a:nth-child(4)')))
    xpathId = '//*[@id="nav-links-top"]/a[4]/img'
    settings.driver.find_element_by_xpath(xpathId).click()
    time.sleep(20)


# Delete old file and rename new download file

def rename():

    # Rename file
    os.rename(settings.source_path + r'\unanet_AQC_imu\reference_files\report.csv',
              settings.source_path + r'\unanet_AQC_imu\reference_files\Datastore_GL_Transactions_v1-0.csv')
