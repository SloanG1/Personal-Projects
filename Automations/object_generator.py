"""
This program was written by Gavin Sloan
February 16th, 2025
This program generates the base code for objects in python
"""

# Import Files/Modules

class object_code_generator:
    # Data Attributes
    __object_name = "None"
    __object_data_attributes = []

    # Init
    def __init__(self, object_name="Error", object_data_attributes="Error"):
        self.set_object_name(object_name)
        self.set_object_data_attributes(object_data_attributes)

    # Helpers

    # Create_Class builds the new class using OOP principles
    def create_class(self):
        self.generate_class_head()
        self.generate_data_attributes()
        self.generate_init()
        self.generate_helpers()
        self.generate_getters()
        self.generate_setters()
        self.generate_tostring()

    def create_py_file(self, data):
        with open(f"{self.get_object_name()}.py", "w") as py_file:  # Create a new py file named after the object
            py_file.writelines(data)  # Write data to pyfile

    def write_to_py_file(self, data):
        with open(f"{self.get_object_name()}.py", "a") as py_file:  # append to the newly created pyfile
            py_file.writelines(data)  # Append data to pyfile

    def generate_data_attributes(self):
        self.write_to_py_file("\t# Data Attributes\n") # Create comment for Data Attributes
        for attribute in self.get_object_data_attributes():  # Iterate through data attributes
            data_attributes = f"\t__{attribute} = \"Error\"\n"  # Create private variable
            self.write_to_py_file(f"{data_attributes}")  # Append to pyfile

    def generate_class_head(self):
        class_head = f"class {self.get_object_name()}: \n"  # Create class head
        self.create_py_file(class_head)  # Write to pyfile

    # generate_init function generates the function header
    def generate_init(self):
        self.write_to_py_file("\n\t# Init\n\tdef __init__(self, ")  # Create comment for Init
        for attribute in self.get_object_data_attributes():  # Iterate through data attributes
            if attribute != self.get_object_data_attributes()[-1]:  # If attribute is not the last item in list
                self.write_to_py_file(f"{attribute}, ")  # Append to pyfile
            else:  # If attribute is the last item in list
                self.write_to_py_file(f"{attribute}): \n")  # Append to pyfile
        self.generate_init_tail()  # Call generate_init_tail

    # generate_init_tail function generates the function information
    def generate_init_tail(self):
        for attribute in self.get_object_data_attributes():  # Iterate through data attributes
            init_tail = f"\t\tself.set_{attribute}({attribute})\n"  # Sets data attributes by passing through attribute
            self.write_to_py_file(init_tail)  # Append to pyfile

    def generate_helpers(self):
        self.write_to_py_file("\n\t# Helpers\n")  # Create comment for helpers

    # generate_getters generates all the getters for the object
    def generate_getters(self):
        self.write_to_py_file("\n\t# Getters\n")  # Create comment for getters
        for attribute in self.get_object_data_attributes():  # Iterate through data attributes
            getter = (f"\tdef get_{attribute}(self): \n"  # Create getter function
                      f"\t\treturn self.__{attribute}\n\n")  # Return self.attribute
            self.write_to_py_file(getter)  # Append to pyfile

    def generate_setters(self):
        self.write_to_py_file("\t# Setters\n")  # Create comment for setters
        for attribute in self.get_object_data_attributes():  # Iterate through data attributes
            setter = (f"\tdef set_{attribute}(self, {attribute}): \n"  # Create setter function
                      f"\t\tself.__{attribute} = {attribute}\n\n")  # sets self.attribute equal to attribute
            self.write_to_py_file(setter)  # Append to pyfile

    def generate_tostring(self):
        self.write_to_py_file(f"\t# ToString\n"  # Create comment for tostring
                              f"\tdef __str__(self):\n"  # Create tostring function
                              f"\t\t{self.get_object_name()}_string = \"\""  # Create empty string
                              f"\n\t\t{self.get_object_name()}_string += "  # Add to the empty string
                              f"(f\"{self.get_object_name().title()} Data Attributes-->\\n\\t\"\t")  # Create a heading
        self.generate_tostring_tail()  # Call the tail to the string

    def generate_tostring_tail(self):
        for attribute in self.get_object_data_attributes():  # Iterate through attributes
            self.write_to_py_file(f"\n\t\t\tf\"{attribute.title()}: {chr(123)}self.get_{attribute}(){chr(125)}\\n\\t\"")
        self.write_to_py_file(f")\n\t\treturn {self.get_object_name()}_string")  # Append to pyfile

    # Getters
    def get_object_name(self):
        return self.__object_name

    def get_object_data_attributes(self):
        return self.__object_data_attributes

    # Setters
    def set_object_name(self, object_name):
        self.__object_name = object_name

    def set_object_data_attributes(self, object_data_attributes):
        self.__object_data_attributes = object_data_attributes

    # To String
