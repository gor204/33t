from tkinter import *
import random

window = Tk()
window.geometry("600x600")


class Steam:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    image = PhotoImage(file=r'C:\Users\valer\PycharmProjects\код будущего\Занятие seven\aroma.png').subsample(4, 4)

    def __add__(self, other):
        pass


class Dust:
    image = PhotoImage(
        file=r'C:\Users\valer\PycharmProjects\код будущего\Занятие seven\free-icon-dust-2396941.png').subsample(4, 4)


class Air:
    image = PhotoImage(
        file=r'C:\Users\valer\PycharmProjects\код будущего\Занятие seven\air.png').subsample(4, 4)


class Clay:
    image = PhotoImage(
        file=r'C:\Users\valer\PycharmProjects\код будущего\Занятие seven\free-icon-pottery-7942410.png').subsample(4, 4)


class Frost:
    image = PhotoImage(
        file=r'C:\Users\valer\PycharmProjects\код будущего\Занятие seven\frost.png').subsample(4, 4)


class Energy:
    image = PhotoImage(
        file=r'C:\Users\valer\PycharmProjects\код будущего\Занятие seven\energy.png').subsample(4, 4)


class Wind:
    image = PhotoImage(file=r'C:\Users\valer\PycharmProjects\код будущего\Занятие seven\wind.png').subsample(4, 4)

    def __add__(self, other):
        if isinstance(other, Earth):
            return Dust()

    def __add__(self, other):
        if isinstance(other, Fire):
            return Energy()

    def __add__(self, other):
        if isinstance(other, Air):
            return Frost()


class Earth:
    image = PhotoImage(file=r'C:\Users\valer\PycharmProjects\код будущего\Занятие seven\ground.png').subsample(4, 4)

    def __add__(self, other):
        if isinstance(other, Wind):
            return Dust()
        elif isinstance(other, Water):
            return Clay()


class Fire:
    image = PhotoImage(
        file=r'C:\Users\valer\PycharmProjects\код будущего\Занятие seven\free-icon-fire-9509865.png').subsample(4, 4)

    def __add__(self, other):
        if isinstance(other, Water):
            return Steam()


class Water:
    image = PhotoImage(
        file=r'C:\Users\valer\PycharmProjects\код будущего\Занятие seven\free-icon-water-drop-4246703.png').subsample(4,
                                                                                                                      4)

    def __add__(self, other):
        if isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Clay()


canvas = Canvas(width=600, height=600)
canvas.pack()

elements = [Earth(), Water(), Wind(), Fire(), Air(), Energy(), Frost()]
for elem in elements:
    canvas.create_image(random.randint(50, 550), random.randint(50, 550), image=elem.image)


def move(event):
    images_ids = canvas.find_overlapping(event.x, event.y, event.x + 10, event.y + 10)
    if len(images_ids) == 2:
        image_id_1, image_id_2 = images_ids[0], images_ids[1]

        elem_1 = elements[image_id_1 - 1]
        elem_2 = elements[image_id_2 - 1]

        new_elem = elem_1 + elem_2
        if new_elem not in elements:
            elements.append(new_elem)
            canvas.create_image(event.x, event.y, image=new_elem.image)

    canvas.coords(images_ids, event.x, event.y)


window.bind('<B1-Motion>', move)

window.mainloop()
