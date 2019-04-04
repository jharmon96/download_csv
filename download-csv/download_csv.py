import settings
import standard_functions

# Used in case of export
output_file = []


# Navigates to the proper pages where changes are to be made / information is to be read, then kicks off the Import /
# Export function

def navigate():

        # Navigates to the URL for the given Expense Type, then clicks the edit pencil for the given Project Type

        webPage = settings.URL + "/reports/financials/general_ledger/detail/report?runFrom=S_175"
        settings.driver.get(webPage)
        xpathId = '//*[@id="nav-links-top"]/a[4]/img'
        settings.driver.find_element_by_xpath(xpathId).click()

