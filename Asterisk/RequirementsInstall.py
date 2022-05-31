import platform
import subprocess


def requirementsinstall():
    # Download the required packages
    if platform.system() == "Windows":
        subprocess.check_call(["pip", "install", "-r", "requirements.txt"], shell=True)
    else:
        subprocess.check_call(['sudo', "pip", "install", "-r", "requirements.txt"])