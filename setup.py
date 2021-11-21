import os
import time
os.system("apt-get install pip")
print("pip installation complete")
time.sleep(1)
os.system("pip install -r requirements.txt")
os.system("pip install instaloader")
print("package installations completed")
os.system("apt-get install xterm")
time.sleep(2)
