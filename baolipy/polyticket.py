from splinter.browser import Browser
from time import sleep
import requests
import ddddocr
# traceback模块被用来跟踪异常返回信息
import traceback

ticket_url = "https://www.polyt.cn/choose/seat?showId=48001&projectId=545998308918296576&sectionId=47867"
user_name = u"15210982682"
password = u"zhang8558155"


def getTicket(bwr):
    sleep(1)
    e = bwr.find_by_id("seatPos")
    e.find_by_xpath("//div[@title='1排45座']").click()
    e.find_by_xpath("//span[contains(@id, 'totalPrice')]").click()
    sleep(1)
    sleep(600)


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
    el_form.find_by_xpath("//input[@placeholder='请填写验证码']").fill(ocr_str)
    el_form.find_by_text(u"登录").click()
    sleep(1)


def flow():
    """
    抢票主流程
    :return:
    """
    bwr = Browser(driver_name="chrome")
    try:
        bwr.visit(ticket_url)
        login(bwr)
        getTicket(bwr)
    finally:
        bwr.quit()


if __name__ == "__main__":
    flow()
    # print(classifyOcr("https://platformpcgateway.polyt.cn/api/1.0/common/getPicCode?&random=481696&token=943e2f13-5a0a-47ab-932a-1a79a9aba388"))
    print("finish")
