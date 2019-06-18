# -*- coding: utf-8 -*-
"""
POSTKNIGHT BOT
trial01 - autofarm

Created on Fri May 31 07:59:57 2019

@author: fddot
"""
version = 4.0

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
import pandas as pd
import numpy as np
import copy

os.chdir('E:\Project\Postknight-auto')

auto.FAILSAFE = True
ocr.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# %%
# DATABASES

stage_database = pd.read_csv(r'IMG\monster\stage_database.csv', index_col = 0)

quest_NMA = [['Cub Care', 'PP_1', 30], ['Dire Hunt', 'PP_2', 30], ['Howling Affair', 'PP_3', 10],
             ['Stolen Shots', 'PP_1', 10], [r"Now You Don't", 'PP_5', 10], ['Call The Cops', 'PP_5', 10], 
             ['Sealed Range', 'PP_5', 10], ['Criminal Command', 'PP_5', 1],
             
             ['Drop It', 'SB_2', 30], ['Bursting Bubbles', 'SB_2', 30], ['Deadly Swims', 'SB_3', 10],
             ['In A Pinch', 'SB_2', 10], ['Ahoy Kiddos', 'SB_5', 10], ['Aye Aye Sir', 'SB_5', 10], 
             ['Song Stopper', 'SB_3', 10], ['Captain Crook', 'SB_5', 1], 
             
             ['Flitter By', 'GF_1', 30], ['Birds Of Prey', 'GF_1', 30], ['Scurry Away', 'GF_3', 10],
             ['Scattered Defense', 'GF_3', 10], ['Snitch Pitch', 'GF_5', 10], ['At Easer', 'GF_5', 10],
             ['Baron Berth', 'GF_5', 10], ['Cyclone Chief', 'GF_5', 1], 
             
             ['Easy Piffsy', 'CD_1', 30], ['Huff And Puff', 'CD_1', 30], ['Spiky Encounter', 'CD_1', 10],
             ['Puffed Effort', 'CD_3', 10], ['Clan Craze', 'CD_5', 10], ['Tuff One', 'CD_3', 10], 
             ['Phony Priest', 'CD_5', 10], ['Sect Lord', 'CD_5', 1], 
             
             ['Chest Clone', 'VOG_1', 30], ['Fragile Form', 'VOG_1', 30], ['Gold Digger', 'VOG_3', 10],
             ['Bombs Away', 'VOG_3', 30], ['What He Lac ks', 'VOG_4', 10], ['Mine Time', 'VOG_5', 10], 
             ['Excavating Exec', 'VOG_5', 10], ['Dredge Dominion', 'VOG_5', 1], 
             
             ['Slimy Situation', 'FF_3', 30], ['Whooping', 'FF_2', 30], ['Prickle Party', 'FF_7', 30],
             ['Masqueraid', 'FF_3', 30], ['Phantom Menace', 'FF_6', 15], ['Worlord', 'FF_3', 15], 
             ['Rowdy Ruffians', 'FF_8', 30], ['Ranged Rufians', 'FF_7', 30], ['Walla Bing Bang', 'FF_8', 10],
             ['Hoo The Boss', 'FF_8', 1],
             
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

city_fullname = {'PP': 'Pompon', 'SB': 'Shello Bay', 'GF': 'Griffondell', 'CD': 'Caldemount',
                 'VOG': 'Valley of Gold', 'FF': 'Fractured Forest', 'HQ': 'Headquarters', }

chest1 = ['delivery_chestB1','delivery_chestA1','delivery_chestS1']
chest2 = ['delivery_chestB2','delivery_chestA2','delivery_chestS2']
areas_buttons = ['areas_HQ', 'areas_PP','areas_SB','areas_GF','areas_CD','areas_VOG','areas_FF']
boards = ['board_HQ', 'board_PP','board_SB','board_GF','board_CD','board_VOG','board_FF']
areas = ['HQ', 'PP', 'SB', 'GF', 'CD', 'VOG', 'FF']
window_list = ['window_routeselect','window_achievement','window_inventory','window_shop','window_skills','window_stats', 'window_division', 'window_delivery', 'window_quest']
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

def click_buttons_HC(button):
    window = scanwindow()
    location = auto.locate(r'IMG\%s.png' %button, window, confidence = 0.9)
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
        whatwindow = auto.locate(r'IMG\%s.png' %window_list[i], check, confidence = 0.9)
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
                cityname = city_fullname[boards[i][6:]]
                print('you are at %s!' %cityname)
                current_areas = boards[i][6:]
                break
        
        if whatcity == None:
            a = scanwindow()
            auto.moveTo(x = main_x+240, y = main_y+215, duration = 0.5)
            auto.dragRel(drag_dist, 0, duration = 0.30)
            time.sleep(1)
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
    print('You are farming %s! Searching for best spot...' %item_name)
    try:
        while place == None:
            if farm_lists[i][0] == item_name:
                place = farm_lists[i][1]
            else:
                i += 1
        print(r"Best spot found! It's in %s! Let's go there." %place)
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

def watch_ads():
    click_buttons(r'monster\traveler_watch_ads')
    while True:
        timeout_ads = time.time()+40
        time.sleep(10)
        window1 = scanwindow()
        time.sleep(10)
        window2 = scanwindow()
        a = auto.locate(window2, window1, confidence = 0.95)
        if a or timeout_ads - time.time() <= 0:
            auto.click(main_x+505, main_y+760)
            time.sleep(5)
            break
    
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
    @staticmethod
    def reader_petgirls(query_img):
        with Image(filename = r'IMG\temp\%s.png' %query_img) as img:
            img.transform('300x300','900%')
            img.save(filename = r'IMG\temp\testla.png')
        
        img = cv2.imread(r'IMG\temp\testla.png')
        a = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        b = a.copy()
        for i in range(len(b)):
            for j in range(len(b[0])):
                if b[i][j] > 110 and b[i][j] < 130:
                    b[i][j] = 0
                else:
                    b[i][j] = 255
        
        return b
    
    
    def read_quest_timer(self):
        namesake = 'quest_timer_pic'
        arbit_timer = [0,0,0]
        pattern = '[0-9]{2}[a-zA-Z][0-9]{2}[a-zA-Z]'
        window = scanwindow()
        hourglass = auto.locate(r'IMG\quest\timer_hourglass.png', window, confidence = 0.6)
        auto.screenshot(r'IMG\temp\%s.png' %namesake, region=(main_x+hourglass[0]-100, main_y+hourglass[1]+20, 80, 20))
        timer_text_matrix = self.reader(namesake)
        for i in range(4):
            timer_text = ocr.image_to_string(timer_text_matrix, config = '--oem %s --psm 7' %i)
            timer_text = timer_text.replace("O","0")
            timer_text = timer_text.replace(" ","")
            #timer_text = timer_text.replace("S", "5")
            timer_regex = re.search(pattern, timer_text)
            if timer_regex:
                print('Timer is ' + str(timer_regex[0]))
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
        click_buttons('close_button')
        time.sleep(2)
        return arbit_timer
    
    def read_petgirls_timer1(self):
        namesake = 'quest_timer_pic'
        arbit_timer = [0,0,0]
        pattern = '[0-9]{2}[a-zA-Z][0-9]{2}[a-zA-Z]'
        window = scanwindow()
        hourglass = auto.locate(r'IMG\petgirls\petgirls_gift.png', window, confidence = 0.6)
        auto.screenshot(r'IMG\temp\%s.png' %namesake, region=(main_x+hourglass[0]-95, main_y+hourglass[1]+10, 90, 25))
        timer_text_matrix = self.reader_petgirls(namesake)
        for i in range(4):
            timer_text = ocr.image_to_string(timer_text_matrix, config = '--oem %s --psm 7' %i)
            timer_text = timer_text.replace("O","0")
            timer_text = timer_text.replace(" ","")
            #timer_text = timer_text.replace("S","5")
            timer_text = timer_text.replace("|","")
            timer_text = timer_text.replace("'","")
            timer_regex = re.search(pattern, timer_text)
            if timer_regex:
                print('Timer is ' + str(timer_regex[0]))
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
            print(timer_text)
            arbit_timer[1] = 2
        try:
            click_buttons('close_button')
        except TypeError:
            pass
        time.sleep(2)
        return arbit_timer

    def read_petgirls_timer2(self):
        namesake = 'quest_timer_pic'
        arbit_timer = [0,0,0]
        pattern = '[0-9]{2}[a-zA-Z][0-9]{2}[a-zA-Z]'
        window = scanwindow()
        hourglass = auto.locate(r'IMG\petgirls\petgirls_receive.png', window, confidence = 0.6)
        auto.screenshot(r'IMG\temp\%s.png' %namesake, region=(main_x+hourglass[0]-95, main_y+hourglass[1], 90, 25))
        timer_text_matrix = self.reader_petgirls(namesake)
        for i in range(4):
            timer_text = ocr.image_to_string(timer_text_matrix, config = '--oem %s --psm 7' %i)
            timer_text = timer_text.replace("O","0")
            timer_text = timer_text.replace(" ","")
            #timer_text = timer_text.replace("S", "5")
            timer_text = timer_text.replace("|","")
            timer_text = timer_text.replace("'","")
            timer_regex = re.search(pattern, timer_text)
            if timer_regex:
                print('Timer is ' + str(timer_regex[0]))
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
            print(timer_text)
            arbit_timer[1] = 2
        try:
            click_buttons('close_button')
        except TypeError:
            pass
        time.sleep(2)
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
                                region = (main_x+quest_list_pre[i][0]+quest_list_pre[i][2] - 235, 
                                main_y+quest_list_pre[i][1]+quest_list_pre[i][3] - 140,
                                205, 35))
                text_matrix = self.reader(namesake)
                
                text = ocr.image_to_string(text_matrix, config = '--oem 0 --psm 7')
                text = text.replace(" ", "")
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
        monster_id = []
        for j in range(len(quest_list)):
            for k in range(len(quest_NMA)):
                try:
                    rege_test = re.search(quest_list[j], quest_NMA[k][0].replace(' ', ''), re.IGNORECASE)
                    #quest_NMA[k].index(quest_list[j])
                    if rege_test:
                        if rege_test[0] == 'Eyeforanad':
                            watch_ads()
                            delivery_chest_claim()
                            continue
                        else:
                            monster_id.append(k)
                            quest_place.append(quest_NMA[k][1])
                            quest_amount.append(quest_NMA[k][2])
                except:
                    continue
        quest_timer = self.read_quest_timer()
        return quest_place, quest_amount, monster_id, quest_timer


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
    auto.click(main_x+270, main_y+130, clicks = 10, interval = 0.5)
    
    '''
    claim_test1 = scanwindow()
    for i in range(len(chest1)):
        click_test1 = auto.locate(r'IMG\%s.png' %chest1[i], claim_test1, confidence = 0.4)
        if click_test1:
            auto.click(main_x+270, main_y+130)
            time.sleep(2)
    claim_test2 = scanwindow()
    for j in range(len(chest2)):
        click_test = auto.locate(r'IMG\%s.png' %chest2[j], claim_test2, confidence = 0.4)
        if click_test:
            while True:
                claim_test3 = scanwindow()
                click_test3 = auto.locate(r'IMG\%s.png' %chest2[j], claim_test3, confidence = 0.7)
                if click_test3:
                    auto.click(main_x+270, main_y+130)
                    time.sleep(1)
                else:
                    time.sleep(2)
                    break
        elif click_test == None:
            continue
    '''
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
            print('delivery done. claiming chest...')
            time.sleep(2)
            if city != 'HQ':
                dialog_box_check()
                time.sleep(2)
            delivery_chest_claim()
            time.sleep(1)
        except TypeError:
            if drag_count != 0:
                print('no more delivery in this city. checking timer...')
                break
            drag_count += 1            
            auto.moveTo(x = main_x+240, y = main_y+430, duration = 0.5)
            auto.dragRel(0, -300, duration = 0.30, pause = 3)
        safe_mode = 0
        i += 1
    a = ocr_prep('a')
    try:
        delivery_post_click(i)
    except TypeError:
        pass
    delivery_timer = a.read_quest_timer()
    safe_mode = 0
    return delivery_timer

# %%
def pet_module():
    #current_city = check_city()
    time.sleep(5)
    pet_timer = []
    a = ocr_prep('a')
    #feed pet
    for i in range(2):
        try:
            auto.click(main_x + 160, main_y + 435)
            time.sleep(1)
            click_buttons_HC('petgirls\pet_feed')
            click_buttons('petgirls\pet_love')
            click_buttons_HC('petgirls\pet_feed')
            time.sleep(1)
            dialog_box_check()
            time.sleep(1)
        except TypeError:
            print('Pet already fed, checking timer...')
            temp1 =  a.read_petgirls_timer1()
            pet_timer.append(temp1)
            auto.click(main_x + 270, main_y + 230)
            time.sleep(1)
            break
    time.sleep(2)
    #pet receive
    for i in range(2):
        try:
            auto.click(main_x + 160, main_y + 435)
            time.sleep(1)
            click_buttons_HC('petgirls\pet_receive')
            time.sleep(1)
            delivery_chest_claim()
            time.sleep(1)
            dialog_box_check()

            time.sleep(1)
        except TypeError:
            print('Already received gift from pet, checking timer...')
            temp2 =  a.read_petgirls_timer2()
            pet_timer.append(temp2)
            auto.click(main_x + 270, main_y + 230)
            time.sleep(1)
            break
    return pet_timer

def girls_module():
    drag_dist = -300
    city_girls = []
    
    for i in range(2):
        try:
            arbit_girl = 'girls_%s' %city+str(i+1)
            while True:
                check = scanwindow()
                wheredagirl = auto.locate(r'IMG\petgirls\%s.png' %arbit_girl, check, confidence = 0.6)
                if wheredagirl != None:
                    print(r"Found some babe. let's date!")
                    time.sleep(1)
                    girls_timer = girls_module2(arbit_girl)
                    city_girls.extend(girls_timer)
                    break
                
                if wheredagirl == None:
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
        except OSError:
            continue
    return city_girls

def girls_module2(arbit_girl):
    time.sleep(3)
    girls_timer = []
    a = ocr_prep('a')
    #feed pet
    for i in range(2):
        try:
            click_buttons(r"petgirls\%s" %arbit_girl)
            time.sleep(1)
            dialog_box_check()
            time.sleep(1)
            click_buttons_HC('petgirls\girls_gift')
            click_buttons('petgirls\pet_love')
            click_buttons_HC('petgirls\girls_gift')
            time.sleep(1)
            dialog_box_check()
            time.sleep(1)
        except TypeError:
            print('Already giving gift to girls, checking timer...')
            temp1 =  a.read_petgirls_timer1()
            girls_timer.append(temp1)
            auto.click(main_x + 270, main_y + 230)
            time.sleep(1)
            break
    time.sleep(2)
    #pet receive
    for i in range(2):
        try:
            click_buttons(r"petgirls\%s" %arbit_girl)
            time.sleep(1)
            dialog_box_check()
            time.sleep(1)
            click_buttons_HC('petgirls\pet_receive')
            time.sleep(1)
            dialog_box_check()
            time.sleep(1)
            #lazy shit coding
            auto.click(main_x + 270, main_y + 230, clicks = 7, interval = 0.5)
            #delivery_chest_claim()
            time.sleep(1)
            dialog_box_check()
            #consecutive += 1
            time.sleep(1)
        except TypeError:         
            print('Already received gift from the gal, checking timer...')
            temp2 =  a.read_petgirls_timer2()
            girls_timer.append(temp2)
            auto.click(main_x + 270, main_y + 230)
            time.sleep(1)
            break
    return girls_timer

def merchant_module():
    drag_dist = -300
    merchant_timer = []
    arbit_merch = 'merchant_%s' %city
    while True:
        try:
            check = scanwindow()
            wheredagirl = auto.locate(r'IMG\merchant\%s.png' %arbit_merch, check, confidence = 0.5)
            if wheredagirl != None:
                print(r"Found the merchant! Let's buy something..")
                time.sleep(1)
                merch_timer = merchant_module2(arbit_merch)
                merchant_timer.extend(merch_timer)
                break
            
            if wheredagirl == None:
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
        except TypeError:
            continue
    return merchant_timer

def merchant_module2(arbit_merch):
    drag_dist = -150
    time.sleep(3)
    merch_timer = []
    a = ocr_prep('a')
    click_buttons(r"merchant\%s" %arbit_merch)
    time.sleep(1)
    dialog_box_check()
    time.sleep(1)    
    #buy item
    while True:
        window = scanwindow()
        can_buy = auto.locate(r"IMG\merchant\merchant_buy.png", window, confidence = 0.8)
        if can_buy:
            auto.click(main_x + can_buy[0] + 100 ,main_y + can_buy[1]+ 30)
            time.sleep(1)
            click_buttons_HC('merchant\merchant_trade')
            time.sleep(1)
        elif can_buy == None:
            window1 = scanwindow()
            auto.moveTo(x = main_x+240, y = main_y+415, duration = 0.5)
            auto.dragRel(0, drag_dist, duration = 0.30)
            time.sleep(2)
            window2 = scanwindow()
            bot_test = auto.locate(window2, window1, confidence = 0.95)
            if bot_test:
                print('Whoops, seems you can buy nothing anymore. Checking timer...')
                temp1 =  a.read_quest_timer()
                merch_timer.extend(temp1)
                time.sleep(1)
                break
    time.sleep(2)
    return merch_timer
        

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
                #auto.click(x = main_x+240, y = main_y+430, duration = 0.5, clicks = 3)
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
                    #print('issamemario')
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
                                #print('isnotdelivery')
                                auto.click(main_x+270, main_y+130)
                                time.sleep(1)
                                continue
                            elif is_a_delivery == 1:
                                #print('issadelivery')
                                break
                        elif a != None:
                            print(r"all's ready! let's go for the next one!")
                            timeout = time.time() + 7
                            break
                    break
        except IndexError:
            print('error?')
            break
    
    return

# %%
        
def auto_farm(place):
    farm_count = 0
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
    check2 = re.search(current_place[6:], place)
    if check2:
        print('the place to farm is in this city, moving to the farming area...')
    else:
        print('the place to farm is elsewhere, moving to the city first...')
        
        #endgame test
        #first_time()
        
        #move to the right city
        click_buttons('go_button')
        pattern = '[a-zA-Z0-9]{2,3}'
        check3 = re.search(pattern, place)
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
    for i in range(n_sortie):
        # farming
        print('Sortie start!')
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
        farm_count += 1
        if farm_count == 1:
            break
    print('sortie finished')
    return

# need to check whether endgame announcement out or not when pressing go_button
# need to do better job at identifying city (can try to swipe)
# need to handle if dead in sortie (and also if HP isn't enough for sortie)

# %%
def save_timer(place_type, city, arbit_timer):
    arbit_timer_save = time.time()+(3600*arbit_timer[0])+(60*arbit_timer[1])+(1*arbit_timer[2])
    time_and_place['%s_%s' %(city, place_type)] = arbit_timer_save
    return

def determine_quest_place(quest_place, quest_amount, monster_id, stage_database):
    quest_place_list = []
    quest_dict = {}
    query = [0] * len(stage_database.columns)
    for i in range(len(monster_id)):
        query[monster_id[i]] = quest_amount[i]
        if quest_place[i] in quest_dict:
            continue
        quest_dict["{0}".format(quest_place[i])] = stage_database.loc[quest_place[i]]
    while sum(query) > 0:
        temp_quest_dict = {}
        for k in range(len(monster_id)):
            if quest_place[k] in temp_quest_dict:
                continue
            temp_quest_dict["{0}".format(quest_place[k])] = list(np.array(quest_dict[quest_place[k]] * np.array(query)))
        max_key = max(temp_quest_dict, key=lambda key: sum(temp_quest_dict[key]))
        new_query = list(np.array(query) - np.array(quest_dict[max_key]))
        for j in range(len(new_query)):
            if new_query[j] < 0:
                new_query[j] = 0
        query = new_query.copy()
        quest_place_list.append(max_key)
        
    return quest_place_list

def timeout_module(timed_out):
    city_lists = []
    arbit_type_lists = []
    for i in range(len(timed_out)):
        pattern1 = r"[A-Z]{2,3}"
        dacity = re.search(pattern1, timed_out[i])
        city_lists.append(dacity[0])
        pattern2 = r"_[A-Za-z0-9]*_?"
        dataipu = re.search(pattern2, timed_out[i])
        dataipu2 = copy.copy(dataipu[0])
        dataipu2 = dataipu2.replace('_','')
        dataipu2 = dataipu2.replace('1','')
        dataipu2 = dataipu2.replace('2','')
        arbit_type_lists.append(dataipu2)
    
    last_task = [0,0]
    for j in range(len(city_lists)):
        if last_task[0] == city_lists[j] and last_task[1] == arbit_type_lists[j]:
            continue
        main_module(city_lists[j], arbit_type_lists[j])
        last_task[0] = city_lists[j]
        last_task[1] = arbit_type_lists[j]
        
    return

#%%

def main_module(city_lists, arbit_type_lists):    
    global n_sortie, city
    
    current_city = check_city()
    city = copy.copy(city_lists)
    cityname = city_fullname[city]
    
    #quest_module
    if arbit_type_lists == 'quest' and quest_trigger == 1:
        print(r"Checking %s's board quest..." %cityname)
        if city != 'HQ':
            if current_city != city:
                move_to(city)
            #HQ doesn't have quest board
            quest_place, quest_amount, monster_id, quest_timer = quest_test.quest_module(city)
            quest_place_list = determine_quest_place(quest_place, quest_amount, monster_id, stage_database)
            print(quest_place_list)
            for j in range(len(quest_place_list)):
                auto_farm(quest_place_list[j])
            if quest_place_list:
                dummy1, dummy2, dummy3, quest_timer = quest_test.quest_module(city)
            save_timer('quest', city, quest_timer)
        print(r"All's done! Let's move on..")
        time.sleep(3)
    
    #delivery module
    if arbit_type_lists == 'delivery' and delivery_trigger == 1:
        if current_city != city:
            move_to(city)
        print(r"Checking %s's delivery quest..." %cityname)
        delivery_timer = delivery()
        save_timer('delivery', city, delivery_timer)
        print(r"All's done! Let's move on..")
    
    #pet_module
    if arbit_type_lists == 'pet' and petting_trigger == 1:
        if city != 'HQ' and city != 'FF':
            if current_city != city:
                move_to(city)
            print(r"Playing with %s's pets..." %cityname)
            pet_timer = pet_module()
            time_type = ['pet_gift', 'pet_receive']
            for i in range(2):
                save_timer(time_type[i], city, pet_timer[i])
            print('Finished playing with the good boi! Moving on...')
    
    #girls_module
    
    if arbit_type_lists == 'girl' and girls_trigger == 1:
        if city != 'HQ' and city!= 'FF' and city != 'SB':
            if current_city != city:
                move_to(city)
            print(r"Date with the %s's gal/s..." %cityname)
            girls_type = ['gift','receive','gift','receive']
            girl_num = [1,1,2,2]
            girls_timer = girls_module()
            for i in range(len(girls_timer)):
                save_timer('girl%s_%s' %(girl_num[i], girls_type[i]), city, girls_timer[i])
            print('Date went well! Moving on...')
    
    #merchant_module
    if arbit_type_lists == 'merchant' and merchant_trigger == 1:
        if city != 'HQ':
            if current_city != city:
                move_to(city)
            print(r"Let's buy some item from the merchant!")
            merchant_timer = merchant_module()
            save_timer('merchant', city, merchant_timer)
            print('We already bought everything that can be traded! Moving on...')
    
    return

def initialization():
    try:
        click_buttons('idle_mail')
        time.sleep(0.5)
        click_buttons('battle_finish')
        click_buttons('battle_finish')
    except TypeError:
        pass
    
    return
# %%
# PARAMETERS
item_name = "firebloom"
sword_skill = 'b1_blitz'
shield_skill = 'b2_elusive_cover'
pot_type = 'b3_4'
# future implementation, check whether skill is equipped.

################
### CONFIGS ####
################
quest_trigger = 1 #1 if you want to automate completing board quest
delivery_trigger = 1 #1 if you want to automate completing delivery quest
farm = 1 #
petting_trigger = 1 #1 if you want to auto feed / receive pets
girls_trigger = 1 #1 if you want auto gift / receive from girls
merchant_trigger = 0 #1 if you want to auto buy all available item at merchant
endgame_check = 1 #1 if you already beat the last boss, 0 if not
safe_mode = 0 # it's automated since v1.5. No need to tamper. If you think your char really weak, then change it to 1.
n_sortie = 100 #number of sortie for auto farm. change as much as you like. default is 100.

if 'time_and_place' in globals():
    init_timer = 0
else:
    init_timer = 1

if init_timer:
    time_and_place = {'PP_quest': 0, 'PP_delivery': 0, 'PP_pet_gift': 0, 
                      'PP_pet_receive': 0, 'PP_girl1_gift': 0, 'PP_girl1_receive': 0,
                      'PP_girl2_gift': 0, 'PP_girl2_receive': 0, 'PP_merchant': 0,
                      
                      'SB_quest': 0, 'SB_delivery': 0, 'SB_pet_gift': 0,
                      'SB_pet_receive': 0, 'SB_merchant': 0,
                      
                      'GF_quest': 0, 'GF_delivery': 0, 'GF_pet_gift': 0, 
                      'GF_pet_receive': 0, 'GF_girl1_gift': 0, 'GF_girl1_receive': 0,
                      'GF_merchant': 0,
                      
                      'CD_quest': 0, 'CD_delivery': 0, 'CD_pet_gift': 0, 
                      'CD_pet_receive': 0, 'CD_girl1_gift': 0, 'CD_girl1_receive': 0,
                      'CD_girl2_gift': 0, 'CD_girl2_receive': 0, 'CD_merchant': 0,
                      
                      'VOG_quest': 0, 'VOG_delivery': 0, 'VOG_pet_gift': 0, 
                      'VOG_pet_receive': 0, 'VOG_girl1_gift': 0, 'VOG_girl1_receive': 0,
                      'VOG_merchant': 0,
                      
                      'FF_quest': 0, 'FF_delivery': 0, 'FF_merchant': 0, 'HQ_delivery': 0}
    
    place_list = list(time_and_place.keys())

#%%
#auto_farm(item_name)

#define where the main window is
print('Initializing...')
print('Cheking your screen whereabout...')
main_screen, main_x, main_y = main_screen_detection()
quest_test = ocr_prep('quest_mod')
print('Main screen found!')

print('Welcome to Postknight-auto v%s! Initializing auto...' %version)

#idle_mail
initialization()
#initial timer search
n_iter = 0

if init_timer:
    while True:    
        #for i in range(len(areas)):
        try:
            current_city = check_city()
            city = areas[n_iter]
            cityname = city_fullname[city]
            if current_city != city:
                move_to(city)
            
            #quest_module
            if quest_trigger == 1:
                if city != 'HQ':
                    print(r"Checking %s's board quest..." %cityname)
                    #HQ doesn't have quest board
                    quest_place, quest_amount, monster_id, quest_timer = quest_test.quest_module(city)
                    quest_place_list = determine_quest_place(quest_place, quest_amount, monster_id, stage_database)
                    print(quest_place_list)
                    for j in range(len(quest_place_list)):
                        auto_farm(quest_place_list[j])
                    if quest_place_list:
                        dummy1, dummy2, dummy3, quest_timer = quest_test.quest_module(city)
                    save_timer('quest', city, quest_timer)
                print(r"All's done! Let's move on..")
                time.sleep(3)
            
            #delivery module
            if delivery_trigger == 1:
                print(r"Checking %s's delivery quest..." %cityname)
                delivery_timer = delivery()
                save_timer('delivery', city, delivery_timer)
                print(r"All's done! Let's move on..")
            
            #pet_module
            if petting_trigger == 1:
                if city != 'HQ' and city != 'FF':
                    print(r"Playing with %s's pets..." %cityname)
                    pet_timer = pet_module()
                    time_type = ['pet_gift', 'pet_receive']
                    for i in range(2):
                        save_timer(time_type[i], city, pet_timer[i])
                    print('Finished playing with the good boi! Moving on...')
            
            #girls_module
            
            if girls_trigger == 1:
                if city != 'HQ' and city!= 'FF' and city != 'SB':
                    print(r"Date with the %s's gal/s..." %cityname)
                    girls_type = ['gift','receive','gift','receive']
                    girl_num = [1,1,2,2]
                    girls_timer = girls_module()
                    for i in range(len(girls_timer)):
                        save_timer('girl%s_%s' %(girl_num[i], girls_type[i]), city, girls_timer[i])
                    print('Date went well! Moving on...')
            
            #merchant_module
            if merchant_trigger == 1:
                if city != 'HQ':
                    print(r"Let's buy some item from the merchant!")
                    merchant_timer = merchant_module()
                    save_timer('merchant', city, merchant_timer)
                    print('We already bought everything that can be traded! Moving on...')
        
            n_iter += 1
        except TypeError:
            continue
        except IndexError:
            break
        
print('Initial timer check completed. Starting farming module...')

while True:
    #farm_module, break every 5 sortie to check timeout.
    try:
        if farm:
            counter = 1
            current_city = check_city()
            place = item_to_place(item_name)
            while main_screen:
                auto_farm(place)
                if counter > 2:
                    break
                counter += 1
        timed_out = []
        print('checking time out...')
        for place_dict, time_dict in time_and_place.items():
            time_now = time.time()
            if time_dict - time_now <= 0:
                timed_out.append(place_dict)
        timeout_module(timed_out)
        print('Finished! Back to farming...')
        
    except TypeError:
        continue
#%%
