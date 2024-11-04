class MainPerson:
    def __init__(self, name):
        self.name = name  # Private variable to store the name

#getter
    @property
    def get_name(self):
        return self.name

# Example usage:
# try_usage = MainPerson("Miriam")
#rint(try_usage.name)  # Output: Alice