
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from categoria.models import Categoria


class CategoriaViewsTestCase(TestCase):
    def setUp(self):

        self.user = get_user_model().objects.create_user(username='testuser', password='testpassword')
        self.client.force_login(self.user)

        self.Categoria1 = Categoria.objects.create(
            nome='Arroz',

        )
        self.Categoria2 = Categoria.objects.create(
            nome='Feijão',

        )

    def test_home_view(self):
        response = self.client.get(reverse('categories:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'categories/index.html')

    def test_save_Categoria_view(self):
        data = {
            'nome': 'Macarrão',

        }
        response = self.client.post(reverse('categories:salvar'), data)
        self.assertEqual(response.status_code, 302)

        # Verificar se o Categoria foi salvo no banco de dados
        macarrao_exists = Categoria.objects.filter(nome='Macarrão').exists()
        self.assertTrue(macarrao_exists)

    def test_list_Categorias_view(self):
        response = self.client.get(reverse('categories:categories'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'categories/categories.html')
        self.assertSetEqual(set(response.context['categorias']),{(self.Categoria1), (self.Categoria2)})

    def test_update_Categoria_view(self):
        response = self.client.get(reverse('categories:update', args=[self.Categoria1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'categories/update.html')
        self.assertEqual(response.context['categorias'], self.Categoria1)


    def test_update_Categoria_view(self):
        data = {
            'nome': 'Arroz Novo',
        }
        response = self.client.post(reverse('categories:update', args=[self.Categoria1.id]), data)
        self.assertEqual(response.status_code, 302)

        self.Categoria1.refresh_from_db()
        self.assertEqual(self.Categoria1.nome, 'Arroz Novo')

    def test_delete_Categoria_view(self):
        response = self.client.get(reverse('categories:delete', args=[self.Categoria1.id]))
        self.assertEqual(response.status_code, 302)

        # Verificar se a Categoria foi removido do banco de dados
        with self.assertRaises(Categoria.DoesNotExist):
            Categoria.objects.get(id=self.Categoria1.id)

    def test_search_Categorias_view(self):
        data = {
            'search': 'Feijão'
        }
        response = self.client.post(reverse('categories:search'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'categories/search.html')
        self.assertSetEqual(set(response.context['categorias']),{ (self.Categoria2)})
        


  