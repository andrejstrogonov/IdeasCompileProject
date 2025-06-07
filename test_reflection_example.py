import unittest
from demonstrated_reflection_incaplusaltion import ExampleClass

class TestExampleClass(unittest.TestCase):
    def setUp(self):
        self.example = ExampleClass()

    def test_encapsulation(self):
        # Test accessing the private attribute through the public method
        self.assertEqual(self.example.get_private_attribute(), "This is a private attribute")

    def test_reflection_access(self):
        # Test accessing the private attribute using reflection
        private_value = getattr(self.example, '_private_attribute')
        self.assertEqual(private_value, "This is a private attribute")

if __name__ == '__main__':
    unittest.main()
