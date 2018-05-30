from django.test import TestCase
from lists.models import List, Item
from unittest import skip

from lists.views import index

class IndexPageTest(TestCase):

  def test_index_page(self):
    List.objects.create(lan='python')
    response = self.client.get('/')
    self.assertTemplateUsed(response, 'index.html')


class PythonPageTest(TestCase):

  def test_index_page(self):
    List.objects.create(lan='python')
    response = self.client.get('/python/')
    self.assertTemplateUsed(response, 'code_text.html')

class CreateDBTest(TestCase):

  def test_can_save_a_POST_request(self):
    lst = List.objects.create(lan='python')
    response = self.client.post('/do/', data={
      'code': 'code', 'name': 'name', 'name_r': 'имя', 
      'description': 'description', 'description_r': 'описание'
    })
    self.assertEqual(Item.objects.count(), 1)