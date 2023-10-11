# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 14:15:14 2023

@author: Fabrizio
"""
import numpy as np
import matplotlib.pyplot as plt 
import os
import time

images = ["altri/giovedi28.jpg",
          "altri/stanchissimo.jpg",
          "baseline/sabato7.jpg",
          "stai_bene/sadhana_pattini_prelievo.jpg", 
          "altri/pingpong.jpg",
          "stai_bene/dom.jpg",
          "altri/scratching.jpg",
          "altri/spaccata.jpg",
          "altri/dopo_mila_4_ore.jpg",
          "altri/10ott_sveglio.jpg",  
          "altri/10ott_sadhana.jpg",
          "altri/10ott_pulizia.jpg",
          "altri/10ott_mela_scr.jpg",
          "altri/10ott_spaccata.jpg",
          "altri/10ott_spacc_vert.jpg",
          "altri/neti_nasya.jpg",
          "altri/mela_backbend.jpg",
          "altri/mass_il.jpg",
          "altri/chess.jpg",
          "altri/dopolu.jpg",
          "altri/scratch.jpg",
          "altri/mela.jpg",
          "altri/chess2.jpg",
          "altri/mela2.jpg",
          "altri/discusmampap.jpg",
          "altri/claire3.jpg",
          "altri/2022_nov.jpg",
          ]

def picture_to_arr(image):
    arr = plt.imread(image)
    arr_list=arr.tolist()
    r=g=b=0
    for row in arr_list:
        for item in row:
            r=r+item[0]
            g=g+item[1]
            b=b+item[2]  
    total=r+g+b
    red=r/total*100
    green=g/total*100
    blue=b/total*100
    return red, green, blue

for i, img in enumerate(images):
    image = plt.imread(img)
    path = img
    ti_c = os.path.getctime(path)
    c_ti = time.ctime(ti_c)
    plt.imshow(image)
    plt.show()
    r, g, b = picture_to_arr(img[:-4]+"_sample.jpg")
    print(i+1)
    print(img[6:])
    print(c_ti)
    print("redness:", int(100*(1-((g+b)/2)/r)), "percent")
    

