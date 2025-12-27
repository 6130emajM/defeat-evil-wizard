import random

class Character:
    """Base character class with core attributes and methods."""
    
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health
    
    def attack(self, opponent):
        """Deals randomized damage to opponent based on attack power."""
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            opponent.health = 0
    
    def heal(self):
        """Restores health without exceeding max_health."""
        heal_amount = random.randint(20, 30)
        self.health += heal_amount
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} heals for {heal_amount} HP! Current health: {self.health}/{self.max_health}")
    
    def display_stats(self):
        """Displays current character statistics."""
        print(f"\n{'='*40}")
        print(f"{self.name}'s Stats:")
        print(f"Health: {self.health}/{self.max_health}")
        print(f"Attack Power: {self.attack_power}")
        print(f"{'='*40}\n")


class Warrior(Character):
    """Warrior class with high health and balanced attack."""
    
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)
    
    def power_strike(self):
        """Special ability: powerful strike dealing extra damage."""
        return random.randint(35, 45)
    
    def defensive_stance(self):
        """Special ability: temporary defense boost reducing next damage."""
        print(f"{self.name} takes a defensive stance!")
        return True


class Mage(Character):
    """Mage class with lower health but higher attack power."""
    
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)
    
    def fireball(self):
        """Special ability: powerful fire spell."""
        return random.randint(40, 55)
    
    def mana_drain(self):
        """Special ability: drains enemy health and restores own."""
        return random.randint(15, 25)


class Archer(Character):
    """Archer class with ranged attacks and evasion abilities."""
    
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=30)
        self.evading = False
    
    def quick_shot(self):
        """Special ability: double ranged attack with bonus damage."""
        damage = random.randint(self.attack_power + 10, self.attack_power + 20)
        print(f"{self.name} fires a quick shot!")
        return damage
    
    def evade(self):
        """Special ability: avoids the next enemy attack."""
        self.evading = True
        print(f"{self.name} prepares to evade the next attack!")


class Paladin(Character):
    """Paladin class with holy abilities and defensive powers."""
    
    def __init__(self, name):
        super().__init__(name, health=130, attack_power=28)
        self.shielded = False
    
    def holy_strike(self):
        """Special ability: holy attack dealing bonus damage."""
        damage = random.randint(self.attack_power + 12, self.attack_power + 22)
        print(f"{self.name} calls upon holy power!")
        return damage
    
    def divine_shield(self):
        """Special ability: blocks the next incoming attack."""
        self.shielded = True
        print(f"{self.name} raises a divine shield!")


class EvilWizard(Character):
    """Evil Wizard boss with regeneration abilities."""
    
    def __init__(self, name="Evil Wizard"):
        super().__init__(name, health=150, attack_power=20)
    
    def regenerate(self):
        """Regenerates health after each player turn."""
        regen_amount = random.randint(5, 10)
        self.health += regen_amount
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} regenerates {regen_amount} HP! Current health: {self.health}/{self.max_health}")


def create_character():
    """Character creation menu."""
    print("\n" + "="*50)
    print("WELCOME TO: DEFEAT THE EVIL WIZARD")
    print("="*50)
    print("\nChoose your character class:")
    print("1. Warrior - High health, balanced attack")
    print("   Abilities: Power Strike, Defensive Stance")
    print("2. Mage - Lower health, high magic damage")
    print("   Abilities: Fireball, Mana Drain")
    print("3. Archer - Ranged attacks, evasion")
    print("   Abilities: Quick Shot, Evade")
    print("4. Paladin - Holy warrior with defense")
    print("   Abilities: Holy Strike, Divine Shield")
    
    while True:
        choice = input("\nEnter your choice (1-4): ").strip()
        if choice in ['1', '2', '3', '4']:
            break
        print("Invalid choice! Please enter 1, 2, 3, or 4.")
    
    name = input("Enter your character's name: ").strip()
    if not name:
        name = "Hero"
    
    if choice == '1':
        return Warrior(name)
    elif choice == '2':
        return Mage(name)
    elif choice == '3':
        return Archer(name)
    else:
        return Paladin(name)


def battle(player, wizard):
    """Main battle loop implementing turn-based combat."""
    print(f"\n{'='*50}")
    print(f"BATTLE START: {player.name} vs {wizard.name}")
    print(f"{'='*50}\n")
    
    while player.health > 0 and wizard.health > 0:
        # Display current status
        print(f"\n{player.name}: {player.health}/{player.max_health} HP")
        print(f"{wizard.name}: {wizard.health}/{wizard.max_health} HP\n")
        
        # Player turn menu
        print("Choose your action:")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            # Normal attack
            player.attack(wizard)
        
        elif choice == '2':
            # Special abilities based on class
            if isinstance(player, Warrior):
                print("\nSpecial Abilities:")
                print("1. Power Strike - Deal massive damage")
                print("2. Defensive Stance - Reduce next damage taken")
                ability_choice = input("Choose ability (1-2): ").strip()
                
                if ability_choice == '1':
                    damage = player.power_strike()
                    wizard.health -= damage
                    print(f"{player.name} uses Power Strike for {damage} damage!")
                elif ability_choice == '2':
                    player.defensive_stance()
                else:
                    print("Invalid choice! Turn wasted.")
            
            elif isinstance(player, Mage):
                print("\nSpecial Abilities:")
                print("1. Fireball - Cast devastating fire spell")
                print("2. Mana Drain - Drain enemy health and heal")
                ability_choice = input("Choose ability (1-2): ").strip()
                
                if ability_choice == '1':
                    damage = player.fireball()
                    wizard.health -= damage
                    print(f"{player.name} casts Fireball for {damage} damage!")
                elif ability_choice == '2':
                    damage = player.mana_drain()
                    wizard.health -= damage
                    player.health += damage // 2
                    if player.health > player.max_health:
                        player.health = player.max_health
                    print(f"{player.name} drains {damage} HP and restores {damage // 2} HP!")
                else:
                    print("Invalid choice! Turn wasted.")
            
            elif isinstance(player, Archer):
                print("\nSpecial Abilities:")
                print("1. Quick Shot - Fire rapid double shot")
                print("2. Evade - Dodge the next enemy attack")
                ability_choice = input("Choose ability (1-2): ").strip()
                
                if ability_choice == '1':
                    damage = player.quick_shot()
                    wizard.health -= damage
                    print(f"Total damage: {damage}!")
                elif ability_choice == '2':
                    player.evade()
                else:
                    print("Invalid choice! Turn wasted.")
            
            elif isinstance(player, Paladin):
                print("\nSpecial Abilities:")
                print("1. Holy Strike - Strike with holy power")
                print("2. Divine Shield - Block the next attack")
                ability_choice = input("Choose ability (1-2): ").strip()
                
                if ability_choice == '1':
                    damage = player.holy_strike()
                    wizard.health -= damage
                    print(f"Total damage: {damage}!")
                elif ability_choice == '2':
                    player.divine_shield()
                else:
                    print("Invalid choice! Turn wasted.")
        
        elif choice == '3':
            # Heal
            player.heal()
        
        elif choice == '4':
            # View stats
            player.display_stats()
            wizard.display_stats()
            continue  # Don't end turn
        
        else:
            print("Invalid choice! Turn wasted.")
        
        # Check if wizard is defeated
        if wizard.health <= 0:
            break
        
        # Wizard's turn
        print(f"\n--- {wizard.name}'s Turn ---")
        wizard.regenerate()
        
        # Check for evasion or shield
        attack_blocked = False
        if isinstance(player, Archer) and player.evading:
            print(f"{player.name} evades the attack!")
            player.evading = False
            attack_blocked = True
        elif isinstance(player, Paladin) and player.shielded:
            print(f"{player.name}'s divine shield blocks the attack!")
            player.shielded = False
            attack_blocked = True
        
        if not attack_blocked:
            wizard.attack(player)
        
        input("\nPress Enter to continue...")
    
    # Battle end
    print(f"\n{'='*50}")
    if player.health > 0:
        print(f"VICTORY! {player.name} has defeated the {wizard.name}!")
        print(f"Remaining HP: {player.health}/{player.max_health}")
    else:
        print(f"DEFEAT! {player.name} has been defeated by the {wizard.name}...")
        print("The evil wizard lives to threaten the land another day.")
    print(f"{'='*50}\n")


def main():
    """Main game function."""
    player = create_character()
    wizard = EvilWizard()
    battle(player, wizard)
    
    # Ask to play again
    play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()
    if play_again in ['yes', 'y']:
        main()
    else:
        print("\nThanks for playing! Goodbye!")


if __name__ == "__main__":
    main()
