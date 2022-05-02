# Write Your Code In This File


# 1 Define an animal class, it should have the attributes name,breed and diet. Diet should be a list. Name and breed should be passed through the constructor.


class Animal:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.diet = []
# 2 Give the animal class an eat method that accepts a paremeter of food. This method to add the provided food to the diet list.

    def eat(self, food):
        self.food = food
        self.diet.append(food)

    def get_diet(self):
        return(self.diet)


# 3 Define a dog class, it should accept name,breed and color as attributes. It should inherit from the animal class. Make sure to pass the dog class name and breed to the animal class! Color should only belong to the dog class.

class Dog(Animal):
    def __init__(self, name, breed, color):
        super().__init__(name, breed)
        self.color = color

# 4 The dog class should have a 2 methods, bark and what_color. The bark method should print the name of the dog that barked, example: Fido barked! The what_color method to should tell me the name of the dog followed by what color they are.
    def bark(self):
        print('{name} barked!'.format(name=self.name))

    def what_color(self):
        print('This is {name} and he is the color {color}'.format(
            name=self.name, color=self.color))

# 5 Create a cat class.It should inherit from the animal as well. Cat should accept name,breed and has_claws as attributes. Pass the name and breed to the animal class, has_claws should be a boolean and unique to the cat class.


class Cat(Animal):
    def __init__(self, name, breed, has_claws):
        super().__init__(name, breed)
        self.has_claws = True

        # 6 Give the cat class two methods: check_has_claws and meow. check_has_claws should check if the cat has claws and print a message stating whether it does or not. The meow method should print the name of the cat and if it meowed or not.
    def check_has_claws(self):
        if self.has_claws == True:
            print("The cat has claws")
        else:
            print("The cat does not have claws")

    def meow(self):
        print("{name} meowed".format(name=self.name))


doggo = Dog('Ned', "Lab", "Black")
doggo.bark()
doggo.what_color()
doggo.eat("banana")
print(doggo.diet)
# print(doggo.diet)

# 7 Create a new instance of the dog class and test your methods.

# 8 Make your instance of the dog class eat some food and print what food's it has eaten.

# 9 Create a new instance of the cat class and test your methods.

# 10 Make your instance of the cat class eat some food and print out what food it has eaten.
