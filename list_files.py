import os
import time
import argparse
from google.cloud import storage


def add_argument():
    parser = argparse.ArgumentParser(
        description="List all file paths in a folder")
    parser.add_argument("-i",
                        "--inputDir",
                        default=None,
                        help="Path to the target folder(only absolute path is accepted, None if using for cloud)",
                        type=str)
    parser.add_argument("-o",
                        "--output",
                        help="Directory path that files will be saved", type=str)

    parser.add_argument("-n", "--num", help="The number of file path in every file", default=10000, type=int)
    parser.add_argument("-m", "--mode",
                        help="mode indicate where you want to list file: local mode: local, cloud mode: cloud storage ",
                        default='local',
                        type=str)
    parser.add_argument("-b", "--bucket_name", help="name of bucket that you want to list file if mode cloud is chosen", default=None, type=str)
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
    mode = args.mode
    if mode == 'local':
        if dir_path is None:
            raise Exception("You have not give input dir yet")
        i = 0
        for path_file in scanRecurse(dir_path):
            start = i // images_per_file
            file_path = os.path.join(output_dir, 'file_path_list_' + str(start) + '.txt')
            with open(file_path, 'a') as f:
                f.write("%s\n" % path_file)
            i = i + 1
    else:
        bucket_name = args.bucket_name
        if bucket_name == None:
            raise Exception("Bucket name can not be None")
        else:
            file_index = 0
            storage_client = storage.Client()
            print("Start to list files in bucket:")
            start_time = time.time()
            blobs = storage_client.list_blobs(bucket_name)
            print("--- %s seconds for list files in bucket ---" % (time.time() - start_time))
            file_path = os.path.join(output_dir, 'file_path_list_' + str(file_index) + '.txt')
            try:
                num_of_blob = 0
                for blob in blobs:
                    print('\rBob name: ', blob, end='')
                    with open(file_path, 'a+') as f:
                        image_path = str(blob.name)
                        f.write("%s\n" % image_path)
                    num_of_blob = num_of_blob + 1
                    if num_of_blob == images_per_file:
                        file_index = file_index + 1
                        print('\rFile index: ', file_index, end='')
                        file_path = os.path.join(output_dir, 'file_path_list_' + str(file_index) + '.txt')
                        num_of_blob = 0
            except Exception as ex:
                print("file_index: ", file_index)

    print("--- %s Total seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    main()

