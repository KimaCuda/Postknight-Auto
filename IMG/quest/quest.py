# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 10:58:31 2019

@author: fddot
"""

#import ocr

areas = ['HQ', 'PP', 'SB', 'GF', 'CD', 'VOG', 'FF']
boards = ['board_HQ', 'board_PP','board_SB','board_GF','board_CD','board_VOG','board_FF']

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

def move_to():
    #use to travel
    return

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
    
    def read_quest(self):
        #use to read quest
        namesake = 'title_take'
        quest_list = []
        window = scanwindow()
        quest_list_pre = list(auto.locateAll(r'IMG\quest\name_box_detect.png', window, confidence = 0.8))
        for i in range(len(quest_list_pre)):
            auto.screenshot(r'IMG\temp\%s.png' %namesake, 
                            region = (main_x+quest_list_pre[i][0]+quest_list_pre[i][2], 
                            main_y+quest_list_pre[i][1]+quest_list_pre[i][3]-35,
                            200, 35))
            text_matrix = self.reader(namesake)
            
            text = ocr.image_to_string(text_matrix, config = '--oem 0')
            quest_list.append(text)
        return quest_list

    def quest_module(self, area_name):
        print('checking quest...')
        move_to(areas[i+1])
        click_buttons(boards[i+1])
        quest_list = self.read_quest()
        quest_place = []
        quest_amount = []
        for j in range(len(quest_list)):
            for k in range(len(quest_NMA)):
                try:
                    quest_NMA[k].index(quest_list[j])
                    quest_place.append(quest_NMA[k][1])
                    quest_amount.append(quest_NMA[k][2])
                except ValueError:
                    continue
        return quest_place, quest_amount
            
            
                    
                    

        