from django.shortcuts import render, redirect
from lists.models import List, Item
from lists.forms import ItemForm

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
  if request.method == 'POST':
    if item_form(request.POST):
      item_form.save()
      return redirect('do')
  else:
    summed_items = Item.objects.count()
    item_form = ItemForm()
    return render(request, 'creation_db.html', {'summed_items': summed_items, 'item_form': item_form})
