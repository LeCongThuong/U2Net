error_line = "/content/U2Net/data/shopee_images~thoi_trang_nam~ao_thun~ao_ngan_tay_khong_co~1__2720029534__162268470~bbb74d7f1b03235ccb9aa2ffab87d64a.jpeg*[Errno 5] Input/output error: '/content/U2Net/u2net_output/shopee_images~thoi_trang_nam~ao_thun~ao_ngan_tay_khong_co~1__2720029534__162268470~bbb74d7f1b03235ccb9aa2ffab87d64a.npy'"

import glob


def main():

    # list error files in error_files_dir
    error_signal = '[Errno 5]'

    error_file_list = glob.glob("/home/love_you/Documents/Study/Thesis/clothes-detection/workspace/U-2-Net/error_files_dir/*.txt")
    # with each file using regex/find to catch [Errno 5] ==> this line is target 
    #catch this line => take path line => save to file
    result = []
    for error_file in error_file_list:
        print(error_file)
        with open(error_file, 'r') as f:
          content = f.readlines()
        for line in content:
            if error_signal in line:
                error_file_path = line.split('*')[0]
                result.append(error_file_path)

    with open('error_file_list_result.txt', 'w') as f:
        for item in result:
            f.write("%s\n" % item)


if __name__ == "__main__":
    main()