# bacchus-adapter

Project for converting bacchus exported PDF to a better one

## Setup

Install requirements
̨̨̨

```
pip3 install pyinstaller
pip3 install -r requirements.txt
```

## How to build executable file
`Pyinstaller s not a cross-compiler; to make a Windows app you run PyInstaller on Windows, and to make a Linux app you run it on Linux, etc.`

Run

```
pyinstaller --onefile --windowed adapter/main.py
```

Executable file is in `dist/`


### Note

On successful PR the Windows exe file build release will fail unless the version in `adapter/__init__.py` is bumped
