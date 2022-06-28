from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time
import requests 
import urllib , json

asocksip = ""

url = "https://asocks.com/control/proxy/ATn91zNC3npTse5oBoE9UqrWQlViMNDv.json"



  






# proxy_ip_port = '109.236.80.7:30013'
# proxy_ip_port = 'asocksip'

def openBrowser():
    proxy_ip_port = asocksip
    proxy = Proxy()
    proxy.proxy_type = ProxyType.MANUAL
    proxy.http_proxy = proxy_ip_port
    proxy.ssl_proxy = proxy_ip_port

    capabilities = webdriver.DesiredCapabilities.CHROME
    proxy.add_to_capabilities(capabilities)

    driver = webdriver.Chrome('D:\selenium\chromedriver.exe' , desired_capabilities = capabilities)

    driver.get('http://telnetmyip.com/')

    time.sleep(5)

    #driver.quit()

def autoAssignProxies():
   # r = requests.get(url)
   # data = json.loads(r.read())
   # print(r.json)

   global asocksip

   source = requests.get(url).json()
   for line in source:
    ProxyListWithoutClean = line.split(",")

   for i in ProxyListWithoutClean:
    cleanProxy = i.replace("[","")
    cleanProxy = i.replace("]","")
    cleanProxy = i.replace("'","")
    asocksip = cleanProxy


    print (cleanProxy)
    openBrowser()

autoAssignProxies()
