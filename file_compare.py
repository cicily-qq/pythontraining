def file_compare(file1,file2):
     #打开文件
    f1=open(file1)
    f2=open(file2)
    count=0
    differ=[]

    for line1 in f1:
        line2=f2.readline()
        if line1!=line2:    #判断哪一行字符不同
            count+=1
            differ.append(count)

     #关闭文件
    f1.close()
    f2.close()



file1=input('请输入文件名：')
file2=input('请输入文件名：')

differ=file_compare(file1,file2)

if len(differ)==0:
    print('两个文件相同')

else:
    print('两个文件不同')
    print('两文件共有%d处不同',%len(differ))

    for each in differ:
        print('第%d行不同',%each)


    
            


    
