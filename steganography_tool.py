from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox
import os

def encode_message(img_path, message, output_path):
    image = Image.open(img_path)
    encoded = image.copy()
    width, height = image.size
    message += "###"  # Delimiter to signal end of message
    data = ''.join([format(ord(char), '08b') for char in message])

    if len(data) > width * height * 3:
        raise ValueError("Message is too long to encode in this image.")

    idx = 0
    for y in range(height):
        for x in range(width):
            pixel = list(image.getpixel((x, y)))
            for n in range(3):
                if idx < len(data):
                    pixel[n] = pixel[n] & ~1 | int(data[idx])
                    idx += 1
            encoded.putpixel((x, y), tuple(pixel))
    encoded.save(output_path)


def decode_message(img_path):
    image = Image.open(img_path)
    width, height = image.size

    bits = ""
    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            for n in range(3):
                bits += str(pixel[n] & 1)

    chars = [bits[i:i+8] for i in range(0, len(bits), 8)]
    message = ""
    for char in chars:
        message += chr(int(char, 2))
        if message.endswith("###"):
            break
    return message[:-3]


# GUI
class SteganographyApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Steganography Tool")
        self.master.geometry("400x300")

        self.label = tk.Label(master, text="Select an image and enter your message")
        self.label.pack(pady=5)

        self.choose_btn = tk.Button(master, text="Choose Image", command=self.choose_image)
        self.choose_btn.pack(pady=5)

        self.message_entry = tk.Entry(master, width=50)
        self.message_entry.pack(pady=5)

        self.encode_btn = tk.Button(master, text="Encode Message", command=self.encode)
        self.encode_btn.pack(pady=5)

        self.decode_btn = tk.Button(master, text="Decode Message", command=self.decode)
        self.decode_btn.pack(pady=5)

        self.image_path = ""

    def choose_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.bmp")])

    def encode(self):
        if not self.image_path:
            messagebox.showerror("Error", "No image selected.")
            return
        message = self.message_entry.get()
        if not message:
            messagebox.showerror("Error", "Message field is empty.")
            return
        output_path = filedialog.asksaveasfilename(defaultextension=".png")
        if output_path:
            try:
                encode_message(self.image_path, message, output_path)
                messagebox.showinfo("Success", f"Message encoded and saved to {output_path}")
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def decode(self):
        if not self.image_path:
            messagebox.showerror("Error", "No image selected.")
            return
        try:
            message = decode_message(self.image_path)
            messagebox.showinfo("Decoded Message", message)
        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == '__main__':
    root = tk.Tk()
    app = SteganographyApp(root)
    root.mainloop()