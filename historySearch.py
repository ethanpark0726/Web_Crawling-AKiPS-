import requests, openpyxl
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

fileName = 'IPAddressHistory.xlsx'

def loadExcelFile(fileName):

    wb = openpyxl.load_workbook(fileName)
    ws = wb.active
    macList = list()

    for i in range(1, ws.max_row + 1):
        macList.append(ws['A' + str(i)].value)

    print('--- Data successfully loaded')
    return macList

def saveExcelFile(IP):

    wb = openpyxl.load_workbook(fileName)
    ws = wb.active

    cellNumber = 1
    for elem in IP:
        ws['B' + str(cellNumber)] = elem
        cellNumber += 1

    wb.save(fileName)
    wb.close()

driver = webdriver.Chrome('C:/Users/hpar0001/AppData/Local/Programs/Python/chromedriver.exe')
login_url = "https://akips11.hsnet.ufl.edu"

driver.get(login_url)

element = driver.find_element_by_name('username')
element.clear()
element.send_keys('admin')
element = driver.find_element_by_name('password')
element.clear()
element.send_keys('1 Problem')
xpath = '/html/body/div[1]/div/div[2]/form/button'
driver.find_element_by_xpath(xpath).click()

mac = loadExcelFile(fileName)
wb = openpyxl.load_workbook(fileName)
ws = wb.active
cellNumber = 1

for elem in mac:
    crawling_url = f"https://akips11.hsnet.ufl.edu/switch-port-map-reporter?mode=history;address={elem};"
    driver.get(crawling_url)

    xpath = '/html/body/table/tbody/tr[2]/td[6]'
    try:
        IP_Addr = driver.find_element_by_xpath(xpath).text
    except NoSuchElementException:
        IP_Addr = "NA"

    ws['B' + str(cellNumber)] = IP_Addr
    cellNumber += 1

    wb.save(fileName)
wb.close()
#saveExcelFile(IPList)
# element = driver.find_element_by_xpath('//*[@id="address"]')
# element.send_keys('000CCC63FE95')
# xpath = '//*[@id="control2"]/fieldset/div[3]/div/button[3]'
# driver.find_element_by_xpath(xpath).click()