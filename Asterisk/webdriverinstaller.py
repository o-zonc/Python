import os
import chromedriver_autoinstaller
import platform
import subprocess


chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
driver_path = f'./{chrome_ver}/chromedriver.exe'


def requirementsinstall():
    # Download the required packages
    if platform.system() == "Windows":
        subprocess.check_call(["pip", "install", "-r", "requirements.txt"], shell=True)
    else:
        subprocess.check_call(['sudo', "pip", "install", "-r", "requirements.txt"])

def webdriverinstall():
    # Check if chrome driver is installed or not
    if os.path.exists(driver_path):
        print(f"chrome driver is insatlled: {driver_path}")
    else:
        print(f"install the chrome driver(ver: {chrome_ver})")
        chromedriver_autoinstaller.install(True)