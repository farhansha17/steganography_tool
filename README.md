# 🕵️‍♂️ Steganography Tool

This Python GUI tool allows you to **hide secret messages inside images** and decode them later. It uses simple **LSB (Least Significant Bit)** steganography and supports `.png` and `.bmp` formats.

## 📸 Features

- Encode secret messages inside images  
- Decode hidden messages from encoded images  
- Simple and clean GUI using `Tkinter`  
- Works with `.png` and `.bmp` formats  
- Easy to use: just select, type, and encode!

## 🛠️ Requirements

- Python 3.x  
- [Pillow (PIL)](https://pypi.org/project/Pillow/)

Install Pillow with:

```bash
pip install pillow
```

## 🚀 How to Use

1. Clone or download this repository.
2. Run the script:

```bash
python steganography_tool.py
```

3. Click **Choose Image** to select a `.png` or `.bmp` file.
4. Type your message and click **Encode Message**.
5. To decode, choose an encoded image and click **Decode Message**.

## 📁 File Structure

```
steganography-tool/
├── steganography_tool.py
└── README.md
```

## 📷 Note

- Supports only `.png` or `.bmp` (non-lossy) formats for encoding.
- Message length is limited by the image size.
- Encoded images are saved separately to avoid overwriting.

## 👤 Author

- GitHub: [farhansha17](https://github.com/farhansha17)  
- Project: Steganography Tool  
- License: Not Applicable  

---

🧠 Hide your secrets in plain sight!
