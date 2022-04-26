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
- PyInstaller
- Python 3.10
### How to build application
```python
pyinstaller main.py -F
```
### How to run built executable
1. Navigate to `dist`
2. Give suitable privileges to main
3. Run main 
		- Linux: ``./main``
		- Run .exe file