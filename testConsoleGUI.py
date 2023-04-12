def out():
    try:
        with open("t.txt", "a") as file:
            file.write("Done\n")

    except:
        with open("t.txt", "x") as file:
            file.write("Done\n")


class App:
    import os
    import time
    import keyboard

    isRunning = False

    # exit function
    def close(self):
        self.isRunning = False

    # just so others can simply add their own options
    optionTemplate = {
        "name": "name",
        "enabled": False,
        "toggleOption": True,
        "onTrigger": callable,
        "onEnable": callable,
        "onDisable": callable
    }

    selected = 0
    options = [
        {
            "name": "God Mode",
            "enabled": False,
            "toggleOption": True,
            "onTrigger": callable,
            "onEnable": out,
            "onDisable": out
        },
        {
            "name": "Heal",
            "enabled": False,
            "toggleOption": False,
            "onTrigger": out,
            "onEnable": callable,
            "onDisable": callable
        },
        {
            "name": "Infinite Ammo",
            "enabled": False,
            "toggleOption": True,
            "onTrigger": callable,
            "onEnable": out,
            "onDisable": out
        },
        {
            "name": "Close",
            "enabled": False,
            "toggleOption": False,
            "onTrigger": close,
            "onEnable": callable,
            "onDisable": callable
        }
    ]

    def __init__(self, FPS: int = 15) -> None:
        self.FPS = FPS
        self.isRunning = True

    def redraw(self):
        self.os.system("cls")

        # draw everything
        for idx, option in enumerate(self.options):
            output = f"{option['name']}"

            if option["enabled"]:
                output = f"~{output}~"

            if idx == self.selected:
                output = f"{output} <"

            # if it is not an toggle option then put back on False (Is here because of visual feedback)
            if option["enabled"] and not option["toggleOption"]:
                option["enabled"] = False

            print(output)

    def start(self):
        keyPressed = False

        while True:
            # sleep so long to reach wanted fps count
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
                    self.options[self.selected]["enabled"] = not self.options[self.selected]["enabled"]

                    if self.options[self.selected]["enabled"] and self.options[self.selected]["toggleOption"]:
                        self.options[self.selected]["onEnable"]()

                    elif self.options[self.selected]["enabled"] and not self.options[self.selected]["toggleOption"]:
                        self.options[self.selected]["onTrigger"]()

                    if not self.options[self.selected]["enabled"] and self.options[self.selected]["toggleOption"]:
                        self.options[self.selected]["onDisable"]()

            else:
                keyPressed = False

            self.redraw()


if __name__ == "__main__":
    app = App()
    app.start()
