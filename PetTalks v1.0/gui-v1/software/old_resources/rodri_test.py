import Tkinter as    tk
from   PIL    import Image, ImageTk, ImageDraw
from   os     import listdir,curdir

class BlendedRectangle(object):

    def __init__(self, xpos=0, ypos=0, width=10, height=10, image=None,
            fill='black', intensity=1.0):

            self.xpos = xpos
            self.ypos = ypos
            self.width = width
            self.height = height
            self.image = image
            self.fill = fill
            self.intensity = intensity


            self.coords = (self.xpos, self.ypos, self.xpos+self.width,
                self.ypos+self.height)


            self.bottom_image = self.image.crop(self.coords)


            self.top_image = self.image.crop(self.coords)

            self.draw = ImageDraw.Draw(self.top_image)

            self.draw.polygon([
                (0, 0), (self.width, 0), (self.width, self.height),
                (0, self.height), (0, 0)], fill= self.fill)

            self.blended_graphic_obj = Image.blend(self.bottom_image,
                self.top_image, self.intensity)

            self.image.paste(self.blended_graphic_obj, (self.xpos , self.ypos))

            self.tk_image  = ImageTk.PhotoImage(self.image)

root = tk.Tk()

image = Image.open("my_image.jpg")
image_width, image_height = image.size

canvas = tk.Canvas(root, width=image_width, height=image_height)
canvas.pack()

image_obj = BlendedRectangle(10, 10, 50, 50, image, 'red', intensity=0.3)
canvas.create_image(0, 0, image=image_obj.tk_image, anchor='nw')

root.mainloop()