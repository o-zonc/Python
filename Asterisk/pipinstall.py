import sys
import subprocess


def pip_install_windows(package):
    subprocess.run(['pip', 'install','--upgrade','pip'],shell=True)
    subprocess.run([sys.executable, "-m", "pip", "install", package], shell=True)


def pip_install_notwn(package):
    subprocess.run(['pip', 'install','--upgrade','pip'])
    subprocess.run(["sudo", sys.executable, "pip", "install", package])