import os
import shutil
import sys
import ntpath

DIRECTORIES = {
    "HTML": [".html5", ".html", ".htm", ".xhtml"],
    "Images": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
               ".heif", ".psd", ".jfif"
               ],
    "File": ["File"],
    "Videos": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
               ".qt", ".mpg", ".mpeg", ".3gp", ".mkv"
               ],
    "Documents": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                  ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                  ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                  "pptx", ".md", ".csv"
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


def crt_dir(file_path, folder, each_file):
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
                crt_dir(file_path, folder, each_file)


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
                crt_dir(file_path, folder, each_file)
            elif 1000 < size < 1000000:
                folder = os.path.join(parent_folder, "KB")
                crt_dir(file_path, folder, each_file)
            elif 1000000 < size < 100000000:
                folder = os.path.join(parent_folder, "100 MB")
                crt_dir(file_path, folder, each_file)
            elif 100000000 < size < 500000000:
                folder = os.path.join(parent_folder, "500 MB")
                crt_dir(file_path, folder, each_file)
            elif size > 1000000000:
                folder = os.path.join(parent_folder, "GB")
                crt_dir(file_path, folder, each_file)


def organize_alphabet():
    input_file_path = os.getcwd()
    for each_file in os.scandir():
        if not each_file.is_dir():
            file_path = os.path.abspath(each_file)
            parent_folder = os.path.join(input_file_path, "Organized")
            if not os.path.exists(parent_folder):
                os.mkdir(parent_folder)
            _, tail = ntpath.split(file_path)
            alpha = tail[0].upper()
            folder = os.path.join(parent_folder, alpha)
            crt_dir(file_path, folder, each_file)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        organize_ext()
    elif len(sys.argv) == 2:
        Organize = sys.argv[1]
        if Organize == "ext":
            organize_ext()
        elif Organize == "size":
            organize_size()
        elif Organize == "alpha":
            organize_alphabet()
        else:
            print("Give input from these three options ext, size or alpha")
