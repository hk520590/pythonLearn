
def OpenAndWriteTxt():
    try:
        f = open('d:/log.txt',"a+",encoding='gb18030', errors='ignore')
        print(f.read())
        f.write('Hello, world!\n')
    finally:
        if f:
            f.close()
