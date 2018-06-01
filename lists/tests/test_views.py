from django.urls import resolve
from django.test import TestCase
from lists.models import List, Item
from unittest import skip

from lists.views import index, list_lan, create_article

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
    self.assertContains(response, lan)    

class LanListsTest(TestCase):
  
  def test_lists_lan_page(self):
    lan = 'python'
    List.objects.create(lan=lan)
    
    found = resolve(f'/{lan}/')
    self.assertEqual(found.func, list_lan)

    response = self.client.get(f'/{lan}/')
    self.assertTemplateUsed(response, 'list_lan.html')

  def test_lists_lan_page_content(self):
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
    item = Item.objects.create(
      lst=lst, name='eng name', name_r='имя',
      description='eng description', description_r='описание',
      code='coding',
    )
    
    response = self.client.get(f'/{lan}/{item.id}/')
    self.assertTemplateUsed(response, 'code_text.html')
    
  def test_python_code_page_content(self):
    lan = 'python'
    lst = List.objects.create(lan=lan)
    Item.objects.create(
      lst=lst, name='eng name', name_r='имя',
      description='eng description', description_r='описание',
      code='coding'
    )
    
    response = self.client.get(f'/{lan}/{lst.id}/')

    self.assertContains(response, 'eng name')
    self.assertContains(response, 'coding')
    self.assertContains(response, 'eng description')

class CreateDBTest(TestCase):

  def test_can_save_a_POST_request(self):
    List.objects.create(lan='python')
    
    found = resolve('/do/')
    self.assertEqual(found.func, create_article)
    
    self.client.post('/do/', data={
      'code': 'code', 'name': 'name eng', 'name_r': 'имя', 
      'description': 'description', 'description_r': 'описание'
    })
    
    
    self.assertEqual(Item.objects.count(), 1)
    self.assertIn('name eng', Item.objects.first().name)