class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return "Human can walk"

    def eat(self):
        return "Human can eat"

    def sit(self):
        return "Human can sit"

    def talk(self):
        return self.name + " is talking"


class Asian(Human):
    language = "Asian"
    skin_color = "White"

    def eat(self):
        return "Asian food"

    def walk(self):
        return "I am Asian, I can also walk"


mustafa = Human("Mustafa", 80)
baran = Asian("Baran", 90)

print(mustafa.walk())
print(baran.walk())

print(mustafa.sit())
print(baran.talk())

print("Language:", baran.language)
print("Skin color:", baran.skin_color)