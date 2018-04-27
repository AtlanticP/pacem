from django.test import TestCase

from lists.models import List, Item

class ModelListAndItemTest(TestCase):

	def test_saves_and_retrievers_data_from_db(self):
		list_one = List.objects.create()
		item_one = Item.objects.create(text='Item one', lst=list_one)
		self.assertEqual(Item.objects.first().text, 'Item one')
		self.assertEqual(item_one.lst, list_one)

		

