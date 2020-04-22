import os
import re
import argparse

def parse_arguments():
    """
    Takes in an argument defining a filepath.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--directory', required=True, help="""Path to the directory 
        you'd like to traverse.""")
    args = parser.parse_args()
    dir_path = args.directory
    return dir_path

def extension_regexp():
    """
    Defines a regular expression to match filename extensions.
    """
    # regular expression that matches a . followed by alpha characters, $ starts from end of string
    # important to remember that this regexp will match any number of cases in the string
    regexp = re.compile('(\.\w+)$')
    return regexp

def traverse(start_loc, regexp):
    """
    Traverses a file tree starting at start_loc. Tabulates information and prints information about
    filetree and files within.
    """
    total_file = 0
    total_jpeg = 0
    total_kb = 0
    for root_dir, directories, files in os.walk(start_loc):
        dir_file_count, dir_jpeg_count, dir_total_kb = examine_file_tree(root_dir, files, regexp)
        total_file += dir_file_count
        total_jpeg += dir_jpeg_count
        total_kb += dir_total_kb
    print_total_information(total_file, total_jpeg, total_kb)

def examine_file_tree(root_dir, filelist, regexp):
    """
    Iterates through a filelist. Tabulates information about each directory.
    """
    dir_file_count = 0
    dir_jpeg_count = 0
    dir_total_kb = 0
    for file in filelist:
        # os.sep translates to \ or / depending on the os and filesystem
        filepath = root_dir + str(os.sep) + file
        if os.path.isfile(filepath):
            extension, kb_filesize = get_file_information(filepath, regexp)
            dir_file_count += 1
        if extension == '.jpg':
            dir_jpeg_count += 1
        dir_total_kb += kb_filesize
    return dir_file_count, dir_jpeg_count, dir_total_kb
            

def get_file_information(filepath, regexp):
    """
    Examines a filepath to determine its extension and filesize.
    """
    kb_filesize = (os.path.getsize(filepath) / 10**3)
    extension = False
    # creates a boolean match object by searching the regexp against the filepath string
    match = re.search(regexp, filepath)
    if match:
        # only matches the first . followed by alpha characters (from end of string), i.e. the extension
        extension = match.group(0)
    print_file_information(filepath, kb_filesize, extension)
    return extension, kb_filesize

def print_file_information(filepath, kb_filesize, extension):
    """
    Pretty-prints information about an individual file.
    """
    print('filepath:', filepath)
    print('file size: ', end='')
    print(kb_filesize, 'KB')
    if extension:
        print('extension:', extension)
    if not extension:
        print('extension: file has no extension' )

def print_total_information(total_file, total_jpeg, total_kb):
    """
    Pretty-prints information about the traversed directory.
    """
    avg_file_size = (total_kb / total_file)
    print('\n*****************************')
    print('Number of file objects:', total_file)
    print('Number of .jpegs:', total_jpeg)
    print('Average file size:', avg_file_size, 'KB')

def main():
    dir_path = parse_arguments()
    regexp = extension_regexp()
    traverse(dir_path, regexp)

if __name__ == "__main__":
    main()

