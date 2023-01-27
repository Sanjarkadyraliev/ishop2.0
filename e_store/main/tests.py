# from django.test import TestCase
# from rest_framework import status
# from rest_framework.reverse import reverse
# from rest_framework.test import APITestCase
# from .models import Product
#
#
# class ProductTest(APITestCase):
#
#     def setUp(self):
#         self.product_url = reverse('product')
#
#     def test_product_create(self):
#         data = {
#             "id": 1,
#             "name": "Samsung",
#             "description": "test",
#             "price": 1500,
#             "category": "Phone"
#         }
#         self.response = self.client.post(self.product_url, data)
#         self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST)