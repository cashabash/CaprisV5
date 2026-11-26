import os
import random
import time

# Налаштування поля за замовчуванням (можна змінювати ззовні: engine.border = 15)
border = 10
borderX = border * 2
borderY = border
your_selfBorder = False
empty = "."

_count = 0
_full_line = ""
_wall_callbacks = []


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def wait(tm):
    time.sleep(tm)


def set_wall_clip(func):
    _wall_callbacks.append(func)


def _sync_borders():
    global borderX, borderY
    if not your_selfBorder:
        borderX = border * 2
        borderY = border


def rand_pos():
    _sync_borders()
    return random.randint(0, borderX - 1), random.randint(0, borderY - 1)


def menu(options, text_before):
    clear()
    print(f"-= {text_before} =-")
    for i, item in enumerate(options):
        print(f"{i + 1}. {item}")

    while True:
        try:
            ans = int(input("Choose: ")) - 1
            if 0 <= ans < len(options):
                break
            print(f"Choose a number from 1 to {len(options)}!")
        except ValueError:
            print("Please number!")

    clear()
    return options[ans], ans


def visible(before, entities, after):
    global _full_line
    try:
        clear()
        print(before)
        _sync_borders()
        lines = []
        for y in range(borderY):
            row = []
            for x in range(borderX):
                placed = False
                for ent in entities:
                    if ent.al and ent.x == x and ent.y == y:
                        row.append(ent.type)
                        placed = True
                        break
                if not placed:
                    row.append(empty)
            lines.append("".join(row))

        _full_line = "\n".join(lines) + "\n"
        print(_full_line)
        print(after)
    except Exception as er:
        print("[Visible error]: try to look at doesn't list")
        print(er)


def coll(im, target):
    if im.al and target.al:
        return im.x == target.x and im.y == target.y
    return False


class Block:
    def __init__(self, x, y, sym_type):
        self.x = x
        self.y = y
        self.type = sym_type if len(sym_type) == 1 else "@"
        self.al = True

    @property
    def pos(self):
        return {"x": self.x, "y": self.y}


def multi_block(x, y, text):
    return [Block(x + i, y, ch) for i, ch in enumerate(text)]


class Entity:
    def __init__(self, x, y, name, sym_type):
        global _count
        _count += 1
        self.id = _count
        self.x = x
        self.y = y
        self.name = name
        self.type = sym_type if len(sym_type) == 1 else "@"
        self.al = True

    @property
    def pos(self):
        return {"x": self.x, "y": self.y}

    @property
    def data(self):
        return {
            "x": self.x,
            "y": self.y,
            "type": self.type,
            "name": self.name,
            "id": self.id,
        }

    def anim(self, frames, vis, times, before, after):
        old_type = self.type
        for frame in frames:
            self.type = frame if len(frame) == 1 else "@"
            visible(before, vis, after)
            time.sleep(times)
        self.type = old_type
        visible(before, vis, after)

    def move(self, dx, dy):
        if not self.al:
            return
        _sync_borders()
        new_x = self.x + dx
        new_y = self.y + dy
        if 0 <= new_x < borderX and 0 <= new_y < borderY:
            self.x = new_x
            self.y = new_y
        else:
            for func in _wall_callbacks:
                func()


# Збережемо аліаси у нижньому регістрі, щоб старі виклики теж працювали
block = Block
entity = Entity


if __name__ == "__main__":
    player = Entity(1, 1, "Hero", "P")
    wall = multi_block(4, 1, "###")
    visible("Test frame", [player, *wall], "Use module in main.py")
  
