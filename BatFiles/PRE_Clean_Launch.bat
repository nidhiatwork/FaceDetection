taskkill /F /IM "PremiereElementsEditor.exe"
taskkill /F /IM "Adobe QT32 Server.exe"
taskkill /F /IM "DynamicLinkManager.exe"
taskkill /F /IM "dwwin.exe"
taskkill /F /IM "Kill_PRE_Application.exe"
taskkill /F /IM "CrashReporterApp.exe"
taskkill /F /IM "Elements Auto Creations 2019.exe"


del /f "C:\Users\%username%\AppData\Roaming\Adobe\Premiere Elements\17.0\Adobe Premiere Elements Prefs"
rd /s /q "C:\Users\%username%\AppData\Roaming\Adobe\Common\Media Cache"
rd /s /q "C:\Users\%username%\AppData\Roaming\Adobe\Common\Media Cache Files"
rd /s /q "C:\Users\%username%\AppData\Roaming\Adobe\Premiere Elements\17.0\Layouts"

"C:\Program Files\Adobe\Adobe Premiere Elements 2019\PremiereElementsEditor.exe"

exit