from django.test import TestCase
from lists.models import List, Item
from unittest import skip

from lists.views import index

class IndexPageTest(TestCase):

  def test_index_page(self):
    lan = 'python'
    lst = List.objects.create(lan=lan)
    response = self.client.get('/')
    self.assertTemplateUsed(response, 'index.html')

  def test_assert_index_page_data(self):
    lan = 'python'
    lst = List.objects.create(lan=lan)
    response = self.client.get('/')
    self.assertContains(response, 'python')    

class LanListsTest(TestCase):
  
  def test_lists_item_page(self):
    lan = 'python'
    List.objects.create(lan=lan)
    response = self.client.get(f'/{lan}/')
    self.assertTemplateUsed(response, 'list_lan.html')

  # @skip('delete items')
  def test_code_page_data(self):
    lan = 'python'
    lst = List.objects.create(lan=lan)
    Item.objects.create(
      lst=lst, name='eng name', name_r='имя',
      description='eng description', description_r='описание',
      code='coding',
    )
    response = self.client.get(f'/{lan}/')
    self.assertContains(response, 'eng name')

class CodePageTest(TestCase):

  def test_code_page(self):
    lan = 'python'
    lst = List.objects.create(lan=lan)
    Item.objects.create(
      lst=lst, name='eng name', name_r='имя',
      description='eng description', description_r='описание',
      code='coding',
    )
    response = self.client.get(f'/{lan}/{lst.id}/')
    self.assertTemplateUsed(response, 'code_text.html')

  def test_python_code_page_data(self):
    lan = 'python'
    lst = List.objects.create(lan=lan)
    Item.objects.create(
      lst=lst, name='eng name', name_r='имя',
      description='eng description', description_r='описание',
      code='coding',
    )
    response = self.client.get(f'/{lan}/{lst.id}/')
    # import pdb; pdb.set_trace()
    # self.assertContains(response, 'oooooo')
    self.assertContains(response, 'eng name')
    self.assertContains(response, 'coding')
    self.assertContains(response, 'eng description')

class CreateDBTest(TestCase):

  def test_can_save_a_POST_request(self):
    lst = List.objects.create(lan='python')
    response = self.client.post('/do/', data={
      'code': 'code', 'name': 'name', 'name_r': 'имя', 
      'description': 'description', 'description_r': 'описание'
    })
    self.assertEqual(Item.objects.count(), 1)