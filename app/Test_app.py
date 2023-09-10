import unittest
import app.models

class TestApp(unittest.TestCase):
    def test_add(self):
        result = app.models.add()
        self.assertEqual(result)

if __name__ == '__name__':
    unittest.main()
