[app]

# (str) Title of your application
title = MyKivyApp

# (str) Package name
package.name = mykivyapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.mykivyapp

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,jpeg,kv,atlas,json,ttf

# (list) Source files to exclude (let empty to not exclude anything)
source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
source.exclude_dirs = .git,__pycache__,build,dist

# (list) List of exclusions using pattern matching
#source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
version = 0.1

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements
requirements = python3,kivy==2.3.0,jnius==1.4.0

# (str) Custom source folders for requirements
#p4a.source_dir = /path/to/python-for-android

# (str) The directory in which python-for-android should look for your own build recipes
#p4a.local_recipes = /path/to/recipes

# (str) Filename to specify the p4a bootstrap
#p4a.bootstrap = sdl2

# (list) Permissions
android.permissions = INTERNET

# (list) features (adds uses-feature -tags to manifest)
#android.features = android.hardware.usb.host

# (int) Target Android API, should be as high as possible.
android.api = 34

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 34

# (str) Android NDK version to use
android.ndk = 25b

# (int) Android NDK API to use. This is the minimum API your app will support, it should usually match android.minapi.
android.ndk_api = 21

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
#android.ndk_path =

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
#android.sdk_path =

# (str) ANT directory (if empty, it will be automatically downloaded.)
#android.ant_path =

# (bool) If True, then skip trying to update the Android SDK
#android.skip_update = False

# (bool) If True, then automatically accept SDK license agreements
android.accept_sdk_license = True

# (str) Android entry point, default is ok for Kivy-based app
#android.entrypoint = org.kivy.android.PythonActivity

# (str) Full screen mode
#android.fullscreen = True

# (str) Android app theme, default is ok for Kivy-based app
#android.apptheme = "@android:style/Theme.NoTitleBar"

# (list) Pattern to whitelist for the Android application
#android.whitelist =

# (str) Path to a custom whitelist file
#android.whitelist_src =

# (str) Path to a custom blacklist file
#android.blacklist_src =

# (bool) Use aapt2 (included in build-tools)
#android.aapt2 = False

# (list) Android application meta-data to set (key=value format)
#android.meta_data =

# (list) Android library project to add (will be added in the
# project.properties automatically.)
#android.library_references =

# (str) Android logcat filters to use
#android.logcat_filters = *:S python:D

# (bool) Copy library instead of making a libpymodules.so
#android.copy_libs = 1

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a, armeabi-v7a

# (int) overrides automatic versionCode computation (used in build.gradle)
#android.numeric_version = 1

# (bool) enables Android auto backup feature (Android API >=23)
#android.allow_backup = True

# (str) XML file to include as an intent filters in <activity> tag
#android.manifest.intent_filters =

# (str) launchMode to set for the main activity
#android.manifest.launch_mode = standard

# (list) Android additional libraries to copy into libs/armeabi
#android.add_libs_armeabi = libs/android/*.so
#android.add_libs_armeabi_v7a = libs/android-v7/*.so
#android.add_libs_arm64_v8a = libs/android-v8/*.so
#android.add_libs_x86 = libs/android-x86/*.so
#android.add_libs_x86_64 = libs/android-x86_64/*.so

# (str) The format used to package the app for release mode (aab or apk or aar).
#android.release_artifact = aab

# (str) Gradle dependencies to add (global)
#android.gradle_dependencies = com.android.support:support-v4:28.0.0

# (str) Gradle repositories to add (global)
#android.gradle_repositories =

# (str) Additional gradle dependencies for the app
#android.add_gradle_dependencies =

# (str) Additional gradle repositories for the app
#android.add_gradle_repositories =

# (bool) Skip byte compile for .py files (default is False)
#android.no-byte-compile-python = False

# (str) The Android app's version name (default is from version.regex)
#android.version_name =

# (str) XML file to include as a splash screen for the app
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) XML file to include as an icon for the app
#icon.filename = %(source.dir)s/data/icon.png

# (list) Include additional data files/directories in the APK
#android.add_src =

# (list) List of Java .jar files to add to the libs so that pyjnius can access
#android.add_jars =

# (list) List of Java files to add to the android project (can be java or a
#android.add_java_src =

# (list) List of Android assets to add to the APK
#android.add_assets =

# (str) Android app's orientation (default is portrait)
#orientation = portrait

# (str) The app's fullscreen mode (default is False)
#fullscreen = 0

# (str) The app's background color (default is white)
#background_color = 0x000000

# (str) The app's icon (default is the Kivy icon)
#icon = %(source.dir)s/data/icon.png

# (str) The app's presplash (default is the Kivy logo)
#presplash = %(source.dir)s/data/presplash.png

# (str) The app's title (default is the app's title)
#title = My Kivy App

# (str) The app's version (default is the app's version)
#version = 0.1

# (str) The app's package name (default is the app's package name)
#package.name = myapp

# (str) The app's package domain (default is the app's package domain)
#package.domain = org.test

# (str) The app's source directory (default is the current directory)
#source.dir = .

# (list) The app's source files to include (default is py,png,jpg,kv,atlas)
#source.include_exts = py,png,jpg,kv,atlas

# (list) The app's source files to exclude (default is spec)
#source.exclude_exts = spec

# (list) The app's source directories to exclude (default is .git,__pycache__)
#source.exclude_dirs = .git,__pycache__

# (list) The app's source patterns to exclude (default is empty)
#source.exclude_patterns = license,images/*/*.jpg

# (str) The app's requirements (default is python3,kivy)
#requirements = python3,kivy

# (str) The app's custom source folders for requirements (default is empty)
#p4a.source_dir = /path/to/python-for-android

# (str) The app's custom build recipes directory (default is empty)
#p4a.local_recipes = /path/to/recipes

# (str) The app's p4a bootstrap (default is sdl2)
#p4a.bootstrap = sdl2

# (str) The app's Android permissions (default is empty)
#android.permissions = INTERNET

# (str) The app's Android features (default is empty)
#android.features = android.hardware.usb.host

# (int) The app's target Android API (default is 31)
#android.api = 31

# (int) The app's minimum Android API (default is 21)
#android.minapi = 21

# (int) The app's Android SDK version (default is 31)
#android.sdk = 31

# (str) The app's Android NDK version (default is 23b)
#android.ndk = 23b

# (int) The app's Android NDK API (default is 21)
#android.ndk_api = 21

# (bool) The app's private storage (default is True)
#android.private_storage = True

# (str) The app's Android NDK directory (default is empty)
#android.ndk_path =

# (str) The app's Android SDK directory (default is empty)
#android.sdk_path =

# (str) The app's ANT directory (default is empty)
#android.ant_path =

# (bool) The app's skip update (default is False)
#android.skip_update = False

# (bool) The app's accept SDK license (default is False)
#android.accept_sdk_license = False

# (str) The app's Android entry point (default is org.kivy.android.PythonActivity)
#android.entrypoint = org.kivy.android.PythonActivity

# (str) The app's fullscreen mode (default is True)
#android.fullscreen = True

# (str) The app's Android app theme (default is "@android:style/Theme.NoTitleBar")
#android.apptheme = "@android:style/Theme.NoTitleBar"

# (list) The app's whitelist (default is empty)
#android.whitelist =

# (str) The app's whitelist source file (default is empty)
#android.whitelist_src =

# (str) The app's blacklist source file (default is empty)
#android.blacklist_src =

# (bool) The app's use aapt2 (default is False)
#android.aapt2 = False

# (list) The app's Android meta-data (default is empty)
#android.meta_data =

# (list) The app's Android library references (default is empty)
#android.library_references =

# (str) The app's Android logcat filters (default is *:S python:D)
#android.logcat_filters = *:S python:D

# (bool) The app's copy library (default is 1)
#android.copy_libs = 1

# (str) The app's Android architectures (default is arm64-v8a, armeabi-v7a)
#android.archs = arm64-v8a, armeabi-v7a

# (int) The app's Android numeric version (default is 1)
#android.numeric_version = 1

# (bool) The app's allow backup (default is True)
#android.allow_backup = True

# (str) The app's Android manifest intent filters (default is empty)
#android.manifest.intent_filters =

# (str) The app's Android manifest launch mode (default is standard)
#android.manifest.launch_mode = standard

# (list) The app's Android additional libraries (default is empty)
#android.add_libs_armeabi = libs/android/*.so
#android.add_libs_armeabi_v7a = libs/android-v7/*.so
#android.add_libs_arm64_v8a = libs/android-v8/*.so
#android.add_libs_x86 = libs/android-x86/*.so
#android.add_libs_x86_64 = libs/android-x86_64/*.so

# (str) The app's Android release artifact (default is aab)
#android.release_artifact = aab

# (str) The app's Android gradle dependencies (default is empty)
#android.gradle_dependencies = com.android.support:support-v4:28.0.0

# (str) The app's Android gradle repositories (default is empty)
#android.gradle_repositories =

# (str) The app's Android add gradle dependencies (default is empty)
#android.add_gradle_dependencies =

# (str) The app's Android add gradle repositories (default is empty)
#android.add_gradle_repositories =

# (bool) The app's Android no byte compile python (default is False)
#android.no-byte-compile-python = False

# (str) The app's Android version name (default is empty)
#android.version_name =

# (str) The app's presplash filename (default is empty)
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) The app's icon filename (default is empty)
#icon.filename = %(source.dir)s/data/icon.png

# (list) The app's Android add src (default is empty)
#android.add_src =

# (list) The app's Android add jars (default is empty)
#android.add_jars =

# (list) The app's Android add java src (default is empty)
#android.add_java_src =

# (list) The app's Android add assets (default is empty)
#android.add_assets =

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
#build_dir = ./.buildozer

# (str) Path to build output (i.e. .apk, .aab) storage
#bin_dir = ./bin

# (str) Path to the buildozer.spec file
#spec_dir = .

# (str) Path to the global directory for Python packages installed by pip
#p4a.pip_dir = ./pip

# (bool) Make buildozer output more verbose
#debug = False

# (bool) Output additional debug information for the Android target
#android.debug = False