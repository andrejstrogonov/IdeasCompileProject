# Futamura Projections with SOLID Principles

from typing import Callable

# Single Responsibility: Each class has a single responsibility
class Interpreter:
    def interpret(self, expression: str) -> float:
        """Interprets a mathematical expression and returns the result."""
        return eval(expression)

# Open/Closed: SpecializedInterpreter can be extended without modifying
class SpecializedInterpreter:
    def __init__(self, interpreter: Interpreter):
        self.interpreter = interpreter

    def specialize(self, expression: str) -> Callable[[], float]:
        """Specializes the interpreter for a specific expression."""
        def specialized():
            return self.interpreter.interpret(expression)
        return specialized

# Liskov Substitution: Compiler can be replaced with any subclass
class Compiler:
    def compile(self, expression: str) -> str:
        """Compiles a mathematical expression into Python code."""
        return f"result = {expression}"

# Interface Segregation: CompilerGenerator uses only necessary methods
class CompilerGenerator:
    def __init__(self, interpreter: Interpreter):
        self.interpreter = interpreter

    def generate(self) -> Callable[[str], str]:
        """Generates a compiler from the interpreter."""
        def compiler(expression: str) -> str:
            return self.interpreter.interpret(expression)
        return compiler

# Dependency Inversion: High-level modules do not depend on low-level modules
class FutamuraProjections:
    def __init__(self, interpreter: Interpreter, compiler: Compiler, generator: CompilerGenerator):
        self.interpreter = interpreter
        self.compiler = compiler
        self.generator = generator

    def demonstrate(self, expression: str):
        # Reflection: Dynamically access and modify the interpreter
        reflection_result = getattr(self.interpreter, 'interpret')(expression)
        print("Reflection Result:", reflection_result)

        # Introspection: Examine the types and structures
        print("Interpreter Class:", self.interpreter.__class__)
        print("Interpreter Module:", self.interpreter.__module__)
        print("Interpret Method Annotations:", self.interpreter.interpret.__annotations__)

        # Annotations: Define and enforce type constraints
        compiled_code = self.compiler.compile(expression)
        exec_locals = {}
        exec(compiled_code, {}, exec_locals)
        compiled_result = exec_locals['result']
        print("Compiled Result:", compiled_result)

        # Generate a compiler using the compiler generator
        generated_compiler = self.generator.generate()
        generated_code = generated_compiler(expression)
        print("Generated Code:", generated_code)

# Demonstration of Futamura Projections
interpreter = Interpreter()
compiler = Compiler()
compiler_generator = CompilerGenerator(interpreter)
futamura_projections = FutamuraProjections(interpreter, compiler, compiler_generator)

expression = "3 + 5 * 2 - 4 / 2"
futamura_projections.demonstrate(expression)
