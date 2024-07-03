import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import PIL
from PIL import Image


class MenuFrame(tk.Frame):
    FILE_TYPES = (
        ('файлы png', '*.png'),
        ('файлы jpg', '*.jpg')
    )

    def __init__(self, parent, ):
        super().__init__(parent)
        self.parent = parent

        self.file_button = tk.Button(self, text='Выбрать файл с изображением',
                command=self.pick_file)
        self.camera_button = tk.Button(self, text='Использовать камеру',
                command=parent.show_camera)
        self.file_button.pack()
        self.camera_button.pack()

    def pick_file(self):
        filename = fd.askopenfilename(filetypes=MenuFrame.FILE_TYPES)
        if not filename.strip():
            return

        try:
            image = Image.open(filename)
            self.parent.image = image
            self.parent.show_editor()
        except (FileNotFoundError, PIL.UnidentifiedImageError):
            mb.showerror(title='Ошибка', message='Не удалось найти файл или содержимое файла повреждено.')
