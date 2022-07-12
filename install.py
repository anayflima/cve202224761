import sys
import subprocess


def installPackages(waitressVersion):
    # implement pip as a subprocess:
    if (False):
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'Flask'])
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'flask-cors'])
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'requests'])
    
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'waitress==' + waitressVersion])

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("Invalid number of arguments")
        exit(1)
    
    waitressVersion = '2.1.0'

    if (sys.argv[1] == '1'):
        waitressVersion = '2.1.1'
    
    print(waitressVersion)
    
    installPackages(waitressVersion)