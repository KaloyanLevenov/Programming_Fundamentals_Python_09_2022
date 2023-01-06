class Weapon:
    def __init__(self, bullets):
        self.bullets = int(bullets)

    def shoot(self):
        if self.bullets > 0:
            result = "shooting..."
            self.bullets -= 1
        else:
            result = "no bullets left"
        return result

    def __repr__(self):
        return f"Remaining bullets: {self.bullets}"


weapon = Weapon(5)
print(weapon)
print(weapon.shoot())
print(weapon.shoot())
print(weapon)

print(weapon)