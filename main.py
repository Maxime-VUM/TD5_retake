from order import Order

def main():
    # To clear the file output.txt
    file = open("output.xt", "w")
    file.close()
    buy_1 = Order(15, 100, True, "buy_1")
    buy_2 = Order(10, 50, True, "buy_2")
    sell_1 = Order(15, 100, False, "sell_1")
    sell_2 = Order(10, 50, False, "sell_2")
    buy_1 + buy_2
    sell_1 + sell_2
    buy_1 + sell_2
    buy_2 + sell_1
    buy_1 >= buy_2
    buy_1 == buy_2
    buy_1 >= sell_1
    buy_1 <= sell_2

if __name__ == "__main__":
    main()
