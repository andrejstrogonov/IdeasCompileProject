# Demonstrating Reflection, Introspection, and Annotations in Python

# Reflection Example
class ReflectionExample:
    def __init__(self, value):
        self.value = value

    def method(self):
        return f"Value is {self.value}"

# Using reflection to dynamically get attributes and methods
reflection_instance = ReflectionExample(10)

# Get the list of attributes and methods
attributes_methods = dir(reflection_instance)
print("Attributes and Methods:", attributes_methods)

# Get the value of an attribute dynamically
value_attr = getattr(reflection_instance, 'value')
print("Value Attribute:", value_attr)

# Call a method dynamically
method_result = getattr(reflection_instance, 'method')()
print("Method Result:", method_result)


# Introspection Example
class IntrospectionExample:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        return f"Name: {self.name}, Age: {self.age}"

# Using introspection to examine the object
introspection_instance = IntrospectionExample("Alice", 30)

# Get the class of an instance
instance_class = introspection_instance.__class__
print("Instance Class:", instance_class)

# Get the module of an instance
instance_module = introspection_instance.__module__
print("Instance Module:", instance_module)

# Get the docstring of a method
method_doc = introspection_instance.display.__doc__
print("Method Docstring:", method_doc)


# Annotations Example
class AnnotationsExample:
    def annotated_method(self, x: int, y: str) -> str:
        """This method takes an integer and a string and returns a string."""
        return f"Integer: {x}, String: {y}"

# Using annotations to get type hints
annotations_instance = AnnotationsExample()

# Get the annotations of a method
method_annotations = annotations_instance.annotated_method.__annotations__
print("Method Annotations:", method_annotations)

# Call the annotated method
annotated_result = annotations_instance.annotated_method(5, "hello")
print("Annotated Method Result:", annotated_result)
