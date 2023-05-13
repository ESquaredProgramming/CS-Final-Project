# tv_remote.py

class Television:
    
    MIN_VOLUME = 0
    MAX_VOLUME = 10
    MIN_CHANNEL = 1
    MAX_CHANNEL = 5
    
    
    
    def __init__(self) -> None:
        
        """
        The initialization function for the class.
        Sets status to False (off) and muted to False
        Sets the volume and channel to the minimum values.
        """
        
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
        self.channels = ["News", "Dreadful News", "Exciting News", "Fake News", "Plant Channel"]
    
    
    
    
    # Accessor Functions so the screen can use the tv's values
    def getVolume(self) -> int:
        """
        Accessor Function for the tv's volume.
        
        :return: self.__volume
        """
        return self.__volume
    
    def getChannel(self) -> int:
        """
        Accessor Function for the tv's current channel.
        
        :return: self.__channel
        """
        return self.__channel
    
    def getMuted(self) -> bool:
        """
        Accessor Function to see if the tv is muted or not.
        
        :return: self.__muted
        """
        return self.__muted
    
    def getStatus(self) -> bool:
        """
        Accessor Function for the tv's status (whether it is on or off).
        
        :return: self.__status
        """
        return self.__status
    
    
    
    
    
    
    
    def power(self) -> None:
        
        """
        Flips the value of Status to either True or False, turning the TV "off" and "on".
        """
        
        self.__status = not(self.__status)
    
    
    def mute(self) -> None:
        
        """
        Flips the value of Status to either True or False if the TV is on.
        """
        
        if self.__status:
            self.__muted = not(self.__muted)
    
    
    
    def channel_up(self) -> None:
        
        """
        If the tv is on, add 1 to self.__channel. If this goes over the maximum channel,
        scroll around to the minimum channel instead.
        """
        
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1
    
    
    def channel_down(self) -> None:
        
        """
        If the tv is on, subtract 1 from self.__channel. If this goes under the minimum channel,
        scroll around to the maximum channel instead.
        """
        
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1
    
    
    
    def volume_up(self) -> None:
        
        """
        If the tv is on and the volume is not already at max, increase the volume by 1.
        This also sets the value of muted to False. 
        """
        
        if self.__status:
            self.__muted = False
            if self.__volume != Television.MAX_VOLUME:
                self.__volume += 1
    
    
    def volume_down(self) -> None:
        
        """
        If the tv is on and the volume is not already at the minimum, decrease the volume by 1.
        This also sets the value of muted to False. 
        """
        
        if self.__status:
            self.__muted = False
            if self.__volume != Television.MIN_VOLUME:
                self.__volume -= 1
    
    
    
    def __str__(self) -> str:
        
        """
        Returns the TV status, including the variables status, channel, and volume.
        The volume is displayed as 0 if muted is True.
        
        I mainly am using this function for debugging purposes. 
        
        :return: A string displaying the Power, Channel, and Volume.
        
        """
        
        if self.__muted:
            return f"TV status: Power = {self.__status}, Channel = {self.__channel}, Volume = 0"
        else:
            return f"TV status: Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
    
    
    
    
    
    
