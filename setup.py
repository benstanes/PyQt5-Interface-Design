from cx_Freeze import setup, Executable
import sys
from PyQt5 import QtWidgets

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
    Executable("main.py", base=base)
]

setup(
    name="YourAppName",
    version="1.0",
    description="Your application description",
    executables=executables,
    options={
        "build_exe": {
            "includes": ["PyQt5.QtCore", "PyQt5.QtGui", "PyQt5.QtWidgets"],
            # Add any other dependencies or options as needed
        }
    }
)
