# GUI

from tkinter import *
from tv_remote import Television


class GUI:
    
    def __init__(self, window) -> None:
        
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
        
        
        
        # Reporter (with shapes stored as variables so the colors can be changed for different channels)
        self.torso = self.screen.create_rectangle(140, 94, 160, 115, fill="black")  # Torso
        self.tie = self.screen.create_rectangle(148, 94, 152, 103, fill="black")       # Tie
        self.head = self.screen.create_oval(142, 79, 158, 95, fill="black")           # Head
        
        # Desk
        self.desk = self.screen.create_rectangle(100, 110, 200, 150, fill="black")
        self.deskText = self.screen.create_text(150, 130, text="NEWS", fill="black", font=('Helvetica 15 bold'))
        
        # News bar on the bottom of the screen
        self.newsBar = self.screen.create_rectangle(10, 160, 290, 180, fill="black")
        self.newsBarText = self.screen.create_text(150, 170, text="Nothing happened today, reports say...", fill="black", font=('Helvetica 7 bold'))
        
        
        
        
        
        # Volume display
        self.volDisplayBack = self.screen.create_line(20, 50, 20, 150, fill="black", width=5)
        self.volDisplay = self.screen.create_line(20, 150 - (self.tv.getVolume() * 10), 20, 150, fill="black", width=5)
        
        # Power light
        self.powerLight = self.screen.create_polygon(135, 202, 140, 193, 160, 193, 165, 202, fill="red4")
        
        # Channel Display
        self.chanDisplay = self.screen.create_text(150, 25, text="Channel 1: Generic News", fill="black", font=('Helvetica 9 bold'))
        
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
        
        
        
    
    
    
    def updateScreen(self) -> None:
        """
        Updates all of the display elements of the tv "screen".
        
        This includes:
         - Turning "on" the tv by recoloring all elements
         - Updating the volume display
         - Updating the current channel text at the top of the screen
         - Changing the content onscreen depending on the current channel
         - Turning "off" the tv by recoloring all elements to black
         - Updating the "power light" to green or red depending on tv.status
        
        """
                
        # If the TV is on
        if self.tv.getStatus():
            
            
            # Turn on light indicating the TV is on
            self.screen.itemconfig(self.powerLight, fill="dark green")
            
            # Reset Volume Display
            self.screen.itemconfig(self.volDisplayBack, fill="white")
            if self.tv.getMuted():
                self.screen.itemconfig(self.volDisplay, fill="grey")
            else:
                self.screen.itemconfig(self.volDisplay, fill="royal blue")
            self.screen.coords(self.volDisplay, [20, 150 - (self.tv.getVolume() * 10), 20, 150])
            
            # Reset Channel Display
            self.screen.itemconfig(self.chanDisplay, text=f"Channel {self.tv.getChannel()}: {self.tv.channels[self.tv.getChannel() - 1]}", fill="white")
            
            
            # Reset what the screen displays depending on the channel:
            
            self.screen.itemconfig(self.torso, fill="grey25")
            self.screen.itemconfig(self.head, fill="tan2")
            self.screen.itemconfig(self.desk, fill="RoyalBlue4")
            self.screen.itemconfig(self.deskText, text="NEWS", fill="white")
            self.screen.itemconfig(self.newsBar, fill="red")
            
            if self.tv.getChannel() == 1:
                self.screen.itemconfig(self.tie, fill="red")
                self.screen.itemconfig(self.newsBarText, fill="white", text="Nothing happened today, reports say...")
                
            elif self.tv.getChannel() == 2:
                self.screen.itemconfig(self.tie, fill="blue")
                self.screen.itemconfig(self.newsBarText, fill="white", text="Beloved reporter's dog died this mo...")
                
            elif self.tv.getChannel() == 3:
                self.screen.itemconfig(self.tie, fill="orange")
                self.screen.itemconfig(self.deskText, text="NEWS!")
                self.screen.itemconfig(self.newsBarText, fill="white", text="Colleges reported to be giving free...")
                
            elif self.tv.getChannel() == 4:
                self.screen.itemconfig(self.tie, fill="brown1")
                self.screen.itemconfig(self.deskText, text="NEWS?")
                self.screen.itemconfig(self.newsBarText, fill="white", text="Aliens landing in Nevada again...")
                
            else:
                self.screen.itemconfig(self.tie, fill="green")
                self.screen.itemconfig(self.deskText, text="PLANTS")
                self.screen.itemconfig(self.newsBarText, fill="white", text="Record-breaking tree wins Olympics...")
            
            
            
        # If the TV is off
        else:
                        
            # Turn off light indicating the TV is off
            self.screen.itemconfig(self.powerLight, fill="red4")
            
            # Recolor everything else to black so the screen is dark and thus "off"
            self.screen.itemconfig(self.volDisplayBack, fill="black")
            self.screen.itemconfig(self.volDisplay, fill="black")
            
            self.screen.itemconfig(self.chanDisplay, fill="black")
            
            self.screen.itemconfig(self.torso, fill="black")
            self.screen.itemconfig(self.tie, fill="black")
            self.screen.itemconfig(self.head, fill="black")
            self.screen.itemconfig(self.desk, fill="black")
            self.screen.itemconfig(self.deskText, fill="black")
            self.screen.itemconfig(self.newsBar, fill="black")
            self.screen.itemconfig(self.newsBarText, fill="black")
            
            
            
            
    
    
    # Remote Button Functions
    def power(self) -> None:
        """
        Calls the tv.power() and updateScreen() functions.
        """
        self.tv.power()
        self.updateScreen()
    
    def mute(self) -> None:
        """
        Calls the tv.mute() and updateScreen() functions.
        """
        self.tv.mute()
        self.updateScreen()
    
    def channelUp(self) -> None:
        """
        Calls the tv.channel_up() and updateScreen() functions.
        """
        self.tv.channel_up()
        self.updateScreen()
    
    def channelDown(self) -> None:
        """
        Calls the tv.channel_down() and updateScreen() functions.
        """
        self.tv.channel_down()
        self.updateScreen()
    
    def volumeUp(self) -> None:
        """
        Calls the tv.volume_up() and updateScreen() functions.
        """
        self.tv.volume_up()
        self.updateScreen()
        
    def volumeDown(self) -> None:
        """
        Calls the tv.volume_down() and updateScreen() functions.
        """
        self.tv.volume_down()
        self.updateScreen()
        
        
        
   
