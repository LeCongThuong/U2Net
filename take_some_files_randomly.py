import argparse
import time
import random
import os
from google.cloud import storage


def add_argument():
    parser = argparse.ArgumentParser(
        description="List all file paths in a folder")
    parser.add_argument("-i",
                        "--inputDir",
                        default=None,
                        help="Path to the target folder",
                        type=str)
    parser.add_argument("-o",
                        "--output",
                        help="Directory path that images will be saved", type=str)

    parser.add_argument("-nf", "--images_per_file", help="The number of image path in every file", default=10, type=int)
    parser.add_argument("-nd", "--files_in_destination_folder", help="The number of file in des folder", default=10, type=int)
    parser.add_argument("-b", "--bucket_name", help="name of image bucket", default=None, type=str)
    args = parser.parse_args()
    return args


def download_blob(bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    # bucket_name = "your-bucket-name"
    # source_blob_name = "storage-object-name"
    # destination_file_name = "local/path/to/file"

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)


def main():
    args = add_argument()
    dir_path = args.inputDir
    images_per_file = args.images_per_file
    files_in_folder = args.files_in_destination_folder
    output_dir = args.output
    bucket_name = args.bucket_name
    index_list = random.sample(range(124, 1275), files_in_folder)
    print(len(index_list))
    for index in index_list:
        file_name = 'file_path_list_{}.txt'.format(index)
        file_path = os.path.join(dir_path, file_name)
        print('\r File name: ', file_name, end='')
        with open(file_path, 'r') as file:
            n_line = [next(file) for x in range(images_per_file)]
        for line in n_line:
            file_name = line.split('/')[-1]
            des_filename = os.path.join(output_dir, file_name)
            download_blob(bucket_name, file_name, des_filename)


if __name__ == '__main__':
    main()