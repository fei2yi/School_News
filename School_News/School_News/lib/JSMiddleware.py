from selenium import webdriver
from scrapy.http import HtmlResponse
import time

js = """
function scrollToBottom() {

    var Height = document.body.clientHeight,  //文本高度
        screenHeight = window.innerHeight,  //屏幕高度
        INTERVAL = 100,  // 滚动动作之间的间隔时间
        delta = 500,  //每次滚动距离
        curScrollTop = 0;    //当前window.scrollTop 值

    var scroll = function () {
        curScrollTop = document.body.scrollTop;
        window.scrollTo(0,curScrollTop + delta);
    };

    var timer = setInterval(function () {
        var curHeight = curScrollTop + screenHeight;
        if (curHeight >= Height){   //滚动到页面底部时，结束滚动
            clearInterval(timer);
        }
        scroll();
    }, INTERVAL)
}
scrollToBottom()
"""


class PhantomJSMiddleware(object):
    @classmethod
    def process_request(cls, request, spider):
        if 'PhantomJS' in request.meta.keys() and request.meta['PhantomJS']:
            # driver = webdriver.PhantomJS()
            driver = webdriver.Chrome()
            driver.get(request.url)

            # driver.execute_script(js)
            time.sleep(1)  # 等待JS执行
            # weiboaction(driver)
            content = driver.page_source.encode('utf-8')
            driver.quit()
            return HtmlResponse(request.url, encoding='utf-8', body=content, request=request)

def weiboaction(driver):
    driver.find_element_by_xpath('//input[@node-type="username"]').send_keys("710609071@qq.com")
    driver.find_element_by_xpath("//input[@node-type='password']").send_keys("yyaiyi..wb")
    while not login(driver):
        login(driver)
    else:
        time.sleep(30)

def login(driver):
    try:
        driver.find_element_by_xpath("//a[@node-type='submitBtn']").click()
        time.sleep(2)
    except:
        return 1
    str = input("Enter your input: ")
    driver.find_element_by_xpath("//input[@node-type='verifycode']").send_keys(str)
    driver.find_element_by_xpath("//a[@node-type='submitBtn']").click()
    time.sleep(3)
    login_proving(driver)

def login_proving(driver):
    try:
        driver.find_element_by_xpath("//input[@node-type='verifycode']")
        print('未登录')
        driver.find_element_by_xpath("//a[@node-type='submitBtn']").click()
        return 0
    except:
        print('登录成功')
        return 1