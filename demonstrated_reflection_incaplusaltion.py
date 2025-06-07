class ExampleClass:
    def __init__(self):
        self._private_attribute = "This is a private attribute"

    def get_private_attribute(self):
        return self._private_attribute

# Demonstrating encapsulation
example = ExampleClass()

# Accessing the private attribute through a public method
encapsulated_value = example.get_private_attribute()
print("Accessed private attribute through encapsulation:", encapsulated_value)

# Access the private attribute using reflection
private_value = getattr(example, '_private_attribute')
print("Accessed private attribute using reflection:", private_value)
