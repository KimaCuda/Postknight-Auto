# -*- coding: utf-8 -*-
"""
POSTKNIGHT BOT
trial01 - autofarm

Created on Fri May 31 07:59:57 2019

@author: fddot
"""

import pyautogui as auto
#from PIL import ImageGrab, ImageOps
#import numpy as np
import time
#import numpy as np
import re
import pytesseract as ocr
import os
from wand.image import Image
import cv2
import sys

os.chdir('E:\Project\Postknight-auto')

auto.FAILSAFE = True
ocr.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# %%
# DATABASES

quest_NMA = [['Cub Care', 'PP_1', 30], ['Dire Hunt', 'PP_1', 30], ['Howling Affair', 'PP_3', 10],
             ['Stolen Shots', 'PP_1', 10], ['Sealed Range', 'PP_5', 10], [r"Now You Don't", 'PP_5', 30],
             ['Call The Cops', 'PP_5', 10], ['Criminal Command', 'PP_5', 1],
             
             ['Drop It', 'SB_2', 30], ['Bursting Bubbles', 'SB_2', 30], ['Deadly Swims', 'SB_3', 10],
             ['In A Pinch', 'SB_2', 10], ['Ahoy Kiddos', 'SB_5', 10], ['Aye Aye Sir', 'SB_5', 10], 
             ['Song Stopper', 'SB_3', 10], ['Captain Crook', 'SB_5', 1], 
             
             ['Flitter By', 'GF_1', 30], ['Birds Of Prey', 'GF_1', 30], ['Scurry Away', 'GF_3', 10],
             ['Scattered Defense', 'GF_3', 10], ['Baron Berth', 'GF_5', 10], ['Snitch Pitch', 'GF_5', 10], 
             ['At Easer', 'GF_5', 10], ['Cyclone Chief', 'GF_5', 1], 
             
             ['Easy Piffsy', 'CD_1', 30], ['Huff And Puff', 'CD_1', 30], ['Spiky Encounter', 'CD_1', 10],
             ['Puffed Effort', 'CD_3', 10], ['Clan Craze', 'CD_5', 10], ['Tuff One', 'CD_3', 10], 
             ['Phony Priest', 'CD_5', 10], ['Sect Lord', 'CD_5', 1], 
             
             ['Chest Clone', 'VOG_1', 30], ['Fragile Form', 'VOG_1', 30], ['Gold Digger', 'VOG_3', 10],
             ['Bombs Away', 'VOG_3', 10], ['What He Lacks', 'VOG_4', 10], ['Mine Time', 'VOG_5', 10], 
             ['Excavating Exec', 'VOG_5', 10], ['Dredge Dominion', 'VOG_5', 1], 
             
             ['Slimy Situation', 'FF_3', 30], ['Whooping', 'FF_2', 30], ['Prickle Party', 'FF_7', 30],
             ['Masqueraid', 'FF_3', 30], ['Phantom Menace', 'FF_6', 15], ['Worlord', 'FF_3', 15], 
             ['Rowdy Ruffians', 'FF_8', 30], ['Ranged Rufians', 'FF_7', 30], ['Walla Bing Bang', 'FF_8', 30],
             ['LastBoss', 'FF_8', 1],
             
             ['Eye for an ad', 'AD', 30]]

farm_lists = [['ceruleaf', 'PP_5'],['puffwort', 'PP_5'],['sage','PP_5'],
              ['wolf_skin', 'PP_2'],['sunblaze', 'PP_5'],
              
              ['angel_wings', 'SB_4'],['costar', 'SB_4'],['chuvie', 'SB_4'],
              ['blooplets', 'SB_2'],['copper_ore', 'SB_5'],['giant_claw', 'SB_2'],
              ['walnut_log', 'SB_4'],['siren_scales', 'SB_5'],['sea_marble', 'SB_5'],
              
              ['argiebii', 'GF_5'],['galesip', 'GF_5'],['danderion', 'GF_5'],
              ['mevari_feather', 'GF_1'],['leather_scraps', 'GF_5'],['flitweave', 'GF_1'],
              ['Zephrite', 'GF_5'],
              
              ['kuroot', 'CD_5'],['tuffler_tusk', 'CD_5'],['firebloom', 'CD_5'],
              ['camphor_log', 'CD_5'],['puff_tuft', 'CD_1'],['robe_piece', 'CD_1'],
              ['silver_ore', 'CD_5'],['myke_hide', 'CD_1'],['spirit_orb', 'CD_5'],
              ['event_token', 'CD_5'],
              
              ['glowbud', 'VOG_5'],['grottoshroom', 'VOG_5'],['moonbud', 'VOG_5'],
              ['elder_pine_log', 'VOG_5'],['mimic_core', 'VOG_1'],['valley_gauze', 'VOG_5'],
              ['gold_ore', 'VOG_5'],['crichip', 'VOG_1'],['crystabit','VOG_5'],
              
              ['blood_acorn', 'FF_7'],['gooberry', 'FF_7'],['golden_basil', 'FF_7'],
              ['goo_remnants', 'FF_6'],['wolo_mask', 'FF_3'],['mythril_ore', 'FF_8'],
              ['niar_pelt', 'FF_8'],['purpleheart_log', 'FF_8'],['mystiq', 'FF_8']]

time_and_place = {'PP_pet_gift': 0, 'PP_pet_receive': 0, 'PP_quest': 0,
                  'PP_delivery': 0, 'PP_girl1_gift': 0, 'PP_girl1_receive': 0,
                  'PP_girl2_gift': 0, 'PP_merchant': 0,
                  
                  'SB_pet_gift': 0, 'SB_pet_receive': 0, 'SB_quest': 0,
                  'SB_delivery': 0, 'SB_merchant': 0,
                  
                  'GF_pet_gift': 0, 'GF_pet_receive': 0, 'GF_quest': 0,
                  'GF_delivery': 0, 'GF_girl_gift': 0, 'GF_girl_receive': 0,
                  'GF_merchant': 0,
                  
                  'CD_pet_gift': 0, 'CD_pet_receive': 0, 'CD_quest': 0,
                  'CD_delivery': 0, 'CD_girl1_gift': 0, 'CD_girl1_receive': 0,
                  'CD_girl2_gift': 0, 'CD_girl2_receive': 0, 'CD_merchant': 0,
                  
                  'VOG_pet_gift': 0, 'VOG_pet_receive': 0, 'VOG_quest': 0,
                  'VOG_delivery': 0, 'VOG_girl_gift': 0, 'VOG_girl_receive': 0,
                  'VOG_merchant': 0,
                  
                  'FF_quest': 0, 'FF_delivery': 0, 'FF_merchant': 0}

place_list = list(time_and_place.keys())
chest1 = ['delivery_chestB1','delivery_chestA1','delivery_chestS1']
chest2 = ['delivery_chestB2','delivery_chestA2','delivery_chestS2']
areas_buttons = ['areas_HQ', 'areas_PP','areas_SB','areas_GF','areas_CD','areas_VOG','areas_FF']
boards = ['board_HQ', 'board_PP','board_SB','board_GF','board_CD','board_VOG','board_FF']
areas = ['HQ', 'PP', 'SB', 'GF', 'CD', 'VOG', 'FF']
window_list = ['window_routeselect','window_achievement','window_inventory','window_shop','window_skills','window_stats', 'window_division', 'window_delivery']
delivery_post = ['delivery_HQ', 'delivery_PP', 'delivery_SB', 'delivery_GF', 'delivery_CD', 'delivery_VOG', 'delivery_FF']

# %%

def main_screen_detection():
    main_screen = auto.locateOnScreen(r'IMG\LDP_detect.png', confidence = 0.6)
    main_x = main_screen[0]+1
    main_y = main_screen[1]+main_screen[3]
    return main_screen, main_x, main_y

# %%

def scanwindow():
    game_window = auto.screenshot(region=(main_x, main_y, 480, 860))
    return game_window
# %%
    
def click_buttons(button):
    window = scanwindow()
    location = auto.locate(r'IMG\%s.png' %button, window, confidence = 0.7)
    auto.click(main_x+auto.center(location)[0], main_y+auto.center(location)[1], duration = 0.5,  pause = 1.2)

def CB_nodelay(button):
    window = scanwindow()
    location = auto.locate(r'IMG\%s.png' %button, window, confidence = 0.6)
    if location != None:
        auto.click(main_x+auto.center(location)[0], main_y+auto.center(location)[1])

# %%

def check_window():
    check = scanwindow()
    for i in range(len(window_list)):
        whatwindow = auto.locate(r'IMG\%s.png' %window_list[i], check, confidence = 0.8)
        if whatwindow != None:
            break
    if whatwindow != None:
        print('you are on the ' + str(window_list[i][7:]) + ' window. Getting ready to move...')
        time.sleep(2)
        close_button = auto.locate(r'IMG\announcement_endgame_close_button.png', check, confidence = 0.6)
        auto.click(main_x+auto.center(close_button)[0], main_y+auto.center(close_button)[1])
        time.sleep(2)
    else:
        print('No window found. please bring emulator to the front! Exiting for now...')
        sys.exit(0)
    return

def check_city():
    check = scanwindow()            
    drag_dist = 300
    #check if it is main window or not. if not make it into main window.
    a = auto.locate(r'IMG\window_main.png', check, confidence = 0.6)
    if a == None:
        check_window()
        
    while True:
        for i in range(len(boards)):
            check = scanwindow()
            whatcity = auto.locate(r'IMG\%s.png' %boards[i], check, confidence = 0.6)
            if whatcity != None:
                print('you are at '+str(boards[i][6:]+'!'))
                current_areas = boards[i][6:]
                break
        
        if whatcity == None:
            a = scanwindow()
            auto.moveTo(x = main_x+240, y = main_y+215, duration = 0.5)
            auto.dragRel(drag_dist, 0, duration = 0.30)
            time.sleep(2)
            b = auto.screenshot(region=(main_x+120, main_y+215, 200, 200))
            c = auto.locate(b, a, confidence = 0.8)
            if c != None:
                drag_dist = drag_dist * -1
                continue
            if c == None:
                drag_dist = drag_dist
                continue
        
        if whatcity:
            global endgame_check
            if endgame_check == 1:
                endgame_check = 0
                first_time()
                
            break
    return current_areas
            
def item_to_place(item_name):
    place = None
    i = 0
    try:
        while place == None:
            if farm_lists[i][0] == item_name:
                place = farm_lists[i][1]
            else:
                i += 1
    except IndexError: 
        print('item_name error. please input it the right way!')
    
    return place

def move_to(city_name):
    click_buttons('go_button')
    #no areas button in HQ
    try:
        click_buttons('areas_button')
    except TypeError:
        pass
    try:
        click_buttons('areas_%s' %city_name)
    except TypeError:
        try:
            auto.moveTo(x = main_x+240, y = main_y+430, duration = 0.5)
            auto.dragRel(0, -300, duration = 0.30, pause = 2)
            click_buttons('areas_%s' %city_name)
        except TypeError:
            auto.moveTo(x = main_x+240, y = main_y+430, duration = 0.5)
            auto.dragRel(0, 300, duration = 0.30, pause = 2)
            click_buttons('areas_%s' %city_name)
    time.sleep(5)
    return


# %%

def first_time():
    #announcement endgame
    click_buttons('go_button')
    time.sleep(2)
    click_buttons('close_button')
    time.sleep(2)
    return

# %%
    
class ocr_prep:
    
    def __init__(self, name):
        self.name = name
    
    @staticmethod
    def reader(query_img):
        with Image(filename = r'IMG\temp\%s.png' %query_img) as img:
            img.transform('300x300','900%')
            img.save(filename = r'IMG\temp\testla.png')
        
        img = cv2.imread(r'IMG\temp\testla.png')
        a = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        b = a.copy()
        for i in range(len(b)):
            for j in range(len(b[0])):
                if b[i][j] > 180 and b[i][j] < 255:
                    b[i][j] = 0
                else:
                    b[i][j] = 255
        
        return b
    
    def read_quest_timer(self):
        namesake = 'quest_timer_pic'
        arbit_timer = [0,0,0]
        pattern = '[0-9]{2}\w[0-9]{2}\w'
        window = scanwindow()
        hourglass = auto.locate(r'IMG\quest\timer_hourglass.png', window, confidence = 0.6)
        auto.screenshot(r'IMG\temp\%s.png' %namesake, region=(main_x+hourglass[0]-100, main_y+hourglass[1]+20, 80, 20))
        timer_text_matrix = self.reader(namesake)
        for i in range(4):
            timer_text = ocr.image_to_string(timer_text_matrix, config = '--oem %s --psm 6' %i)
            timer_text = timer_text.replace("O","0")
            timer_text = timer_text.replace(" ","")
            timer_regex = re.match(pattern, timer_text)
            if timer_regex:
                print('will check back in ' + str(timer_regex[0]))
                for i in range(2):
                    if i == 0:
                        if timer_regex[0][2] == 'H':
                            arbit_timer[0] = int(timer_regex[0][0:2])
                        if timer_regex[0][2] == 'M':
                            arbit_timer[1] = int(timer_regex[0][0:2])
                    if i == 1:
                        if timer_regex[0][5] == 'M':
                            arbit_timer[1] = int(timer_regex[0][3:5])
                        if timer_regex[0][5] == 'S':
                            arbit_timer[2] = int(timer_regex[0][3:5])
                break
            else:
                continue
        
        if arbit_timer == [0,0,0]:
            print('quest timer not identified. will check again in the next 2 minutes..')
            arbit_timer[1] = 2
        
        return arbit_timer
    
    
    def read_quest(self):
        #use to read quest
        namesake = 'title_take'
        quest_list = []
        window = scanwindow()
        quest_list_pre = list(auto.locateAll(r'IMG\quest\name_box_detect.png', window, confidence = 0.9))
        print(len(quest_list_pre))
        for i in range(len(quest_list_pre)):
            claim_query = self.check_claim(quest_list_pre[i])
            if claim_query:
                auto.screenshot(r'IMG\temp\%s.png' %namesake, 
                                region = (main_x+quest_list_pre[i][0]+quest_list_pre[i][2] - 250, 
                                main_y+quest_list_pre[i][1]+quest_list_pre[i][3] - 140,
                                240, 35))
                text_matrix = self.reader(namesake)
                
                text = ocr.image_to_string(text_matrix, config = '--oem 0')
                print(text)
                quest_list.append(text)
            else:
                continue
        return quest_list
    
    @staticmethod
    def check_claim(quest_list_pre):
        claim_query = 0
        claim_test = auto.screenshot(region = (main_x+quest_list_pre[0]+quest_list_pre[2] - 250, 
                        main_y+quest_list_pre[1], 240, 145))
        claim_chest = auto.locate(r'IMG\quest\quest_claim.png', claim_test, confidence = 0.7)
        if claim_chest:
            click_buttons(r'quest\quest_claim')
            time.sleep(1)
            auto.click(main_x+270, main_y+130)
            time.sleep(1)
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
        
        elif claim_chest == None:
            claim_test = auto.screenshot(region = (main_x+quest_list_pre[0]+quest_list_pre[2] - 250, 
                        main_y+quest_list_pre[1], 240, 145))                        
            claimed = auto.locate(r'IMG\quest\quest_claimed.png', claim_test, confidence = 0.8)
            if claimed == None:
                claim_query = 1
        
        return claim_query
        
    def quest_module(self, area_name):
        print('checking quest...')
        click_buttons('board_%s' %area_name)
        quest_list = self.read_quest()
        quest_place = []
        quest_amount = []
        for j in range(len(quest_list)):
            for k in range(len(quest_NMA)):
                try:
                    rege_test = re.match(quest_list[j], quest_NMA[k][0], re.IGNORECASE)
                    #quest_NMA[k].index(quest_list[j])
                    if rege_test:
                        quest_place.append(quest_NMA[k][1])
                        quest_amount.append(quest_NMA[k][2])
                except:
                    continue
        quest_timer = self.read_quest_timer()
        return quest_place, quest_amount, quest_timer

#%%
        
def dialog_box_check():
    while True:
        window = scanwindow()
        dialog_box = auto.locate(r'IMG\delivery\delivery_finish1.png', window, confidence = 0.6)
        if dialog_box:
            auto.click(main_x+270, main_y+130)
            time.sleep(1)
        else:
            break
    return

def delivery_post_click(i):
    if city == 'HQ' and i == 0:
        auto.moveTo(x = main_x+240, y = main_y+215, duration = 0.5)
        auto.dragRel(-300, 0, duration = 0.30)
    time.sleep(2)
    click_buttons('delivery\delivery_%s' %city)
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
    claim_test1 = scanwindow()
    for i in range(len(chest1)):
        click_test1 = auto.locate(r'IMG\%s.png' %chest1[i], claim_test1, confidence = 0.6)
        if click_test1:
            auto.click(main_x+270, main_y+130)
            time.sleep(2)
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
    drag_count = 0
    window = scanwindow()
    i = 0
    while True:
        try:
            delivery_post_click(i)
        except TypeError:
            pass
        try:
            window = scanwindow()
            if city == 'HQ':
                safe_mode = 1
                if i == 0:
                    print('You are fighting ninjas! Hard enemies detected. Safe mode engaged.')
                view_button = auto.locate(r'IMG\delivery\delivery_view_HQ.png', window, confidence = 0.6)
            else:
                view_button = auto.locate(r'IMG\delivery\delivery_view.png', window, confidence = 0.6)
                check_rank = auto.screenshot(r'IMG\temp\asdasd.png', region = (main_x + view_button[0], main_y + view_button[1] - 100, 150, 100))
                rank_S = auto.locate(r'IMG\delivery\delivery_rankS.png', check_rank, confidence = 0.9)
                if rank_S:
                    safe_mode = 1
                    print('Hard enemies detected. Safe mode engaged!')
            window = scanwindow()
            if city == 'HQ':
                click_buttons('delivery\delivery_view_HQ')
            else:
                click_buttons('delivery\delivery_view')
            time.sleep(1)
            window = scanwindow()
            if city != 'HQ':
                click_buttons('go_button')
            time.sleep(3)
            combat_module()
            #time.sleep(3)
            if city != 'HQ':
                dialog_box_check()
            time.sleep(1)
            delivery_chest_claim()
        except TypeError:
            auto.moveTo(x = main_x+240, y = main_y+430, duration = 0.5)
            auto.dragRel(0, -300, duration = 0.30, pause = 3)
            if drag_count != 0:
                print('no more delivery in this city. checking timer...')
                break
            drag_count += 1
        safe_mode = 0
        i += 1
    a = ocr_prep('a')
    try:
        delivery_post_click(i)
    except TypeError:
        pass
    delivery_timer = a.read_quest_timer()
    return delivery_timer

#%%
    
def combat_module():
    is_a_delivery = 0
    timeout = time.time() + 7
    while True:
        try:
            auto.PAUSE = 0.1
            # battle
            battle_window = scanwindow()
            atk = auto.locate(r'IMG\%s.png' %sword_skill, battle_window, confidence = 0.8)
            shield = auto.locate(r'IMG\%s.png' %shield_skill, battle_window, confidence = 0.8)
            pot = auto.locate(r'IMG\%s.png' %pot_type, battle_window, confidence = 0.8)
            if shield != None:
                auto.click(main_x+auto.center(shield)[0], main_y+auto.center(shield)[1])
                timeout = time.time() + 7
                #safe mode: only use charge when shield active
                if safe_mode:
                    if atk != None:
                            auto.click(main_x+auto.center(atk)[0], main_y+auto.center(atk)[1])
                            timeout = time.time() + 7
            if safe_mode == 0:
                if atk != None:
                    auto.click(main_x+auto.center(atk)[0], main_y+auto.center(atk)[1])
                    timeout = time.time() + 7
            if pot != None:
                auto.click(main_x+auto.center(pot)[0], main_y+auto.center(pot)[1])
                timeout = time.time() + 7
            
            #time out meaning midroll ads
            if time.time() > timeout:
                auto.PAUSE = 1
                # remove dialog (needs improving)
                auto.click(x = main_x+240, y = main_y+430, duration = 0.5, clicks = 3)
                midroll_window = scanwindow()
                traveler = auto.locate(r'IMG\battle_midroll.png', midroll_window, confidence = 0.6)
                midroll_go1 = auto.locate(r'IMG\go_button.png', midroll_window, confidence = 0.6)
                finish = auto.locate(r'IMG\battle_finish.png', midroll_window, confidence = 0.6)
                deliver_dialog = auto.locate(r'IMG\delivery\delivery_finish1.png', midroll_window, confidence = 0.6)
                if traveler:
                    print('traveler found! skipping...')
                    close_button = auto.locate(r'IMG\announcement_endgame_close_button.png', midroll_window, confidence = 0.6)
                    auto.click(main_x+auto.center(close_button)[0], main_y+auto.center(close_button)[1], duration = 0.5)
                    a = scanwindow()
                    midroll_go2 = auto.locate(r'IMG\go_button.png', a, confidence = 0.6)
                    auto.click(main_x+auto.center(midroll_go2)[0], main_y+auto.center(midroll_go2)[1], duration = 0.5)
                    timeout = time.time() + 7
                if midroll_go1:
                    print('The harem girls found! receiving love...')
                    auto.click(main_x+auto.center(midroll_go1)[0], main_y+auto.center(midroll_go1)[1], duration = 0.5)
                    timeout = time.time() + 7
                if deliver_dialog:
                    is_a_delivery = 1
                    auto.click(main_x+270, main_y+130, clicks = 7, interval = 1)
                    timeout = time.time() + 4
                if finish:
                    auto.click(main_x+auto.center(finish)[0], main_y+auto.center(finish)[1], duration = 0.5)
                    print('sortie finished!')
                    timeout = time.time() + 7
                    time.sleep(8)
                    while True:
                        check = scanwindow()
                        a = auto.locate(r'IMG\go_button.png', check, confidence = 0.6)
                        if a == None:
                            print('not ready for next sortie. waiting...')
                            if is_a_delivery == 0:
                                auto.click(main_x+270, main_y+130)
                                time.sleep(1)
                                continue
                            else:
                                break
                        if a != None:
                            print(r"all's ready! let's go for the next one!")
                            timeout = time.time() + 7
                            break
                    break
        except IndexError:
            print('error?')
            break
    
    return

# %%
        
def auto_farm(item_name):
    
    place = item_to_place(item_name)
    
    window = scanwindow()
    # check where you at
    current_place = None
    check = None
    for i in range(len(areas_buttons)):
        check = auto.locate(r'IMG\%s.png' %boards[i], window, confidence = 0.6)
        if check == None:
            continue
        else:
            current_place = boards[i]
            break
    
    #check whether the current place is the place to farm or not
    check2 = re.match(current_place[6:], place)
    if check2:
        print('the place to farm is in this city, moving to the farming area...')
    else:
        print('the place to farm is elsewhere, moving to the city first...')
        
        #endgame test
        #first_time()
        
        #move to the right city
        click_buttons('go_button')
        pattern = '[a-zA-Z0-9]{2,3}'
        check3 = re.match(pattern, place)
        try:
            click_buttons('areas_button')
            click_buttons('areas_%s' %check3[0])
        except TypeError:
            auto.moveTo(x = main_x+240, y = main_y+430, duration = 0.5)
            auto.dragRel(0, -300, duration = 0.30, pause = 2)
            click_buttons('areas_%s' %check3[0])
        print(r"you're in the city now. starting farm...")   
        time.sleep(7)
    
    #first_time()    
    for i in range(10000):
        # farming
        print('Sortie #' + str(i+1))
        click_buttons('go_button')
        time.sleep(2)
        try:
            click_buttons(place)
        except TypeError:
            try:
                auto.moveTo(x = main_x+240, y = main_y+430, duration = 0.5)
                auto.dragRel(0, -300, duration = 0.30, pause = 3)
                click_buttons(place)
            except TypeError:
                auto.moveTo(x = main_x+240, y = main_y+430, duration = 0.5)
                auto.dragRel(0, 300, duration = 0.30, pause = 3)
                click_buttons(place)
        time.sleep(3)
        combat_module()
    print('sortie finished')
    return

# need to check whether endgame announcement out or not when pressing go_button
# need to do better job at identifying city (can try to swipe)
# need to handle if dead in sortie (and also if HP isn't enough for sortie)


# %%
# PARAMETERS
item_name = "ceruleaf"
sword_skill = 'b1_blitz'
shield_skill = 'b2_elusive_cover'
pot_type = 'b3_4'
# future implementation, check whether skill is equipped.


#safe_mode is automated
safe_mode = 0
#endgame_check is used once only
endgame_check = 1

farm = 0
#%%
#auto_farm(item_name)

#define where the main window is
main_screen, main_x, main_y = main_screen_detection()
quest_test = ocr_prep('quest_mod')

current_city = check_city()
city = 'HQ'
if current_city != city:
    move_to(city)
time.sleep(3)
delivery_timer = delivery()

'''
for i in range(len(areas)-1):
    current_city = check_city()
    city = areas[i+1]
    if current_city != city:
        move_to(city)
    
    quest_place, quest_amount, quest_timer = quest_test.quest_module(city)
    quest_timer_save = time.time()+(3600*quest_timer[0])+(60*quest_timer[1])+(1*quest_timer[2])
    time_and_place['%s_quest' %city] = quest_timer_save
    
    
if farm:
    while main_screen:
        auto_farm(item_name)
'''    
'''
while True:
    try:
        check_city()
    except:
        try:
            click_buttons('battle_finish')
        except:
            try:
                click_buttons('close_button')
            except:
                pass
        time.sleep(10)
        continue
'''

#%%
