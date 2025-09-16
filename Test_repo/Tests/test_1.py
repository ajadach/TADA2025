from DemoQADriver.DemoQALib.demoqa import DemoQA

driver = DemoQA()

driver.open_browser()
driver.navigate_to_page()
driver.elements.navigate_to_page()
driver.elements.text_box.navigate_to_page()
try:
    error = driver.elements.text_box.choose_parameters("Full Name", "Artur Ziolkowski")
except Exception as e:
    print(f"Error: {e}")
driver.elements.check_box.navigate_to_page()