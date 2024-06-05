import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from functions import download_video, check_youtube_url
import threading
import webbrowser

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()        

    def create_widgets(self):
        self.master.geometry("400x200")
        self.master.resizable(False, False)
        self.master.title("YouTube to MP3 Converter")

        self.url_label = ttk.Label(self, text="YouTube URL:")
        self.url_label.pack(pady=10)

        self.url_entry = ttk.Entry(self, width=50)
        self.url_entry.pack(pady=5)

        self.download_button = ttk.Button(self, text="Download MP3", command=self.start_download)
        self.download_button.pack(pady=10)

        self.progress = ttk.Progressbar(self, orient="horizontal", length=300, mode="determinate")
        self.progress.pack(pady=10)

        self.signature_label = ttk.Label(self, text="Developed by Thalles-J-G-Silva", cursor="hand2")
        self.signature_label.bind("<Button-1>", lambda event: webbrowser.open_new_tab("https://github.com/Thalles-JG-Silva"))
        self.signature_label.pack(pady=10)

    def start_download(self):
        url = self.url_entry.get()
        if check_youtube_url(url):
            output_path = filedialog.askdirectory()
            if output_path:
                self.progress.start()
                download_thread = threading.Thread(target=self.download_mp3, args=(url, output_path))
                download_thread.start()
            else:
                messagebox.showerror("Error", "Please select a valid directory")
        else:
            messagebox.showerror("Error", "Invalid YouTube URL")

    def download_mp3(self, url, output_path):
        try:
            new_file = download_video(url, output_path)
            self.progress.stop()
            messagebox.showinfo("Success", f"Downloaded and converted to MP3: {new_file}")
        except Exception as e:
            self.progress.stop()
            messagebox.showerror("Error", f"Failed to download: {e}")

def start_gui():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
