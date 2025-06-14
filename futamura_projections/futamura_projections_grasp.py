# Futamura Projections with GRASP Principles

from typing import Callable

# Information Expert: Interpreter class is responsible for interpreting expressions
class Interpreter:
    def interpret(self, expression: str) -> float:
        """Interprets a mathematical expression and returns the result."""
        return eval(expression)

# Creator: SpecializedInterpreter creates instances of specialized functions
class SpecializedInterpreter:
    def __init__(self, interpreter: Interpreter):
        self.interpreter = interpreter

    def specialize(self, expression: str) -> Callable[[], float]:
        """Specializes the interpreter for a specific expression."""
        def specialized():
            return self.interpreter.interpret(expression)
        return specialized

# Low Coupling: Compiler is independent of the interpreter
class Compiler:
    def compile(self, expression: str) -> str:
        """Compiles a mathematical expression into Python code."""
        return f"result = {expression}"

# High Cohesion: CompilerGenerator focuses on generating compilers
class CompilerGenerator:
    def __init__(self, interpreter: Interpreter):
        self.interpreter = interpreter

    def generate(self) -> Callable[[str], str]:
        """Generates a compiler from the interpreter."""
        def compiler(expression: str) -> str:
            return self.interpreter.interpret(expression)
        return compiler

# Demonstration of Futamura Projections
interpreter = Interpreter()
specialized_interpreter = SpecializedInterpreter(interpreter)
compiler = Compiler()
compiler_generator = CompilerGenerator(interpreter)

# Reflection: Dynamically access and modify the interpreter
expression = "3 + 5 * 2 - 4 / 2"
reflection_result = getattr(interpreter, 'interpret')(expression)
print("Reflection Result:", reflection_result)

# Introspection: Examine the types and structures
print("Interpreter Class:", interpreter.__class__)
print("Interpreter Module:", interpreter.__module__)
print("Interpret Method Annotations:", interpreter.interpret.__annotations__)

# Annotations: Define and enforce type constraints
compiled_code = compiler.compile(expression)
exec_locals = {}
exec(compiled_code, {}, exec_locals)
compiled_result = exec_locals['result']
print("Compiled Result:", compiled_result)

# Generate a compiler using the compiler generator
generated_compiler = compiler_generator.generate()
generated_code = generated_compiler(expression)
print("Generated Code:", generated_code)
