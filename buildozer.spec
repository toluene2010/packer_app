[app]

# (str) Title of your application
title = Packers Daily Entry

# (str) Package name
package.name = packersentry

# (str) Package domain (needed for android/ios packaging)
package.domain = com.packerentry

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,json,txt

# (int) Android API to use
android.api = 31

# (int) Minimum API required
android.minapi = 21

# (str) Android archs to build for
android.archs = arm64-v8a

# (bool) Indicate whether the app should be backed up
android.allow_backup = True

# (bool) Accept the Android SDK license
android.accept_sdk_license = True

# (list) Permissions
android.permissions = INTERNET

# (list) Application requirements
# IMPORTANT: use pyjnius instead of jnius
requirements = python3,kivy,requests,urllib3,chardet,idna,certifi,pyjnius

# (str) Orientation of the app
orientation = portrait

# (bool) Fullscreen mode
fullscreen = 0

# (list) Supported orientations
# orientation = landscape

[buildozer]
# (int) Log level (0 = quiet, 1 = info, 2 = debug)
log_level = 2

# (int) Warn about root
warn_on_root = 1