from django.shortcuts import render, redirect
from lists.models import List, Item
from lists.forms import ItemForm, ExistingListItemForm

def index(request):
  lists = List.objects.all()
  return render(request, 'index.html', {'lists': lists})


# lists the list of a particular list
def list_lan(request, lst_name):

  lst = List.objects.get(lan=lst_name)
  lists = List.objects.all()
  return render(request, 'list_lan.html', {'list': lst, 'lists': lists}) 


# lists the specific item from a list
def code_page(request, lst_name, item_id):
  lst = List.objects.get(lan=lst_name)
  item = Item.objects.get(id=item_id)
  lists = List.objects.all()
  return render(request, 'code_text.html', {'item': item, 'lists': lists})

# function that creates articles for db
def create_article(request):

  lists = List.objects.all()
  lst = List.objects.get(lan='python')
  
  if request.method == 'POST':
    item_form = ExistingListItemForm(for_list=lst, data=request.POST)
    
    if item_form.is_valid():
      
      item_form.save()
      return redirect('do')
  
  else:
    
    summed_items = Item.objects.count()
    item_form = ItemForm()
    return render(
      request, 'creation_db.html', 
      {
      'summed_items': summed_items, 'item_form': item_form, 'lists': lists
      })

def contacts(request):
  lists = List.objects.all()
  return render(request, 'contacts.html', {'lists': lists})

def jQuery_index(request):
  jquery_list = List.objects.get(lan='jQuery')
  lists = List.objects.all()
  return render(request, 'jQuery_index.html', {'list': jquery_list, 'lists': lists})

def jQuery_view(request, item_id):
  item = Item.objects.get(id=item_id)
  context = {'item': item}
  return render(request, 'jQuery_view_page.html', context)