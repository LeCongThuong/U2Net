import os
import time
start_time = time.time()

dir_path = '/home/love_you/Documents/Study/Mobile/test/'

def scanRecurse(baseDir):
    for entry in os.scandir(baseDir):
        if entry.is_file():
            yield os.path.join(baseDir,entry.name)
        else:
            yield from scanRecurse(entry.path)
images_per_file = 10000
end_number = 0
i = 0
for path_file in scanRecurse(dir_path):
    start = (i // images_per_file)*images_per_file
    end = start + images_per_file -1
    file_path = 'file_path_list_' + str(start)+ '_' + str(end) + '.txt'
    with open(file_path, 'a') as f:
        f.write("%s\n" % path_file)
    i = i + 1

print("--- %s seconds ---" % (time.time() - start_time))

