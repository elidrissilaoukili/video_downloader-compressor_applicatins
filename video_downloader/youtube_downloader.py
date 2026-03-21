# import os
# import sys
# import threading
# from tkinter import filedialog, messagebox
# import customtkinter as ctk
# import yt_dlp
# import webbrowser
# from PIL import Image

# ctk.set_appearance_mode("System")
# ctk.set_default_color_theme("blue")

# class YouTubeDownloader(ctk.CTk):
#     def __init__(self):
#         super().__init__()
#         self.title("Free Video Downloader - idrilogic")
#         self.geometry("700x500")
#         self.minsize(600, 500)
#         self.resizable(True, True)
        
#         # Add icon - Add these lines:
#         try:
#             # Get the correct path for both script and frozen exe
#             if getattr(sys, 'frozen', False):
#                 # Running as compiled exe
#                 icon_path = os.path.join(sys._MEIPASS, 'icon.ico')
#             else:
#                 # Running as script
#                 icon_path = 'icon.ico'
            
#             if sys.platform.startswith('win'):
#                 self.iconbitmap(icon_path)  # For Windows - shows in taskbar and window
#                 # Force icon to appear in taskbar
#                 self.after(201, lambda: self.iconbitmap(icon_path))
#             else:
#                 # For Linux/Mac, use PhotoImage
#                 from PIL import Image, ImageTk
#                 img = Image.open(icon_path)
#                 photo = ImageTk.PhotoImage(img)
#                 self.iconphoto(True, photo)
#         except Exception as e:
#             print(f"Could not load icon: {e}")
        
        
        
        
                
#         # Main container with padding
#         self.main_frame = ctk.CTkScrollableFrame(self, fg_color="transparent")
#         self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
#         # Title
#         title = ctk.CTkLabel(
#             self.main_frame, 
#             text="🎬 Free Video Downloader - تحميل الفيديوهات مجانًا",
#             font=("Arial", 24, "bold")
#         )
#         title.pack(pady=(0, 20))
        
#         # Branding
#         brand = ctk.CTkLabel(
#             self.main_frame,
#             text="idrilogic",
#             font=("Arial", 16, "bold"),
#             text_color="#1f538d"
#         )
#         brand.pack(pady=(0, 10))
        
#         self.supportButtonsFrame()
        
#         # URL input section
#         url_frame = ctk.CTkFrame(self.main_frame)
#         url_frame.pack(fill="x", pady=(0, 15))
        
#         self.url_label = ctk.CTkLabel(
#             url_frame, 
#             text="YouTube URL(s):", 
#             font=("Arial", 14, "bold")
#         )
#         self.url_label.pack(anchor="w", padx=15, pady=(15, 5))
        
#         self.url_textbox = ctk.CTkTextbox(
#             url_frame, 
#             height=100, 
#             font=("Arial", 11),
#             wrap="word"
#         )
        
        
#         self.url_textbox.pack(fill="x", padx=15, pady=(0, 10))
#         self.url_textbox.insert("1.0", "Paste YouTube URLs here (one per line for multiple videos)")
#         self.url_textbox.bind("<FocusIn>", self.clear_placeholder)

#         # Add helper buttons frame - ADD THIS SECTION
#         helper_buttons_frame = ctk.CTkFrame(url_frame, fg_color="transparent")
#         helper_buttons_frame.pack(fill="x", padx=15, pady=(0, 5))

#         paste_helper_btn = ctk.CTkButton(
#             helper_buttons_frame,
#             text="📋 Paste URLs",
#             command=self.paste_helper,
#             width=100,
#             height=28,
#             font=("Arial", 10),
#             fg_color=("gray70", "gray30"),
#             hover_color=("#1f538d", "#14375e")
#         )
#         paste_helper_btn.pack(side="left", padx=(0, 5))

#         copy_helper_btn = ctk.CTkButton(
#             helper_buttons_frame,
#             text="📄 Copy All",
#             command=self.copy_helper,
#             width=100,
#             height=28,
#             font=("Arial", 10),
#             fg_color=("gray70", "gray30"),
#             hover_color=("#1f538d", "#14375e")
#         )
#         copy_helper_btn.pack(side="left", padx=(0, 5))

#         clear_helper_btn = ctk.CTkButton(
#             helper_buttons_frame,
#             text="🗑️ Clear",
#             command=self.clear_helper,
#             width=80,
#             height=28,
#             font=("Arial", 10),
#             fg_color=("gray70", "gray30"),
#             hover_color=("#8B0000", "#CC0000")
#         )
#         clear_helper_btn.pack(side="left")
        
#         help_label = ctk.CTkLabel(
#             url_frame,
#             text="💡 Supports: Single videos, playlists, and multiple URLs",
#             font=("Arial", 10),
#             text_color="gray"
#         )
#         help_label.pack(anchor="w", padx=15, pady=(0, 10))
        
        
#         # Options section
#         options_frame = ctk.CTkFrame(self.main_frame)
#         options_frame.pack(fill="x", pady=(0, 15))
        
#         # Format selection
#         format_container = ctk.CTkFrame(options_frame, fg_color="transparent")
#         format_container.pack(side="left", fill="both", expand=True, padx=15, pady=15)
        
#         format_label = ctk.CTkLabel(
#             format_container, 
#             text="Format:", 
#             font=("Arial", 13, "bold")
#         )
#         format_label.pack(anchor="w", pady=(0, 8))
        
#         self.format_var = ctk.StringVar(value="mp4")
        
#         radio_frame = ctk.CTkFrame(format_container, fg_color="transparent")
#         radio_frame.pack(anchor="w")
        
#         self.mp4_radio = ctk.CTkRadioButton(
#             radio_frame,
#             text="Video (MP4)",
#             variable=self.format_var,
#             value="mp4",
#             font=("Arial", 11),
#             command=self.toggle_quality
#         )
#         self.mp4_radio.pack(anchor="w", pady=2)
        
#         self.mp3_radio = ctk.CTkRadioButton(
#             radio_frame,
#             text="Audio (MP3)",
#             variable=self.format_var,
#             value="mp3",
#             font=("Arial", 11),
#             command=self.toggle_quality
#         )
#         self.mp3_radio.pack(anchor="w", pady=2)
        
#         # Quality selection
#         quality_container = ctk.CTkFrame(options_frame, fg_color="transparent")
#         quality_container.pack(side="left", fill="both", expand=True, padx=15, pady=15)
        
#         self.quality_label = ctk.CTkLabel(
#             quality_container,
#             text="Video Quality:",
#             font=("Arial", 13, "bold")
#         )
#         self.quality_label.pack(anchor="w", pady=(0, 8))
        
#         self.quality_var = ctk.StringVar(value="best")
#         self.quality_menu = ctk.CTkOptionMenu(
#             quality_container,
#             variable=self.quality_var,
#             values=["Best Quality", "1080p", "720p", "480p", "360p", "240p", "144p"],
#             font=("Arial", 11),
#             width=150
#         )
#         self.quality_menu.pack(anchor="w")
        
#         # Download type
#         type_container = ctk.CTkFrame(options_frame, fg_color="transparent")
#         type_container.pack(side="left", fill="both", expand=True, padx=15, pady=15)
        
#         type_label = ctk.CTkLabel(
#             type_container,
#             text="Download Type:",
#             font=("Arial", 13, "bold")
#         )
#         type_label.pack(anchor="w", pady=(0, 8))
        
#         self.playlist_var = ctk.CTkCheckBox(
#             type_container,
#             text="Download Playlists",
#             font=("Arial", 11)
#         )
#         self.playlist_var.pack(anchor="w", pady=2)
#         self.playlist_var.select()
        
#         # Save location section
#         save_frame = ctk.CTkFrame(self.main_frame)
#         save_frame.pack(fill="x", pady=(0, 15))
        
#         save_label = ctk.CTkLabel(
#             save_frame,
#             text="Save Location:",
#             font=("Arial", 13, "bold")
#         )
#         save_label.pack(anchor="w", padx=15, pady=(15, 8))
        
#         location_frame = ctk.CTkFrame(save_frame, fg_color="transparent")
#         location_frame.pack(fill="x", padx=15, pady=(0, 15))
        
#         self.folder_path = ctk.StringVar(value=os.path.expanduser("~/Downloads"))
#         self.folder_display = ctk.CTkEntry(
#             location_frame,
#             textvariable=self.folder_path,
#             font=("Arial", 10),
#             state="readonly",
#             height=35
#         )
#         self.folder_display.pack(side="left", fill="x", expand=True, padx=(0, 10))
        
#         self.save_button = ctk.CTkButton(
#             location_frame,
#             text="Browse",
#             command=self.choose_folder,
#             width=100,
#             height=35,
#             font=("Arial", 11)
#         )
#         self.save_button.pack(side="right")
        
#         # Download button
#         self.download_btn = ctk.CTkButton(
#             self.main_frame,
#             text="⬇ Start Download",
#             command=self.start_download,
#             height=45,
#             font=("Arial", 16, "bold"),
#             fg_color="#1f538d",
#             hover_color="#14375e"
#         )
#         self.download_btn.pack(fill="x", pady=(0, 15))
        
#         # Progress section
#         progress_frame = ctk.CTkFrame(self.main_frame)
#         progress_frame.pack(fill="x", pady=(0, 0))
        
#         self.progress = ctk.CTkProgressBar(progress_frame, height=20)
#         self.progress.set(0)
#         self.progress.pack(fill="x", padx=15, pady=(15, 10))
        
#         self.status = ctk.CTkLabel(
#             progress_frame,
#             text="Ready to download",
#             font=("Arial", 11),
#             text_color="gray"
#         )
#         self.status.pack(padx=15, pady=(0, 15))
        
#         self.downloading = False

#         # Footer with author info and social links
#         footer_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
#         footer_frame.pack(fill="x", pady=(15, 0))
     
#         # Separator line
#         separator = ctk.CTkFrame(footer_frame, height=2, fg_color="gray")
#         separator.pack(fill="x", pady=(0, 10))
        
#         # Author info
#         author_label = ctk.CTkLabel(
#             footer_frame,
#             text="Created by Mohammed El Idrissi Laoukili",
#             font=("Arial", 10),
#             text_color="gray"
#         )
#         author_label.pack(pady=(0, 8))

#         self.socialButtonsFrame(footer_frame)


#     def supportButtonsFrame(self):
#         # support with author info and social links
#         support_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
#         support_frame.pack(fill="x", pady=(10, 0))
     
#         # # Separator line
#         # separator = ctk.CTkFrame(support_frame, height=2, fg_color="gray")
#         # separator.pack(fill="x", pady=(0, 10))
        
#         # Social buttons frame
#         social_frame = ctk.CTkFrame(support_frame, fg_color="transparent")
#         social_frame.pack()
        
#         # Paypal button
#         support_btn = ctk.CTkButton(
#             social_frame,
#             text="☕ Buy us a coffee — دعمك يهمنا",
#             command=self.open_support,
#             width=160,
#             height=36,
#             corner_radius=18,
#             font=("Arial", 16, "bold"),
#             fg_color="#CA6128",      # coffee/orange tone
#             hover_color="#8D3A16",
#             text_color="white",
#             cursor="hand2"
#         )
#         support_btn.pack(side="left", padx=6, pady=12)

#     def socialButtonsFrame(self, footer_frame):
#         # Social buttons frame
#         social_frame = ctk.CTkFrame(footer_frame, fg_color="transparent")
#         social_frame.pack()

#         # website button
#         website_btn = ctk.CTkButton(
#             social_frame,
#             text="🌐 الموقع — idricoding",
#             command=self.open_idricodingdotcom,
#             width=120,
#             height=32,
#             corner_radius=18,
#             font=("Arial", 12, "bold"),
#             fg_color="#DDDDDD",
#             hover_color="#A1A1A1",
#             text_color="#161616",
#             cursor="hand2"
#         )
#         website_btn.pack(side="left", padx=6)

        
#         # YouTube button
#         youtube_btn = ctk.CTkButton(
#             social_frame,
#             text="🎥 YouTube",
#             command=self.open_youtube,
#             width=120,
#             height=32,
#             font=("Arial", 11),
#             fg_color="#FF0000",
#             hover_color="#CC0000"
#         )
#         youtube_btn.pack(side="left", padx=5)
        
#         # YouTube button
#         github_btn = ctk.CTkButton(
#             social_frame,
#             text="💻 Github",
#             command=self.open_github,
#             width=120,
#             height=32,
#             font=("Arial", 11),
#             fg_color="#000000",
#             hover_color="#484848"
#         )
#         github_btn.pack(side="left", padx=5)
        
#         # Instagram button
#         instagram_btn = ctk.CTkButton(
#             social_frame,
#             text="📷 Instagram",
#             command=self.open_instagram,
#             width=120,
#             height=32,
#             font=("Arial", 11),
#             fg_color="#E4405F",
#             hover_color="#C13584"
#         )
#         instagram_btn.pack(side="left", padx=5)

#     def paste_helper(self):
#         """Simple paste button for users who don't know Ctrl+V"""
#         try:
#             # Clear placeholder if present
#             current_text = self.url_textbox.get("1.0", "end-1c")
#             if current_text == "Paste YouTube URLs here (one per line for multiple videos)":
#                 self.url_textbox.delete("1.0", "end")
            
#             clipboard_text = self.clipboard_get()
#             self.url_textbox.insert("insert", clipboard_text)
#         except:
#             messagebox.showinfo("Info", "No text found in clipboard!")

#     def copy_helper(self):
#         """Simple copy button for users who don't know Ctrl+C"""
#         try:
#             all_text = self.url_textbox.get("1.0", "end-1c")
#             if all_text and all_text != "Paste YouTube URLs here (one per line for multiple videos)":
#                 self.clipboard_clear()
#                 self.clipboard_append(all_text)
#                 messagebox.showinfo("Success", "URLs copied to clipboard!")
#             else:
#                 messagebox.showinfo("Info", "No URLs to copy!")
#         except Exception as e:
#             messagebox.showerror("Error", f"Failed to copy: {e}")

#     def clear_helper(self):
#         """Simple clear button"""
#         self.url_textbox.delete("1.0", "end")
#         self.url_textbox.insert("1.0", "Paste YouTube URLs here (one per line for multiple videos)")


#     def open_support(self):
#         webbrowser.open("https://www.paypal.com/ncp/payment/2KZ7WLGB24A6U")

#     def open_idricodingdotcom(self):
#         webbrowser.open("https://idricoding.vercel.app/")
        
#     def open_youtube(self):
#         webbrowser.open("https://www.youtube.com/channel/UCLfvN8mgGZMoySSVIWGSNTQ")
    
#     def open_github(self):
#         webbrowser.open("https://www.github.com/elidrissilaoukili")
    
#     def open_instagram(self):
#         webbrowser.open("https://www.instagram.com/__elidrissii/")


#     def clear_placeholder(self, event):
#         if self.url_textbox.get("1.0", "end-1c") == "Paste YouTube URLs here (one per line for multiple videos)":
#             self.url_textbox.delete("1.0", "end")

#     def toggle_quality(self):
#         if self.format_var.get() == "mp3":
#             self.quality_menu.configure(state="disabled")
#             self.quality_label.configure(text_color="gray")
#         else:
#             self.quality_menu.configure(state="normal")
#             self.quality_label.configure(text_color=("gray10", "gray90"))

#     def choose_folder(self):
#         folder = filedialog.askdirectory()
#         if folder:
#             self.folder_path.set(folder)

#     def start_download(self):
#         if self.downloading:
#             messagebox.showwarning("Warning", "Download already in progress!")
#             return
            
#         urls_text = self.url_textbox.get("1.0", "end-1c").strip()
#         if not urls_text or urls_text == "Paste YouTube URLs here (one per line for multiple videos)":
#             messagebox.showerror("Error", "Please enter at least one YouTube URL!")
#             return
        
#         # Parse URLs (split by newline)
#         urls = [url.strip() for url in urls_text.split('\n') if url.strip()]
        
#         # blocking specific domains
#         blocked_urls = [url for url in urls if self.is_blocked_domain(url)]
#         if blocked_urls:
#             messagebox.showerror(
#                 "Blocked Content", 
#                 f"The following URL(s) contain blocked content, it cannot be downloaded:\n\n" + 
#                 "\n".join(blocked_urls[:3]) + 
#                 ("\n..." if len(blocked_urls) > 3 else "")
#             )
#             return
        
#         self.downloading = True
#         self.download_btn.configure(state="disabled", text="Downloading...")
#         self.progress.set(0)
#         self.status.configure(text="Initializing download...")
        
#         thread = threading.Thread(
#             target=self.download_videos,
#             args=(urls, self.folder_path.get(), self.format_var.get())
#         )
#         thread.daemon = True
#         thread.start()

#     def get_ffmpeg_dir(self):
#         """Get directory containing FFmpeg binaries"""
#         if getattr(sys, 'frozen', False):
#             return sys._MEIPASS
#         else:
#             return os.getcwd()

#     def get_format_string(self):
#         """Get yt-dlp format string based on quality selection"""
#         if self.format_var.get() == "mp3":
#             return 'bestaudio/best'
        
#         quality = self.quality_var.get()
#         if quality == "Best Quality":
#             return 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
#         elif quality == "1080p":
#             return 'bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[height<=1080][ext=mp4]/best'
#         elif quality == "720p":
#             return 'bestvideo[height<=720][ext=mp4]+bestaudio[ext=m4a]/best[height<=720][ext=mp4]/best'
#         elif quality == "480p":
#             return 'bestvideo[height<=480][ext=mp4]+bestaudio[ext=m4a]/best[height<=480][ext=mp4]/best'
#         elif quality == "360p":
#             return 'bestvideo[height<=360][ext=mp4]+bestaudio[ext=m4a]/best[height<=360][ext=mp4]/best'
#         elif quality == "240p":
#             return 'bestvideo[height<=240][ext=mp4]+bestaudio[ext=m4a]/best[height<=240][ext=mp4]/best'
#         elif quality == "144p":
#             return 'bestvideo[height<=144][ext=mp4]+bestaudio[ext=m4a]/best[height<=144][ext=mp4]/best'
#         return 'best'

#     def is_blocked_domain(self, url):
#         """Check if URL contains blocked adult domains"""
#         blocked_domains = [
#             # Major porn sites
#             'pornhub.com',
#             'xvideos.com',
#             'xnxx.com',
#             'xhamster.com',
#             'redtube.com',
#             'youporn.com',
#             'tube8.com',
#             'spankbang.com',
#             'eporner.com',
#             'motherless.com',
#             'txxx.com',
#             'porn.com',
#             'sex.com',
#             'xxx.com',

#             # Additional large networks
#             'brazzers.com',
#             'bangbros.com',
#             'realitykings.com',
#             'naughtyamerica.com',
#             'digitalplayground.com',
#             'mofos.com',
#             'teamskeet.com',

#             # Aggregators / mirrors
#             'beeg.com',
#             'drtuber.com',
#             'keezmovies.com',
#             'nuvid.com',
#             'sunporno.com',
#             'upornia.com',
#             'yespornplease.com',
#             'anyporn.com',

#             # Amateur / cam / misc
#             'cam4.com',
#             'chaturbate.com',
#             'myfreecams.com',
#             'livejasmin.com',
#             'stripchat.com',

#             # Hentai / animated
#             'hanime.tv',
#             'hentaihaven.xxx',
#             'nhentai.net',
#             'rule34.xxx',
#             'e-hentai.org',
#             'exhentai.org',

#             # Reddit & image boards (NSFW-heavy)
#             'reddit.com/r/nsfw',
#             'reddit.com/r/porn',
#             '4chan.org',
#             '8kun.top',
#         ]

#         url_lower = url.lower()
#         return any(domain in url_lower for domain in blocked_domains)


#     def download_videos(self, urls, save_dir, format_type):
#         try:
#             ffmpeg_dir = self.get_ffmpeg_dir()
            
#             ydl_opts = {
#                 'outtmpl': os.path.join(save_dir, '%(title)s.%(ext)s'),
#                 'progress_hooks': [self.update_progress],
#                 'quiet': True,
#                 'no_warnings': True,
#                 'ffmpeg_location': ffmpeg_dir,
#                 'noplaylist': not self.playlist_var.get(),
#                 'age_limit': 18,
#                 'match_filter': yt_dlp.utils.match_filter_func("!is_live & age_limit<?18"),
#             }
            
#             if format_type == "mp3":
#                 ydl_opts.update({
#                     'format': 'bestaudio/best',
#                     'postprocessors': [{
#                         'key': 'FFmpegExtractAudio',
#                         'preferredcodec': 'mp3',
#                         'preferredquality': '192',
#                     }]
#                 })
#             else:
#                 ydl_opts['format'] = self.get_format_string()
            
            
#             total_urls = len(urls)
            
#             with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#                 for idx, url in enumerate(urls, 1):
#                     self.after(0, lambda i=idx, t=total_urls: self.status.configure(
#                         text=f"Processing URL {i}/{t}..."
#                     ))
#                     ydl.download([url])
            
#             self.after(0, lambda: self.status.configure(
#                 text=f"✅ Successfully downloaded {total_urls} item(s)!",
#                 text_color="green"
#             ))
#             self.after(0, lambda: self.progress.set(1))
            
#         except Exception as e:
#             error_msg = str(e)[:100] + "..." if len(str(e)) > 100 else str(e)
#             self.after(0, lambda: self.status.configure(
#                 text=f"❌ Error: {error_msg}",
#                 text_color="red"
#             ))
#         finally:
#             self.downloading = False
#             self.after(0, lambda: self.download_btn.configure(
#                 state="normal",
#                 text="⬇ Start Download"
#             ))

#     def update_progress(self, d):
#         if d['status'] == 'downloading':
#             total = d.get('total_bytes') or d.get('total_bytes_estimate') or 1
#             downloaded = d.get('downloaded_bytes', 0)
#             pct = downloaded / total if total > 0 else 0
#             speed = d.get('speed', 0)
#             speed_str = f"{speed / 1024 / 1024:.2f} MB/s" if speed else "N/A"
            
#             self.after(0, lambda: self.progress.set(pct))
#             self.after(0, lambda p=pct, s=speed_str: self.status.configure(
#                 text=f"Downloading... {p:.1%} | Speed: {s}",
#                 text_color=("gray10", "gray90")
#             ))
#         elif d['status'] == 'finished':
#             self.after(0, lambda: self.status.configure(
#                 text="Processing file...",
#                 text_color=("gray10", "gray90")
#             ))

# if __name__ == "__main__":
#     app = YouTubeDownloader()
#     app.mainloop()





import os
import sys
import threading
from tkinter import filedialog, messagebox
import customtkinter as ctk
import yt_dlp
import webbrowser
from PIL import Image

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class YouTubeDownloader(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Free Video Downloader - idrilogic")
        self.geometry("700x500")
        self.minsize(600, 500)
        self.resizable(True, True)
        
        try:
            if getattr(sys, 'frozen', False):
                icon_path = os.path.join(sys._MEIPASS, 'icon.ico')
            else:
                icon_path = 'icon.ico'
            
            if sys.platform.startswith('win'):
                self.iconbitmap(icon_path)
                self.after(201, lambda: self.iconbitmap(icon_path))
            else:
                from PIL import Image, ImageTk
                img = Image.open(icon_path)
                photo = ImageTk.PhotoImage(img)
                self.iconphoto(True, photo)
        except Exception as e:
            print(f"Could not load icon: {e}")

        self.main_frame = ctk.CTkScrollableFrame(self, fg_color="transparent")
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        title = ctk.CTkLabel(
            self.main_frame, 
            text="🎬 Free Video Downloader - تحميل الفيديوهات مجانًا",
            font=("Arial", 24, "bold")
        )
        title.pack(pady=(0, 20))
        
        brand = ctk.CTkLabel(
            self.main_frame,
            text="idrilogic",
            font=("Arial", 16, "bold"),
            text_color="#1f538d"
        )
        brand.pack(pady=(0, 10))
        
        self.supportButtonsFrame()
        
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

        helper_buttons_frame = ctk.CTkFrame(url_frame, fg_color="transparent")
        helper_buttons_frame.pack(fill="x", padx=15, pady=(0, 5))

        paste_helper_btn = ctk.CTkButton(
            helper_buttons_frame,
            text="📋 Paste URLs",
            command=self.paste_helper,
            width=100,
            height=28,
            font=("Arial", 10),
            fg_color=("gray70", "gray30"),
            hover_color=("#1f538d", "#14375e")
        )
        paste_helper_btn.pack(side="left", padx=(0, 5))

        copy_helper_btn = ctk.CTkButton(
            helper_buttons_frame,
            text="📄 Copy All",
            command=self.copy_helper,
            width=100,
            height=28,
            font=("Arial", 10),
            fg_color=("gray70", "gray30"),
            hover_color=("#1f538d", "#14375e")
        )
        copy_helper_btn.pack(side="left", padx=(0, 5))

        clear_helper_btn = ctk.CTkButton(
            helper_buttons_frame,
            text="🗑️ Clear",
            command=self.clear_helper,
            width=80,
            height=28,
            font=("Arial", 10),
            fg_color=("gray70", "gray30"),
            hover_color=("#8B0000", "#CC0000")
        )
        clear_helper_btn.pack(side="left")
        
        help_label = ctk.CTkLabel(
            url_frame,
            text="💡 Supports: Single videos, playlists, and multiple URLs",
            font=("Arial", 10),
            text_color="gray"
        )
        help_label.pack(anchor="w", padx=15, pady=(0, 10))
        
        options_frame = ctk.CTkFrame(self.main_frame)
        options_frame.pack(fill="x", pady=(0, 15))
        
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
        
        quality_container = ctk.CTkFrame(options_frame, fg_color="transparent")
        quality_container.pack(side="left", fill="both", expand=True, padx=15, pady=15)
        
        self.quality_label = ctk.CTkLabel(
            quality_container,
            text="Video Quality:",
            font=("Arial", 13, "bold")
        )
        self.quality_label.pack(anchor="w", pady=(0, 8))
        
        # FIX 3: default value matches the first option in the list
        self.quality_var = ctk.StringVar(value="Best Quality")
        self.quality_menu = ctk.CTkOptionMenu(
            quality_container,
            variable=self.quality_var,
            values=["Best Quality", "1080p", "720p", "480p", "360p", "240p", "144p"],
            font=("Arial", 11),
            width=150
        )
        self.quality_menu.pack(anchor="w")
        
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

        footer_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        footer_frame.pack(fill="x", pady=(15, 0))
     
        separator = ctk.CTkFrame(footer_frame, height=2, fg_color="gray")
        separator.pack(fill="x", pady=(0, 10))
        
        author_label = ctk.CTkLabel(
            footer_frame,
            text="Created by Mohammed El Idrissi Laoukili",
            font=("Arial", 10),
            text_color="gray"
        )
        author_label.pack(pady=(0, 8))

        self.socialButtonsFrame(footer_frame)


    def supportButtonsFrame(self):
        support_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        support_frame.pack(fill="x", pady=(10, 0))
        
        social_frame = ctk.CTkFrame(support_frame, fg_color="transparent")
        social_frame.pack()
        
        support_btn = ctk.CTkButton(
            social_frame,
            text="☕ Buy us a coffee — دعمك يهمنا",
            command=self.open_support,
            width=160,
            height=36,
            corner_radius=18,
            font=("Arial", 16, "bold"),
            fg_color="#CA6128",
            hover_color="#8D3A16",
            text_color="white",
            cursor="hand2"
        )
        support_btn.pack(side="left", padx=6, pady=12)

    def socialButtonsFrame(self, footer_frame):
        social_frame = ctk.CTkFrame(footer_frame, fg_color="transparent")
        social_frame.pack()

        website_btn = ctk.CTkButton(
            social_frame,
            text="🌐 الموقع — idricoding",
            command=self.open_idricodingdotcom,
            width=120,
            height=32,
            corner_radius=18,
            font=("Arial", 12, "bold"),
            fg_color="#DDDDDD",
            hover_color="#A1A1A1",
            text_color="#161616",
            cursor="hand2"
        )
        website_btn.pack(side="left", padx=6)

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
        
        github_btn = ctk.CTkButton(
            social_frame,
            text="💻 Github",
            command=self.open_github,
            width=120,
            height=32,
            font=("Arial", 11),
            fg_color="#000000",
            hover_color="#484848"
        )
        github_btn.pack(side="left", padx=5)
        
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

    def paste_helper(self):
        try:
            current_text = self.url_textbox.get("1.0", "end-1c")
            if current_text == "Paste YouTube URLs here (one per line for multiple videos)":
                self.url_textbox.delete("1.0", "end")
            clipboard_text = self.clipboard_get()
            self.url_textbox.insert("insert", clipboard_text)
        except:
            messagebox.showinfo("Info", "No text found in clipboard!")

    def copy_helper(self):
        try:
            all_text = self.url_textbox.get("1.0", "end-1c")
            if all_text and all_text != "Paste YouTube URLs here (one per line for multiple videos)":
                self.clipboard_clear()
                self.clipboard_append(all_text)
                messagebox.showinfo("Success", "URLs copied to clipboard!")
            else:
                messagebox.showinfo("Info", "No URLs to copy!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to copy: {e}")

    def clear_helper(self):
        self.url_textbox.delete("1.0", "end")
        self.url_textbox.insert("1.0", "Paste YouTube URLs here (one per line for multiple videos)")

    def open_support(self):
        webbrowser.open("https://www.paypal.com/ncp/payment/2KZ7WLGB24A6U")

    def open_idricodingdotcom(self):
        webbrowser.open("https://idricoding.vercel.app/")
        
    def open_youtube(self):
        webbrowser.open("https://www.youtube.com/channel/UCLfvN8mgGZMoySSVIWGSNTQ")
    
    def open_github(self):
        webbrowser.open("https://www.github.com/elidrissilaoukili")
    
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
        
        urls = [url.strip() for url in urls_text.split('\n') if url.strip()]
        
        blocked_urls = [url for url in urls if self.is_blocked_domain(url)]
        if blocked_urls:
            messagebox.showerror(
                "Blocked Content", 
                f"The following URL(s) contain blocked content and cannot be downloaded:\n\n" + 
                "\n".join(blocked_urls[:3]) + 
                ("\n..." if len(blocked_urls) > 3 else "")
            )
            return
        
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
        # FIX 4: also check common system paths so FFmpeg is found even if not
        # in the working directory
        for path in [os.getcwd(), "/usr/bin", "/usr/local/bin"]:
            if os.path.isfile(os.path.join(path, "ffmpeg")) or \
               os.path.isfile(os.path.join(path, "ffmpeg.exe")):
                return path
        return None  # Let yt-dlp search PATH itself

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
        elif quality == "240p":
            return 'bestvideo[height<=240][ext=mp4]+bestaudio[ext=m4a]/best[height<=240][ext=mp4]/best'
        elif quality == "144p":
            return 'bestvideo[height<=144][ext=mp4]+bestaudio[ext=m4a]/best[height<=144][ext=mp4]/best'
        return 'best'

    def is_blocked_domain(self, url):
        """Check if URL contains blocked adult domains"""
        blocked_domains = [
            'pornhub.com', 'xvideos.com', 'xnxx.com', 'xhamster.com',
            'redtube.com', 'youporn.com', 'tube8.com', 'spankbang.com',
            'eporner.com', 'motherless.com', 'txxx.com', 'porn.com',
            'sex.com', 'xxx.com', 'brazzers.com', 'bangbros.com',
            'realitykings.com', 'naughtyamerica.com', 'digitalplayground.com',
            'mofos.com', 'teamskeet.com', 'beeg.com', 'drtuber.com',
            'keezmovies.com', 'nuvid.com', 'sunporno.com', 'upornia.com',
            'yespornplease.com', 'anyporn.com', 'cam4.com', 'chaturbate.com',
            'myfreecams.com', 'livejasmin.com', 'stripchat.com', 'hanime.tv',
            'hentaihaven.xxx', 'nhentai.net', 'rule34.xxx', 'e-hentai.org',
            'exhentai.org', 'reddit.com/r/nsfw', 'reddit.com/r/porn',
            '4chan.org', '8kun.top',
        ]
        url_lower = url.lower()
        return any(domain in url_lower for domain in blocked_domains)

    def download_videos(self, urls, save_dir, format_type):
        try:
            ffmpeg_dir = self.get_ffmpeg_dir()
            
            ydl_opts = {
                'outtmpl': os.path.join(save_dir, '%(title)s.%(ext)s'),
                'progress_hooks': [self.update_progress],
                'quiet': True,
                'no_warnings': True,
                # FIX 2: use int comparison so checkbox 0/1 value is handled correctly
                'noplaylist': self.playlist_var.get() == 0,
                # FIX 1: removed age_limit filter that was blocking normal videos;
                # kept the domain blocklist in is_blocked_domain() instead
            }

            # Only set ffmpeg_location if we actually found it
            if ffmpeg_dir:
                ydl_opts['ffmpeg_location'] = ffmpeg_dir
            
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