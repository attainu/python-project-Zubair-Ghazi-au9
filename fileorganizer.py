import os
import shutil

DIRECTORIES = {
    "HTML": [".html5", ".html", ".htm", ".xhtml"],
    "Images": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
               ".heif", ".psd", ".jfif"
               ],
    "File": ["File"],
    "Videos": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
               ".qt", ".mpg", ".mpeg", ".3gp"
               ],
    "Documents": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                  ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                  ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                  "pptx"
                  ],
    "Archives": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                 ".dmg", ".rar", ".xar", ".zip"
                 ],
    "Audio": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"
              ],
    "Plaintext": [".txt", ".in", ".out"],
    "Pdf": [".pdf"],
    "Python": [".py"],
    "XML": [".xml"],
    "Exe": [".exe"],
    "Shell": [".sh"],
    "JS": [".js"],
    "Torrent": [".torrent"],
    "Json": [".json"]
}
FILE_FORMATS = {file_format: directory
                for directory, file_formats in DIRECTORIES.items()
                for file_format in file_formats}


def _folder(file_path, parent_folder, folder, each_file):
    if not os.path.exists(folder):
        os.mkdir(folder)
    shutil.copy2(file_path, folder)
    destination = os.path.join(folder, each_file)
    if os.path.exists(destination):
        os.remove(file_path)


def organize_ext():
    input_file_path = os.getcwd()
    for each_file in os.scandir():
        if not each_file.is_dir():
            file_path = os.path.abspath(each_file)
            file_extension = os.path.splitext(file_path)[1].lower()
            if file_extension in FILE_FORMATS:
                parent_folder = os.path.join(input_file_path, "Organized")
                if not os.path.exists(parent_folder):
                    os.mkdir(parent_folder)
                folder = os.path.join(parent_folder,
                                      FILE_FORMATS[file_extension])
                _folder(file_path, parent_folder, folder, each_file)


def organize_size():
    input_file_path = os.getcwd()
    for each_file in os.scandir():
        if not each_file.is_dir():
            file_path = os.path.abspath(each_file)
            size = os.stat(each_file).st_size
            parent_folder = os.path.join(input_file_path, "Organized")
            if not os.path.exists(parent_folder):
                os.mkdir(parent_folder)

            if 0 <= size < 1000:
                folder = os.path.join(parent_folder, "Bytes")
                _folder(file_path, parent_folder, folder, each_file)

            elif 1000 < size < 1000000:
                folder = os.path.join(parent_folder, "KB")
                _folder(file_path, parent_folder, folder, each_file)

            elif 1000000 < size < 100000000:
                folder = os.path.join(parent_folder, "100 MB")
                _folder(file_path, parent_folder, folder, each_file)

            elif 100000000 < size < 500000000:
                folder = os.path.join(parent_folder, "500 MB")
                _folder(file_path, parent_folder, folder, each_file)

            elif size > 1000000000:
                folder = os.path.join(parent_folder, "GB")
                _folder(file_path, parent_folder, folder, each_file)


if __name__ == "__main__":
    organize_size()
