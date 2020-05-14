import os
import time
import argparse





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

    parser.add_argument("-n", "--num", help="The number of file path in every file", default=10000, type=int)
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
    images_per_file = args.num
    output_dir = args.output
    i = 0
    for path_file in scanRecurse(dir_path):
        start = i // images_per_file
        file_path = os.path.join(output_dir, 'file_path_list_' + str(start) + '.txt')
        with open(file_path, 'a') as f:
            f.write("%s\n" % path_file)
        i = i + 1
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    main()

