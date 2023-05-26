from django.test import TestCase
from django.urls import reverse
from .models import Item

class ItemViewsTestCase(TestCase):
    def setUp(self):
        self.item1 = Item.objects.create(
            nome='Arroz',
            categoria='Alimentos',
            marca='Marca A',
            peso='1kg',
            validade='2023-06-01'
        )
        self.item2 = Item.objects.create(
            nome='Feijão',
            categoria='Alimentos',
            marca='Marca B',
            peso='500g',
            validade='2023-05-31'
        )

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_save_item_view(self):
        data = {
            'nome': 'Macarrão',
            'categoria': 'Alimentos',
            'marca': 'Marca C',
            'peso': '500g',
            'validade': '2023-06-02'
        }
        response = self.client.post(reverse('save_item'), data)
        self.assertEqual(response.status_code, 302)

        # Verificar se o item foi salvo no banco de dados
        macarrao_exists = Item.objects.filter(nome='Macarrão').exists()
        self.assertTrue(macarrao_exists)

    def test_list_items_view(self):
        response = self.client.get(reverse('items'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'items.html')
        self.assertQuerysetEqual(response.context['itens'], [repr(self.item1), repr(self.item2)])

    def test_update_item_view(self):
        response = self.client.get(reverse('update_item', args=[self.item1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'update.html')
        self.assertEqual(response.context['item'], self.item1)

    def test_update_view(self):
        data = {
            'nome': 'Arroz Integral',
            'categoria': 'Alimentos',
            'marca': 'Marca A',
            'peso': '1kg',
            'validade': '2023-06-01'
        }
        response = self.client.post(reverse('update', args=[self.item1.id]), data)
        self.assertEqual(response.status_code, 302)

        self.item1.refresh_from_db()
        self.assertEqual(self.item1.nome, 'Arroz Integral')

    def test_delete_item_view(self):
        response = self.client.get(reverse('delete_item', args=[self.item1.id]))
        self.assertEqual(response.status_code, 302)

        # Verificar se o item foi removido do banco de dados
        with self.assertRaises(Item.DoesNotExist):
            Item.objects.get(id=self.item1.id)

    def test_search_items_view(self):
        data = {
            'search': 'Feijão'
        }
        response = self.client.post(reverse('search_items'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search.html')
        self.assertQuerysetEqual(response.context['itens'], [repr(self.item2)])
