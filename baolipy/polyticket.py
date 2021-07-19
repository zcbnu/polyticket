from splinter.browser import Browser
from time import sleep
import requests
import ddddocr
import _thread
import re
# traceback模块被用来跟踪异常返回信息
import traceback

ticket_url = "https://www.polyt.cn/choose/seat?showId=48001&projectId=545998308918296576&sectionId=47867"
user_name = u"15210982682"
password = u"zhang8558155"
str_seat = '1排45座'
delayMin = 0.1
getTicketCount = 0

def getAllTicket(bwr):
    e = bwr.find_by_id("seatPos")
    for e in e.find_by_tag('div'):
        if e['title'] is not None:
            if e.html.find('not-allowed') == -1:
                print(e['title'])
    sleep(60)


def selectTicket(bwr, seat):
    sleep(delayMin)
    e = bwr.find_by_id("seatPos")
    e.find_by_xpath("//div[@title='{0}']".format(seat)).click()
    e.find_by_xpath("//span[contains(@id, 'totalPrice')]").click()
    sleep(delayMin)
    bwr.find_by_text(u"选择观演人").click()
    # sleep(10000)
    sleep(delayMin)
    bwr.find_by_xpath("//div[@aria-label='常用观演人']").find_by_text(u"确定").click()
    sleep(delayMin)
    bwr.find_by_text(u"支付订单").click()
    sleep(delayMin)


def classifyOcr(img_url):
    """
    识别验证码
    :return:
    """
    r = requests.get(img_url, allow_redirects=True)
    ocr = ddddocr.DdddOcr()
    open("tmp.png", 'wb').write(r.content)
    return ocr.classification(r.content)


def login(bwr):
    bwr.find_by_text(u" 登录/注册").click()
    # bwr.find_by_text(u" 密码登录 ").click()
    # -- 选择密码登录页签
    bwr.find_by_xpath("//div[@class='flex cur-hand font-666 tabActive']").click()
    el_form = bwr.find_by_xpath("//div[@class='login-content']")
    el_form.find_by_xpath("//input[@placeholder='请填写手机号码']").fill(user_name)
    el_form.find_by_xpath("//input[@type='password']").fill(password)
    img_url = el_form.find_by_xpath("//img[contains(@src, 'getPicCode')]")['src']
    ocr_str = classifyOcr(img_url)
    if len(ocr_str) == 4:
        el_form.find_by_xpath("//input[@placeholder='请填写验证码']").fill(ocr_str)
        el_form.find_by_text(u"登录").click()
        sleep(delayMin)
    else:
        el_form.find_by_xpath("//i[@class='el-icon-close']").click()
        login(bwr)


def flow(seat):
    """
    抢票主流程
    :return:
    """
    print("start flow ", seat)
    bwr = Browser(driver_name="chrome")
    try:
        bwr.visit(ticket_url)
        login(bwr)
        selectTicket(bwr, seat)
        # getAllTicket(bwr)
    finally:
        print("close flow", seat)
        bwr.quit()


if __name__ == "__main__":
    seat_str = "{0}排{1}座"
    for x in range(1, 2):
        for y in range(33, 40):
            try:
                _thread.start_new_thread(flow, (seat_str.format(x, y),))
            except:
                print("ERROR start thread")
    # print(classifyOcr("https://platformpcgateway.polyt.cn/api/1.0/common/getPicCode?&random=481696&token=943e2f13-5a0a-47ab-932a-1a79a9aba388"))
    while 1:
        sleep(1)

        continue
    print("finish")
