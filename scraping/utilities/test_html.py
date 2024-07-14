# from bs4 import BeautifulSoup
# import requests
# import prettify

# url = 'https://www.nrl.com/draw/nrl-premiership/2024/round-1/sea-eagles-v-rabbitohs/'

# result = requests.get(url)

# doc = BeautifulSoup(result.text, "html.parser")

# print(doc.prettify())
    
#print(soup.prettify())

# tag = soup.title
# print(tag)

#  url = 'https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbWphVFIteXQ0QkRYcHZsenphSmtGamk4d0xyZ3xBQ3Jtc0tuZDBnTkVJMjR3dXJCVXBIVnpPcTdqRHV3NmVQWF9faTBJWkxCZ3VvR3Rkdld6QjdBaldqdVVNTzV4djU5WmlVT0d0TXgzWGkzeVIyNWlfMEpRc2VReXJwSnhacVJTMHducEdWQ2RsNktWb0UzWldVRQ&q=https%3A%2F%2Fwww.newegg.ca%2Fgigabyte-geforce-rtx-3080-ti-gv-n308tgaming-oc-12gd%2Fp%2FN82E16814932436%3FDescription%3D3080%26cm_re%3D3080-_-14-932-436-_-Product&v=gRLHr664tXA'

# result = requests.get(url)
# doc = BeautifulSoup(result.text, "html.parser")

# prices = doc.find_all(string='$')
# print(prices)


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Runs Chrome in headless mode.

# Set path to chromedriver as per your configuration
webdriver_service = Service(ChromeDriverManager().install())

# Set the browser
browser = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# URL you want to scrape
#url = 'https://www.newegg.ca/gigabyte-geforce-rtx-3080-ti-gv-n308tgaming-oc-12gd/p/N82E16814932436?Description=3080&cm_re=3080-_-14-932-436-_-Product'
url = 'https://www.nrl.com/draw/nrl-premiership/2024/round-1/sea-eagles-v-rabbitohs/'

# Use Selenium to get the page
browser.get(url)

# Navigate to the URL
browser.get(url)

# Wait for the page to load and locate the match stats elements
# This is a placeholder - you'll need to replace the selector with the actual one
# Example: Find elements by XPath or CSS selector
stats_elements = browser.find_elements_by_xpath('//div[@class="match-stats"]')

# Extract and print the stats
for element in stats_elements:
    print(element.text)

# Close the browser
browser.quit()