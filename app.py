import webbrowser
import pyautogui
from time import sleep 


#webbrowser.open('https://www.tiktok.com/login/phone-or-email/email')
#sleep(2)
#pyautogui.click(957,412, duration=2)
#sleep(2)
#pyautogui.click(985,276, duration=2)
#sleep(2)
#pyautogui.click(823,319, duration=2)
#sleep(2)
#pyautogui.write("kaiquedeveza1234@hotmail.com")
#sleep(2)
#pyautogui.click(817,369, duration=2)
#sleep(2)
#pyautogui.write("ade345he@")
#sleep(2)
#pyautogui.click(943,465, duration=2)
##sleep(10)
webbrowser.open('https://www.tiktok.com/@oreidosites')
sleep(5)
pyautogui.click(378,577, duration=2)

try:

    image = pyautogui.locateOnScreen("curtida.png")
    sleep(5)


    if image:
        sleep(5)
        pyautogui.click(1501,694, duration=2)
        sleep(5)
        pyautogui.press("down")


        
    else:
        raise pyautogui.ImageNotFoundException
    
except pyautogui.ImageNotFoundException:   
    sleep(5)
    pyautogui.click(1448,699, duration=2)
    sleep(5)
    pyautogui.press("down")