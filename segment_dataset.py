import os

def run_segment(path_to_bucket, output_dir_path, start, end, colab_num, log_error_folder_path):
    error_file_path = os.path.join(log_error_folder_path, str(colab_num) + 'error_file.txt')
    indicator_file_name = 'indicator_file_dir/segmentation/' + str(colab_num)+'_seg_indicator_file.txt'
    indicator_file= os.path.join(path_to_bucket, indicator_file_name)
    try:
        with open(indicator_file, 'r') as ind_file:
                start = int(ind_file.read()) + 1
    except Exception as ex:
        print(ex)
        print("This exception happens because the indication file is initialized")


    for i in range(start, end+ 1):
        name_file = 'image_name_files_dir/file_path_list_' + str(i) + '.txt'
        file_list_path = os.path.join(path_to_bucket, name_file)
        !python3 u2net_test.py --input {file_list_path} --output_dir {output_dir_path} --errorFile {error_file_path}
        with open(indicator_file, 'w') as ind_file:
                ind_file.write(str(i))





