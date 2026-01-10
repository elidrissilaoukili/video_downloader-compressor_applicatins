import os
import sys
import threading
from tkinter import filedialog, messagebox
import customtkinter as ctk
import yt_dlp
import webbrowser

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class YouTubeDownloader(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Video Downloader Pro - idrilogic")
        self.geometry("700x750")
        self.minsize(600, 500)
        self.resizable(True, True)
        
        # Main container with padding
        self.main_frame = ctk.CTkScrollableFrame(self, fg_color="transparent")
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Title
        title = ctk.CTkLabel(
            self.main_frame, 
            text="🎬 Video Downloader Pro",
            font=("Arial", 24, "bold")
        )
        title.pack(pady=(0, 20))
        
        
                # Branding
        brand = ctk.CTkLabel(
            self.main_frame,
            text="idrilogic",
            font=("Arial", 16, "bold"),
            text_color="#1f538d"
        )
        brand.pack(pady=(0, 20))
        
        
        # URL input section
        url_frame = ctk.CTkFrame(self.main_frame)
        url_frame.pack(fill="x", pady=(0, 15))
        
        self.url_label = ctk.CTkLabel(
            url_frame, 
            text="YouTube URL(s):", 
            font=("Arial", 14, "bold")
        )
        self.url_label.pack(anchor="w", padx=15, pady=(15, 5))
        
        self.url_textbox = ctk.CTkTextbox(
            url_frame, 
            height=100, 
            font=("Arial", 11),
            wrap="word"
        )
        self.url_textbox.pack(fill="x", padx=15, pady=(0, 10))
        self.url_textbox.insert("1.0", "Paste YouTube URLs here (one per line for multiple videos)")
        self.url_textbox.bind("<FocusIn>", self.clear_placeholder)
        
        help_label = ctk.CTkLabel(
            url_frame,
            text="💡 Supports: Single videos, playlists, and multiple URLs",
            font=("Arial", 10),
            text_color="gray"
        )
        help_label.pack(anchor="w", padx=15, pady=(0, 10))
        
        # Options section
        options_frame = ctk.CTkFrame(self.main_frame)
        options_frame.pack(fill="x", pady=(0, 15))
        
        # Format selection
        format_container = ctk.CTkFrame(options_frame, fg_color="transparent")
        format_container.pack(side="left", fill="both", expand=True, padx=15, pady=15)
        
        format_label = ctk.CTkLabel(
            format_container, 
            text="Format:", 
            font=("Arial", 13, "bold")
        )
        format_label.pack(anchor="w", pady=(0, 8))
        
        self.format_var = ctk.StringVar(value="mp4")
        
        radio_frame = ctk.CTkFrame(format_container, fg_color="transparent")
        radio_frame.pack(anchor="w")
        
        self.mp4_radio = ctk.CTkRadioButton(
            radio_frame,
            text="Video (MP4)",
            variable=self.format_var,
            value="mp4",
            font=("Arial", 11),
            command=self.toggle_quality
        )
        self.mp4_radio.pack(anchor="w", pady=2)
        
        self.mp3_radio = ctk.CTkRadioButton(
            radio_frame,
            text="Audio (MP3)",
            variable=self.format_var,
            value="mp3",
            font=("Arial", 11),
            command=self.toggle_quality
        )
        self.mp3_radio.pack(anchor="w", pady=2)
        
        # Quality selection
        quality_container = ctk.CTkFrame(options_frame, fg_color="transparent")
        quality_container.pack(side="left", fill="both", expand=True, padx=15, pady=15)
        
        self.quality_label = ctk.CTkLabel(
            quality_container,
            text="Video Quality:",
            font=("Arial", 13, "bold")
        )
        self.quality_label.pack(anchor="w", pady=(0, 8))
        
        self.quality_var = ctk.StringVar(value="best")
        self.quality_menu = ctk.CTkOptionMenu(
            quality_container,
            variable=self.quality_var,
            values=["Best Quality", "1080p", "720p", "480p", "360p"],
            font=("Arial", 11),
            width=150
        )
        self.quality_menu.pack(anchor="w")
        
        # Download type
        type_container = ctk.CTkFrame(options_frame, fg_color="transparent")
        type_container.pack(side="left", fill="both", expand=True, padx=15, pady=15)
        
        type_label = ctk.CTkLabel(
            type_container,
            text="Download Type:",
            font=("Arial", 13, "bold")
        )
        type_label.pack(anchor="w", pady=(0, 8))
        
        self.playlist_var = ctk.CTkCheckBox(
            type_container,
            text="Download Playlists",
            font=("Arial", 11)
        )
        self.playlist_var.pack(anchor="w", pady=2)
        self.playlist_var.select()
        
        # Save location section
        save_frame = ctk.CTkFrame(self.main_frame)
        save_frame.pack(fill="x", pady=(0, 15))
        
        save_label = ctk.CTkLabel(
            save_frame,
            text="Save Location:",
            font=("Arial", 13, "bold")
        )
        save_label.pack(anchor="w", padx=15, pady=(15, 8))
        
        location_frame = ctk.CTkFrame(save_frame, fg_color="transparent")
        location_frame.pack(fill="x", padx=15, pady=(0, 15))
        
        self.folder_path = ctk.StringVar(value=os.path.expanduser("~/Downloads"))
        self.folder_display = ctk.CTkEntry(
            location_frame,
            textvariable=self.folder_path,
            font=("Arial", 10),
            state="readonly",
            height=35
        )
        self.folder_display.pack(side="left", fill="x", expand=True, padx=(0, 10))
        
        self.save_button = ctk.CTkButton(
            location_frame,
            text="Browse",
            command=self.choose_folder,
            width=100,
            height=35,
            font=("Arial", 11)
        )
        self.save_button.pack(side="right")
        
        # Download button
        self.download_btn = ctk.CTkButton(
            self.main_frame,
            text="⬇ Start Download",
            command=self.start_download,
            height=45,
            font=("Arial", 16, "bold"),
            fg_color="#1f538d",
            hover_color="#14375e"
        )
        self.download_btn.pack(fill="x", pady=(0, 15))
        
        # Progress section
        progress_frame = ctk.CTkFrame(self.main_frame)
        progress_frame.pack(fill="x", pady=(0, 0))
        
        self.progress = ctk.CTkProgressBar(progress_frame, height=20)
        self.progress.set(0)
        self.progress.pack(fill="x", padx=15, pady=(15, 10))
        
        self.status = ctk.CTkLabel(
            progress_frame,
            text="Ready to download",
            font=("Arial", 11),
            text_color="gray"
        )
        self.status.pack(padx=15, pady=(0, 15))
        
        self.downloading = False

        # Footer with author info and social links
        footer_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        footer_frame.pack(fill="x", pady=(15, 0))
     
        # Separator line
        separator = ctk.CTkFrame(footer_frame, height=2, fg_color="gray")
        separator.pack(fill="x", pady=(0, 10))
        
        # Author info
        author_label = ctk.CTkLabel(
            footer_frame,
            text="Created by Mohammed El Idrissi Laoukili",
            font=("Arial", 10),
            text_color="gray"
        )
        author_label.pack(pady=(0, 8))
        
        # Social buttons frame
        social_frame = ctk.CTkFrame(footer_frame, fg_color="transparent")
        social_frame.pack()
        
        # YouTube button
        youtube_btn = ctk.CTkButton(
            social_frame,
            text="🎥 YouTube",
            command=self.open_youtube,
            width=120,
            height=32,
            font=("Arial", 11),
            fg_color="#FF0000",
            hover_color="#CC0000"
        )
        youtube_btn.pack(side="left", padx=5)
        
        # Instagram button
        instagram_btn = ctk.CTkButton(
            social_frame,
            text="📷 Instagram",
            command=self.open_instagram,
            width=120,
            height=32,
            font=("Arial", 11),
            fg_color="#E4405F",
            hover_color="#C13584"
        )
        instagram_btn.pack(side="left", padx=5)

    def open_youtube(self):
        webbrowser.open("https://www.youtube.com/channel/UCLfvN8mgGZMoySSVIWGSNTQ")
    
    def open_instagram(self):
        webbrowser.open("https://www.instagram.com/__elidrissii/")


    def clear_placeholder(self, event):
        if self.url_textbox.get("1.0", "end-1c") == "Paste YouTube URLs here (one per line for multiple videos)":
            self.url_textbox.delete("1.0", "end")

    def toggle_quality(self):
        if self.format_var.get() == "mp3":
            self.quality_menu.configure(state="disabled")
            self.quality_label.configure(text_color="gray")
        else:
            self.quality_menu.configure(state="normal")
            self.quality_label.configure(text_color=("gray10", "gray90"))

    def choose_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.folder_path.set(folder)

    def start_download(self):
        if self.downloading:
            messagebox.showwarning("Warning", "Download already in progress!")
            return
            
        urls_text = self.url_textbox.get("1.0", "end-1c").strip()
        if not urls_text or urls_text == "Paste YouTube URLs here (one per line for multiple videos)":
            messagebox.showerror("Error", "Please enter at least one YouTube URL!")
            return
        
        # Parse URLs (split by newline)
        urls = [url.strip() for url in urls_text.split('\n') if url.strip()]
        
        self.downloading = True
        self.download_btn.configure(state="disabled", text="Downloading...")
        self.progress.set(0)
        self.status.configure(text="Initializing download...")
        
        thread = threading.Thread(
            target=self.download_videos,
            args=(urls, self.folder_path.get(), self.format_var.get())
        )
        thread.daemon = True
        thread.start()

    def get_ffmpeg_dir(self):
        """Get directory containing FFmpeg binaries"""
        if getattr(sys, 'frozen', False):
            return sys._MEIPASS
        else:
            return os.getcwd()

    def get_format_string(self):
        """Get yt-dlp format string based on quality selection"""
        if self.format_var.get() == "mp3":
            return 'bestaudio/best'
        
        quality = self.quality_var.get()
        if quality == "Best Quality":
            return 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
        elif quality == "1080p":
            return 'bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[height<=1080][ext=mp4]/best'
        elif quality == "720p":
            return 'bestvideo[height<=720][ext=mp4]+bestaudio[ext=m4a]/best[height<=720][ext=mp4]/best'
        elif quality == "480p":
            return 'bestvideo[height<=480][ext=mp4]+bestaudio[ext=m4a]/best[height<=480][ext=mp4]/best'
        elif quality == "360p":
            return 'bestvideo[height<=360][ext=mp4]+bestaudio[ext=m4a]/best[height<=360][ext=mp4]/best'
        
        return 'best'

    def download_videos(self, urls, save_dir, format_type):
        try:
            ffmpeg_dir = self.get_ffmpeg_dir()
            
            ydl_opts = {
                'outtmpl': os.path.join(save_dir, '%(title)s.%(ext)s'),
                'progress_hooks': [self.update_progress],
                'quiet': True,
                'no_warnings': True,
                'ffmpeg_location': ffmpeg_dir,
                'noplaylist': not self.playlist_var.get(),
            }
            
            if format_type == "mp3":
                ydl_opts.update({
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }]
                })
            else:
                ydl_opts['format'] = self.get_format_string()
            
            total_urls = len(urls)
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                for idx, url in enumerate(urls, 1):
                    self.after(0, lambda i=idx, t=total_urls: self.status.configure(
                        text=f"Processing URL {i}/{t}..."
                    ))
                    ydl.download([url])
            
            self.after(0, lambda: self.status.configure(
                text=f"✅ Successfully downloaded {total_urls} item(s)!",
                text_color="green"
            ))
            self.after(0, lambda: self.progress.set(1))
            
        except Exception as e:
            error_msg = str(e)[:100] + "..." if len(str(e)) > 100 else str(e)
            self.after(0, lambda: self.status.configure(
                text=f"❌ Error: {error_msg}",
                text_color="red"
            ))
        finally:
            self.downloading = False
            self.after(0, lambda: self.download_btn.configure(
                state="normal",
                text="⬇ Start Download"
            ))

    def update_progress(self, d):
        if d['status'] == 'downloading':
            total = d.get('total_bytes') or d.get('total_bytes_estimate') or 1
            downloaded = d.get('downloaded_bytes', 0)
            pct = downloaded / total if total > 0 else 0
            speed = d.get('speed', 0)
            speed_str = f"{speed / 1024 / 1024:.2f} MB/s" if speed else "N/A"
            
            self.after(0, lambda: self.progress.set(pct))
            self.after(0, lambda p=pct, s=speed_str: self.status.configure(
                text=f"Downloading... {p:.1%} | Speed: {s}",
                text_color=("gray10", "gray90")
            ))
        elif d['status'] == 'finished':
            self.after(0, lambda: self.status.configure(
                text="Processing file...",
                text_color=("gray10", "gray90")
            ))

if __name__ == "__main__":
    app = YouTubeDownloader()
    app.mainloop()