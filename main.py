def main():
    print("███████╗███╗   ███╗ ██████╗ ██╗  ██╗ ██╗██████╗\n"
          "██╔════╝████╗ ████║██╔═████╗██║ ██╔╝███║██╔══██\n"
          "█████╗  ██╔████╔██║██║██╔██║█████╔╝ ╚██║██║  ██║\n"
          "██╔══╝  ██║╚██╔╝██║████╔╝██║██╔═██╗  ██║██║  ██║\n"
          "███████╗██║ ╚═╝ ██║╚██████╔╝██║  ██╗ ██║██████╔╝\n"
          "╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═╝╚═════╝ ")
    print("\n"*3)
    while True:
        print("Make your choise!~~\n"
              "Сложить: +\n"
              "Вычесть: -\n"
              "Умножить: *\n"
              "Поделить: /\n"
              "Выйти: exit\n")
        action = input("Действие: ")
        if action == "exit":
            print("Выход из программы")
            break
        if action in ('+', '-', '*', '/'):
            x = float(input("x = "))
            y = float(input("y = "))

            if action == '+':
                print('%.2f + %.2f = %.2f' % (x, y, x+y))
                print("\n")

            if action == '-':
                print('%.2f - %.2f = %.2f' % (x, y, x-y))
                print("\n")

            elif action == '*':
                print('%.2f * %.2f = %.2f' % (x, y, x*y))
                print("\n")

            elif action == '/':
                if y != 0:
                    print('%.2f / %.2f = %.2f' % (x, y, x/y))
                else:
                    print("На ноль не дели!")


if __name__ == '__main__':
    main()


