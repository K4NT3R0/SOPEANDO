import os, re
APP_ID = "ca-app-pub-6672720525194990~6251794481"

m = "android/app/src/main/AndroidManifest.xml"
s = open(m, encoding="utf-8").read()
if "APPLICATION_ID" not in s:
    meta = '    <meta-data android:name="com.google.android.gms.ads.APPLICATION_ID" android:value="%s"/>\n' % APP_ID
    s = s.replace("</application>", meta + "</application>", 1)
open(m, "w", encoding="utf-8").write(s)

g = "android/app/build.gradle"
s = open(g, encoding="utf-8").read()
s = re.sub(r"versionCode\s*=?\s*\d+", "versionCode " + os.environ.get("RUN_NUMBER", "1"), s, 1)
if os.environ.get("SIGN") == "1":
    sc = """signingConfigs {
        release {
            storeFile file(System.getenv("KEYSTORE_FILE") ?: "release.keystore")
            storePassword System.getenv("KEYSTORE_PASSWORD")
            keyAlias "upload"
            keyPassword System.getenv("KEYSTORE_PASSWORD")
        }
    }
    buildTypes {"""
    s = s.replace("buildTypes {", sc, 1)
    s = re.sub(r"(minifyEnabled\s*=?\s*false)", r"signingConfig signingConfigs.release\n            \1", s, 1)
open(g, "w", encoding="utf-8").write(s)
