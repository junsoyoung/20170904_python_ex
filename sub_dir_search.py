import os

def search(dirname, delim):
    try:
        filenames = os.listdir(dirname) # add try for preventing this os.listdir()
        for fname in filenames:
            fullname = os.path.join( dirname, fname)

            if( os.path.isdir( fullname)):
                search(fullname, delim)
            else:
                ext = os.path.splitext(fullname)[1]

                if( len(delim)):
                    if (ext == delim):
                        print(fullname)
                else:
                    print(fullname )
        print("*"*30)
    except PermissionError:
        pass

search("E:\\003_Work\\03_PythonWorkSpace\\20170904_python_ex", '.py')