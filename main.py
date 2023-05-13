# main.py

from gui import *


def main():
    '''
    Initializes the GUI window, sets the dimensions,
    and runs the window's mainloop.
    '''
    window = Tk()
    window.title('TV Remote')
    window.geometry('400x500')
    window.resizable(False, False)
    
    GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()
