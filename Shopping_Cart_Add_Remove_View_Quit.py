shopping_cart = []

def main():
  while True:
      print("\n 1.Add 2.View 3.Remove 4.Quit")
      choice = input("Enter choice: ")

      if choice == '1':
        item = input("Item to add: ")
        shopping_cart.append(item)
      
      elif choice == '2':
          if shopping_cart:
              print("Items in your cart: ")
              for item in shopping_cart:
                  print("-", item)
          else:
              print("Your cart is empty.")

      elif choice == '3':
          item = input("Item to remove: ")
          try:
              shopping_cart.remove(item)
              print(f"{item} removed from cart.")
          except ValueError:
              print("Item not found.")

      elif choice == '4':
          break
 
  print("Final cart:", shopping_cart)

main()
