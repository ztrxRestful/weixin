import cv2 as cv
import pyautogui
import pyperclip
import os
import time

from PIL import ImageGrab

class begin():
    def __init__(self,wechat_path):
        self.wechat_path = wechat_path

    path = os.getcwd().replace('\\', '/')
    def scanner_img(self,name):
        clip = ImageGrab.grab()
        # clip = ImageGrab.grabclipboard()

        if (clip != None):

            clip.save(self.path+"/image/" + name + ".jpg")
            return self.path+"/image/" + name + ".jpg"
        return "err"

    def find_image(self,obj_path, src_path):
        source = cv.imread(src_path)
        template = cv.imread(obj_path)
        result = cv.matchTemplate(source, template, cv.TM_CCOEFF_NORMED)

        pos_start = cv.minMaxLoc(result)[3]

        x = int(pos_start[0]) + int(template.shape[1] / 2)
        y = int(pos_start[1]) + int(template.shape[0] / 2)
        similarity = cv.minMaxLoc(result)[1]
        if similarity < 0.85:
            return (-1, -1)
        else:
            return (x, y)

    def check_img(self,obj_path, src_path):
        x = -1
        y = -1
        while x == -1:
            x, y = self.find_image(obj_path, src_path)
            #print(x,y)
        return (x, y)

    '''
        打开微信(需要用户自己截取屏幕上的微信图片，已jpg形式放在image文件夹下)
    '''
    def open_wechat_cv(self):
        pyautogui.hotkey('win', 'd')
        # res_name = gitBigImg.git_src_img("temp")
        res_name = self.scanner_img("temp")
        src_path = res_name
        #print(src_path)
        obj_path = self.path+'/image/wechat.jpg'
        x, y = self.check_img(obj_path, src_path)

        # pyautogui.hotkey('win','d')
        pyautogui.PAUSE = 1.0
        # pyautogui.moveTo(res[0][0],res[0][1],duration=2)
        pyautogui.doubleClick(x, y)

    def open_wechat(self):
        pyautogui.hotkey('win', 'd')
        cmd = self.wechat_path+'\WeChat.exe'
        file = os.popen(cmd)
        #print(file)
        file.close()
        time.sleep(2)

    def send_msg_obj(self,name):
        # res_name = gitBigImg.git_src_img("temp2")
        res_name = self.scanner_img("temp2")

        src_path = res_name
        # 寻找搜索图片
        obj_path = self.path+'/image/lan.jpg'
        x, y = self.find_image(obj_path, src_path)
        pyautogui.click(x, y)
        pyautogui.PAUSE = 1.0

        pyperclip.copy(name)

        pyautogui.hotkey('ctrl', 'v')
        #print(x,y)
        y = y+100
        #print(x,y)
        pyautogui.click(x, y)

    '''
    需要发送的信息文本
    '''
    def send_msg(self,text):
        pyperclip.copy(text)
        pyautogui.hotkey('ctrl', 'v')

    '''
    微信换行
    '''
    def huang_hang(self):
        pyautogui.hotkey('shift', 'enter')
    '''
    信息发送
    '''
    def send(self):
        pyautogui.hotkey('enter')

if __name__ == '__main__':
    #使用class时，需要初始化微信的所在位置
    wechat = begin('C:\Program Files (x86)\Tencent\WeChat')
    wechat.open_wechat()
    wechat.send_msg_obj('测试目标')
    wechat.send_msg('测试一下')
    wechat.huang_hang()
    wechat.send_msg('再来一遍')
    wechat.send()

