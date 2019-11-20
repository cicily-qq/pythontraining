def file_view(file_name, line_num):
    if line_num.strip()==':':
        begin='1'
        end='-1'

    (begin,end)=line_num.split(':')
    if begin=='':
        begin='1'
    if end=='':
        end='-1'

    if begin=='1' and end=='-1':
        prompt='的全文'

    elif begin=='1':
        prompt='从开始到%s' %end

    elif end=='-1':
        prompt='%s到结束'%begin

    else:
        prompt='从%s行到%s行',%(begin,end)

    print('\n文件%s%s的内容如下:\n' %(file_name,prompt))
    
    begin=int(begin)-1
    end=int(end)
    lines=end-begin

    
    f=open(file_name)

    for i in range(begin):
        f.readline()

     if lines<0:
            print(f.read())

     else:
            for j in range(lines):
                print(f.readline(),end='')

    f.close()

    






file_name=input('please enter the filename:');
line_num=input('please enter rows[lke 13:21 or :21 or 21: or ]:')
file_view(file_name, line_num)
