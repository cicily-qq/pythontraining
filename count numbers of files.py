import os

all_files=os.listdir(os.curdir)
type_dict=dict()

for each_file in all_files:
    if os.path.isdir(each_file):
        type_dict.setdefault('文件夹',0)
        type_dict['文件夹']+=1

    else:
        ext=os.path.splitext(each_file)[1]
        type_dict.setdefault(ext,0)
        tepe_dict[ext]+=1


for each_type in type_dict.keys():
    print('该文件夹下[%s]的文件夹【%d】个',%(each_type,type_dict[each_type]))
