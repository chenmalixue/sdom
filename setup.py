from cx_Freeze import setup, Executable
 
setup(
    name = "SCOM",
    version = "0.1",
    description = "SCOM",
    executables = [Executable("manage.py", base="Win32GUI")]  # Use "Win32GUI" for Windows to hide the console window
)