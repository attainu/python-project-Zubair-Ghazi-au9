# File Organizer

We all have drives full of random and un-organized files. Due to the large number of files, it is really a tough task to sit and organize each and every file. To make that task easy this Python script comes handy and all the files are organized in a well-manner within seconds.

## Libraries used in this Project

```python
import os
import shutil
import sys
import ntpath
```
## Functionality

### 1. Organize by extension

Using this option user can organize their files by their file extension then folders will be created according to their file type/extension and finally all folder will be moved to a parent folder (Organized)

### 2. Organize by size

Using this option user can organize their files by their file size then folders will be created according to their file size and finally all folder will moved to a parent folder (Organized)

### 3. Organize by alphabet

Using this option user can organize their files by their file names then folders will be created according to their first alphabet of files name and finally all folder will be moved to a parent folder (Organized)

## Usage

To run the command in CLI, you have to paste the fileorganizer.py file inside that folder where all the un-organized files are present and then open the CLI and pass these commands.

###### To organize with Extension

```bash
python fileorganizer.py ext
```

###### To organize with Size

```bash
python fileorganizer.py size
```

###### To organize with Alphabets

```bash
python fileorganizer.py alpha
```