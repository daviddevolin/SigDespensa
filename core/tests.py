from django.test import TestCase
from django.urls import reverse
from core.models import Usuario

class UsuarioViewsTestCase(TestCase):
    def setUp(self):
        self.usuario_felipe = Usuario.objects.create(
            nome='Felipe Souza',
            email='felipe@example.com',
            cpf='12345678901',
            telefone='1234567890'
        )
        self.usuario_isabele = Usuario.objects.create(
            nome='Isabele Santos',
            email='isabele@example.com',
            cpf='98765432109',
            telefone='9876543210'
        )

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_save_user_view(self):
        data = {
            'nome': 'John Doe',
            'email': 'john@example.com',
            'cpf': '12345678902',
            'telefone': '9876543210'
        }
        response = self.client.post(reverse('salvar'), data)
        self.assertEqual(response.status_code, 200)

        # Verificar se o usuário foi salvo no banco de dados
        john_exists = Usuario.objects.filter(nome='John Doe').exists()
        self.assertTrue(john_exists)

        john = Usuario.objects.get(nome='John Doe')
        self.assertEqual(john.email, 'john@example.com')
        self.assertEqual(john.cpf, '12345678902')
        self.assertEqual(john.telefone, '9876543210')

    def test_list_users_view(self):
        response = self.client.get(reverse('users'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users.html')
        self.assertQuerysetEqual(response.context['usuarios'], [repr(self.usuario_felipe), repr(self.usuario_isabele)])

    def test_update_user_view(self):
        response = self.client.get(reverse('editar', args=[self.usuario_felipe.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'update.html')
        self.assertEqual(response.context['usuario'], self.usuario_felipe)

    def test_update_view(self):
        data = {
            'nome': 'Felipe Souza Novo',
            'email': 'felipe@example.com',
            'cpf': '12345678901',
            'telefone': '1234567890'
        }
        response = self.client.post(reverse('update', args=[self.usuario_felipe.id]), data)
        self.assertEqual(response.status_code, 302)

        self.usuario_felipe.refresh_from_db()
        self.assertEqual(self.usuario_felipe.nome, 'Felipe Souza Novo')

    def test_delete_user_view(self):
        response = self.client.get(reverse('delete', args=[self.usuario_felipe.id]))
        self.assertEqual(response.status_code, 302)

        # Verificar se o usuário foi removido do banco de dados
        with self.assertRaises(Usuario.DoesNotExist):
            Usuario.objects.get(id=self.usuario_felipe.id)

    def test_search_users_view(self):
        data = {
            'search': 'Isabele'
        }
        response = self.client.post(reverse('search'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search.html')
        self.assertQuerysetEqual(response.context['usuarios'], [repr(self.usuario_isabele)])
