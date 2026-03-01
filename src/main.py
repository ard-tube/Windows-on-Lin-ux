import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os

def launch_app():
    file_path = filedialog.askopenfilename(filetypes=[("Executable files", "*.exe")])
    if file_path:
        # Senin yazdigin scripti NVIDIA destegiyle cagiriyoruz
        try:
            subprocess.Popen(["bash", "../run-windows-on-linux.sh", file_path])
            messagebox.showinfo("Success", f"Launching {os.path.basename(file_path)} with NVIDIA acceleration.")
        except Exception as e:
            messagebox.showerror("Error", f"Could not launch: {e}")

root = tk.Tk()
root.title("Arda-OS Windows Bridge")
root.geometry("400x200")

label = tk.Label(root, text="Windows on Linux Wrapper", font=("Arial", 14))
label.pack(pady=20)

btn = tk.Button(root, text="Select and Run .exe", command=launch_app, bg="#3498db", fg="white")
btn.pack(pady=10)

root.mainloop()
