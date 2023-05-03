# GUI

from tkinter import *
from tv_remote import *


class GUI:
    
    def __init__(self, window):
        
        tv = Television
        self.window = window
    
    
    
    # Button Functions
    def power(self):
        tv.power()
    
    
    
    def channelUp(self):
        tv.channel_up()
    
    def channelDown(self):
        tv.channel_down()
    
    
    
    def volumeUp(self):
        tv.volume_up()
    
    def volumeDown(self):
        tv.volume_down()
        
    def mute(self):
        tv.mute()