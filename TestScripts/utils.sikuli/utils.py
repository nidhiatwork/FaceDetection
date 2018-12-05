from sikuli import *
import os, sys
import traceback
from TestScripts import Constants as Constants
reload(Constants)
import BaselineImages
reload(BaselineImages)

Settings.TypeDelay = 0.000004

if len(sys.argv)>3:
        Technology = sys.argv[2]
        Mode = sys.argv[3]
else:
        Technology = Constants.Tech
        Mode = Constants.M

def close_AA_PRE_And_Launch_AA_PRE():

        print "Technology is: " + Technology + " and Mode is: " + Mode
        setAutoWaitTimeout(60)
        
        print "\n~~~~~~~~Closing Auto creations~~~~~~~~"
        os.system("sh " + Constants.BatFilesFolder + "Mac_Kill_AA.sh")
        os.system("sh " + Constants.BatFilesFolder + "Mac_Kill_PRE.sh")
        os.system("killall 'Terminal'")
        os.system("open -a Terminal") 
        wait(2)
        type("N", Key.CMD)
        keyDown(Key.CMD + Key.SHIFT + Key.LEFT)
        wait(1)
        keyUp(Key.CMD + Key.SHIFT + Key.LEFT)
        type("~/Desktop/LaunchPRE.sh")
        type(Key.ENTER)
        launchAA()
        try:

                #setBundlePath(Constants.BaselineFolder)
                # find(Pattern("Button_GoalScreen_CloseGoalScreen.png").similar(0.80))
                wait(3)
        except:
                print("Unable to launch AA application after waiting for 60 seconds. End of execution.")
                closePRE()
                sys.exit(0)

        setAutoWaitTimeout(15)

def closePRE():
        print "~~~~~~~~Closing any open instance of PRE application~~~~~~~~"
        os.system("sh " + Constants.BatFilesFolder + "Mac_Kill_PRE.sh")
        wait(3)

def launchAA():
        print "~~~~~~~~~~Launching AA ~~~~~~~~~~~~~~"
        os.system("open -a Terminal") 
        type("N", Key.CMD)
        keyDown(Key.CMD + Key.SHIFT + Key.LEFT)
        keyUp(Key.CMD + Key.SHIFT + Key.LEFT)
        type("~/Desktop/LaunchAA.sh")
        type(Key.ENTER)
        wait(2)
def findElement( element ):       
        print "Finding element: " + str(element)
        try:
                
                find(element)
        except:
                stack = traceback.extract_stack(limit = 2)
                print "Unable to find element: " + Constants.BaselineFolder + str(element) + "\nBelow are exception details:\n" + str(sys.exc_info()[0]) + " -- line no. " + str(stack[0][1])
                assert False

def clickElement( element ):
        print "Clicking on element: " + str(element)
        try:
                
                click(element)
        except:
                stack = traceback.extract_stack(limit = 2)
                print "Unable to click element: " + Constants.BaselineFolder + str(element) + "\nBelow are exception details:\n" + str(sys.exc_info()[0]) + " -- line no. " + str(stack[0][1])
                assert False

def doubleClickElement( element ):
        print "Double clicking on element: " + str(element)
        try:                
                doubleClick(element)
        except:
                stack = traceback.extract_stack(limit = 2)
                print "Unable to double click element: " + Constants.BaselineFolder + str(element) + "\nBelow are exception details:\n" + str(sys.exc_info()[0]) + " -- line no. " + str(stack[0][1])
                assert False

def assertElementExists( element ):
        print "Asserting whether element exists: " + str(element)
        if not exists(element):
                stack = traceback.extract_stack(limit = 2)
                print "Unable to assert image exists: " + Constants.BaselineFolder + str(element) + "\nBelow are exception details:\n" + str(sys.exc_info()[0]) + " -- line no. " + str(stack[0][1])
                assert False

def hoverElement( element ):       
        print "Hovering on element: " + str(element)
        try:
                
                hover(element)
        except:
                stack = traceback.extract_stack(limit = 2)
                print "Unable to hover on element: " + Constants.BaselineFolder + str(element) + "\nBelow are exception details:\n" + str(sys.exc_info()[0]) + " -- line no. " + str(stack[0][1])
                assert False

def typeKeys( data ):
        print "Typing: " + str(data)
        try:

                type(data)
        except:
                stack = traceback.extract_stack(limit = 2)
                print "Unable to type: " + str(data) + "\nBelow are exception details:\n" + str(sys.exc_info()[0]) + " -- line no. " + str(stack[0][1])
                assert False


def dragAndDropElement( sourceImg, destImg ):       
        print "Dragging and dropping: " + str(sourceImg) + " to " + str(destImg)
        try:
                clickElement(sourceImg)
                mouseDown(Button.LEFT)
                mouseMove(4,4)
                wait(1)
                mouseMove(sourceImg)
                wait(1)
                mouseMove(destImg)
                wait(1)
                mouseUp()

        except:
                stack = traceback.extract_stack(limit = 2)
                print "Unable to drag and drop: " + Constants.BaselineFolder + str(sourceImg) + " to " + Constants.BaselineFolder + str(destImg) + "\nBelow are exception details:\n" + str(sys.exc_info()[0]) + " -- line no. " + str(stack[0][1])
                assert False
