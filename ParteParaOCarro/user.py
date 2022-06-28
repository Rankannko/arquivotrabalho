class User:
    def __init__(self, id, name, hashpass, email) -> None:
        self.name = name
        self.hashpass = hashpass
        self.id = id
        self.email = email
