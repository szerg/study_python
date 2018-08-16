#!/usr/bin/python
# coding=utf-8

from sound import music
import graphics # aici import un pachet 
#from graphics import *
import sys # aici import un modul si e ok

if __name__ == '__main__':
    song = music.all_songs[0]
    print "Playing",song
    image = graphics.splashscreen.logo # aici e o problema pentru ca vede graphics ca un modul, cand de fapt e un pachet
    # corect ar fi sa am import graphics.splashscreen
    print 'Showing image',image
    print sys.path # asta e o variabila din modulul ala
    
