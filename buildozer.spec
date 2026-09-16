[app]
title = Packers Daily Entry
package.name = packersentry
package.domain = com.packerentry

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,txt
version = 1.0

# Use API 31 (Android 12) and NDK 23b for maximum compatibility
android.api = 31
android.minapi = 21
android.ndk = 23b
android.ndk_api = 21
android.archs = arm64-v8a
android.allow_backup = True
android.accept_sdk_license = True
android.permissions = INTERNET

# Add jnius to prevent the 'Py_REFCNT' error
requirements = python3,kivy,requests,urllib3,chardet,idna,certifi,jnius

orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1