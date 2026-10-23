from products import Product
from store import Store

# ANSI Escape Codes für Farben
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"


def start(store_obj):
    """Startet die interaktive Benutzeroberfläche für den Store."""
    while True:
        print(f"\n{BOLD}{CYAN}   Store Menu{RESET}")
        print(f"{CYAN}   ----------{RESET}")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        user_choice = input(f"\n{YELLOW}Please choose an option: {RESET}").strip()

        if user_choice == "1":
            products = store_obj.get_all_products()
            print(f"\n{CYAN}------ Products in Store ------{RESET}")
            for index, product in enumerate(products, start=1):
                print(f"{index}. {product.name}, Price: ${product.price}, Quantity: {product.quantity}")
            print(f"{CYAN}-------------------------------{RESET}")
            input(f"\n{YELLOW}Press Enter to return to menu...{RESET}")

        elif user_choice == "2":
            total_quantity = store_obj.get_total_quantity()
            print(f"\n{GREEN}Total of {total_quantity} items in store.{RESET}")
            input(f"\n{YELLOW}Press Enter to return to menu...{RESET}")

        elif user_choice == "3":
            products = store_obj.get_all_products()
            shopping_list = []

            print(f"\n{CYAN}------ Available Products ------{RESET}")
            for index, product in enumerate(products, start=1):
                print(
                    f"{index}. {product.name}, Price: ${product.price}, Quantity: {product.quantity}"
                )
            print(f"{CYAN}--------------------------------{RESET}")
            print("When you want to finish order, enter empty text.")

            while True:
                prod_num_input = input(
                    f"{YELLOW}Which product # do you want? {RESET}"
                ).strip()
                if not prod_num_input:
                    break

                try:
                    prod_index = int(prod_num_input) - 1
                    if prod_index < 0 or prod_index >= len(products):
                        print(
                            f"{RED}Error: Invalid product number. Please try again.{RESET}"
                        )
                        continue

                    amount_input = input(
                        f"{YELLOW}What amount do you want? {RESET}"
                    ).strip()
                    amount = int(amount_input)

                    selected_product = products[prod_index]
                    shopping_list.append((selected_product, amount))
                    print(f"{GREEN}Product added to list!{RESET}\n")

                except ValueError:
                    print(
                        f"{RED}Error: Invalid input. Please enter valid numbers.{RESET}\n"
                    )

            if shopping_list:
                # Übersicht der bestellten Artikel anzeigen
                print(f"\n{CYAN}------ Order Summary ------{RESET}")
                for product, amount in shopping_list:
                    subtotal = product.price * amount
                    print(
                        f"- {amount}x {product.name} à ${product.price} = {GREEN}${subtotal}{RESET}"
                    )
                print(f"{CYAN}---------------------------{RESET}")

                try:
                    total_price = store_obj.order(shopping_list)
                    print(f"\n{GREEN}********{RESET}")
                    print(f"{GREEN}Order made! Total payment: ${total_price}{RESET}")
                    print(f"{GREEN}********{RESET}")
                except ValueError as err:
                    print(f"\n{RED}Order failed: {err}{RESET}")

            input(f"\n{YELLOW}Press Enter to return to menu...{RESET}")

        elif user_choice == "4":
            print(f"\n{GREEN}Goodbye! Thanks for shopping with Best Buy.{RESET}")
            break

        else:
            print(f"{RED}Error: Invalid choice. Please select 1-4.{RESET}")


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
