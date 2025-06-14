import unittest
from unittest.mock import patch
from futamura_projections.futamura_projection import interpret, specialized_interpreter, compiler, compiler_generator

class TestFutamuraProjection(unittest.TestCase):
    def test_interpret(self):
        # Test the general interpreter with various expressions
        expressions = [
            ("3 + 5 * 2 - 4 / 2", 10.0),
            ("10 / 2 + 3 * 4 - 1", 15.0),
            ("(3 + 5) * 2", 16.0),
            ("3 + 5 * (2 - 4) / 2", 2.0),
            ("-3 + 5 * 2", 7.0),
            ("3 + 5 * 2 - 4 / 0", None)  # Assuming interpret handles division by zero
        ]
        for expression, expected in expressions:
            with self.subTest(expression=expression):
                if expected is None:
                    with self.assertRaises(ZeroDivisionError):
                        interpret(expression)
                else:
                    result = interpret(expression)
                    self.assertEqual(result, expected)

    def test_specialized_interpreter(self):
        # Test the specialized interpreter with different scenarios
        # Assuming specialized_interpreter can take different inputs or scenarios
        result = specialized_interpreter()
        self.assertEqual(result, 10.0)

    def test_compiler(self):
        # Test the compiler function with various expressions
        expressions = [
            ("3 + 5 * 2 - 4 / 2", 10.0),
            ("10 / 2 + 3 * 4 - 1", 15.0),
            ("(3 + 5) * 2", 16.0),
            ("3 + 5 * (2 - 4) / 2", 2.0),
            ("-3 + 5 * 2", 7.0)
        ]
        for expression, expected in expressions:
            with self.subTest(expression=expression):
                code = compiler(expression)
                exec_locals = {}
                exec(code, {}, exec_locals)
                result = exec_locals['result']
                self.assertEqual(result, expected)

    def test_compiler_generator(self):
        # Test the compiler generator with various interpreters and expressions
        interpreters = [interpret]  # Add more interpreters if available
        expressions = [
            ("3 + 5 * 2 - 4 / 2", 10.0),
            ("10 / 2 + 3 * 4 - 1", 15.0),
            ("(3 + 5) * 2", 16.0),
            ("3 + 5 * (2 - 4) / 2", 2.0),
            ("-3 + 5 * 2", 7.0)
        ]
        for interpreter in interpreters:
            for expression, expected in expressions:
                with self.subTest(interpreter=interpreter, expression=expression):
                    generated_compiler = compiler_generator(interpreter)
                    code = generated_compiler(expression)
                    exec_locals = {}
                    exec(code, {}, exec_locals)
                    result = exec_locals['result']
                    self.assertEqual(result, expected)

    @patch('builtins.exec')
    def test_exec_mock(self, mock_exec):
        # Mock the exec function to test without executing code
        expressions = [
            "3 + 5 * 2 - 4 / 2",
            "10 / 2 + 3 * 4 - 1",
            "(3 + 5) * 2",
            "3 + 5 * (2 - 4) / 2",
            "-3 + 5 * 2"
        ]
        for expression in expressions:
            with self.subTest(expression=expression):
                code = compiler(expression)
                exec_locals = {}
                exec(code, {}, exec_locals)
                mock_exec.assert_called_with(code, {}, exec_locals)

if __name__ == '__main__':
    unittest.main()