# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    """The main player."""
    def __init__(self, location):
        self.location = location

    def __str__(self):
        return f"This is a player!"

    def __repr__(self):
        return f"{self}"
