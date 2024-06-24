import os
import shutil

OriginRoute = 'C:/Users/User/Downloads'
extension_folders = {
    '.jpeg': 'JPEGs',
    '.png': 'PNGs',
    '.pdf': 'PDFs'
}
    

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
        return True 
    except OSError:
        print('Error: Creating directory ' + directory)
        return False
    
def moveFile(file,src, dest): 
    try:
        createFolder(dest)
        shutil.move(src, dest)
        return True
    except OSError:
        print('Error: Moving file ' + file)
        return False


def main():
    files = os.listdir(OriginRoute) 
    moved_files = []
    for file in files:
        file_validation = file.lower()
        file_extension = os.path.splitext(file_validation)[1]

        if file_extension not in extension_folders:
            print(file_extension, 'Extension is not in the list')
            continue

        src = os.path.join(OriginRoute, file) 
        dest = os.path.join(OriginRoute, extension_folders[file_extension])

        if moveFile(file, src, dest):
            moved_files.append(file)

    files_moved = len(moved_files)

    return f'{files_moved} files have been moved'


if __name__ == "__main__":
    result = main()
    print(result) 
