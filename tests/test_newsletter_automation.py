from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from percy import percy_snapshot


chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)


def test_title():
	driver.get("https://staging-newsletter-generator.qxf2.com")

	title = driver.title

	assert title=="Home"

	percy_snapshot(driver=driver,name="Home page")

	driver.quit()