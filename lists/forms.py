from django.forms import ModelForm
from lists.models import List, Item

class ItemForm(ModelForm):

  def save(self, for_list):
    lan = List.objects.get(lan=for_list)
    self.instance.lst = lan
    return super().save()

  class Meta:

    model = Item
    fields = ['code', 'name', 'name_r', 'description', 'description_r']

class ExistingListItemForm(ItemForm):

  def __init__(self, for_list, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.instance.lst = for_list

  def save(self):
    return ModelForm.save(self)