# crsdoku - command-line sudoku 
---
Terminal User Interface (TUI) implementation of 9x9 Sudoku, written in Python using curses module.

This application was created as part of a coursework for the module SET08122.
# Ways of running the game
There are three ways of running crsdoku:
---
## 1. Running the pre-built executable (Recommended)
### Prerequisites
- Executable from [releases](https://github.com/lawclaw/sudoku-cw/releases/)
	- Note: Please download the executable corresponding to your platform
		- MacOS is untested but could potentially run the Linux executable
### How to run the application
1. Run the executable:
	- Windows: Run `.exe` file (make sure to unblock from Windows Defender) <br>
	- Linux: Give permissions and run it from preferred terminal <br>
	- MacOS (Untested): Same instructions as Linux

---
## 2. Running the application as a Python script 
### Prerequisites
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

---
## 3. Building application from scratch
 **Note: Building executables is architecture dependent, meaning if you build on Linux, the executable will only run on Linux. Same with  Windows.  MacOS is currently untested.**
### Building with PyInstaller
#### Prerequisites
- Python 3.10
- [PyInstaller](https://pyinstaller.org/en/stable/installation.html)
- **For Windows**: [windows-curses](https://pypi.org/project/windows-curses/)
#### How to build application
1. Clone branch:
	-  Linux & Windows -> main
	-  MacOS (untested) -> main
2. Build using PyInstaller
	- Linux: ```pyinstaller main.py -F -n crsdoku```
	- Windows: ```python -m PyInstaller main.py -F -n crsdoku -i icon.ico```
#### How to run built executable
1. Change directory to `dist`
2. Give suitable privileges to executale
3. Run executable  
		- Linux: `./main` <br>
		- Windows: Run `.exe` file