[app]
title = 4-7-8 Breathing
package.name = breathing478
package.domain = com.breathing
version = 1.0.0
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
requirements = python3,kivy==2.3.0
orientation = portrait
fullscreen = 0

# تنظیمات به‌روز اندروید
android.api = 33
android.minapi = 21
# حذف android.sdk (منسوخ شده)
android.ndk = 25b 
# NDK نسخه ۲۵ - پایدارترین نسخه
android.ndk_api = 21
android.archs = arm64-v8a,armeabi-v7a  # استفاده از archs جدید
android.permissions = INTERNET
android.accept_sdk_license = true
android.wakelock = True

# تنظیمات پیشرفته برای حل مشکلات
p4a.branch = develop
android.private_storage = True
android.enable_androidx = True
