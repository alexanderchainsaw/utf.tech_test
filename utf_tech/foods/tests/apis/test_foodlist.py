import json
import os
from django.test import TestCase
from django.core.management import call_command
from pathlib import Path
from django.urls import reverse


class FoodAPITests(TestCase):
    url = reverse('api:foods:food_list')

    def load_json(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)

    def load_fixtures(self, case_name):
        base_path = os.path.join(Path(__file__).parent.parent.parent,
                                 'fixtures\\test_foodlist_api', case_name)
        call_command('loaddata', os.path.join(base_path, 'catalog_data.json'))
        self.expected_data = self.load_json(os.path.join(base_path, 'expected_response.json'))

    def test_case_1(self):
        self.load_fixtures('test_case_1')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content.decode('utf-8'), self.expected_data)

    def test_case_2(self):
        self.load_fixtures('test_case_2')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content.decode('utf-8'), self.expected_data)

    def test_case_3(self):
        self.load_fixtures('test_case_3')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content.decode('utf-8'), self.expected_data)

    def test_case_4(self):
        self.load_fixtures('test_case_4')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content.decode('utf-8'), self.expected_data)

    def test_case_5(self):
        self.load_fixtures('test_case_5')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content.decode('utf-8'), self.expected_data)





