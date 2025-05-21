class Player:
    def __init__(self, name, marker):
        self.name = name
        self.marker = marker

    def get_move(self):
        while True:
            try:
                move = int(input(f"{self.name}, הכנס מספר בין 1 ל-9: "))
                if 1 <= move <= 9:
                    return move
                else:
                    print("הזן מספר בין 1 ל-9")
            except ValueError:
                print("הזן מספר חוקי")

