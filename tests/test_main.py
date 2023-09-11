import unittest
from unittest.mock import patch
from app.main import add_tenant, remove_tenant, list_tenants, add_property, remove_property, list_properties, relate_tenant, add_payment, remove_payment

class TestMainFunctions(unittest.TestCase):

    @patch('builtins.input', side_effect=["Test Tenant"])
    def test_add_tenant(self, mock_input):
        add_tenant()  

    @patch('builtins.input', return_value=1)
    def test_remove_tenant(self, mock_input):
        remove_tenant()  

    @patch('builtins.input', return_value=1)
    def test_list_tenants(self, mock_input):
        list_tenants()  

    @patch('builtins.input', side_effect=["Test Property", "Test Address"])
    def test_add_property(self, mock_input):
        add_property()  

    @patch('builtins.input', return_value=1)
    def test_remove_property(self, mock_input):
        remove_property()  

    @patch('builtins.input', return_value=1)
    def test_list_properties(self, mock_input):
        list_properties()  

    @patch('builtins.input', side_effect=["1", "1"])
    def test_relate_tenant(self, mock_input):
        relate_tenant()  

    @patch('builtins.input', side_effect=["1", "1", "2023-09-06", "1000.00"])
    def test_add_payment(self, mock_input):
        add_payment()  

    @patch('builtins.input', return_value=1)
    def test_remove_payment(self, mock_input):
        remove_payment()  

if __name__ == '__main__':
    unittest.main()
