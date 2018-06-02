from django.shortcuts import render, redirect
from lists.models import List, Item
from lists.forms import ItemForm, ExistingListItemForm

def index(request):
  lsts = List.objects.all()
  return render(request, 'index.html', {'lists': lsts})


# lists the list of a particular list
def list_lan(request, lst_name):
  lst = List.objects.get(lan=lst_name)
  return render(request, 'list_lan.html', {'list': lst}) 


# lists the specific item from a list
def code_page(request, lst_name, item_id):
  lst = List.objects.get(lan=lst_name)
  item = Item.objects.get(id=item_id)
  return render(request, 'code_text.html', {'item': item})

# function that creates articles for db
def create_article(request):

  # import pdb; pdb.set_trace()
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
