import tkinter #tkinter module to develop gui 
import cv2 #pip install opencv-python
import PIL.Image, PIL.ImageTk
from matplotlib import image #pip install pillow
from functools import partial # this will partial our function to use in buttons 
import threading # thread method to call multiple functions in one function
import imutils # imutils to set the size of pic or vid to screen size 
import time  # using time.sleep module to give some seconds of gap between pictures

# took flag as global variable to blink descion pending text while checking the video 
flag=True

# using opencv module's videcapture method to get the video clip in our gui
stream=cv2.VideoCapture('virat.mp4')
def play(speed):
    """this function will run to play the video clip to take descion , so it will take a argument from the user 
    so those arguments will be passed inside the button so, so according to the speed of those next(slow and speed)
    previous(slow and speed)it will play the video clip"""
    
    # making flag variable as global to use it inside this function 
    global flag
    
    # play the video in reverse mode or forward mode according to the argument of play
    # using get method to get the clip as small small frames to watch slowly 
    frame1=stream.get(cv2.CAP_PROP_POS_FRAMES)
    
    # using set method to set the speed to play according to user input ,set method will take two parameter 
    # firstly frames and the speed of frames, where we are calculating video frame + argument of play function
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1+speed)
    
    # crating two variables to read the video frame which is inside the stream variable
    grabbed, frame=stream.read()
    frame=imutils.resize(frame, width=set_Width, height=set_height)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
    if flag:
        canvas.create_text(155, 26, fill="yellow", font="Times 25 bold", text="Descision is pending...")
    flag=not flag
        
    print(f"You clicked on play. and your speed is {speed}")

def pending(descios):
    """in this function we are calling both out and not_out function using threading method ,before that we are 
    displaying pending,sponsor and then we are calling both out and not_out function in order to display out 
    and not_out images,hence we are using 2 condition to call those functions"""
    # 1.display descion pending image
    frame=cv2.cvtColor(cv2.imread("pending.jpg"), cv2.COLOR_BGR2RGB)
    frame=imutils.resize(frame, width=set_Width, height=set_height)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
    
    # 2.wait for 2 second
    time.sleep(2)
    
    # 3.display sponsor image a
    wrame=cv2.cvtColor(cv2.imread("sponser.jpg"), cv2.COLOR_BGR2RGB)
    wrame=imutils.resize(wrame, width=set_Width, height=set_height)
    wrame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(wrame))
    canvas.image=wrame
    canvas.create_image(0,0, image=wrame, anchor=tkinter.NW)
    
    # 4.wait for 2 sec
    time.sleep(2)
    
    # 5.display out or notout
    # displaying out if third umpire clicks to out 
    # here we are calling out and not_out function according to the conditions using thread we are using multiple 
    # function inside pending function
    if descios =="out":
        grame=cv2.cvtColor(cv2.imread("itsout.jpg"), cv2.COLOR_BGR2RGB)
        grame=imutils.resize(grame, width=set_Width, height=set_height)
        grame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(grame))
        canvas.image=grame
        canvas.create_image(0,0, image=grame, anchor=tkinter.NW)
    # displaying not_out if third umpire clicks to not_out button
    elif descios =="not_out":
        grame=cv2.cvtColor(cv2.imread("itsnot_out.jpg"), cv2.COLOR_BGR2RGB)
        grame=imutils.resize(grame, width=set_Width, height=set_height)
        grame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(grame))
        canvas.image=grame
        canvas.create_image(0,0, image=grame, anchor=tkinter.NW)
    
    # 6.wait for 1.5 second
    time.sleep(1.5)
    
def out():
    """in this function we are using threading method to call multiple functions at a time in order to call both
    out and not_out functions according to users click, hence we are calling pending function here and passing 
    argument as out, so we can call this function inside the pending function"""
    thread=threading.Thread(target=pending,args=("out",))
    thread.daemon = 1
    thread.start()
    print("Player is out")

def not_out():
    """in this function we are using threading method to call multiple functions at a time in order to call both
    out and not_out functions according to users click, hence we are calling pending function here and passing 
    argument as not_out, so we can call this function inside the pending function"""
    thread=threading.Thread(target=pending,args=("not_out",))
    thread.daemon = 1
    thread.start()
    print("Player is not out")

# taking width of our main screen by creating variable set_width
set_Width=650
# taking  height of our main screen by creating variable set_height
set_height=368

# creating a window using tkinter module
window=tkinter.Tk()
# set title for main screen of our tkinter
window.title("Arvind karanje's third umpire decision review")
# setting welcome image to show 
cv_img=cv2.cvtColor(cv2.imread("welme.png"),cv2.COLOR_BGR2RGB)
# creating canvas to display the screen to procees, taking the variables set_width and set_height
canvas=tkinter.Canvas(window, width=set_Width, height=set_height)
# created the variable as photo & and reading it from the array format which is already assigned in cv_img var
photo=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
# assigned a variable to create image and display on the screen
image_on_canvas=canvas.create_image(0, 0, ancho=tkinter.NW, image=photo)
canvas.pack()

# creating buttons to take decsions using tkinter.button method where it will take 3 parameters 
# 2 button for play the previous seconds or to go back ,in two ways to satisfy with descion slow and fast
btn=tkinter.Button(window, text="<<Previous (fast)", width=40, command=partial(play,-25))
"""in the button we are assigning command as partial where we are calling a function play which will plat according
to the speed which we have set inside the buttons, so partial is the function from functools"""
btn.pack()
btn=tkinter.Button(window, text="<<Previous (slow)", width=40, command=partial(play, -2))
btn.pack()

# 2 buttons for playing the next moment of the video, next slow and next fast two ways to satisfaction to take decsions  
btn=tkinter.Button(window, text="Next>> (fast)", width=40, command=partial(play,25))
btn.pack()
btn=tkinter.Button(window, text="Next>> (slow)", width=40, command=partial(play,2))
btn.pack()

# 2 buttons to give either out or not out,by clicking them we can display the out or not out decsion 
btn=tkinter.Button(window, text="Give out", width=40, command=out)
btn.pack()
btn=tkinter.Button(window, text="Give not out", width=40, command=not_out)
btn.pack()

# calling the mainloop function to display the screen 
window.mainloop()