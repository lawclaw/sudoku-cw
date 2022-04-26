# crsdoku - command-line sudoku 
---
CLI implementation of 9x9 Sudoku, written in Python using curses module.

# Running pre-built application (Recommended)
## Prerequisites
-  Python 3.10, remember to set PATH if using Windows
## How to run application
Run the application in your console:
```python
python main.py
```
or 
```python
python3 main.py
```


# Building application
 **Note: Building executables is architecture dependent, meaning if you build on Linux, the executable will only run on Linux. Same with  Windows. **
## Building in Linux (PyInstaller)
## Prerequisites
- Python 3.10
- [PyInstaller](https://pyinstaller.org/en/stable/installation.html)
- [windows-curses](https://pypi.org/project/windows-curses/)
## How to build application
1. Clone correct branch:
	-  Linux/MacOS -> main
	-  Windows -> windows
2. Build using PyInstaller
	- Linux: ```pyinstaller main.py -F -n crsdoku```
	- Windows: ```python -m PyInstaller main.py -F -n crsdoku -i icon.ico```
## How to run built executable
1. Change directory to `dist`
2. Give suitable privileges to executale
3. Run executable  
		- Linux: `./main` <br>
		- Run .exe file