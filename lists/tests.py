from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.views import home_page


class HomePageTest(TestCase):
    def test_root_url_resolve_to_home_page(self):
        found = resolve("/")
        self.assertEqual(found.func, home_page)
