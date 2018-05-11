from django.test import TestCase
from lists.forms import ItemForm, ExistingListItemForm
from lists.models import List, Item
from unittest import skip

# new_item = ExistingListItemForm(for_list='python', data={'name': 'name', 'name_r': 'имя', 'description': 'description', 'description_r': 'описание'})

class ExistingListItemFormTest(TestCase):
  
  # @skip('ualya')
  def test_form_save(self):
    lst = List.objects.create()
    form = ExistingListItemForm(for_list=lst, data={
      'code': 'code', 'name': 'name', 'name_r': 'имя',
      'description': 'description', 'description_r': 'описание'
    })
    self.assertTrue(form.is_valid())

    self.assertEquals(form.save(), Item.objects.all()[0])
    self.assertEquals(Item.objects.all()[0].name_r, 'имя')


