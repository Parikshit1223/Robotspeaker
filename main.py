import os

if __name__ == '__main__':
    print("Welcome to RobotSpeaker 1.1 created by Parikshit Singh")
    while True :
        x = input("Enter what do you want me to speak :")
        if x == "q":
            break
        command = f"say {x}"
        os.system(command)