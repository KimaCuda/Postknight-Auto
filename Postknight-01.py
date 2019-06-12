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

os.chdir('E:\Project\Postknight')

auto.FAILSAFE = True
ocr.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#%%
#OCR SPACE


            

    
    
    

# %%
# DATABASES


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

announcement = ['announcement_endgame', 'announcement_endgame_close_button']
global_buttons = ['areas_button', 'routes_button', 'go_button', 'go_button2']
battle_buttons = ['battle_1', 'battle_2', 'battle_3','battle_finish']
areas_buttons = ['areas_HQ', 'areas_PP','areas_SB','areas_GF','areas_CD','areas_VOG','areas_FF']
boards = ['board_HQ', 'board_PP','board_SB','board_GF','board_CD','board_VOG','board_FF']
areas = ['HQ', 'PP', 'SB', 'GF', 'CD', 'VOG', 'FF']
window_list = ['window_routeselect','window_achievement','window_inventory','window_shop','window_skills','window_stats']

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
    location = auto.locate(r'IMG\%s.png' %button, window, confidence = 0.6)
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
        quit()
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
                areas_name = boards[i][6:]
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
            break
    return areas_name


# %%

def first_time():
    #announcement endgame
    click_buttons('go_button')
    time.sleep(2)
    click_buttons('close_button')
    time.sleep(2)
    return    
    
# %%
        
def auto_farm(item_name):
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
        first_time()
        
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
    
    first_time()    
    for i in range(10000):
        # farming
        print('Sortie #' + str(i+1))
        click_buttons('go_button')
        time.sleep(2)
        try:
            click_buttons(place)
        except TypeError:
            auto.moveTo(x = main_x+240, y = main_y+430, duration = 0.5)
            auto.dragRel(0, -300, duration = 0.30, pause = 3)
            click_buttons(place)
        time.sleep(3)
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
                    if traveler != None:
                        print('traveler found! skipping...')
                        close_button = auto.locate(r'IMG\announcement_endgame_close_button.png', midroll_window, confidence = 0.6)
                        auto.click(main_x+auto.center(close_button)[0], main_y+auto.center(close_button)[1], duration = 0.5)
                        a = scanwindow()
                        midroll_go2 = auto.locate(r'IMG\go_button.png', a, confidence = 0.6)
                        auto.click(main_x+auto.center(midroll_go2)[0], main_y+auto.center(midroll_go2)[1], duration = 0.5)
                        timeout = time.time() + 7
                    if midroll_go1 != None:
                        print('The harem girls found! receiving love...')
                        auto.click(main_x+auto.center(midroll_go1)[0], main_y+auto.center(midroll_go1)[1], duration = 0.5)
                        timeout = time.time() + 7
                    if finish != None:
                        auto.click(main_x+auto.center(finish)[0], main_y+auto.center(finish)[1], duration = 0.5)
                        print('sortie finished!')
                        timeout = time.time() + 7
                        time.sleep(8)
                        while True:
                            check = scanwindow()
                            a = auto.locate(r'IMG\go_button.png', check, confidence = 0.6)
                            if a == None:
                                print('not ready for next sortie. waiting...')
                                auto.click(main_x+70, main_y+130)
                                time.sleep(1)
                                continue
                            if a != None:
                                print(r"all's ready! let's go for the next one!")
                                timeout = time.time() + 7
                                break
                        break
            except IndexError:
                print('error?')
                break
    print('sortie finished')
    return

# need to check whether endgame announcement out or not when pressing go_button
# need to do better job at identifying city (can try to swipe)
# need to handle if dead in sortie (and also if HP isn't enough for sortie)


# %%
# PARAMETERS
item_name = "moonbud"
sword_skill = 'b1_blitz'
shield_skill = 'b2_elusive_cover'
pot_type = 'b3_2'
safe_mode = 0

#%%
#auto_farm(item_name)

#define where the main window is
main_screen, main_x, main_y = main_screen_detection()

a = check_city()

while main_screen:
    auto_farm(item_name)
    

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
