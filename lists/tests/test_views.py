from django.urls import resolve
from django.test import TestCase
from unittest import skip

from lists.models import List, Item, Graph
from lists.views import index, list_lan, create_article

class BaseTest(TestCase):

  def assert_lists_context(self, response):
    lists = List.objects.all()
    return self.assertEqual(len(response.context['lists']), len(lists))

class IndexPageTest(BaseTest):
  
  def test_index_page(self):
    response = self.client.get('/')
    
    self.assertTemplateUsed(response, 'index.html')
    self.assert_lists_context(response)


  def test_index_page_content(self):
    lan = 'python'
    List.objects.create(lan=lan)
    lst = List.objects.create(lan='js')
    
    response = self.client.get('/')
    
    self.assertIn('js', response.content.decode())
    self.assertContains(response, lan)    

class LanListsTest(BaseTest):
  
  def test_lists_lan_page(self):
    lan = 'python'
    List.objects.create(lan=lan)
    
    found = resolve(f'/{lan}/')
    self.assertEqual(found.func, list_lan)

    response = self.client.get(f'/{lan}/')

    
    self.assertTemplateUsed(response, 'list_lan.html')
    self.assert_lists_context(response)

  def test_lists_lan_page_context(self):
    lan = 'python'
    lst = List.objects.create(lan=lan)
    Item.objects.create(
      lst=lst, name='eng name', name_r='имя',
      description='eng description', description_r='описание',
      code='coding',
    )

    response = self.client.get(f'/{lan}/')

    self.assertIsInstance(response.context['list'], List)
    self.assertContains(response, 'eng name')

class CodePageTest(BaseTest):

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
    self.assert_lists_context(response)
    
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

class AboutMeTest(TestCase):

  def test_about_me_assert_template_used(self):

    response = self.client.get('/contacts/')
    self.assertTemplateUsed(response, 'contacts.html')


class jQueryTest(TestCase):


  def test_jQuery_index(self):

    lan = 'jQuery'
    lst = List.objects.create(lan=lan)
    item = Item.objects.create(lst=lst, name='jQuery Test')

    response = self.client.get('/jQuery/')

    self.assertTemplateUsed(response, 'jQuery_index.html')
    self.assertContains(response, 'jQuery Crash Course')

    context_variable = List.objects.get(lan='jQuery')
    # import pdb; pdb.set_trace()
    self.assertEqual(response.context['list'], context_variable)
    
    self.assertEqual(context_variable.item_set.first().name, 'jQuery Test')
    self.assertContains(response, 'jQuery Test')


  def test_jQuery_view_code_page(self):
  
    lan = 'jQuery'
    lst = List.objects.create(lan=lan)
    item = Item.objects.create(lst=lst, name='jQuery Test', code='jQuery Page with a code')

    List.objects.create(lan='another_list')
    lists = List.objects.all()

    response = self.client.get(f'/jQuery/{item.id}/')

    self.assertTemplateUsed(response, 'jQuery_view_page.html')
    self.assertContains(response, 'jQuery Test')
    self.assertContains(response, 'jQuery Page with a code')
    self.assertEqual(len(response.context['lists']), len(lists))

class TheoryTest(TestCase):

  def test_theory_lists(self):

    lst = List.objects.create(lan='Theory')
    Graph.objects.create(termin='first termin', lst=lst)
    Graph.objects.create(termin='second termin', lst=lst)

    graph = Graph.objects.all()
    lists = List.objects.all()
    
    response = self.client.get(f'/Theory/')

    self.assertTemplateUsed(response, 'theory_lists.html')
    self.assertEqual(len(response.context['graph']), len(graph))
    self.assertEqual(len(response.context['lists']), len(lists))
    self.assertIn('first termin', response.content.decode())

  