class NamingConvention(type):
    def __new__(cls, name, bases, class_dict):
        if not name[0].isupper():
            raise TypeError(f"❌ Class name '{name}' must start with an uppercase letter.")
        print(f"✅ Class '{name}' passed naming convention check.")
        return super().__new__(cls, name, bases, class_dict)

# Try with a proper name
class MyClass(metaclass=NamingConvention):
    pass

# Uncomment to test with an invalid class name
# class myclass(metaclass=NamingConvention):
#     pass
