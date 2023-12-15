import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def lambda_handler(event, context):
    # Retrieve the URL from the event
    url = event.get("url")
    if not url:
        return {"statusCode": 400, "body": json.dumps("No URL provided")}

    # Set up Chrome options for Selenium
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1366x768")
    chrome_options.add_argument(
        "--disable-dev-shm-usage"
    )  # Overcome limited resource problems
    chrome_options.add_argument("--disable-extensions")  # Disable extensions
    chrome_options.add_argument("--no-first-run")  # Avoids first run dialogs
    chrome_options.add_argument("--disable-infobars")  # Disabling infobars
    chrome_options.add_argument("--disable-setuid-sandbox")  # Bypass OS security model

    # Enable browser logging
    caps = DesiredCapabilities.CHROME
    caps["goog:loggingPrefs"] = {"browser": "ALL"}

    # Path to chromedriver (adjust according to where it's located in your Lambda environment)
    path_to_chromedriver = "/usr/bin/chromedriver"

    # Initialize WebDriver
    driver = webdriver.Chrome(
        desired_capabilities=caps,
        executable_path=path_to_chromedriver,
        options=chrome_options,
    )

    try:
        # Open the page
        driver.get(url)

        # Retrieve console logs
        logs = driver.get_log("browser")

        # Return any log messages found
        return {"statusCode": 200, "body": json.dumps(logs)}

    finally:
        driver.quit()
