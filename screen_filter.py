import tkinter as tk
from win32gui import SetWindowLong, GetWindowLong, SetLayeredWindowAttributes
from win32con import WS_EX_LAYERED, WS_EX_TRANSPARENT, GWL_EXSTYLE
import subprocess
import psutil

def setClickThrough(hwnd):
    try:
        styles = GetWindowLong(hwnd, GWL_EXSTYLE)
        styles = WS_EX_LAYERED | WS_EX_TRANSPARENT
        SetWindowLong(hwnd, GWL_EXSTYLE, styles)
        SetLayeredWindowAttributes(hwnd, 0, 255, 0x00000001)
    except Exception as e:
        print(e)

def check_app_status():
    if ("Aquile Reader.exe" in [p.name() for p in psutil.process_iter()]):
        window.after(5000, check_app_status)
    else:
        print("Aquile Reader stopped running.")
        window.destroy()

if __name__ == "__main__":
    window = tk.Tk()
    
    window.attributes('-fullscreen', True)
    window['bg'] = '#FBF0D9'
    window.attributes('-alpha', 0.3)
    window.attributes('-transparentcolor', '#000000', '-topmost', 1)
    window.overrideredirect(True)

    setClickThrough(window.winfo_id())

    aumid = '21676OptimiliaStudios.AquileReader_k42naep6bwmrc!App'
    command_to_run = f'explorer shell:appsfolder\\{aumid}'
    print(f'Attempting to launch Aquile Reader using command: {command_to_run}')

    try:
        subprocess.run(command_to_run, shell=True, capture_output=True, text=True)
        print('Aquile Reader launched successfully.')
    except FileNotFoundError:
        print("Error: 'explorer' command not found")
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
    
    window.after(1000, check_app_status)

    window.mainloop()