from pyFiles import CheckoutInterface as cI


class Main:
    def __init__(self):
        """Main"""
        check = cI.CheckoutInterface()
        screen = check.window_()
        check.home(screen)
        check.make()


if __name__ == "__main__":
    m = Main()
