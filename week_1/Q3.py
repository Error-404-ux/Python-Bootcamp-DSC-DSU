#Name = Laksh kumar
#Q3
import time
def delay(lyrics):
    x = lyrics.split(",")
    length = len(x)
    for i in range(length):
        print(x[i])
        time.sleep(1)
    
    
    
lyrics="You were the shadow to my light,Did you feel us?,Another start,You fade away,Afraid our aim is out of sight,Wanna see us,Alive."#input("Enter lyrics of your fav song")
delay(lyrics)