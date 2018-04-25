from django.test import TestCase

from lists.views import index

class IndexPageTest(TestCase):

	def test_index_page(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'index.html')
