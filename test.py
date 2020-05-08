from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument('--disable-dev-shm-usage')
prefs = {"profile.default_content_settings.popups": 0,
                 "download.default_directory": r"/home/chih_he_taiwan/MMDC_Crawel/", # IMPORTANT - ENDING SLASH V IMPORTANT
                 "directory_upgrade": True}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('https://mail.google.com/')
driver.maximize_window()
sleep(2) 
driver.find_element_by_id('identifierId').send_keys('chih.he.taiwan@gmail.com')
sleep(2) 
driver.find_element_by_class_name('CwaK9').click()
sleep(2) 
driver.find_element_by_name('password').send_keys('42708891')
sleep(2) 
driver.find_element_by_class_name('CwaK9').click()
sleep(5) 

driver.find_element_by_class_name("zA").click()
sleep(2)
driver.find_element_by_link_text("查看報表").click()

sleep(25)