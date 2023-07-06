from django.test import TestCase
from django.urls import reverse
from django.shortcuts import get_object_or_404
from item.models import Item
from despensa.models import Despensa
from categoria.models import Categoria
from item.forms import ItemForm

class ItemViewsTestCase(TestCase):
    def setUp(self):

        self.categoria = Categoria.objects.create(
            nome="Alimentos"
        )

        self.item1 = Item.objects.create(
            nome='Arroz',
            categoria=self.categoria,
            marca='Marca A',
            peso=1000,
            data_validade='2023-06-01'
        )
        self.item2 = Item.objects.create(
            nome='Feijão',
            categoria=self.categoria,
            marca='Marca B',
            peso=500,
            data_validade='2023-05-31'
        )
        self.despensa = Despensa.objects.create(
            nome='DespensaTeste',
            quantTotal=1000,
            capacidade=2000
        )

    def test_home_view(self):
        response = self.client.get(reverse('items:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'items/index.html')

    def test_save_item_view(self): 

        form = ItemForm()

        form.data['despensa'] = self.despensa.id
        form.data['categoria'] = self.categoria.id
        form.data['nome'] = 'Macarrão'
        form.data['marca'] = 'Marca C'
        form.data['peso'] = 500
        form.data['data_validade'] = '2023-06-02'

        response = self.client.post(reverse('items:salvar'), form.data)
        self.assertEqual(response.status_code, 200)

        # Verificar se o item foi salvo no banco de dados
        macarrao_exists = Item.objects.filter(nome='Macarrão').exists()
        self.assertTrue(macarrao_exists)

    def test_list_items_view(self):
        response = self.client.get(reverse('items:items'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'items/items.html')
        self.assertSetEqual(set(response.context['items']),{(self.item1), (self.item2)})

    def test_update_item_view(self):
        response = self.client.get(reverse('items:update', args=[self.item1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'items/update.html')
        self.assertEqual(response.context['item'], self.item1)


    def test_update_item_view(self):
        form = ItemForm()

        form.data['despensa'] = self.despensa.id
        form.data['categoria'] = self.categoria.id
        form.data['nome'] = 'Arroz Novo'
        form.data['marca'] = 'Marca A'
        form.data['peso'] = 1000
        form.data['data_validade'] = '2023-06-01'

        response = self.client.post(reverse('items:update', args=[self.item1.id]), form.data)
        self.assertEqual(response.status_code, 302)

        self.item1.refresh_from_db()
        self.assertEqual(self.item1.nome, 'Arroz Novo')

    def test_delete_item_view(self):
        response = self.client.get(reverse('items:delete', args=[self.item1.id]))
        self.assertEqual(response.status_code, 302)

        # Verificar se o item foi removido do banco de dados
        with self.assertRaises(Item.DoesNotExist):
            Item.objects.get(id=self.item1.id)

    def test_search_items_view(self):
        data = {
            'search': 'Feijão'
        }
        response = self.client.post(reverse('items:search'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'items/search.html')
        self.assertSetEqual(set(response.context['items']),{ (self.item2)})
        
