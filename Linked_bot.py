import pyautogui
# from selenium import webdriver
import time
import random
time.sleep(5)
messages=list(pyautogui.locateAllOnScreen('message.png'))     #this will locate the message button
var=0
end=5
while var<end:
    for message in messages:
        if pyautogui.locateOnScreen('New_message.PNG')==None:
            #Click Randomly in the Message Button area
            variable_message=((message[0]+random.randrange(message[2])),(message[1]+random.randrange(message[3]))) 
            pyautogui.moveTo(variable_message,duration=random.randrange(.6,1.9)           
            pyautogui.click(variable_message)
            time.sleep(random.randint(1,4))
            #Clicked on the message Button
            
            pyautogui.moveTo(1380,812,duration=1)
            #Enter the string in the message box
            pyautogui.typewrite('Hi ...')                     
            time.sleep(1.5)
            
            #Search for the send Button
            send=pyautogui.locateOnScreen('send.PNG')
            variable_send=((send[0]+random.randrange(send[2])),(send[1]+random.randrange(send[3]))) 
            pyautogui.moveTo(variable_send,duration=random.randrange(.6,1.9))           
            pyautogui.click(variable_send)
            time.sleep(random.randint(1,4))
            #Clicked on the Send Button
            
            #Search for all open Message Box
            all_cross=list(pyautogui.locateAllOnScreen('cross.PNG'))
            cross=pyautogui.locateOnScreen('cross.PNG')
            variable_cross=((cross[0]+random.randrange(cross[2])),(cross[1]+random.randrange(cross[3]))) 
            pyautogui.moveTo(variable_cross,duration=random.randrange(.6,1.9))
            if len(all_cross)==1:
                pyautogui.click(variable_cross)
                time.sleep(0.5)
            elif len(all_cross)>1:
                pyautogui.click(clicks=len(all_cross),interval=0.25)
                time.sleep(0.5)
            else:
                pass
            
            #if any new one replyd to the message
        elif pyautogui.locateOnScreen('New_message.PNG')!=None:
            new_message=pyautogui.locateOnScreen('New_message.PNG')
            variable_new_message=((new_message[0]+random.randrange(new_message[2])),(new_message[1]+random.randrange(new_message[3]))) 
            pyautogui.moveTo(variable_new_message,duration=random.randrange(.6,1.9))           
            pyautogui.click(variable_new_message)
            time.sleep(random.randint(1,4))
    
    #Scroller the page for 30 seconds
    scroler=pyautogui.locateOnScreen('scroler.PNG')
    variable_scroler=((scroler[0]+random.randrange(scroler[2])),(scroler[1]+random.randrange(scroler[3]))) 
    pyautogui.moveTo(variable_scroler,duration=random.randrange(.6,1.9))           
    pyautogui.click(clicks=2,interval=0.25)
    time.sleep(30)
    pyautogui.click(clicks=2,interval=0.25)
    var+=1
                             
            