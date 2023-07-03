from django.test import TestCase
from django.urls import reverse
from core.models import Usuario

class UsuarioViewsTestCase(TestCase):
    def setUp(self):
        self.usuario_felipe = Usuario.objects.create(
            username='Felipinho',
            first_name='Felipe',
            last_name='Souza',
            email='felipe@example.com',
            password='S3nh4django',
            cpf='958.778.420-05',
            telefone='1234567890'
        )
        self.usuario_isabele = Usuario.objects.create(
            username='Belinha',
            first_name='Isabele',
            last_name='Santos',
            email='isabele@example.com',
            password='S3nh4django',
            cpf='293.482.350-44',
            telefone='9876543210'
        )

    def test_home_view(self):
        response = self.client.get(reverse('users:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/index.html')

    def test_save_user_view(self):
        data = {
            'username': 'John',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john@example.com',
            'password': 'S3nh4django',
            'cpf': '636.652.580-30',
            'telefone': '9876543210'
        }
        response = self.client.post(reverse('users:salvar'), data)
        self.assertEqual(response.status_code, 200)

        # Verificar se o usuário foi salvo no banco de dados
        john_exists = Usuario.objects.filter(username='John').exists()
        self.assertTrue(john_exists)

        john = Usuario.objects.get(username='John')
        self.assertEqual(john.first_name, 'John')
        self.assertEqual(john.last_name, 'Doe')
        self.assertEqual(john.email, 'john@example.com')
        self.assertTrue(john.check_password('S3nh4django'))
        self.assertEqual(john.cpf, '636.652.580-30')
        self.assertEqual(john.telefone, '9876543210')

    def test_list_users_view(self):
        response = self.client.get(reverse('users:users'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/users.html')
        self.assertSetEqual(set(response.context['usuarios']), {(self.usuario_felipe),(self.usuario_isabele)})


    def test_update_user_view(self):
        response = self.client.get(reverse('users:editar', args=[self.usuario_felipe.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/update.html')
        self.assertEqual(response.context['usuario'], self.usuario_felipe)
        

    def test_update_view(self):
        data = {
            'username': 'Felipão',
            'first_name' :'Felipe',
            'last_name': 'Santos',
            'email': 'felipe@example.com',
            'password': 'S3nh4django',
            'cpf': '958.778.420-05',
            'telefone': '1234567890'
        }
        response = self.client.post(reverse('users:update', args=[self.usuario_felipe.id]), data)
        self.assertEqual(response.status_code, 302)

        self.usuario_felipe.refresh_from_db()
        self.assertEqual(self.usuario_felipe.username, 'Felipão')
        self.assertEqual(self.usuario_felipe.first_name, 'Felipe')
        self.assertEqual(self.usuario_felipe.last_name, 'Santos')
        self.assertEqual(self.usuario_felipe.email, 'felipe@example.com')
        self.assertEqual(self.usuario_felipe.cpf, '958.778.420-05')
        self.assertEqual(self.usuario_felipe.telefone, '1234567890')

    def test_delete_user_view(self):
        response = self.client.get(reverse('users:delete', args=[self.usuario_felipe.id]))
        self.assertEqual(response.status_code, 302)

        # Verificar se o usuário foi removido do banco de dados
        with self.assertRaises(Usuario.DoesNotExist):
            Usuario.objects.get(id=self.usuario_felipe.id)

    def test_search_users_view(self):
        data = {
            'search': 'Belinha'
        }
        response = self.client.post(reverse('users:search'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/search.html')
        self.assertQuerysetEqual(response.context['usuarios'], [(self.usuario_isabele)])
