import os
import sys
import threading
import webbrowser
from tkinter import filedialog, messagebox
import customtkinter as ctk
from moviepy.video.io.VideoFileClip import VideoFileClip

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class VideoCompressor(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Video Compressor Pro - idrilogic")
        self.geometry("700x750")
        self.minsize(600, 500)
        self.resizable(True, True)
        
        # Main container with padding
        self.main_frame = ctk.CTkScrollableFrame(self, fg_color="transparent")
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Title
        title = ctk.CTkLabel(
            self.main_frame, 
            text="🎞️ Video Compressor Pro",
            font=("Arial", 24, "bold")
        )
        title.pack(pady=(0, 5))
        
        # Branding
        brand = ctk.CTkLabel(
            self.main_frame,
            text="idrilogic",
            font=("Arial", 16, "bold"),
            text_color="#1f538d"
        )
        brand.pack(pady=(0, 20))
        
        # Input file section
        input_frame = ctk.CTkFrame(self.main_frame)
        input_frame.pack(fill="x", pady=(0, 15))
        
        input_label = ctk.CTkLabel(
            input_frame,
            text="Input Video File:",
            font=("Arial", 14, "bold")
        )
        input_label.pack(anchor="w", padx=15, pady=(15, 8))
        
        file_select_frame = ctk.CTkFrame(input_frame, fg_color="transparent")
        file_select_frame.pack(fill="x", padx=15, pady=(0, 10))
        
        self.input_path = ctk.StringVar(value="No file selected")
        self.input_display = ctk.CTkEntry(
            file_select_frame,
            textvariable=self.input_path,
            font=("Arial", 10),
            state="readonly",
            height=35
        )
        self.input_display.pack(side="left", fill="x", expand=True, padx=(0, 10))
        
        self.browse_button = ctk.CTkButton(
            file_select_frame,
            text="Browse",
            command=self.select_input_file,
            width=100,
            height=35,
            font=("Arial", 11)
        )
        self.browse_button.pack(side="right")
        
        # File info display
        self.file_info = ctk.CTkLabel(
            input_frame,
            text="",
            font=("Arial", 10),
            text_color="gray"
        )
        self.file_info.pack(anchor="w", padx=15, pady=(0, 15))
        
        # Compression options section
        options_frame = ctk.CTkFrame(self.main_frame)
        options_frame.pack(fill="x", pady=(0, 15))
        
        options_label = ctk.CTkLabel(
            options_frame,
            text="Compression Settings:",
            font=("Arial", 14, "bold")
        )
        options_label.pack(anchor="w", padx=15, pady=(15, 10))
        
        # Compression method
        method_frame = ctk.CTkFrame(options_frame, fg_color="transparent")
        method_frame.pack(fill="x", padx=15, pady=(0, 15))
        
        method_label = ctk.CTkLabel(
            method_frame,
            text="Compression Method:",
            font=("Arial", 12, "bold")
        )
        method_label.pack(anchor="w", pady=(0, 8))
        
        self.method_var = ctk.StringVar(value="target_size")
        
        method_radio_frame = ctk.CTkFrame(method_frame, fg_color="transparent")
        method_radio_frame.pack(anchor="w")
        
        self.target_size_radio = ctk.CTkRadioButton(
            method_radio_frame,
            text="Target File Size",
            variable=self.method_var,
            value="target_size",
            font=("Arial", 11),
            command=self.toggle_compression_method
        )
        self.target_size_radio.pack(anchor="w", pady=2)
        
        self.quality_radio = ctk.CTkRadioButton(
            method_radio_frame,
            text="Quality/Resolution Based",
            variable=self.method_var,
            value="quality",
            font=("Arial", 11),
            command=self.toggle_compression_method
        )
        self.quality_radio.pack(anchor="w", pady=2)
        
        # Target size controls
        self.target_size_frame = ctk.CTkFrame(options_frame, fg_color="transparent")
        self.target_size_frame.pack(fill="x", padx=15, pady=(0, 15))
        
        target_size_label = ctk.CTkLabel(
            self.target_size_frame,
            text="Target Size (MB):",
            font=("Arial", 12, "bold")
        )
        target_size_label.pack(anchor="w", pady=(0, 8))
        
        target_input_frame = ctk.CTkFrame(self.target_size_frame, fg_color="transparent")
        target_input_frame.pack(anchor="w")
        
        self.target_size_var = ctk.StringVar(value="10")
        self.target_size_entry = ctk.CTkEntry(
            target_input_frame,
            textvariable=self.target_size_var,
            width=100,
            height=35,
            font=("Arial", 12)
        )
        self.target_size_entry.pack(side="left", padx=(0, 10))
        
        size_info = ctk.CTkLabel(
            target_input_frame,
            text="Enter desired file size in megabytes",
            font=("Arial", 10),
            text_color="gray"
        )
        size_info.pack(side="left")
        
        # Quality controls (hidden by default)
        self.quality_frame = ctk.CTkFrame(options_frame, fg_color="transparent")
        
        quality_label = ctk.CTkLabel(
            self.quality_frame,
            text="Video Quality (CRF):",
            font=("Arial", 12, "bold")
        )
        quality_label.pack(anchor="w", pady=(0, 8))
        
        quality_input_frame = ctk.CTkFrame(self.quality_frame, fg_color="transparent")
        quality_input_frame.pack(anchor="w", pady=(0, 10))
        
        self.crf_slider = ctk.CTkSlider(
            quality_input_frame,
            from_=18,
            to=28,
            number_of_steps=10,
            width=200
        )
        self.crf_slider.set(23)
        self.crf_slider.pack(side="left", padx=(0, 10))
        
        self.crf_value_label = ctk.CTkLabel(
            quality_input_frame,
            text="23 (Balanced)",
            font=("Arial", 11)
        )
        self.crf_value_label.pack(side="left")
        
        self.crf_slider.configure(command=self.update_crf_label)
        
        crf_info = ctk.CTkLabel(
            self.quality_frame,
            text="Lower = Better Quality (larger file) | Higher = Smaller File (lower quality)",
            font=("Arial", 9),
            text_color="gray"
        )
        crf_info.pack(anchor="w", pady=(0, 10))
        
        # Resolution scale
        scale_label = ctk.CTkLabel(
            self.quality_frame,
            text="Resolution Scale:",
            font=("Arial", 12, "bold")
        )
        scale_label.pack(anchor="w", pady=(0, 8))
        
        self.scale_var = ctk.StringVar(value="1.0")
        self.scale_menu = ctk.CTkOptionMenu(
            self.quality_frame,
            variable=self.scale_var,
            values=["1.0 (Original)", "0.75 (75%)", "0.5 (50%)", "0.25 (25%)"],
            font=("Arial", 11),
            width=200
        )
        self.scale_menu.pack(anchor="w")
        
        # Output location section
        output_frame = ctk.CTkFrame(self.main_frame)
        output_frame.pack(fill="x", pady=(0, 15))
        
        output_label = ctk.CTkLabel(
            output_frame,
            text="Output Location:",
            font=("Arial", 13, "bold")
        )
        output_label.pack(anchor="w", padx=15, pady=(15, 8))
        
        output_select_frame = ctk.CTkFrame(output_frame, fg_color="transparent")
        output_select_frame.pack(fill="x", padx=15, pady=(0, 15))
        
        self.output_path = ctk.StringVar(value=os.path.expanduser("~/Downloads"))
        self.output_display = ctk.CTkEntry(
            output_select_frame,
            textvariable=self.output_path,
            font=("Arial", 10),
            state="readonly",
            height=35
        )
        self.output_display.pack(side="left", fill="x", expand=True, padx=(0, 10))
        
        self.output_button = ctk.CTkButton(
            output_select_frame,
            text="Browse",
            command=self.select_output_folder,
            width=100,
            height=35,
            font=("Arial", 11)
        )
        self.output_button.pack(side="right")
        
        # Compress button
        self.compress_btn = ctk.CTkButton(
            self.main_frame,
            text="🗜️ Compress Video",
            command=self.start_compression,
            height=45,
            font=("Arial", 16, "bold"),
            fg_color="#1f538d",
            hover_color="#14375e"
        )
        self.compress_btn.pack(fill="x", pady=(0, 15))
        
        # Progress section
        progress_frame = ctk.CTkFrame(self.main_frame)
        progress_frame.pack(fill="x", pady=(0, 0))
        
        self.progress = ctk.CTkProgressBar(progress_frame, height=20)
        self.progress.set(0)
        self.progress.pack(fill="x", padx=15, pady=(15, 10))
        
        self.status = ctk.CTkLabel(
            progress_frame,
            text="Ready to compress",
            font=("Arial", 11),
            text_color="gray"
        )
        self.status.pack(padx=15, pady=(0, 15))
        
        self.compressing = False
        self.selected_file = None
        
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

    def toggle_compression_method(self):
        if self.method_var.get() == "target_size":
            self.target_size_frame.pack(fill="x", padx=15, pady=(0, 15))
            self.quality_frame.pack_forget()
        else:
            self.target_size_frame.pack_forget()
            self.quality_frame.pack(fill="x", padx=15, pady=(0, 15))

    def update_crf_label(self, value):
        crf = int(float(value))
        if crf <= 20:
            quality = "High Quality"
        elif crf <= 24:
            quality = "Balanced"
        else:
            quality = "Smaller Size"
        self.crf_value_label.configure(text=f"{crf} ({quality})")

    def select_input_file(self):
        file_path = filedialog.askopenfilename(
            title="Select Video File",
            filetypes=[
                ("Video Files", "*.mp4 *.avi *.mov *.mkv *.flv *.wmv *.webm"),
                ("All Files", "*.*")
            ]
        )
        if file_path:
            self.selected_file = file_path
            self.input_path.set(file_path)
            
            # Display file info
            file_size = os.path.getsize(file_path) / (1024 * 1024)
            self.file_info.configure(
                text=f"📁 File size: {file_size:.2f} MB",
                text_color=("gray10", "gray90")
            )

    def select_output_folder(self):
        folder = filedialog.askdirectory(title="Select Output Folder")
        if folder:
            self.output_path.set(folder)

    def start_compression(self):
        if self.compressing:
            messagebox.showwarning("Warning", "Compression already in progress!")
            return
        
        if not self.selected_file:
            messagebox.showerror("Error", "Please select an input video file!")
            return
        
        # Validate target size
        if self.method_var.get() == "target_size":
            try:
                target_size = float(self.target_size_var.get())
                if target_size <= 0:
                    messagebox.showerror("Error", "Target size must be greater than 0!")
                    return
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid target size!")
                return
        
        self.compressing = True
        self.compress_btn.configure(state="disabled", text="Compressing...")
        self.progress.set(0)
        self.status.configure(text="Starting compression...")
        
        thread = threading.Thread(target=self.compress_video)
        thread.daemon = True
        thread.start()

    def compress_video(self):
        try:
            input_file = self.selected_file
            output_folder = self.output_path.get()
            
            # Generate output filename
            base_name = os.path.splitext(os.path.basename(input_file))[0]
            output_file = os.path.join(output_folder, f"{base_name}_compressed.mp4")
            
            # Make sure output file doesn't overwrite
            counter = 1
            while os.path.exists(output_file):
                output_file = os.path.join(output_folder, f"{base_name}_compressed_{counter}.mp4")
                counter += 1
            
            self.after(0, lambda: self.status.configure(
                text="Loading video...",
                text_color=("gray10", "gray90")
            ))
            
            # Load video
            clip = VideoFileClip(input_file)
            duration = clip.duration
            
            if self.method_var.get() == "target_size":
                # Target size method
                target_size_mb = float(self.target_size_var.get())
                target_size_kb = target_size_mb * 1024
                bitrate = int((target_size_kb * 8) / duration)
                bitrate = max(bitrate, 500)  # Minimum 500 kbps
                
                self.after(0, lambda: self.status.configure(
                    text=f"Compressing to {target_size_mb} MB (bitrate: {bitrate} kbps)...",
                    text_color=("gray10", "gray90")
                ))
                
                self.after(0, lambda: self.progress.set(0.3))
                
                clip.write_videofile(
                    output_file,
                    bitrate=f"{bitrate}k",
                    audio_bitrate="128k",
                    codec="libx264",
                    audio_codec="aac",
                    logger=None
                )
            else:
                # Quality/resolution method
                crf = int(self.crf_slider.get())
                scale_value = float(self.scale_var.get().split()[0])
                
                self.after(0, lambda: self.status.configure(
                    text=f"Compressing with CRF {crf}, scale {scale_value}...",
                    text_color=("gray10", "gray90")
                ))
                
                self.after(0, lambda: self.progress.set(0.3))
                
                # Resize if needed
                if scale_value < 1.0:
                    clip = clip.resize(scale_value)
                
                clip.write_videofile(
                    output_file,
                    codec="libx264",
                    audio_codec="aac",
                    bitrate=None,
                    preset='medium',
                    ffmpeg_params=['-crf', str(crf)],
                    logger=None
                )
            
            self.after(0, lambda: self.progress.set(0.9))
            
            # Calculate results
            original_size = os.path.getsize(input_file) / (1024 * 1024)
            compressed_size = os.path.getsize(output_file) / (1024 * 1024)
            reduction = (1 - compressed_size / original_size) * 100
            
            clip.close()
            
            self.after(0, lambda: self.progress.set(1))
            self.after(0, lambda: self.status.configure(
                text=f"✅ Complete! {original_size:.2f} MB → {compressed_size:.2f} MB ({reduction:.1f}% reduction)",
                text_color="green"
            ))
            
            messagebox.showinfo(
                "Success",
                f"Video compressed successfully!\n\n"
                f"Original: {original_size:.2f} MB\n"
                f"Compressed: {compressed_size:.2f} MB\n"
                f"Reduction: {reduction:.1f}%\n\n"
                f"Saved to: {output_file}"
            )
            
        except Exception as e:
            error_msg = str(e)
            self.after(0, lambda: self.status.configure(
                text=f"❌ Error: {error_msg[:50]}...",
                text_color="red"
            ))
            messagebox.showerror("Error", f"Compression failed:\n{error_msg}")
        finally:
            self.compressing = False
            self.after(0, lambda: self.compress_btn.configure(
                state="normal",
                text="🗜️ Compress Video"
            ))

if __name__ == "__main__":
    app = VideoCompressor()
    app.mainloop()