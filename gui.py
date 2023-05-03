# GUI

from tkinter import *
from tv_remote import *


class GUI:
    
    def __init__(self, window):
        
        tv = Television
        self.window = window
        
        # Frame for Channel buttons
        self.channelFrame = Frame(self.window)
        
        self.channelLabel = Label(self.channelFrame, text="Channel")
        self.channelPlusButton = Button(self.channelFrame, text='+', command=self.channelUp)
        self.channelMinusButton = Button(self.channelFrame, text='-', command=self.channelDown)
        
        self.channelLabel.pack(side='top')
        self.channelPlusButton.pack(pady=5, side='top')
        self.channelMinusButton.pack(pady=5, side='top')
        
        self.channelFrame.pack(anchor='w', padx=25, pady=50)
        
        
        
        # Frame for Volume buttons
        self.volumeFrame = Frame(self.window)
        
        self.volumeLabel = Label(self.volumeFrame, text="Volume")
        self.volumePlusButton = Button(self.volumeFrame, text='+', command=self.volumeUp)
        self.volumeMinusButton = Button(self.volumeFrame, text='-', command=self.volumeDown)
        
        self.volumeLabel.pack(side='top')
        self.volumePlusButton.pack(pady=5, side='top')
        self.volumeMinusButton.pack(pady=5, side='top')
        
        self.volumeFrame.pack(anchor='w', padx=25, pady=30)
        
        
        
        # Frame for Power and Mute buttons
        self.baseFrame = Frame(self.window)
        
        self.powerButton = Button(self.baseFrame, text='Power', command=self.power)
        self.muteButton = Button(self.baseFrame, text='Mute', command=self.mute)
        
        self.powerButton.pack(side='left')
        self.muteButton.pack(padx=20, side='left')
        
        self.baseFrame.pack(pady=15)
        
        
    
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
