import os
import customtkinter as ctk
from tkinter import filedialog
import tkinterdnd2 as tkdnd

# Initialize appearance
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")  # You can switch to 'dark-blue', 'green', etc.

class FileSizeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("✨ File Size Analyzer – Drag, Drop or Browse")
        self.root.geometry("750x550")
        self.root.configure(bg="#111827")

        # Title
        self.title_label = ctk.CTkLabel(root, text="📂 Drop or Browse a File", text_color="#93c5fd",
                                        font=("Segoe UI Black", 26))
        self.title_label.pack(pady=20)

        # Browse Button
        self.browse_btn = ctk.CTkButton(root, text="📁 Browse File", fg_color="#4f46e5", hover_color="#6366f1",
                                        text_color="white", font=("Arial", 16), command=self.browse_file)
        self.browse_btn.pack(pady=10)

        # Drop Zone
        self.drop_zone = ctk.CTkFrame(root, height=110, width=520, fg_color="#1f2937",
                                      border_color="#60a5fa", border_width=3, corner_radius=20)
        self.drop_zone.pack(pady=20)
        self.drop_label = ctk.CTkLabel(self.drop_zone, text="⬇️ Drag and drop your file here",
                                       text_color="#d1d5db", font=("Segoe UI", 17))
        self.drop_label.pack(pady=30)

        # Register drag-n-drop
        root.drop_target_register("*")
        root.dnd_bind("<<Drop>>", self.handle_drop)

        # File info
        self.file_label = ctk.CTkLabel(root, text="", wraplength=650, text_color="#f9fafb", font=("Arial", 14))
        self.file_label.pack(pady=10)

        # Result box
        self.result_box = ctk.CTkTextbox(root, height=140, font=("Consolas", 14), text_color="#f1f5f9",
                                         fg_color="#1e293b", scrollbar_button_color="#4f46e5")
        self.result_box.pack(padx=30, pady=10, fill="both", expand=False)

        # Footer
        self.footer = ctk.CTkLabel(root, text="🔎 Powered by Y7X 💗", font=("Arial Rounded MT Bold", 14),
                                   text_color="#a5b4fc")
        self.footer.pack(pady=10)

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
        file_path = event.data.strip('{}')  # Windows paths might be wrapped in {}
        if os.path.isfile(file_path):
            self.show_file_size(file_path)
        else:
            self.result_box.delete("0.0", "end")
            self.result_box.insert("0.0", "⚠️ Invalid file drop!")

# Launch
if __name__ == "__main__":
    dnd_root = tkdnd.TkinterDnD.Tk()
    app = FileSizeApp(dnd_root)
    dnd_root.mainloop()