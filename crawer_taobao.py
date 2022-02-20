from curses.panel import bottom_panel
from json.tool import main
from time import sleep

from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

import os
import sys
import termios
import pickle

shopList_herfs=[]
topImage_list=[]
bottomImage_list=[]

def login_t (browser):  
    sleep(1)
    button = WebDriverWait(browser, timeout=30).until(EC.presence_of_element_located((By.CLASS_NAME, 'h')))
    button.click()
    username_sender = WebDriverWait(browser, timeout=30).until(EC.presence_of_element_located((By.ID, 'fm-login-id')))
    username_sender.send_keys("uuuuuuuuuuuusername")
    password_sender=WebDriverWait(browser, timeout=30).until(EC.presence_of_element_located((By.ID, 'fm-login-password')))
    password_sender.send_keys("ppppppppppppppppwd")
    sleep(3)
    try:
        browser.switch_to.frame(0)
        # 找到滑块
        slider = browser.find_element(By.XPATH,"//span[contains(@class, 'btn_slide')]")
        # 判断滑块是否可见
        if slider.is_displayed():
            # 点击并且不松开鼠标
            ActionChains(browser).click_and_hold(on_element=slider).perform()
            # 往右边移动258个位置
            ActionChains(browser).move_by_offset(xoffset=258, yoffset=0).perform()
            # 松开鼠标
            ActionChains(browser).pause(0.5).release().perform()
            browser.switch_to.default_content()
    except:
        pass
    button = WebDriverWait(browser, timeout=30).until(EC.presence_of_element_located((By.CLASS_NAME, 'password-login')))
    button.click()

def press_any_key_exit(msg):
      # 获取标准输入的描述符
  fd = sys.stdin.fileno()

  # 获取标准输入(终端)的设置
  old_ttyinfo = termios.tcgetattr(fd)

  # 配置终端
  new_ttyinfo = old_ttyinfo[:]

  # 使用非规范模式(索引3是c_lflag 也就是本地模式)
  new_ttyinfo[3] &= ~termios.ICANON
  # 关闭回显(输入不会被显示)
  new_ttyinfo[3] &= ~termios.ECHO

  # 输出信息
  sys.stdout.write(msg)
  sys.stdout.flush()
  # 使设置生效
  termios.tcsetattr(fd, termios.TCSANOW, new_ttyinfo)
  # 从终端读取
  os.read(fd, 7)

  # 还原终端设置
  termios.tcsetattr(fd, termios.TCSANOW, old_ttyinfo)

def findGoods(browser):
    linkers=browser.find_elements(By.XPATH,'//*[@id="J_ShopSearchResult"]/div/div[2]/div/dl/dt/a')
    for link in linkers:
        herf=link.get_attribute('href')
        print(herf)
        shopList_herfs.append(herf)
        
def findTopPics (browser):
    linkers=browser.find_elements(By.XPATH,'//*[@id="J_UlThumb"]//div/a/img')
    for link in linkers:
        src=link.get_attribute('src')
        src=src.split('.jpg')[0]+'.jpg'
        print(src)
        topImage_list.append(src)

def findBottomPics(browser):
    linkers=browser.find_elements(By.XPATH,'//*[@align="absmiddle"]')
    for link in linkers:
        src=link.get_attribute('src')
        print(src)
        bottomImage_list.append(src)


def main():

    option = webdriver.ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])  # 这里去掉window.navigator.webdriver的特性
    option.add_argument("--disable-blink-features=AutomationControlled")   # 屏蔽webdriver特征
    browser = webdriver.Chrome(options=option)
    browser.get('lllllllllllllllllllllink')
    browser.maximize_window()
    #用户自主登录
    press_any_key_exit("按任意键继续...")
    browser.get('llllllllllllllllllllink')
    press_any_key_exit("按任意键继续...")


    for i in range (5):
        findGoods(browser=browser)
        browser.find_element(By.XPATH,'//*[@class="J_SearchAsync next"]').click()
        print(i,'page done!')
        sleep(3)
    
    press_any_key_exit("按任意键继续...")

    
    for good in shopList_herfs:
        browser.get(good)
        sleep(1)
        findTopPics(browser=browser)
        findBottomPics(browser=browser)
        sleep(1)
    
    browser.close()

    f=open('topimg.pkl','wb')
    pickle.dump(topImage_list,f,True)
    f.close()

    f=open('botimg.pkl','wb')
    pickle.dump(bottomImage_list,f,True)
    f.close()
    # 防止后续下载出现错误，先进行数据持久化
    # 然后分别运行topImageDownload和botImgDownload即可




if __name__ == '__main__':
    main()
    
