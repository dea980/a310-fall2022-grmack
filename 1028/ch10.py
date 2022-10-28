import shutil
# Moving and renaming a file
# shutil.move('spam.txt', 'quizzes/moved.txt')

# Copying a file
# shutil.copy('spam.txt', 'quizzes/copied.txt')

# Delete a file
import os 
#os.unlink('spam.txt')
# Delete a directory
#os.rmdir('dirtodelete')

# Delete (to recycle bin/trash)
import send2trash
#send2trash.send2trash('spam.txt')

# os.walk()

# for folderName, subfolders, filenames in os.walk('delicious'):
#     print(f"The current folder is {folderName}")
#     for subfolder in subfolders:
#         print(f"Subfolder of {folderName}: {subfolder}")
#     for filename in filenames:
#         print(f"File inside: {folderName}: {filename}")
#     print()


import zipfile 
# Write to a zip file 

# new_zip_file = zipfile.ZipFile('new.zip', 'w')
# new_zip_file.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
# new_zip_file.close()

# Extracting from zip
# read_from_zip = zipfile.ZipFile('new.zip')
# read_from_zip.extractall()
# read_from_zip.close()

# Read a zip
exampleZip = zipfile.ZipFile('new.zip')
spamInfo = exampleZip.getinfo('spam.txt')
print(spamInfo.file_size) # 83 bytes (original)
print(spamInfo.compress_size) # 64 bytes (compressed)

# Project
# renaming files with MM-DD-YYYY to DD-MM-YYYY
import shutil
import os 
import re 

datePattern = re.compile(r"""^(.*?)  # all text before the date
    ((0|1)?\d)-                      # one or two digits for the month
    ((0|1|2|3)?\d)-                  # one or two digits for the day
    ((19|20)\d\d)                    # four digits for the year (must start with 19 or 20)
    (.*?)$                           # all text after the date
    """, re.VERBOSE)

for fileName in os.listdir('.'):
    mo = datePattern.search(fileName)
    if mo == None:
        continue 
    
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    newName = f"{beforePart}{dayPart}-{monthPart}-{yearPart}{afterPart}"

    absWorkingDir = os.path.abspath(".")
    amerFilename = os.path.join(absWorkingDir, fileName)
    euroFilename = os.path.join(absWorkingDir, newName)

    print(f"Renaming {amerFilename} to {euroFilename}")
    shutil.move(amerFilename, euroFilename)
