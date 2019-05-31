from os import sys, path
import os

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

import time
import download
import standard
import settings
from pynput.keyboard import Controller

# Main.py kicks off the script


# initialize keyboard controller
settings.keyboard = Controller()

# initialize web browser used to retrieve / input information
standard.initialize_browser()

# call the login function
standard.login()

# Kick off process
download.navigate()

# Rename file
download.rename()

# exit out of web browser
time.sleep(1)
settings.driver.quit()
