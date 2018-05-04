from django.shortcuts import render
from lists.models import List, Item

def index(request):
  lst = List.objects.get(lan='python')
  # items = Item.objects.all()
  return render(request, 'index.html', {'items': items})

def list_articles(request):
  with open('/home/atl/Desktop/Link to tutorials/Python tutorial/CS Parsing Names From a CSV to an HTML List/patreon.py', "r") as data_file:
    code = data_file.read()
    lst = List.objects.create()
    Item.objects.create(text=code, lst=lst)
    code = Item.objects.first().text
    return render(request, 'python/py_text_data.html', {'page': page})

# function that export data from my files to mysql db
def create_article(request):
  import os

  PATH = '/home/atl/Desktop/Link to Yandex.Disk/Программирование/tutorials/Python tutorial'
  lst_of_py_files = filter(lambda x: x[-3:] == '.py', os.listdir(PATH))

  # os.chdir(PATH)
  pyth = List.objects.get(lan='python')

  for i in lst_of_py_files:
    with open(f'{PATH}/{i}', 'r') as data_file:
      print(i)
      item = Item()
      item.text = data_file.read()
      item.lst = pyth
      item.name = item.description = f'i'
      item.save()


  return render(request, 'index.html', {'list': pyth})
