from selenium import webdriver
from time import sleep
import json,requests
import pandas as pd
import xml.etree.ElementTree as XET

"""
driver = webdriver.Chrome()
driver.get('https://mail.google.com/')
driver.maximize_window()

#username = input("chih.he.taiwan@gmail.com")

#password = input("42708891")

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

sleep(30)
"""

tree = XET.parse(r'/Users/bensonChang/Downloads/廣告活動.xml')
root = tree.getroot() 
dic = []
count = 0
for i in root[0].findall('row'):
    arr = {}
    arr['name'] = i.get('廣告活動')
    if i.get('廣告活動狀況') == '已啟用':
        arr['enabled'] = 1
    else:
        arr['enabled'] = 0
    arr['type'] = i.get('廣告活動類型')
    arr['currency'] = i.get('幣別').replace(',','')
    arr['click'] = int(i.get('點擊').replace(',',''))
    arr['exposure'] = int(i.get('曝光').replace(',',''))
    arr['click_rate'] = float(i.get('點閱率').replace('%',''))/100
    arr['cpc_average'] = i.get('平均單次點擊出價')
    arr['cost'] = int(float(i.get('費用').replace(',','')))
    arr['conversion'] = float(i.get('轉換').replace(',',''))
    arr['conversion_after_view'] = float(i.get('瀏覽後轉換').replace(',',''))
    arr['single_conversion_cost'] = float(i.get('單次轉換費用').replace(',',''))
    arr['conversion_rate'] = float(i.get('轉換率').replace('%',''))/100
    dic.append(arr)

json_str = json.dumps(dic)
print(json_str)
r = requests.post("https://bbe6661a.ngrok.io/api/Py", data=json_str)
