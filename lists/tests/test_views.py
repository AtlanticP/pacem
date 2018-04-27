from django.test import TestCase

from lists.views import index

class IndexPageTest(TestCase):

  def test_index_page(self):
    response = self.client.get('/')
    self.assertTemplateUsed(response, 'index.html')

class PyTextDataTest(TestCase):
  
  def test_py_text_data_page(self):
    response = self.client.get('/py_text_data/')
    self.assertTemplateUsed(response, 'python/py_text_data.html')

  def test_py_text_data_displays_correct_context(self):
    response = self.client.get('/py_text_data/')
    self.assertContains(response, "Mary Jacobs")
  
