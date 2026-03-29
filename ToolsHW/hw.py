import webbrowser, sys, time, random, os  

RR_URL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
B1 = False  
def input_math():
    try:
        while True:
            user_input = input("1 times 1 = ? ")
            if user_input == 1: 
                ROLL()
                B1 = True
                break
            elif user_input == "exit":
                sys.exit()
            else:
                print("Wrong! Try again.")
                ROLL()
    except:
        pass 

def ROLL():
    webbrowser.open(RR_URL)
    os.system("echo 'Rickroll incoming...'")
    os.system("ls")