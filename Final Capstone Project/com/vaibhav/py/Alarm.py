'''
Created on Sep 23, 2017

@author: vaisharm
'''
import time
import winsound


from __builtin__ import int
#Alarm Clock - A simple clock where it plays a sound after X number of minutes/seconds or at a particular time.


def start_clock():
    '''
    This function starts the timer for 10 seconds and triggers the sound once the time is completed
    '''
    time.sleep(10)
    trigger_alarm()
            
            

def trigger_alarm():
    '''
    This functions plays the Sound
    '''
    winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
    
    
start_clock()