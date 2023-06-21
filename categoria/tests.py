from django.test import TestCase
from django.urls import reverse
from categoria.models import Categoria

class CategoriaViewsTestCase(TestCase):
    def setUp(self):
        self.categoria1 = Categoria.objects.create(
            nome='Arroz',

        )
        self.categoria2 = Categoria.objects.create(
            nome='Feijão',

        )

    def test_home_view(self):
        response = self.client.get(reverse('categoria:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'categoria/index.html')

    def test_save_item_view(self):
        data = {
            'nome': 'Macarrão',
        }
        response = self.client.post(reverse('categorias:salvar'), data)
        self.assertEqual(response.status_code, 200)

        # Verificar se o item foi salvo no banco de dados
        macarrao_exists = Categoria.objects.filter(nome='Macarrão').exists()
        self.assertTrue(macarrao_exists)

    def test_list_items_view(self):
        response = self.client.get(reverse('items:items'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'categorias/categorias.html')
        self.assertSetEqual(set(response.context['categorias']),{(self.categoria1), (self.categoria2)})

    def test_update_item_view(self):
        response = self.client.get(reverse('categorias:update', args=[self.categoria1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'categorias/update.html')
        self.assertEqual(response.context['categoria'], self.categoria1)


    def test_update_item_view(self):
        data = {
            'nome': 'Arroz Novo',

        }
        response = self.client.post(reverse('categorias:update', args=[self.categoria1.id]), data)
        self.assertEqual(response.status_code, 302)

        self.categoria1.refresh_from_db()
        self.assertEqual(self.categoria1.nome, 'Arroz Novo')

    def test_delete_item_view(self):
        response = self.client.get(reverse('categorias:delete', args=[self.categoria1.id]))
        self.assertEqual(response.status_code, 302)

        # Verificar se o item foi removido do banco de dados
        with self.assertRaises(Categoria.DoesNotExist):
            Categoria.objects.get(id=self.categoria1.id)

    def test_search_categorias_view(self):
        data = {
            'search': 'Feijão'
        }
        response = self.client.post(reverse('categorias:search'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'categorias/search.html')
        self.assertSetEqual(set(response.context['categorias']),{ (self.categoria2)})
        
