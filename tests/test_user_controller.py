import unittest
from unittest.mock import MagicMock
from controllers.user_controller import UserController
from services.user_service import UserService
from models.user import User

class TestUserController(unittest.TestCase):

    def setUp(self):
        # Crear instancias simuladas del servicio
        self.mock_service = MagicMock(spec=UserService)
        self.controller = UserController(self.mock_service)

    def test_get_user_success(self):
        # Configurar el servicio simulado
        user_data = User(id=1, name="John Doe", email="john.doe@example.com")
        self.mock_service.get_user_by_id.return_value = user_data

        # Llamar al controlador
        response = self.controller.get_user(1)

        # Verificar los resultados
        self.mock_service.get_user_by_id.assert_called_once_with(1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"id": 1, "name": "John Doe", "email": "john.doe@example.com"})

    def test_get_user_not_found(self):
        # Configurar el servicio simulado para devolver None
        self.mock_service.get_user_by_id.return_value = None

        # Llamar al controlador
        response = self.controller.get_user(999)

        # Verificar los resultados
        self.mock_service.get_user_by_id.assert_called_once_with(999)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"error": "User not found"})

if _name_ == '_main_':
    unittest.main()
    