class Llama:
    def __init__ (self, nameOfLlama, catchphrase, blades_of_grass_eaten):
        
        # print("__init__ has run!")
        self.name = nameOfLlama
        self.catchphrase = catchphrase
        self.blades_of_grass_eaten = blades_of_grass_eaten
        self.owner = {"name": "Joey", "age": 29}
        
        
    # methods go here
    def say_info(self):
        print(f"My name is {self.name}")
        print(f"I have eaten {self.blades_of_grass_eaten} blades of grass")
        return self
    def owner_info(self):
        print("My owners name is " + self.owner['name'])
        return self
    def spit(self, nameOfLlama):
        print(self.name + " spit at " + nameOfLlama)
# instances are made here(outside class)
jose = Llama("jose", "What it do?", 17) #{name: "jose"}
harold = Llama("harold", "Howdy!", 998) #{name: "harold"}
jose.say_info().owner_info()
jose.spit(harold.name)
harold.owner_info()

