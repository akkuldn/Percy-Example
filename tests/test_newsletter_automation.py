from selenium import webdriver
from percy import percy_snapshot

driver = webdriver.Chrome()


def test_title():
	driver.get("https://staging-newsletter-generator.qxf2.com")

	title = driver.title

	assert title=="Home"

	percy_snapshot(driver=driver,name="Home page")

	driver.quit()