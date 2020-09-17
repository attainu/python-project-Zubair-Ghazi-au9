import os
import datetime

input_file_path = os.getcwd()
for each_file in os.scandir():
    if not each_file.is_dir():
        file_path = os.path.abspath(each_file)
        mtime = os.stat(each_file).st_mtime
        timestamp_str = datetime.datetime.fromtimestamp(mtime).strftime('%Y-%m-%d-%H:%M')
        # time=(int(_time))
        # day = time // (24 * 3600)
        # print(day)
print(timestamp_str)
