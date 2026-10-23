from products import Product


class Store:
    """Repräsentiert das Geschäft, das eine Liste von Produkten verwaltet."""

    def __init__(self, products=None):
        """Initialisiert den Store mit einer Liste von Produkten."""
        if products is None:
            self.products = []
        else:
            self.products = products

    def add_product(self, product: Product):
        """Fügt ein Produkt zur Produktliste des Stores hinzu."""
        self.products.append(product)

    def remove_product(self, product: Product):
        """Entfernt ein Produkt aus dem Store, falls vorhanden."""
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        """Gibt die Gesamtzahl aller Artikel im Store zurück."""
        total = 0
        for product in self.products:
            total += product.get_quantity()
        return total

    def get_all_products(self):
        """Gibt eine Liste aller aktiven Produkte im Store zurück."""
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list) -> float:
        """Kauft eine Liste von Produkten (Tupel aus Produkt und Menge) und gibt den Gesamtpreis zurück."""
        total_price = 0.0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price


if __name__ == "__main__":
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = Store(product_list)
    active_products = best_buy.get_all_products()

    print(best_buy.get_total_quantity())
    print(best_buy.order([(active_products[0], 1), (active_products[1], 2)]))

