class Product:
    """Repräsentiert ein Produkt im Shop-Inventar."""

    def __init__(self, name: str, price: float, quantity: int):
        """Initialisiert ein neues Produkt mit Name, Preis und Menge."""
        if not name:
            raise ValueError("Der Name darf nicht leer sein.")
        if price < 0:
            raise ValueError("Der Preis darf nicht negativ sein.")
        if quantity < 0:
            raise ValueError("Die Menge darf nicht negativ sein.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True


    def get_quantity(self) -> int:
        """Gibt die aktuelle Lagermenge zurück."""
        return self.quantity


    def set_quantity(self, quantity: int):
        """Setzt die Lagermenge. Deaktiviert das Produkt, wenn die Menge <= 0 ist."""
        self.quantity = quantity
        if self.quantity <= 0:
            self.deactivate()


    def is_active(self) -> bool:
        """Prüft, ob das Produkt aktiv ist."""
        return self.active


    def activate(self):
        """Aktiviert das Produkt."""
        self.active = True


    def deactivate(self):
        """Deaktiviert das Produkt."""
        self.active = False


    def show(self):
        """Gibt die Produktdetails auf der Konsole aus."""
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")


    def buy(self, quantity: int) -> float:
        """Kauft eine bestimmte Menge des Produkts und gibt den Gesamtpreis zurück."""
        if not self.is_active():
            raise ValueError("Das Produkt ist nicht mehr aktiv.")
        if quantity <= 0:
            raise ValueError("Die Kaufmenge muss größer als 0 sein.")
        if quantity > self.quantity:
            raise ValueError("Nicht genügend Bestand auf Lager.")

        total_price = float(self.price * quantity)
        self.set_quantity(self.quantity - quantity)
        return total_price


if __name__ == "__main__":
    """Testen der Class. Wird später beim Aufruf aus Main.py ignoriert."""
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()
