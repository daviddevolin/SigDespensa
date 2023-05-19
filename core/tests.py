from django.test import TestCase
from .models import Usuario

class UsuarioCRUDTestCase(TestCase):
    def test_criar_usuario(self):
        usuario_felipe = Usuario.objects.create(
            nome='Felipe Souza',
            email='felipe@example.com',
            cpf='12345678901',
            telefone='1234567890'
        )
        self.assertEqual(usuario_felipe.nome, 'Felipe Souza')
        self.assertEqual(usuario_felipe.email, 'felipe@example.com')
        self.assertEqual(usuario_felipe.cpf, '12345678901')
        self.assertEqual(usuario_felipe.telefone, '1234567890')

        usuario_isabele = Usuario.objects.create(
            nome='Isabele Santos',
            email='isabele@example.com',
            cpf='98765432109',
            telefone='9876543210'
        )
        self.assertEqual(usuario_isabele.nome, 'Isabele Santos')
        self.assertEqual(usuario_isabele.email, 'isabele@example.com')
        self.assertEqual(usuario_isabele.cpf, '98765432109')
        self.assertEqual(usuario_isabele.telefone, '9876543210')