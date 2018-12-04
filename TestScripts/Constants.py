import os, sys, platform
from sikuli import *

AppPath_PRE = "/Applications/Adobe Premiere Elements 2019/Support Files/Adobe Premiere Elements.app/Contents/MacOS/Adobe Premiere Elements"
AAPath = "/Applications/Adobe Elements 2019 Organizer.app/Contents/Elements Auto Creations 2019.app/Contents/MacOS/Elements Auto Creations 2019"
userdir = os.path.expanduser('~')

RootFolder = userdir + "/Desktop/FD_Automation"
BaselineFolder = RootFolder + "/BaselineImages/"
OutputFolder = RootFolder + "/Output/"
Sikuli_Path = userdir + "/Downloads"
FD_Test_Execution_Data = RootFolder + "/TestData/FD_Test_Execution_Data.xls"
ScreenshotsFolder = OutputFolder + "Screenshots"
BatFilesFolder = RootFolder + "/BatFiles/"
CollectionFolder = RootFolder + "/Collection/"
Technology = "Cognitive"
# Technology = "Mona"
# Mode = "Image"
Mode = "Video"