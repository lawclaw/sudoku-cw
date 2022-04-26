# sudoku-cw
Coursework for ADS module

## Running (Recommended)
### Prerequisites
-  Python 3.10, remember to set PATH if using Windows
### How to run application
Run the application in your console:
```python
python main.py
```
or 
```python
python3 main.py
```


## Building application
 **Note: Building executables is architecture dependent, meaning if you build on Linux, the executable will only run on Linux. Same with  Windows. **
### Building in Linux (PyInstaller)
### Prerequisites
- Python 3.10
- [PyInstaller](https://pyinstaller.org/en/stable/installation.html)
- [windows-curses](https://pypi.org/project/windows-curses/)
### How to build application
Linux
```shell
pyinstaller main.py -F
```
Windows
```shell
python -m PyInstaller --icon=icon.ico -F
```
### How to run built executable
1. Change directory to `dist`
2. Give suitable privileges to executale
3. Run executable 
		- Linux: ``./main``
		- Run .exe file