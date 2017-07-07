SOLR_URL='http://solr.org' #这样就算是定义了一个在函数外全局变量，函数以外的变量叫全局变量


def tt():
    global SOLR_URL #使用外面的全局变量，全局变量在一个模块中使用要谨慎，最好是把全局变量单独定义在一个模块中，然后再导入程序使用
    SOLR_URL=SOLR_URL+'#aa'

def tt2():
    print SOLR_URL
if __name__=='__main__':
    tt()
    tt2()
    print SOLR_URL