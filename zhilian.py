#coding:utf-8
import requests
from bs4 import BeautifulSoup

headers = {'accept':'image/webp,image/*,*/*;q=0.8',
'accept-encoding':'gzip, deflate, sdch, br',
'accept-language':'zh-CN,zh;q=0.8',
'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',}

url = 'https://sou.zhaopin.com/?jl=801&sf=25001&st=35000&kw=Python&kt=3'

wbdata = requests.get(url)
# wbdata.encoding = 'gb18030'


soup = BeautifulSoup(wbdata.content, 'lxml')
print (soup)
job_name = soup.select('div.jobName > a')
print (job_name)