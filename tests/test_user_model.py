
import unittest
from ..models.user import User






class TestUserModel(unittest.TestCase):

    def setUp(self):
        # Configuración inicial para las pruebas
        self.user = User(id=1, name="John Doe", email="john.doe@example.com")

    def test_user_creation(self):
        # Verificar que el usuario se crea correctamente
        self.assertEqual(self.user.id, 1)
        self.assertEqual(self.user.name, "John Doe")
        self.assertEqual(self.user.email, "john.doe@example.com")

if __name__ == '__main__':
    unittest.main()

