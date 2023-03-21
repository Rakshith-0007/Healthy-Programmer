import pygame
import time
import datetime
import threading

##Assuming that the program is starting at 9:00 AM and ends at 5:00 PM

def water():
    water_drank_history=0
    while True:
            time.sleep(1)
            print("Its time to have 0.4375 lts of water to stay hydrated!")
            pygame.mixer.init()
            pygame.mixer.music.load("D:\Rakshith gowda\water_drinking.mp3")
            pygame.mixer.music.play()
            b=int(input("Enter a code\n1.Drank 0.4375 lts of water\n2.Remind me after 5 min\n3.Show water dranked history\n"))
            if b==1:
                file=open("Healthy_prgrammer_water.txt", "a")
                current_Time=datetime.datetime.now()
                current_Time=str(current_Time)
                file.write("Drank water on "+current_Time+"\n")
                pygame.mixer.music.stop()
                water_drank_history=water_drank_history+0.4375

            if water_drank_history == 3.5:
                print("Today you have dranked 3.5 lts of water")
                break

            elif b==3:
                print(f"Today you had {water_drank_history} lts of water :)")

            elif b==2:
                print("Reminder set for 5 minutes")
                pygame.mixer.music.stop()
                time.sleep(0.1)
def  eye_excersise():
    eye_excersise_history=0
    while True:
        time.sleep(10)
        pygame.mixer.init()
        pygame.mixer.music.load("D:\Rakshith gowda\Eye_Excersise.mp3")
        pygame.mixer.music.play()
        b=int(input("Enter a code\n1.Eydone\n2.Remind me after 5 min\n3.See eye excersise history\n"))
        if b==1:
                eye_excersise_history=eye_excersise_history+1
                pygame.mixer.music.stop()
                file=open("Healthy_prgrammer_eye_excersise.txt", "a")
                current_time=str(datetime.datetime.now())
                file.write("Done Eye Excesise at "+current_time+"\n")
        if eye_excersise_history==16:
                print("Today you have done eye excersise for 16 times and todays task is completed")
                break
        elif b==2:
                pygame.mixer.music.stop()
                print("Reminder set for 5 minutes")
                time.sleep(0.2)
        elif b==3:
                print(f"Today done eye excersise for {eye_excersise_history} times")


def physical_activity():
    excersise_done_time=0
    while True:
        time.sleep(15)
        pygame.mixer.init()
        pygame.mixer.music.load("D:\Rakshith gowda\Pysical_activity.mp3")
        pygame.mixer.music.play()
        b=int(input("Enter the code\n1.Ex Done\n2.Remind me after 5 min\n3.Check todays activity\n"))
        if b==1:
            file=open("Healthy_prgrammer_physicalActivity.txt", "a")
            current_time=str(datetime.datetime.now())
            file.write("Physical activity done at "+current_time+"\n")
            excersise_done_time+=1
        if excersise_done_time==10:
            print("Today you have completed your physical activity task :)")
            break
        elif b==2:
            print("Reminder set for 5 minutes!")
            time.sleep(0.2)
        elif b==3:
            print(f"Today you have done excersise for {excersise_done_time} times")


threading.Thread(target=water).start()
threading.Thread(target=eye_excersise).start()
threading.Thread(target=physical_activity).start()






