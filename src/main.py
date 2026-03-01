import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os

# Arda-OS Windows Bridge v1.0
# Character-safe English interface for Linux environments

class WindowsBridge:
    def __init__(self, root):
        self.root = root
        self.root.title("Arda-OS Windows Bridge")
        self.root.geometry("450x250")
        self.root.configure(bg="#2c3e50") # Gray-blue theme

        self.label = tk.Label(root, text="Windows-on-Linux Runner", fg="#ecf0f1", bg="#2c3e50", font=("Arial", 14, "bold"))
        self.label.pack(pady=20)

        self.run_btn = tk.Button(root, text="Select and Run .exe", command=self.launch_app, 
                                 bg="#3498db", fg="white", font=("Arial", 10), width=20, height=2)
        self.run_btn.pack(pady=10)

        self.status = tk.Label(root, text="Status: Ready", fg="#95a5a6", bg="#2c3e50")
        self.status.pack(side="bottom", pady=10)

    def launch_app(self):
        file_path = filedialog.askopenfilename(filetypes=[("Executable files", "*.exe")])
        if file_path:
            self.status.config(text=f"Launching: {os.path.basename(file_path)}", fg="#2ecc71")
            try:
                # Calling the bash wrapper with NVIDIA hardware acceleration
                subprocess.Popen(["bash", "../run-windows-on-linux.sh", file_path])
            except Exception as e:
                messagebox.showerror("Error", f"Failed to launch: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = WindowsBridge(root)
    root.mainloop()
