from django.shortcuts import render
from lists.models import List, Item

def index(request):
  return render(request, 'index.html')

def list_articles(request):
  with open('/home/atl/Desktop/Link to tutorials/Python tutorial/CS Parsing Names From a CSV to an HTML List/patreon.py', "r") as data_file:
    code = data_file.read()
    lst = List.objects.create()
    Item.objects.create(text=code, lst=lst)
    code = Item.objects.first().text
    return render(request, 'python/py_text_data.html', {'page': page})

def create_article(request):
  with open('/home/atl/Desktop/Link to tutorials/Python tutorial/CS Parsing Names From a CSV to an HTML List/patreon.py', "r") as data_file:
    page = data_file.read()
    lst = List.objects.get(lan='python')
    Item.objects.create(text=page, lst=lst, name='parse_css_to_html')
    page = Item.objects.get(name='parse_css_to_html')
    return render(request, 'python/py_text_data.html', {'page': page})