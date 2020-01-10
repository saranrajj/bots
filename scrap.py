from selenium import webdriver
import time
import os
from selenium.webdriver.chrome.options import Options
#url for grabing values
url = "https://www.timeanddate.com/worldclock/india/chennai"

'''
list of identifiers for screengrabbing
supports identifier - [id,name,class or xpath]
value is the value of the identifier for the element to grab
'''
identifiers = [{'identifier':'id',
                'value':"ct"}]
# no of iterations for grabbing
iterations = 10
# delay in seconds for grabbing
delay = 1

#fetches the value for all teh identifiers given
def fetch(driver,identifiers):
    for ele in identifiers:
        if(ele['identifier']+"-"+ele['value'] not in caches):
            print("key found!!!")
            element = _getElement(driver,ele)
            caches[ele['identifier']+"-"+ele['value']] = element
        else:
            element = caches[ele['identifier']+"-"+ele['value']]
        print(fetchValue(element))

#get the element for the given identifier
def _getElement(driver,map):
    if('identifier' in map):
        if('value' in map):
            print('start processing')
            if(str(map['identifier']).upper()=='ID'):
                return driver.find_element_by_id(map['value'])
            elif(str(map['identifier']).upper()=='NAME'):
                return driver.find_element_by_name(map['value'])
            elif(str(map['identifier']).upper()=='CLASS'):
                return driver.find_element_by_class(map['value'])
            elif(str(map['identifier']).upper()=='XPATH'):
                return driver.find_element_by_xpath(map['value'])
        else:
            print('value not found')
    else:
        print('identifier not found')

#return the text for the given element
def fetchValue(element):
    return element.text

#used to cache the reference of the element that is already fetched
caches={}
cwd = os.getcwd()
#need to place the driver in the path
driverPath = cwd+'/driver/chromedriver.exe'
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(executable_path=driverPath,chrome_options=chrome_options)
driver.get(url)
count=0
while(count<iterations):
    fetch(driver,identifiers)
    time.sleep(delay)
    count+=1
driver.close()