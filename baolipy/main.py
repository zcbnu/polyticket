# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import requests
import time

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def _parseCookie(cookies):
	ret = {}
	for line in cookies.split(';'):
		name,value = line.strip().split('=',1)
		ret[name] = value
	return ret


def showTypeId():
    pid="1099120000000000003"
    url = f"https://www.polyt.cn/search?showTypeId={pid}"
    cookie_str = "loginSession=6407cd72641ec3f7aa1ed5749692806f&&35e995006cdbbd1b70cc35a3a95bb699; Hm_lvt_0cb4627679a11906d6bf0ced685dc014=1625475825,1625736650,1625736826; Hm_lpvt_0cb4627679a11906d6bf0ced685dc014=1625736826"
    response = requests.get(url, cookies=_parseCookie(cookie_str))
    print(response.text)

def getLoginUser():
    url = "https://platformpcgateway.polyt.cn/api/1.0/searchRange/searchRangeList"
    cookie_str = "acw_tc=2f624a3116257386933294592e16043c104dc4d5b7ee9b22a2a88858d98d06;path=/;Max-Age=1800"
    response = requests.options(url, cookies=_parseCookie(cookie_str))
    print(response.text)

def searchTheater():
    url = "https://platformpcgateway.polyt.cn/api/1.0/search/searchTheater"
    token = "e1d17365a7e0f2831e223c23d41f1e6c"
    t = time.time()
    cookie_str = "loginSession=6407cd72641ec3f7aa1ed5749692806f&&35e995006cdbbd1b70cc35a3a95bb699; Hm_lvt_0cb4627679a11906d6bf0ced685dc014=1625475825,1625736650,1625736826,1625738693; Hm_lpvt_0cb4627679a11906d6bf0ced685dc014=1625738693"

    data = {
        "cityId": "",
        "keyWords": "",
        "priceZone": "0",
        "requestModel": {
            "applicationCode": "plat_pc",
            "applicationSource": "plat_pc",
            "atgc": token,
            "current": 1,
            "size": 12,
            "timestamp": t,
            "utgc": "utoken"
        },
        "shelfChannel": "",
        "showTypeId": "1099120000000000003",
        "sortType": "sortByTime",
        "timeType": "0"
    }
    response = requests.post(url, data=data, cookies=_parseCookie(cookie_str))
    print(response.text)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    getLoginUser()
    searchTheater()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
