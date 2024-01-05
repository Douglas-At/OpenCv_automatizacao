import cv2 
import pyautogui 
import numpy as np
import os
import time 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
from pandas.tseries.offsets import BDay


class OpenCv:
    def img_def(self,img_name):
        return os.path.join(os.getcwd(),"dep_img",img_name)
    
    def crop_img(self,img_name, cordenadas, output_name):
        image = cv2.imread(self.img_def(img_name))
        x1,y1,x2,y2 = cordenadas
        #cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 2)
        cropped_image = image[y1:y2, x1:x2]
        cv2.imwrite(self.img_def(output_name), cropped_image)

    def screenshot(self):
        screenshot = pyautogui.screenshot()
        img = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        return img
    
    def save_img(self,img,name):
        cv2.imwrite(self.img_def(name),img)


    def show_img(self,img):
        cv2.imshow("'-'", img)
        cv2.waitKey()
        cv2.destroyAllWindows()

    def find_and_click(self,img2):
        """
        tela que acha e clicka no parametro de uma tela inteira
        """
        diver = cv2.imread(ocv.img_def(img2), cv2.IMREAD_UNCHANGED)
        w = diver.shape[1]
        h = diver.shape[0]

        while True:
            tela = ocv.screenshot()
            
            
            result = cv2.matchTemplate(tela, diver, cv2.TM_CCOEFF_NORMED)
            self.show_img(result)
            self.show_img(tela)
            
            #check the values of max if >0,9 clicko 
            min_val,max_val, min_loc,max_loc = cv2.minMaxLoc(result)

            print(max_val)
            if max_val > 0.9:
                x, y = max_loc
            
                pyautogui.moveTo(x+(w>>1), y+(h>>1))
                pyautogui.click()
                break

class SeleniumUse:
    def __init__(self,driver):
        self._driver = driver
    def hub_verify(self):
        for handle in self._driver.window_handles:
            self._driver.switch_to.window(handle)
            link = self._driver.current_url 
            if "https://hub.xpi.com.br/new/relatorios/#/relatorios-gerencias" in link:
                break
    
    def open_diver(self):
        self.hub_verify()
        
        driver = self._driver
        driver.get("https://hub.xpi.com.br/new/relatorios/#/relatorios-gerencias")
        driver.refresh()



data_atual = datetime.today().date()
bday = BDay()
dois_dias = data_atual - 2 * bday
mes = dois_dias.strftime("%Y%m")


if __name__ == "__main__":
    
    PATH = r"C:\Users\dougl\OneDrive\Documentos\chromedriver.exe"
    service = Service(executable_path=PATH)
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_experimental_option("debuggerAddress", "localhost:9191")
    driver = webdriver.Chrome(service=service, options=options)
    actions = ActionChains(driver)
    web = SeleniumUse(driver)
    ocv = OpenCv()
    #abrir a tela de diversificação 
    #web.open_diver()
    #regra para o relatorio nao vir vazio
    ocv.find_and_click("bot_diver.png")
    ocv.find_and_click("bot_diver_data.png")
    #agora escolher o mes
    ocv.find_and_click("cropped_1.png")

        


    
    
