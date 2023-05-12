# GUI

from tkinter import *
from tv_remote import Television


class GUI:
    
    def __init__(self, window):
        
        """
        The initialization function for the GUI class.
        Sets up and packs the entire GUI, including:
         - Visual represenation of the "TV screen"
         - Volume + and - buttons
         - Channel + and - buttons
         - Mute button
         - Power button
        """
        
        self.tv = Television()
        self.window = window
        
        
        
        
        # Frame for TV Screen
        self.screenFrame = Frame(self.window)
        
        
        # Display the TV screen using a canvas
        self.screen = Canvas(self.screenFrame,width=300, height=200, bg="black")
        
        # Volume display
        self.volDisplayBack = self.screen.create_line(20, 65, 20, 165, fill="black", width=5)
        self.volDisplay = self.screen.create_line(20, 165 - (self.tv.getVolume() * 10), 20, 165, fill="black", width=5)
        
        # Power light
        self.powerLight = self.screen.create_polygon(135, 202, 140, 193, 160, 193, 165, 202, fill="red")
        
        # Channel Display
        self.chanDisplay = self.screen.create_text(40, 25, text="Channel 1", fill="black", font=('Helvetica 9 bold'))
        
        self.screen.pack()
        
        self.spacer = Label(self.screenFrame, text="   ", ).pack(pady=10)
        self.remoteLabel = Label(self.screenFrame, text="TV Remote").pack(pady=5)
        self.remoteBorderLabel = Label(self.screenFrame, text="-----------------------------------------------------------------------").pack()
        
        self.screenFrame.pack(pady=15)
        
        
        
        # Frame for Power and Mute buttons
        self.baseFrame = Frame(self.window)

        self.powerButton = Button(self.baseFrame, text='Power', command=self.power)
        self.muteButton = Button(self.baseFrame, text='Mute', command=self.mute)
        
        self.powerButton.pack(padx=10, side='left')
        self.muteButton.pack(padx=10, side='right')
        
        self.baseFrame.pack()
        
    
        
        # Frame for Channel buttons
        self.channelFrame = Frame(self.window)
        
        self.channelLabel = Label(self.channelFrame, text="Channel")
        self.channelPlusButton = Button(self.channelFrame, text='  +  ', command=self.channelUp)
        self.channelMinusButton = Button(self.channelFrame, text='  -  ', command=self.channelDown)
        
        self.channelLabel.pack(side='top')
        self.channelPlusButton.pack(pady=5, side='top')
        self.channelMinusButton.pack(pady=5, side='top')
        
        self.channelFrame.pack(padx=75, side='left')
        
        
        
        # Frame for Volume buttons
        self.volumeFrame = Frame(self.window)
        
        self.volumeLabel = Label(self.volumeFrame, text="Volume")
        self.volumePlusButton = Button(self.volumeFrame, text='  +  ', command=self.volumeUp)
        self.volumeMinusButton = Button(self.volumeFrame, text='  -  ', command=self.volumeDown)
        
        self.volumeLabel.pack(side='top')
        self.volumePlusButton.pack(pady=5, side='top')
        self.volumeMinusButton.pack(pady=5, side='top')
        
        self.volumeFrame.pack(padx=75, side='right')
        
    
    
    
    def updateScreen(self):
        
        # If the TV is on
        if self.tv.getStatus():
            
            # Turn on light indicating the TV is on
            self.screen.itemconfig(self.powerLight, fill="green")
            
            # Reset Volume Display
            self.screen.itemconfig(self.volDisplayBack, fill="white")
            if self.tv.getMuted():
                self.screen.itemconfig(self.volDisplay, fill="grey")
            else:
                self.screen.itemconfig(self.volDisplay, fill="blue")
            self.screen.coords(self.volDisplay, [20, 165 - (self.tv.getVolume() * 10), 20, 165])
            
            # Reset Channel Display
            self.screen.itemconfig(self.chanDisplay, text=f"Channel {self.tv.getChannel()}", fill="white")
            
            
        # If the TV is off
        else:
            
            # Turn off light indicating the TV is off
            self.screen.itemconfig(self.powerLight, fill="red")
            
            # Recolor everything else to black so the screen is dark and thus "off"
            self.screen.itemconfig(self.volDisplayBack, fill="black")
            self.screen.itemconfig(self.volDisplay, fill="black")
            self.screen.itemconfig(self.chanDisplay, fill="black")
            
    
    
    # Button Functions
    def power(self):
        self.tv.power()
        self.updateScreen()
    
    def mute(self):
        self.tv.mute()
        self.updateScreen()
    
    def channelUp(self):
        self.tv.channel_up()
        self.updateScreen()
    
    def channelDown(self):
        self.tv.channel_down()
        self.updateScreen()
    
    def volumeUp(self):
        self.tv.volume_up()
        self.updateScreen()
        
    def volumeDown(self):
        self.tv.volume_down()
        self.updateScreen()
        
        
