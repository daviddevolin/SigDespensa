# Relatório de Teste - UsuarioCRUDTestCase 

O código fornecido contém uma classe de teste chamada `UsuarioCRUDTestCase` que herda de `django.test.TestCase`. A classe contém um método de teste chamado `test_criar_usuario` que verifica se a criação de objetos Usuario está funcionando corretamente. 

## Método de Teste 
`test_criar_usuario(self)`:

Este método de teste verifica se os objetos `Usuario` são criados corretamente com os atributos desejados. Dois usuários são criados usando o método `create` do gerenciador de objetos `Usuario.objects`. Em seguida, são feitas asserções (`assertions`) para verificar se os atributos dos usuários criados correspondem aos valores esperados.

## Observações:

Os testes realizados se concentram na criação de usuários e na verificação dos atributos dos objetos criados.

## Conclusão:
Com base nos testes fornecidos, é possível afirmar que a criação de objetos `Usuario` está funcionando corretamente. Os testes verificam se os atributos dos usuários criados correspondem aos valores esperados.