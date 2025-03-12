import time
def greeting(hour,time1):
    if(hour>=0 and hour<12):
        print("Good morning, it's ",time1,"AM")
    elif(hour==12):
        print("It's 12 Noon")
    elif(hour>12 and hour<=17):
        print("Good afternoon, Its ",time1,"PM")
    elif (hour>17 and hour<=19):
        print("Good Evening Its ",time1,"PM")
    else:
        print("Good night Its ",time1,"PM")

def main():
    time1=time.strftime("%H:%M")
    hour=int(time.strftime("%H"))
    """For Custom Input"""
    # hour=input("Enter Hour :")
    # time1=input("Enter minutes :")
    # time1=hour+":"+time1

    greeting(int(hour),time1)

main()


