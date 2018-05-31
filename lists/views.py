from django.shortcuts import render, redirect
from lists.models import List, Item
from lists.forms import ItemForm, ExistingListItemForm

def index(request):

  lst = List.objects.all()
  return render(request, 'index.html', {'lists': lst})


# lists the list of a particular list
def list_lan(request):

  lst = List.objects.get(lan='python')
  return render(request, 'list_lan.html', {'list': lst})


# lists the specific item from a list
def code_page(request, item_id):

  lst = List.objects.get(lan='python')
  item = Item.objects.get(id=item_id)
  return render(request, 'code_text.html', {'item': item})

# function that creates articles for db
def create_article(request):

  lst = List.objects.get(lan='python')

  if request.method == 'POST':
    item_form = ExistingListItemForm(for_list=lst, data=request.POST)
    
    if item_form.is_valid():
      
      item_form.save()
      return redirect('do')
  
  else:
    
    summed_items = Item.objects.count()
    item_form = ItemForm()
    return render(request, 'creation_db.html', {'summed_items': summed_items, 'item_form': item_form})
