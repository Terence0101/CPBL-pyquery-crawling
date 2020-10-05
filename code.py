import re
import requests
from pyquery import PyQuery as pq
response = requests.get('http://www.cpbl.com.tw/en/stats/\
all.html?&game_type=01&online=0&year=2019&stat=pbat&sort=G&order=desc')

infoset = []
doc = pq(response.text)
doc.make_links_absolute(base_url=response.url)

for i in range (1,7):
    for eachpage in doc('.page_bar > a:nth-child({})'.format(i)).items():
        eachPageDoc = pq(eachpage.attr("href"))
        for info in eachPageDoc("tr:nth-child(n+2)").items():
            infoDict = {}
            infoDict["name"] = re.sub('\(.*?\)','',info("td:nth-child(2)").text()).strip('*').strip(' ')
            infoDict["G"] = info("td.display1:nth-child(3)").text()
            infoDict["PA"] = info("td.display1:nth-child(4)").text()
            infoDict["AB"] = info("td.display1:nth-child(5)").text()
            infoDict["RBI"] = info("td.display1:nth-child(6)").text()
            infoDict["R"] = info("td.display1:nth-child(7)").text()
            infoDict["H"] = info("td.display1:nth-child(8)").text()
            infoDict["1B"] = info("td.display1:nth-child(9)").text()
            infoDict["2B"] = info("td.display1:nth-child(10)").text()
            infoDict["3B"] = info("td.display1:nth-child(11)").text()
            infoDict["HR"] = info("td.display1:nth-child(12)").text()
            infoDict["TB"] = info("td.display1:nth-child(13)").text()
            infoDict["SO"] = info("td.display1:nth-child(14)").text()
            infoDict["SB"] = info("td.display1:nth-child(15)").text()
            infoDict["OBP"] = info("td.display1:nth-child(16)").text()
            infoDict["SLG"] = info("td.display1:nth-child(17)").text()
            infoDict["AVG"] = info("td.display1:nth-child(18)").text()
            infoset.append(infoDict)  
  
a = input()
b = input()
result = []
for i in infoset:
    title = [j for j in i.values()]
    info = [x for x in i.keys()]
    if title[0] == a:
        result += [a]
        for k in range (len(i)):
            if info[k] == b:
                result += [title[k]]
print(result[0],'({}):'.format(b),result[1],sep="")
