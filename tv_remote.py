
class Television:
    
    MIN_VOLUME = 0
    MAX_VOLUME = 10
    MIN_CHANNEL = 0
    MAX_CHANNEL = 5
    
    
    
    def __init__(self):
        
        """
        The initialization function for the class.
        Sets status to False (off) and muted to False
        Sets the volume and channel to the minimum values.
        """
        
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
    
    
    def power(self):
        
        """
        Flips the value of Status to either True or False, turning the TV "off" and "on".
        """
        
        self.__status = not(self.__status)
    
    
    def mute(self):
        
        """
        Flips the value of Status to either True or False if the TV is on.
        """
        
        if self.__status:
            self.__muted = not(self.__muted)
    
    
    
    def channel_up(self):
        
        """
        If the tv is on, add 1 to self.__channel. If this goes over the maximum channel,
        scroll around to the minimum channel instead.
        """
        
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1
    
    
    def channel_down(self):
        
        """
        If the tv is on, subtract 1 from self.__channel. If this goes under the minimum channel,
        scroll around to the maximum channel instead.
        """
        
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1
    
    
    
    def volume_up(self):
        
        """
        If the tv is on and the volume is not already at max, increase the volume by 1.
        This also sets the value of muted to False. 
        """
        
        if self.__status:
            self.__muted = False
            if self.__volume != Television.MAX_VOLUME:
                self.__volume += 1
    
    
    def volume_down(self):
        
        """
        If the tv is on and the volume is not already at the minimum, decrease the volume by 1.
        This also sets the value of muted to False. 
        """
        
        if self.__status:
            self.__muted = False
            if self.__volume != Television.MIN_VOLUME:
                self.__volume -= 1
    
    
    
    def __str__(self):
        
        """
        Returns the TV status, including the variables status, channel, and volume.
        The volume is displayed as 0 if muted is True.
        
        :return: A string displaying the Power, Channel, and Volume.
        
        """
        
        if self.__muted:
            return f"TV status: Power = {self.__status}, Channel = {self.__channel}, Volume = 0"
        else:
            return f"TV status: Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
    
    
    
    
    
    
