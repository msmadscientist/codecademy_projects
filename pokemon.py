class Pokemon:
    def __init__ (self, name, level, type, max_health, health, is_knocked_out):
        self.name = name
        self.level = level
        self.type = type
        self.max_health = max_health
        self.health = health
        self.is_knocked_out = is_knocked_out
        
    def lose_health (self, health_change):
        self.health = self.health - health_change
        if self.health <= 0:
            self.health = 0
            print("{} is knocked out.".format(self.name))
            self.is_knocked_out = True
            
    def gain_health (self, health_change):
        self.health = self.health + health_change
        if self.health > self.max_health:
            self.health = self.max_health
        if self.health > 0:
            self.is_knocked_out = False
        print("{} now has {} health.".format(self.name,self.health))
        
    def attack (self, other_pokemon):
        damage = 0
        if self.type == "Fire" and other_pokemon.type == "Fire":
            damage = 0.5 * self.level
        elif self.type == "Fire" and other_pokemon.type == "Water":
             damage = 0.5 * self.level
        elif self.type == "Fire" and other_pokemon.type == "Grass":
            damage = 2 * self.level
        elif self.type == "Water" and other_pokemon.type == "Fire":
            damage = 2 * self.level
        elif self.type == "Water" and other_pokemon.type == "Water":
            damage = 0.5 * self.level
        elif self.type == "Water" and other_pokemon.type == "Grass":
            damage = 0.5 * self.level
        elif self.type == "Grass" and other_pokemon.type == "Fire":
            damage = 0.5 * self.level
        elif self.type == "Grass" and other_pokemon.type == "Water":
            damage = 2 * self.level
        else:
            damage = 0.5 * self.level            
        
        print("{} has attacked {} and caused {} points of damage.".format(self.name, other_pokemon.name,damage))
        Pokemon.lose_health(other_pokemon,damage)
        print("{}'s health is now {}.".format(other_pokemon.name, other_pokemon.health))
        

class Trainer (Pokemon):
    def __init__ (self, name, pokemons, current_pokemon, potions):
        self.name = name
        self.pokemons = pokemons
        self.current_pokemon = current_pokemon
        self.potions = potions
        len(pokemons) <= 6
        
    def use_potion (self, potion):
        Pokemon.gain_health(self.current_pokemon,self.potions[potion])   
        
    def attack_other_trainer (self, other_trainer):
        if self.current_pokemon.is_knocked_out == False:
            Pokemon.attack(self.current_pokemon,other_trainer.current_pokemon)
        else:
            print("{} is knocked out and cannot attack.".format(self.current_pokemon.name))
        
    def change_current_pokemon (self, new_pokemon):
        if new_pokemon in self.pokemons and new_pokemon != self.current_pokemon:
            self.current_pokemon = new_pokemon
            print("Current pokemon is now {}.".format(self.current_pokemon.name))
        elif self.current_pokemon.is_knocked_out:
            print("You cannot change to a pokemon that is knocked out.  Try again.")
        else:
            print("This change is not allowed. Try again.")
