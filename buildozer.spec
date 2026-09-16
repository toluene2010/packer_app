[app]
title = Packers Daily Entry
package.name = packersentry
package.domain = com.packerentry

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,txt
version = 1.0

android.api = 31
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.archs = arm64-v8a
android.allow_backup = True
android.accept_sdk_license = True
android.permissions = INTERNET

requirements = python3,kivy,requests,urllib3,chardet,idna,certifi,jnius

orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1