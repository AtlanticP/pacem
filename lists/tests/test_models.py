from django.test import TestCase

from lists.models import List, Item

class ModelListAndItemTest(TestCase):

  def test_saves_and_retrievers_data_from_db(self):
    lst = List.objects.create()
    item_one = Item.objects.create(
      lst=lst, name='name', name_r='имя',
      description='eng description', description_r='описание'
    )
    self.assertEqual(Item.objects.first().description, 'eng description')
    self.assertEqual(Item.objects.first().name_r, 'имя')
    self.assertEqual(item_one.lst, lst)

  def test_saves_items_only_to_existing_list(self):
    list_one = List.objects.create()
    list_two = List.objects.create()
    item_one = Item.objects.create(
      lst=list_two, name='name', name_r='имя',
      description='description', description_r='описание'
    )
    self.assertEqual(Item.objects.first().name_r, 'имя')
    self.assertEqual(item_one.lst, list_two)

