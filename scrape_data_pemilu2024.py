from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# setup chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")  # ensure GUI is off
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# set the target URL
url = "https://pemilu2024.kpu.go.id/"

# set up the webdriver
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

wait = WebDriverWait(driver, 100)  # Timeout after 100 seconds
table_xpath = "/html/body/div/div[1]/div/div[2]/div/div[2]/div[3]/div/div/table"
table_element = wait.until(EC.presence_of_element_located((By.XPATH, table_xpath)))

# Now that the table is loaded, extract the data
# This example assumes the table rows are direct children of the table_element located by the XPath
rows = table_element.find_elements(By.XPATH, ".//tr")
data = []
for row in rows:
    # Extract text from each cell in the row
    cells = row.find_elements(By.XPATH, ".//td")
    if not cells:  # If the first row consists of headers <th>
        cells = row.find_elements(By.XPATH, ".//th")
    data.append([cell.text for cell in cells])

# Assuming the first row contains headers
headers = data[0] if data else []
data_rows = data[1:] if len(data) > 1 else []

# Convert to DataFrame
df = pd.DataFrame(data_rows, columns=headers)

# Don't forget to close the browser
driver.quit()
df.to_csv("data_pemilu.csv", index=False)
