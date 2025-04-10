from PyInstaller.__main__ import run

# Define the options for PyInstaller
options = [
    'afk_monitor.py',  # Main script to convert
    '--onefile',       # Create a single executable file
    '--name=ED-AFK-Monitor',  # Name of the output executable
]

# Run PyInstaller with the specified options
if __name__ == '__main__':
    run(options)
