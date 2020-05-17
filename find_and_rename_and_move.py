import os
import shutil
import time
import argparse


def copy_rename(src_file_path: str, output_dir) -> str:

    des_file_name = src_file_path.replace('/', '~')
    des_file_path = os.path.join(output_dir, des_file_name)
    shutil.copy(src_file_path, des_file_path)


def add_argument():
    parser = argparse.ArgumentParser(
        description="List all file paths in a folder")
    parser.add_argument("-i",
                        "--inputDir",
                        help="Path to the target folder(only absolute path is accepted)",
                        type=str)
    parser.add_argument("-o",
                        "--output",
                        help="Directory path that files will be saved", type=str)
    args = parser.parse_args()
    return args


def scanRecurse(baseDir):
    for entry in os.scandir(baseDir):
        if entry.is_file():
            yield os.path.join(baseDir, entry.name)
        else:
            yield from scanRecurse(entry.path)

def main():
    start_time = time.time()
    args = add_argument()
    dir_path = args.inputDir
    output_dir = args.output
    i = 1
    for path_file in scanRecurse(dir_path):
        copy_rename(path_file, output_dir)
        print(i, end='\r')
        i = i + 1
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    main()
