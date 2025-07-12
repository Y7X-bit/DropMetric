import os
import customtkinter as ctk
from tkinter import filedialog
import tkinterdnd2 as tkdnd

# AMOLED + Red styling (visually), but no text mentions
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class DropMetricApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📦 DropMetric")
        self.root.geometry("760x580")
        self.root.configure(bg="#000000")

        self.title_label = ctk.CTkLabel(root, text="📂 Drop or Browse a File", text_color="#ff0000",
                                        font=("Segoe UI Black", 26))
        self.title_label.pack(pady=20)

        self.browse_btn = ctk.CTkButton(root, text="📁 Browse File", fg_color="#ff0000", hover_color="#cc0000",
                                        text_color="white", font=("Arial", 16), command=self.browse_file,
                                        corner_radius=30)
        self.browse_btn.pack(pady=10)

        self.drop_zone = ctk.CTkFrame(root, height=110, width=540, fg_color="#000000",
                                      border_color="#ff0000", border_width=3, corner_radius=32)
        self.drop_zone.pack(pady=20)
        self.drop_label = ctk.CTkLabel(self.drop_zone, text="⬇️ Drag and drop your file here",
                                       text_color="#ffffff", font=("Segoe UI", 17))
        self.drop_label.pack(pady=30)

        root.drop_target_register("*")
        root.dnd_bind("<<Drop>>", self.handle_drop)

        self.file_label = ctk.CTkLabel(root, text="", wraplength=680, text_color="#ff0000", font=("Arial", 14))
        self.file_label.pack(pady=10)

        self.result_box = ctk.CTkTextbox(root, height=150, font=("Consolas", 14),
                                         text_color="#ffffff", fg_color="#000000",
                                         border_color="#ff0000", border_width=2,
                                         scrollbar_button_color="#ff0000", corner_radius=24)
        self.result_box.pack(padx=30, pady=10, fill="both", expand=False)

        footer_frame = ctk.CTkFrame(root, fg_color="#000000", corner_radius=20)
        footer_frame.pack(pady=10)
        self.footer = ctk.CTkLabel(footer_frame, text="🔎 Powered by Y7X 💗",
                                   font=("Arial Rounded MT Bold", 14),
                                   text_color="#ff0000")
        self.footer.pack(padx=20, pady=6)

    def show_file_size(self, file_path):
        try:
            size = os.stat(file_path).st_size
            kb = size / 1024
            mb = kb / 1024
            result = (
                f"📁 File Path:\n{file_path}\n\n"
                f"📏 File Size:\n"
                f"• Bytes     : {size}\n"
                f"• Kilobytes : {kb:.2f} KB\n"
                f"• Megabytes : {mb:.2f} MB\n"
            )
            self.file_label.configure(text=f"✅ File Loaded:\n{file_path}")
            self.result_box.delete("0.0", "end")
            self.result_box.insert("0.0", result)
        except Exception as e:
            self.result_box.delete("0.0", "end")
            self.result_box.insert("0.0", f"❌ Error: {e}")

    def browse_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.show_file_size(file_path)

    def handle_drop(self, event):
        file_path = event.data.strip('{}')
        if os.path.isfile(file_path):
            self.show_file_size(file_path)
        else:
            self.result_box.delete("0.0", "end")
            self.result_box.insert("0.0", "⚠️ Invalid file drop!")

# 🚀 Launch App
if __name__ == "__main__":
    dnd_root = tkdnd.TkinterDnD.Tk()
    app = DropMetricApp(dnd_root)
    dnd_root.mainloop()