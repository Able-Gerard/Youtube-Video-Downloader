import tkinter as tk
from tkinter import filedialog, messagebox
import yt_dlp
import os

def select_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        path_var.set(folder_selected)

def download_video():
    url = url_entry.get()
    folder = path_var.get()

    if not url:
        messagebox.showerror("Error", "Please enter a YouTube URL.")
        return
    if not folder:
        messagebox.showerror("Error", "Please select a download location.")
        return

    # Always save downloads to a 'YT' subfolder inside the selected folder
    download_dir = os.path.join(folder, 'YT')
    os.makedirs(download_dir, exist_ok=True)
    ydl_opts = {
        'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
        'format': 'best',
        'merge_output_format': 'mp4',
        'quiet': True,
        'noplaylist': True,
        'ignoreerrors': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Success", "Video downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Download Error", str(e))

# GUI setup
root = tk.Tk()
root.title("YouTube Downloader (yt-dlp)")
root.geometry("500x250")
root.resizable(False, False)

# URL Input
tk.Label(root, text="YouTube Video URL:", font=("Arial", 12)).pack(pady=10)
url_entry = tk.Entry(root, width=60)
url_entry.pack()

# Folder Selection
tk.Label(root, text="Download Folder:", font=("Arial", 12)).pack(pady=10)
path_var = tk.StringVar()
folder_frame = tk.Frame(root)
folder_frame.pack()
folder_entry = tk.Entry(folder_frame, textvariable=path_var, width=40)
folder_entry.pack(side="left", padx=5)
browse_button = tk.Button(folder_frame, text="Browse", command=select_folder)
browse_button.pack(side="left")

# Download Button
download_button = tk.Button(root, text="Download Video", font=("Arial", 12), bg="green", fg="white", command=download_video)
download_button.pack(pady=20)

root.mainloop()
