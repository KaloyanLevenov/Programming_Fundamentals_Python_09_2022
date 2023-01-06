class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        Zoo.__animals += 1
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        if species == 'bird':
            self.birds.append(name)

    def get_info(self, species):
        if species == 'mammal':
            print(
                f"Mammals in {self.name}: {', '.join([animal for animal in self.mammals])}\nTotal animals: {Zoo.__animals}")
        elif species == 'bird':
            print(
                f"Birds in {self.name}: {', '.join([animal for animal in self.birds])}\nTotal animals: {Zoo.__animals}")
        elif species == 'fish':
            print(
                f"Fishes in {self.name}: {', '.join([animal for animal in self.fishes])}\nTotal animals: {Zoo.__animals}")


zoo_name = input()
zoo = Zoo(zoo_name)
number_of_animals = int(input())

for animal in range(number_of_animals):
    animal_info = input()
    species, animal_name = animal_info.split(' ')
    zoo.add_animal(species, animal_name)

species_info = input()
zoo.get_info(species_info)
