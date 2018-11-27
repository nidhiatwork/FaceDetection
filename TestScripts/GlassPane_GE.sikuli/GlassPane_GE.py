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
        print "Started..."
    def test_UI_GlassPane_GE(self):
        wait(1)
        os.chdir(Constants.CollectionFolder)
        click("AddMedia.png")
        setAutoWaitTimeout(60)
        files = list()
        i=1
        for filename in os.listdir(Constants.CollectionFolder):
            if filename.find(".")==0:
                continue
            now = datetime.datetime.now()
            postfix = str(now.day) + str(now.month) + str(now.year) + "_" + str(now.hour) + str(now.minute) + str(now.second)
            newfilename = "Image#" + str(i) + "_"+ postfix + filename[filename.find("."):]
            print "Filename changed from " + filename + " to " + newfilename
            shutil.copy(Constants.CollectionFolder+filename,Constants.CollectionFolder+newfilename)
            os.remove(Constants.CollectionFolder+filename)
            
            clickElement("AddMedia.png")
            clickElement("Filesandfolder.png")
        
            clickElement("Search.png")
            type(newfilename)
            type(Key.ENTER)
            clickElement("CoIlection.png")
            wait(2)
            doubleClickElement(Pattern("Image_Number.png").similar(0.85))
            if Constants.Technology=="Mona":
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
            clickElement("AddMedia.png")
            clickElement("Tools.png")
            clickElement("PanZoomTool.png")
            wait(5)
            findElement("Done.png")
            os.system("python " + Constants.BatFilesFolder + "TakeScreenshot.py '" + newfilename + "' " + Constants.Technology)
            clickElement("Done.png")
            wait(5)
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
