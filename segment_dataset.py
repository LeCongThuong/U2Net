import os


def run_segment(path_to_bucket, start, end, colab_num):
    indicator_file_name = str(colab_num)+'_seg_indicatior_file.txt'
    output_dir_path = os.path.join(path_to_bucket, 'output_numpy_dir')
    indicator_file= os.path.join(path_to_bucket, indicator_file_name)
    try:
        with open(indicator_file, 'r') as ind_file:
                start = int(ind_file.read())
    except Exception:
        print(Exception)
        print("This exception happens because the indication file is initialized")
        with open(indicator_file, 'w') as ind_file:
            ind_file.write(str(start))


    for i in range(start, end+ 1):
        name_file = 'file_list_dir/file_path_list_' + str(i) + '.txt'
        file_list_path = os.path.join(path_to_bucket, name_file)
        !python3 u2net_test.py --input {file_list_path} --output_dir {output_dir_path}
        with open(indicator_file, 'w') as ind_file:
                ind_file.write(str(i))



