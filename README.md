# Dos-atack 💣
Good day dear user 👋, I am glad that you decided to install this tool. Dos-Atack script will help you to stress-test your sites. Let's get started, how do you install a script?
## Termux
Write the following commands into the console one by one:
```
apt update && apt upgrade -y
pkg install git
pkg install python3
git clone https://github.com/AXL033/dos-atack.git
cd dos-atack
python -m pip install --upgrade pip
pip install -r requirements.txt
python3 dos.py
```
## Windows
In order to install the script on Windows, you need Python3, you can download it from [official website](https://www.python.org/downloads/) 🐍.
After installing Python3, you should preferably update PIP, you do this with a command:
```
python -m pip install --upgrade pip
```
Next, download the requirements.txt file, and the dos.py file. Then run the command:
```
pip install -r ./requirements.txt
```
It is important to remember that you are in the same directory as the files ❗
Finally, run the script with a command:
```
python ./dos.py
```
