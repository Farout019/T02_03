import unittest
from unittest.mock import MagicMock
from services.user_service import UserService
from models.user import User

class TestUserService(unittest.TestCase):

    def setUp(self):
        # Crear una instancia del servicio con un repositorio simulado
        self.mock_repository = MagicMock()
        self.user_service = UserService(self.mock_repository)

    def test_create_user(self):
        # Configurar el repositorio simulado
        user_data = {"id": 1, "name": "Jane Doe", "email": "jane.doe@example.com"}
        self.mock_repository.add.return_value = User(**user_data)

        # Llamar al método a probar
        created_user = self.user_service.create_user(user_data)

        # Verificar resultados
        self.mock_repository.add.assert_called_once_with(user_data)
        self.assertEqual(created_user.name, "Jane Doe")
        self.assertEqual(created_user.email, "jane.doe@example.com")

    def test_get_user_by_id(self):
        # Simular una respuesta del repositorio
        self.mock_repository.get_by_id.return_value = User(id=1, name="John Doe", email="john.doe@example.com")

        # Llamar al método a probar
        user = self.user_service.get_user_by_id(1)

        # Verificar resultados
        self.mock_repository.get_by_id.assert_called_once_with(1)
        self.assertEqual(user.name, "John Doe")

if _name_ == '_main_':
    unittest.main()