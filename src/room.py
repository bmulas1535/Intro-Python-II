# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    """Main room constructor"""
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}."

    def __repr__(self):
        return f"{self}"

