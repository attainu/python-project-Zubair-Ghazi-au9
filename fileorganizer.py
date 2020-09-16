import os
import shutil

DIRECTORIES = {
    "HTML": [".html5", ".html", ".htm", ".xhtml"],
    "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
               ".heif", ".psd", ".jfif"
               ],
    "FILE": ["File"],
    "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
               ".qt", ".mpg", ".mpeg", ".3gp"
               ],
    "DOCUMENTS": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                  ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                  ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                  "pptx"
                  ],
    "ARCHIVES": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                 ".dmg", ".rar", ".xar", ".zip"
                 ],
    "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"
              ],
    "PLAINTEXT": [".txt", ".in", ".out"],
    "PDF": [".pdf"],
    "PYTHON": [".py"],
    "XML": [".xml"],
    "EXE": [".exe"],
    "SHELL": [".sh"],
    "JS": ["javaScript File"],
    "torrent": ["TORRENT File"],
    "JSON": ["JSON File"]
}
FILE_FORMATS = {file_format: directory
                for directory, file_formats in DIRECTORIES.items()
                for file_format in file_formats}


def organize_by_ext():
    input_file_path = os.getcwd()
    for each_file in os.scandir():
        if not each_file.is_dir():
            file_path = os.path.abspath(each_file)
            file_extension = os.path.abspath(file_path)[1].lower()
            if file_extension in FILE_FORMATS:
                parent_folder = os.path.join(input_file_path, "Organized")
                if not os.path.exists(parent_folder):
                    os.mkdir(parent_folder)
                folder = os.path.join(parent_folder,
                                      FILE_FORMATS[file_extension])
                if not os.path.exists(folder):
                    os.mkdir(folder)
                shutil.copy2(file_path, folder)
                destination = os.path.join(folder, each_file)
                if os.path.exists(destination):
                    os.remove(file_path)


if __name__ == "__main__":
    organize_by_ext()
