# 🗂️ File Organizer

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

A lightweight **Python script** that automatically sorts files in a directory into categorized subfolders based on their file extensions.

No more messy **Downloads** folder. 🎉

---

# ✨ Features

- 🧠 **Smart Categorization**  
  Automatically sorts files into folders like Images, Documents, Audio, Video, Archives, Code, and Others.

- 🔒 **Safe Operation**  
  Files are **only moved**, never deleted.

- ⚙️ **Customizable**  
  Easily add or remove file extensions using a simple dictionary.

- 💻 **CLI Friendly**  
  Organize any folder directly from the command line.

- ⚡ **Lightweight**  
  Pure Python with **zero external dependencies**.

---

# 📦 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/file-organizer.git
cd file-organizer
```

### 2️⃣ Ensure Python 3 is Installed

```bash
python --version
```

Expected output:

```
Python 3.x.x
```

✅ No additional packages required.

---

# 🚀 Usage

Run the script and specify the folder you want to organize:

```bash
python organizer.py "C:\Users\YourName\Downloads"
```

### Organize the Current Directory

If no path is provided, the script will organize the **current working directory**.

```bash
python organizer.py
```

---

# 📂 Example

### Before

```
Downloads/
├── holiday.jpg
├── report.pdf
├── song.mp3
├── script.py
└── archive.zip
```

### After

```
Downloads/
├── Images/
│   └── holiday.jpg
├── Documents/
│   └── report.pdf
├── Audio/
│   └── song.mp3
├── Code/
│   └── script.py
└── Archives/
    └── archive.zip
```

---

# ⚙️ Customization

You can modify which extensions belong to which category.

Open **`organizer.py`** and edit the `file_types` dictionary:

```python
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp'],
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx', '.md', '.odt'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac', '.ogg', '.m4a'],
    'Video': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv'],
    'Archives': ['.zip', '.tar', '.gz', '.rar', '.7z', '.bz2'],
    'Code': ['.py', '.js', '.html', '.css', '.cpp', '.java', '.sh', '.rb', '.php'],
    'Others': []
}
```

You can also:

- Add new categories
- Remove unwanted file types
- Create custom folder groups

The script will **automatically create folders** if they do not exist.

---

# 🤝 Contributing

Contributions are welcome!

1. **Fork the project**
2. Create your feature branch

```bash
git checkout -b feature/AmazingFeature
```

3. Commit your changes

```bash
git commit -m "Add some amazing feature"
```

4. Push to the branch

```bash
git push origin feature/AmazingFeature
```

5. Open a **Pull Request**

---

# 📄 License

Distributed under the **MIT License**.

See the `LICENSE` file for more information.

---

# ⭐ Support

If you find this project useful:

- Give it a **star ⭐ on GitHub**
- Share it with others
- Contribute improvements

It helps the project grow!
