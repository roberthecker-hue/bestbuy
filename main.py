from products import Product
from store import Store


def start(store_obj):
    """Startet das Menu für den Store."""
    while True:
        print("\n   Store Menu")
        print("   ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        user_choice = input("Please choose an option: ").strip()

        if user_choice == "1":
            pass  # Wird noch implementiert
        elif user_choice == "2":
            pass  # Wird noch implementiert
        elif user_choice == "3":
            pass  # Wird noch implementiert
        elif user_choice == "4":
            print("Goodbye!")
            break
        else:
            print("Error: Invalid option. Please try again.")


def main():
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]
    best_buy = Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()