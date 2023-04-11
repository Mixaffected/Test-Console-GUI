import time


class App:
    import os
    import time
    import keyboard

    selected = 0
    options = ["God Mode", "Add Money", "Infinit Ammo", "Close"]
    active = [False for i in options]

    FPS = 1

    def __init__(self, FPS: int = 15) -> None:
        self.FPS = FPS

    def clear(self):
        self.os.system("cls")

    def redraw(self):
        self.clear()

        for idx, option in enumerate(self.options):
            isActive = self.active[idx]

            output = f"{option}"

            if isActive:
                output = f"<{output}>"

            if idx == self.selected:
                output = f"#{output}#"

            print(output)

    def start(self):
        keyPressed = False

        while True:
            self.time.sleep((1000 / self.FPS) / 1000)

            # selction
            if self.keyboard.is_pressed("down"):
                if not keyPressed:
                    keyPressed = True
                    self.selected += 1
                    if self.selected > len(self.options) - 1:
                        self.selected = 0

            elif self.keyboard.is_pressed("up"):
                if not keyPressed:
                    keyPressed = True
                    self.selected -= 1
                    if self.selected < 0:
                        self.selected = len(self.options) - 1

            elif self.keyboard.is_pressed("enter"):
                if not keyPressed:
                    keyPressed = True
                    self.active[self.selected] = not self.active[self.selected]

            else:
                keyPressed = False

            self.redraw()


if __name__ == "__main__":
    app = App()
    app.start()
