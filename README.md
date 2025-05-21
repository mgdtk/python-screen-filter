# ✨ Custom Yellow Screen Filter for Reading on Windows ✨

This small Python project was born out of my personal need to make my reading experience more comfortable. I developed it to create a soothing yellow screen filter that automatically activates when I open my preferred reading application (specifically Aquile Reader) on Windows, and gracefully disappears when I'm done reading. It's a simple, tailored solution for my eyes! 😉

## 📌 Description

- 🎨 Creates a full-screen yellow overlay with customizable color and transparency.

- 🖱️ It's completely click-through! You can interact with the windows underneath as usual.

- 👻 Doesn't appear in the Windows taskbar, staying discreetly in the background.

- 🚀 Launches Aquile Reader for you when the program starts.

- 🕵️‍♂️ Monitors Aquile Reader and automatically closes the filter when the app is shut down.

- 📦 Can be packaged into a single executable (`.exe`) for easy use on any Windows machine without needing Python installed!

## 🛠️ Technologies Used

- **Python**

## 📋 Prerequisites

- 🐍 **Python 3.x** installed on your Windows machine.

- 💻 **Windows Operating System** (it uses Windows-specific functionalities like `pywin32`).

- 📚 The **"Aquile Reader"** application from the Microsoft Store installed.

## 🚀 Getting Started

1.  💾 **Save the Code:** Take the complete Python code you've developed and save it to a file, for example, `screen_filter.py`.

2.  ▶️ **Execute:** Open your terminal (Command Prompt or PowerShell) in the folder where you saved the file and run:

    ```bash
    python screen_filter.py
    ```
3.  ✨ The script will attempt to launch Aquile Reader (using its unique AUMID) and your yellow filter will appear.
4.  😌 The filter will stay active while you read. Close Aquile Reader, and the filter will disappear!

**Important:** The code uses the AUMID `21676OptimiliaStudios.AquileReader_k42naep6bwmrc!App`, which is the specific identifier for the Aquile Reader app from the Microsoft Store. If you're using a different app or a different version, you'll need to find its correct AUMID.

## 🔎 How to Find Your App's AUMID

Finding the **Application User Model ID (AUMID)** for Microsoft Store (UWP) apps can be a bit tricky, but it's essential for launching them programmatically. Here's how you can usually find it:

1.  **Open PowerShell:** Search for "PowerShell" in the Windows Start Menu and open it.

2.  **List Installed Apps and Their AUMIDs:** In the PowerShell window, paste and run the following command:

    ```powershell
    Get-StartApps | Select-Object Name, AppID
    ```

3.  **Find Your App:** This command will list the names and AppIDs (which are often the AUMIDs) of all apps installed via the Start Menu. Scroll through the list or use `Ctrl+F` to search for your reading app (e.g., "Aquile Reader").

4.  **Copy the AppID:** The value under the `AppID` column for your application is its AUMID. It usually follows the format `PackageFamilyName!AppId`. Copy this entire string.

5.  **Update Your Code:** Replace the placeholder AUMID in your Python script with the one you found.

## 💾 Building the .exe

If you want to use the program without installing Python or its dependencies, you can turn it into an executable using **PyInstaller**!

1.  📦 **Install PyInstaller:**
    ```bash
    pip install pyinstaller
    ```

2.  📂 **Navigate to Your Script's Folder:**
    Use `cd` in your terminal to go to the directory where you saved `screen_filter.py`.

3.  🔨 **Create the Executable:**
    Run the PyInstaller command.

    ```bash
    pyinstaller --onefile --windowed screen_filter.py
    ```

    - If your terminal says `pyinstaller` is not recognized, it might be because your Python's `Scripts` folder isn't in your system's PATH. You'll either need to use the full path to `pyinstaller.exe` (which `pip` usually shows you during installation) or add the folder to your Windows PATH.

4.  🎉 **Your .exe is Ready!**
    Look for the `dist` folder in the same directory as your script. Inside, you'll find `screen_filter.exe`!

## 📝 Technical Notes

- Launching the Store app is done via a special command (`explorer shell:appsfolder\<AUMID>`) that communicates directly with Windows, avoiding permission issues with protected `WindowsApps` folders.

- App monitoring with `psutil` runs in the background using `tkinter.after()`, ensuring your screen doesn't freeze.

- A smart `try...except` block within the `psutil` loop ensures your program doesn't crash if other Windows processes unexpectedly terminate or deny access while being checked. It makes everything more robust!

## 🤝 Want to Contribute?

While this project was built for a personal need, I'm always open to ideas! If you find a bug or have a cool suggestion, feel free to fork this repository, open an issue, or send a Pull Request! All help is welcome! 😊

## 🔑 License

This project is licensed under the MIT License. Please see the `LICENSE` file for more details.