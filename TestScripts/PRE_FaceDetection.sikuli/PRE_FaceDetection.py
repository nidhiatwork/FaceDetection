import utils
reload(utils)
from utils import *
import os
import sys
import unittest
import shutil
import datetime

class TestGlassPane_GE(unittest.TestCase):

    def setUp(self):
        close_AA_PRE_And_Launch_AA_PRE()

    def test_UI_GlassPane_GE(self):
        wait(1)        
        os.chdir(Constants.CollectionFolder)
        setAutoWaitTimeout(60)
        i=1
        l = os.listdir(Constants.CollectionFolder)
        l.sort()
        for filename in l:
            if filename.find(".")==0:
                continue
            now = datetime.datetime.now()
            postfix = str(now.day) + str(now.month) + str(now.year) + "_" + str(now.hour) + str(now.minute) + str(now.second)
            if Constants.Mode == "Image":
                newfilename = "Image#" + str(i) + "_"+ postfix + filename[filename.find("."):]
            else:
                newfilename = "Video#" + str(i) + "_"+ postfix + filename[filename.find("."):]

            print "Filename changed from " + filename + " to " + newfilename
            shutil.copy(Constants.CollectionFolder+filename,Constants.CollectionFolder+newfilename)
            os.remove(Constants.CollectionFolder+filename)
            os.system("osascript -e 'tell application \"Adobe Premiere Elements\" to activate'")
            clickElement("AddMedia.png")
            clickElement("Filesandfolder.png")
            clickElement("Search.png")
            type(newfilename)
            type(Key.ENTER)
            clickElement("CoIlection.png")
            wait(2)
            if Constants.Mode=="Image":
                doubleClickElement(Pattern("Image_Number.png").similar(0.85))
            else:
                doubleClickElement(Pattern("Video.png").similar(0.85))
            wait(2)
            print("Launching AA again to ensure process is running")
            os.system("open -a Terminal")
            wait(2)
            type("N", Key.CMD)
            wait(2)
            keyDown(Key.CMD + Key.SHIFT + Key.LEFT)
            wait(1)
            keyUp(Key.CMD + Key.SHIFT + Key.LEFT)
            type(Key.ENTER)                 
            wait(3)
            os.system("osascript -e 'tell application \"Adobe Premiere Elements\" to activate'")
            clickElement("Tools.png")
            if Constants.Mode=="Image":
                clickElement("PanZoomTool.png")
                setAutoWaitTimeout(15)
                if exists("Done.png"):
                    print "Pan and zoom workflow complete."
                elif exists("AutoAnalyzerError.png"):
                    print "Auto AA error appeared on screen. Trying to handle..."
                    click(Pattern("OK.png").similar(0.75))
                    
                os.system("python " + Constants.BatFilesFolder + "TakeScreenshot.py '" + newfilename + "' " + Constants.Technology)
                findElement("Done.png")
                clickElement("Done.png")
                setAutoWaitTimeout(30)
            else:
                clickElement("SmartTrim.png")
                wait(1)
                clickElement("ShowPresets.png")
                wait(1)
                clickElement("People_Preset.png")
                wait(2)
                setAutoWaitTimeout(3600)
                findElement(Pattern("Playbar.png").similar(0.79))
                os.system("python " + Constants.BatFilesFolder + "TakeScreenshot.py '" + newfilename + "' " + Constants.Technology)
                click(Pattern("CloseWindow.png").similar(0.78))
                findElement("No_button.png")
                clickElement("No_button.png")
                
                setAutoWaitTimeout(60)

            wait(3)
            type("N", Key.CMD)
            findElement("No_button.png")
            clickElement("No_button.png")
            wait(3)
            findElement("Cancel_button.png")
            clickElement("Cancel_button.png")
            print "Completed screenshot taking process for file: " + newfilename
            i = i+1
            if Constants.Technology=="Mona":
                os.system("killall 'Elements Auto Creations 2019'")
                wait(2)
    def tearDown(self):
       closePRE()