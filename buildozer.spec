[app]
title = Packers Daily Entry
package.name = packersentry
package.domain = com.packerentry

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,txt
version = 1.0

# Use a specific Kivy version and add jnius for compatibility
requirements = python3,kivy==2.1.0,requests,urllib3,chardet,idna,certifi,jnius

orientation = portrait
fullscreen = 0

android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.archs = arm64-v8a
android.allow_backup = True
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
