import tkinter as tk
from win32gui import SetWindowLong, GetWindowLong, SetLayeredWindowAttributes
from win32con import WS_EX_LAYERED, WS_EX_TRANSPARENT, GWL_EXSTYLE

def setClickThrough(hwnd):
    try:
        styles = GetWindowLong(hwnd, GWL_EXSTYLE)
        styles = WS_EX_LAYERED | WS_EX_TRANSPARENT
        SetWindowLong(hwnd, GWL_EXSTYLE, styles)
        SetLayeredWindowAttributes(hwnd, 0, 255, 0x00000001)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    window = tk.Tk()
    
    window.attributes('-fullscreen', True)
    window['bg'] = '#FBF0D9'
    window.attributes('-alpha', 0.3)
    window.attributes('-transparentcolor', '#000000', '-topmost', 1)

    setClickThrough(window.winfo_id())

    window.mainloop()