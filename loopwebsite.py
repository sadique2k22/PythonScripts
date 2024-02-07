from selenium import webdriver
import time

# URL of the main page
MAIN_PAGE_URL = 'https://payglas.site'

# URL of the website you want to visit in the new tabs
WEBSITE_URL = 'https://payglas.site/get.php'

# Number of tabs to open at once
NUM_TABS = 5

# Time delay between opening new tabs
TAB_DELAY = 0.5  # in seconds

# Time delay before closing tabs
CLOSING_DELAY = 3  # in seconds

# Create a new instance of the webdriver
driver = webdriver.Chrome()  # Assuming chromedriver.exe is in the same directory as the script

# Open the main page
driver.get(MAIN_PAGE_URL)

# Loop to open tabs in batches
xx = input("enter here: ")
if xx == "y":
    #if xx=="y":
    while True:
        # Open new tabs
        for _ in range(NUM_TABS):
            driver.execute_script("window.open('{}', '_blank');".format(WEBSITE_URL))
            time.sleep(TAB_DELAY)
    
        # Wait for 2 seconds
        time.sleep(CLOSING_DELAY)
    
        # Close all the tabs except the main one
        for handle in driver.window_handles[1:]:
            driver.switch_to.window(handle)
            driver.close()
    
        # Switch back to the main page
        driver.switch_to.window(driver.window_handles[0])

else:
    driver.quit()
