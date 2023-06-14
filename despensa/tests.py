from django.test import TestCase
from django.urls import reverse
from despensa.models import Despensa

# Create your tests here.


class DespensaViewsTestCase(TestCase):
    def setUp(self):
        self.despensa1 = Despensa.objects.create(
            nome = 'casa',
            quantTotal = 10,
            capacidade = 200,
            categoria = 'alimentos'
        )
        self.despensa2 = Despensa.objects.create(
            nome = 'apartamento',
            quantTotal = 15,
            capacidade = 200,
            categoria = 'limpeza'
        )


    def test_despensa_create_view(self):
        data = {
            'nome' : 'sitio',
            'quantTotal' : 30,
            'capacidade' : 200,
            'categoria' : 'ração'
        }
        response = self.client.post(reverse('despensas:despensa_create'), data)
        self.assertEqual(response.status_code, 302)

        # Verificar se o despensa foi salvo no banco de dados
        sitio_exists = Despensa.objects.filter(nome='sitio').exists()
        self.assertTrue(sitio_exists)

    def test_despensa_list_view(self):
        response = self.client.get(reverse('despensas:despensa_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'despensa/list.html')
        self.assertSetEqual(set(response.context['despensas']),{(self.despensa1), (self.despensa2)})

    def test_despensa_update_view(self):
        response = self.client.get(reverse('despensas:despensa_update', args=[self.despensa1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'despensa/update.html')
        self.assertEqual(response.context['despensa'], self.despensa1)


    # def test_update_view(self):
    #     data = {
    #         'nome' : 'casa-SP',
    #         'quantTotal' : 40,
    #         'capacidade' : 200,
    #         'categoria' : 'alimentos'
    #     }
    #     response = self.client.post(reverse('update', args=[self.despensa1.id]), data)
    #     self.assertEqual(response.status_code, 302)

    #     self.despensa1.refresh_from_db()
    #     self.assertEqual(self.despensa1.nome, 'casa-SP')

   #def test_despensa_delete_view(self):
    #    response = self.client.get(reverse('despensas:despensa_delete', args=[self.despensa1.id]))
     #   self.assertEqual(response.status_code, 200)

        # Verificar se o despensa foi removido do banco de dados
        #with self.assertRaises(Despensa.DoesNotExist):
        #   Despensa.objects.get(id=self.despensa1.id)

   
