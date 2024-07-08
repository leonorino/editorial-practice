import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import PIL
from PIL import Image


class MenuFrame(tk.Frame):
    """
    A frame that displays the menu options for the image editor.

    Attributes:
        parent (App): The parent application window.
        FILE_TYPES (tuple): A tuple of file types for the file dialog.
        file_button (tkinter.Button): The button for selecting an image file.
        camera_button (tkinter.Button): The button for using the camera.

    Methods:
        pick_file(): Opens a file dialog to select an image file and displays the editor frame.
    """

    FILE_TYPES = (
        ('файлы png', '*.png'),
        ('файлы jpg', '*.jpg')
    )

    def __init__(self, parent):
        """
        Initializes the menu frame and sets up the menu buttons.

        Args:
            parent (App): The parent application window.
        """

        super().__init__(parent)
        self.parent = parent

        file_button = tk.Button(self, text='Выбрать файл с изображением',
                command=self.pick_file)
        camera_button = tk.Button(self, text='Использовать камеру',
                command=parent.show_camera)
        close_button = tk.Button(self, text='Закрыть окно', command=self.parent.destroy)
        file_button.pack()
        camera_button.pack()
        close_button.pack()

    def pick_file(self):
        """
        Opens a file dialog to select an image file and displays the editor frame.
        """

        filename = fd.askopenfilename(filetypes=MenuFrame.FILE_TYPES)
        if not filename.strip():
            return

        try:
            image = Image.open(filename)
            self.parent.image = image
            self.parent.show_editor()
        except (FileNotFoundError, PIL.UnidentifiedImageError):
            mb.showerror(title='Ошибка', message='Не удалось найти файл или содержимое файла повреждено.')
