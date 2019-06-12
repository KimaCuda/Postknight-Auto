# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 17:43:06 2019

@author: fddot
"""

class Person:
   def setavalue(self, name):         
      self.myname = name      
   def printaname(self):         
      print("Name", self.myname)

#%%

delivery_post = ['delivery_HQ', 'delivery_PP', 'delivery_SB', 'delivery_GF', 'delivery_CD', 'delivery_VOG', 'delivery_FF']

       
def delivery_post_click():
    if city == 'HQ':
        auto.moveTo(x = main_x+240, y = main_y+215, duration = 0.5)
        auto.dragRel(-300, 0, duration = 0.30)
    click_buttons('delivery_%s' %city)
    if city == 'HQ':
        while True:
            window = scanwindow()
            dialog_box = auto.locate(r'IMG\delivery\delivery_finish1.png', window, confidence = 0.6)
            if dialog_box:
                auto.click(main_x+270, main_y+130)
                time.sleep(1)
            else:
                break
    return

def delivery_chest_claim():
    claim_test2 = scanwindow()
    for j in range(len(chest2)):
        click_test = auto.locate(r'IMG\%s.png' %chest2[j], claim_test2, confidence = 0.6)
        if click_test:
            while True:
                claim_test3 = scanwindow()
                click_test3 = auto.locate(r'IMG\%s.png' %chest2[j], claim_test3, confidence = 0.6)
                if click_test3:
                    auto.click(main_x+270, main_y+130)
                    time.sleep(1)
                else:
                    time.sleep(2)
                    break
        elif click_test == None:
            continue
    return

def delivery():
    global safe_mode 
    delivery_post_click()    
    window = scanwindow()
    while True:
        try:
            if city == 'HQ':
                safe_mode = 1
                view_button = auto.locate(r'IMG\delivery\delivery_view_HQ.png', window, confidence = 0.6)
            else:
                view_button = auto.locate(r'IMG\delivery\delivery_view.png', window, confidence = 0.6)
                check_rank = auto.screenshot(region = (main_x + view_button[0], main_y + view_button[1] - 100, 150, 100))
                rank_S = auto.locate(r'IMG\delivery\delivery_rankS.png', check_rank, confidence = 0.7)
                if rank_S:
                    safe_mode = 1
            if city == 'HQ':
                click_buttons('delivery\delivery_view_HQ')
            else:
                click_buttons('delivery\delivery_view')
            time.sleep(1)
            if city != 'HQ':
                click_buttons('go_button')
            time.sleep(3)
            combat_module()
            time.sleep(3)
            delivery_chest_claim()
        except TypeError:
            try:
                auto.moveTo(x = main_x+240, y = main_y+430, duration = 0.5)
                auto.dragRel(0, -300, duration = 0.30, pause = 3)
            except TypeError:
                print('no more delivery in this city. checking timer...')
                break
    a = ocr_prep('a')
    delivery_post_click()
    delivery_timer = a.read_quest_timer()
    return delivery_timer
            