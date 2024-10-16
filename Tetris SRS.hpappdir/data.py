"""

Data file named save.txt, is like :

    max_score:int:4320;
    das:float:0.167;
    arr:float:0.033;

Details :
    name_of_the_value:type_of_the_value:value

Character "\n" separate the values

"""


class Data:

    def __init__(self):
        self.dictionary = {}
        self.get_values()

    # Get the dictionary from the save file (or create a new one if no save file or corrupt file)
    def get_values(self):

        try:
            f = open('save.txt', 'r')

        except OSError:
            # Fail to open file (don't exist or corrupted). Get base configuration
            self.dictionary = base_dictionary
            return

        d = {}

        values = f.read().split("\n")

        # Remove empty element in the list
        values = list(filter(None, values))

        for items in values:
            item = items.split(":")

            if len(item) != 3:
                continue

            # Normally now item like this : item = ["name", "type", "value"]
            # They all string

            d[str(item[0])] = Var(item[1], convert_type(item[1], item[2]))

        f.close()

        temp = base_dictionary.copy()

        # Check if values from the save file are missing, at the end of the loop, temp is a dict with the keys missing
        for key in d:
            temp.pop(key, None)

        # That means one or more values are missing from the save file
        if len(temp) != 0:
            for key in temp:
                # Add the values missing using the base_dictionary
                d[key] = base_dictionary[key]

        self.dictionary = d

    # Save the dictionary into the save file
    def save(self):
        f = open('save.txt', 'w')
        string = self.str_save()
        f.write(string)

    # Return string to put in save file
    def str_save(self):
        string = ""

        for thing in self.dictionary:
            string += (thing + ":" + str(self.dictionary[thing].value_type) + ":" + str(
                self.dictionary[thing].value) + "\n")

        return string

    # Return one value from dictionary
    def get(self, name):
        return self.dictionary[str(name)].value

    # For code simplicity
    def __call__(self, name):
        return self.get(str(name))

    # Set one value onto dictionary
    def set(self, name, value):
        self.dictionary[str(name)].value = value


# Convert the value to the type in parameter
def convert_type(value_type, value):
    if value_type == "str":
        return str(value)
    elif value_type == "int":
        return int(value)
    elif value_type == "float":
        return float(value)


class Var:
    def __init__(self, value_type, value):
        self.value_type = str(value_type)
        self.value = None
        self.set_value(value)

    def set_value(self, value):
        self.value = convert_type(self.value_type, value)



base_dictionary = {'best_time': Var("int", 0),
                   'ARR': Var("float", 0.033),
                   'DAS': Var("float", 0.167),
                   'DCD': Var("float", 0.017),
                   'SDF': Var("int", 4)}
