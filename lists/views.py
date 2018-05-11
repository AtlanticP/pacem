from django.shortcuts import render, redirect
from lists.models import List, Item
from lists.forms import ItemForm, ExistingListItemForm

def index(request):
  # import pdb; pdb.set_trace()
  lst = List.objects.get(lan='python')
  return render(request, 'index.html', {'list': lst})

# function that creates articles for db
def create_article(request):

  lst = List.objects.get(lan='python')

  if request.method == 'POST':
    item_form = ExistingListItemForm(for_list=lst, data=request.POST)
    
    # import pdb; pdb.set_trace()
    if item_form.is_valid():
      
      item_form.save()
      return redirect('do')
  
  else:
    
    summed_items = Item.objects.count()
    item_form = ItemForm()
    return render(request, 'creation_db.html', {'summed_items': summed_items, 'item_form': item_form})
