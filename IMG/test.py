# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 12:13:29 2019

@author: fddot
"""

#from delivery.delivery import Customer
#%%

class read_timer(Object):
    

    def read_timer(timer_img):
        arbit_timer = [0,0,0]
        pattern = '[0-9]{2}\w[0-9]{2}\w'
        with Image(filename = r'IMG\delivery\%s.png' %timer_img) as img:
            img.transform('300x300','900%')
            img.save(filename = r'IMG\delivery\testla.png')
        
        img = cv2.imread(r'IMG\delivery\testla.png')
        a = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        b = a.copy()
        for i in range(len(b)):
            for j in range(len(b[0])):
                if b[i][j] > 180 and b[i][j] < 255:
                    b[i][j] = 0
                else:
                    b[i][j] = 255
        
        c = ocr.image_to_string(b)
    
        for i in range(4):
            text_data = ocr.image_to_string(r'IMG\delivery\testla.png', config = '--oem %s' %i)
            text_data = text_data.replace("O","0")
            text_data = text_data.replace(" ","")
            timer_regex = re.match(pattern, text_data)
            for i in range(2):
                if i == 0:
                    if timer_regex[2] == 'H':
                        arbit_timer[0] == int(timer_regex[0:2])
                    if timer_regex[2] == 'M':
                        arbit_timer[1] == int(timer_regex[0:2])
                if i == 1:
                    if timer_regex[5] == 'M':
                        arbit_timer[1] == int(timer_regex[0:2])
                    if timer_regex[5] == 'S':
                        arbit_timer[2] == int(timer_regex[0:2])
            if timer_regex != None:
                break
    
        return arbit_timer
    
    def insert_time(arbit_timer, place_time):
        
        timestamp = time.time() + arbit_timer[0]*3600 + arbit_timer[1]*60 + arbit_timer[2]
        time_and_place[place_time] = timestamp
        
        return
    
    def check_time():
        # always do before sortie
        print('checking timer...')
        for i in range(len(time_and_place)):
            if time.time() > time_and_place[i]:
                print(time_and_place[place_list[i] + str(r" timer is up! time to do it to 'em. Moving..."))