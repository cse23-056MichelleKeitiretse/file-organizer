# 🗂️ File Organizer

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

A lightweight Python script that automatically sorts files in a specified directory into categorized subfolders based on their file extensions. No more messy downloads folder!



## ✨ Features

- **Smart Categorization** – Sorts files into predefined folders: Images, Documents, Audio, Video, Archives, Code, and Others.
- **Safe Operation** – Only moves files; never deletes anything.
- **Customizable** – Easily add or remove file extensions by editing a simple dictionary.
- **CLI Friendly** – Provide a target folder as a command-line argument, or let it organize the current directory.
- **Lightweight** – Pure Python, no external dependencies.

## 📦 Installation

1. **Clone the repository** (or download the script directly):
   ```bash
   git clone https://github.com/yourusername/file-organizer.git
   cd file-organizer
Ensure Python 3 is installed:

bash
python --version   # Should be 3.x
That's it – no additional packages required.

🚀 Usage
Run the script from the terminal, specifying the folder you want to organize:

bash
python organizer.py "C:\Users\YourName\Downloads"
If you omit the folder path, it will organize the current working directory:

bash
python organizer.py
Example
Before:

text
Downloads/
  ├── holiday.jpg
  ├── report.pdf
  ├── song.mp3
  ├── script.py
  └── archive.zip
After running:

text
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
⚙️ Customization
You can easily change which file extensions belong to which category. Open organizer.py and locate the file_types dictionary:

python
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp'],
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx', '.md', '.odt'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac', '.ogg', '.m4a'],
    'Video': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv'],
    'Archives': ['.zip', '.tar', '.gz', '.rar', '.7z', '.bz2'],
    'Code': ['.py', '.js', '.html', '.css', '.cpp', '.java', '.sh', '.rb', '.php'],
    'Others': []  # everything else
}
Add or remove extensions, or even create new categories. The script will automatically create the necessary folders.

🤝 Contributing
Contributions, issues, and feature requests are welcome!
Feel free to check the issues page.

Fork the project

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some amazing feature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

📄 License
Distributed under the MIT License. See LICENSE for more information.

☕ Support
If you find this project useful, consider giving it a ⭐ on GitHub – it helps others discover it!
