"""
Futamura Projection Demonstration

This script demonstrates the three Futamura projections using a simple arithmetic interpreter.

1. First Projection: Specializes the interpreter for a specific program.
2. Second Projection: Creates a compiler from the interpreter.
3. Third Projection: Generates a compiler generator from the interpreter.
"""

# Simple Interpreter for Arithmetic Expressions

def interpret(expression):
    """
    Evaluates arithmetic expressions using Python's eval function.

    Args:
        expression (str): The arithmetic expression to evaluate.

    Returns:
        float: The result of the evaluated expression.

    Supported operations: +, -, *, /
    """
    return eval(expression)

# Specific Program: Define an arithmetic expression to be evaluated
specific_program = "3 + 5 * 2 - 4 / 2"

# First Futamura Projection: Specialize the interpreter for the specific program
# by creating a hardcoded version of the interpreter.

# Second Futamura Projection: Create a compiler from the interpreter
# that generates Python code for a specific program.

# Third Futamura Projection: Create a compiler generator from the interpreter
# that can generate compilers for different programs.

def compiler_generator(interpreter):
    """
    Creates a compiler for a given program using the interpreter.

    Args:
        interpreter (function): The interpreter function to base the compiler on.

    Returns:
        function: A compiler function that generates Python code for a program.
    """
    def generated_compiler(program):
        # Generate Python code as a string
        code = f"result = {program}"
        return code
    return generated_compiler

# Generate a compiler for the specific program
program_compiler = compiler_generator(interpret)

# Compile the specific program
compiled_program_code = program_compiler(specific_program)

# Execute the compiled program
exec_locals_compiled = {}
exec(compiled_program_code, {}, exec_locals_compiled)
result_compiled_program = exec_locals_compiled['result']
print(f"Result using generated compiler: {result_compiled_program}")

def compiler(expression):
    """
    Generates Python code for a specific arithmetic expression.

    Args:
        expression (str): The arithmetic expression to compile.

    Returns:
        str: The generated Python code as a string.
    """
    # Generate Python code as a string
    code = f"result = {expression}"
    return code

# Generate code for the specific program
compiled_code = compiler(specific_program)

# Execute the generated code
exec_locals = {}
exec(compiled_code, {}, exec_locals)
result_compiled = exec_locals['result']
print(f"Result using compiled code: {result_compiled}")

def specialized_interpreter():
    """
    Evaluates the specific arithmetic expression directly.

    Returns:
        float: The result of the evaluated expression.
    """
    return 3 + 5 * 2 - 4 / 2

# Test the specialized interpreter
if __name__ == "__main__":
    # Evaluate using the general interpreter
    result_general = interpret(specific_program)
    print(f"Result using general interpreter: {result_general}")

    # Evaluate using the specialized interpreter
    result_specialized = specialized_interpreter()
    print(f"Result using specialized interpreter: {result_specialized}")

    # Evaluate using the generated compiler
    print(f"Result using generated compiler: {result_compiled_program}")

    # Evaluate using the compiled code
    print(f"Result using compiled code: {result_compiled}")
