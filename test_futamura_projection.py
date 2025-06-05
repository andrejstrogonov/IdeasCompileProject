import unittest
from unittest.mock import patch
from futamura_projection import interpret, specialized_interpreter, compiler, compiler_generator

class TestFutamuraProjection(unittest.TestCase):
    def test_interpret(self):
        # Test the general interpreter
        expression = "3 + 5 * 2 - 4 / 2"
        result = interpret(expression)
        self.assertEqual(result, 10.0)

    def test_specialized_interpreter(self):
        # Test the specialized interpreter
        result = specialized_interpreter()
        self.assertEqual(result, 10.0)

    def test_compiler(self):
        # Test the compiler function
        expression = "3 + 5 * 2 - 4 / 2"
        code = compiler(expression)
        exec_locals = {}
        exec(code, {}, exec_locals)
        result = exec_locals['result']
        self.assertEqual(result, 10.0)

    def test_compiler_generator(self):
        # Test the compiler generator
        expression = "3 + 5 * 2 - 4 / 2"
        generated_compiler = compiler_generator(interpret)
        code = generated_compiler(expression)
        exec_locals = {}
        exec(code, {}, exec_locals)
        result = exec_locals['result']
        self.assertEqual(result, 10.0)

    @patch('builtins.exec')
    def test_exec_mock(self, mock_exec):
        # Mock the exec function to test without executing code
        expression = "3 + 5 * 2 - 4 / 2"
        code = compiler(expression)
        exec_locals = {}
        exec(code, {}, exec_locals)
        mock_exec.assert_called_once_with(code, {}, exec_locals)

if __name__ == '__main__':
    unittest.main()