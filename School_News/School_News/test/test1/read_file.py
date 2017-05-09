import time



start_filename = [

    'http___www.china-cdt.com_dtwz__indexAction.ndo_action=showNewsInYearList&t=index_news&s=news_dtxw.txt',

]
for i in start_filename:
    new_path_filename = r'C:\Users\yf\Desktop\aaa\{}'.format(i)
    print(new_path_filename)
    try:
        f0 = open(new_path_filename, 'r', encoding='utf8')
        print(f0.read())
    except :
        pass




    # old_path_filename = r'C:\Users\yf\Desktop\abc\1.txt'
    # f = open(old_path_filename, 'a', encoding='utf8')
    # f.write(f0.read()+'\n'+'---------------------------------')
    # f.close()
    # f0.close()

