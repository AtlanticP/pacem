# os.chdir('C:\\Users\\Михаил\\Desktop')
# mod_time = os.stat('count.txt').st_mtime   #21511190856
# print(datetime.datetime.fromtimestamp(mod_time))    #2017-11-20 18:14:16.131076 - human format


# os.walk() is a generator that yields a tuple of 3 values 
# as it's walking a directory tree
# the directory path, the directory within that path, the files within that path

# for dirpath, dirnames, filenames in os.walk('C:\\Users\\Home\\Desktop'):
#   print('Current Path:', dirpath)
#   print('Directories:', dirnames)
#   print('filenames:', filenames)
#   print()

# os.chdir('C:\\Users\\Home\\Desktop')
# print(os.environ('__pycache__'))

# print(os.environ['HOME'])   #Linux/Mac Users
# print(os.environ['USERPROFILE'])  #C:\Users\Михаил  - Windows User

# print(os.path.dirname('C:\\Users\\Михаил\\Desktop'))    #C:\Users\Михаил - HEAD
# print(os.path.basename('C:\\Users\\Михаил\\Desktop'))   #C:\Users\Михаил
# print(os.path.split('C:\\Users\\Михаил\\Desktop'))    #C:\Users\Михаил - HEAD, Desktop - Tail, ('C:\\Users\\Михаил', 'Desktop')

# print(os.path.exists('C:\\Users\\Михаил\\Desktop\\count.txt'))  #True
# print(os.path.exists('C:\\Users\\Михаил\\Desktop')) #True
# print(os.path.exists('C:\\Users\\Михаил\\Desktopp'))  #False

# print(os.path.isfile('C:\\Users\\Михаил\\Desktop\\count.txt'))  #True
# print(os.path.isfile('C:\\Users\\Михаил\\Desktop\\countt.txt')) #False
# print(os.path.isfile('C:\\Users\\Михаил\\Desktop\\count.txt'))  #False

# print(os.path.splitext('C:\\Users\\Михаил\\Desktop\\count.txt'))  #('C:\\Users\\Михаил\\Desktop\\count', '.txt')