import tkinter as tk
from tkinter import messagebox as mb
import cv2
from PIL import Image, ImageTk


class CameraFrame(tk.Frame):
    """
    A frame that displays the camera feed and allows taking a photo.

    Attributes:
        parent (App): The parent application window.
        video_capture (cv2.VideoCapture): The video capture object for the camera.
        video_label (tkinter.Label): The label that displays the camera feed.

    Methods:
        get_image(): Captures an image from the camera and returns it as a PIL.Image object.
        update_camera(): Updates the camera feed display at regular intervals.
        take_photo(): Captures a photo and displays the editor frame.
        destroy(): Releases the video capture object and destroys the frame.
    """

    def __init__(self, parent):
        """
        Initializes the camera frame and sets up the camera capture.

        Args:
            parent (App): The parent application window.
        """

        super().__init__(parent)
        self.parent = parent

        for i in range(2, -1, -1):
            capture = cv2.VideoCapture(i)
            if capture.isOpened():
                self.video_capture = capture
                break
        else:
            mb.showerror(title='Ошибка', message='Не удалось определить камеру')
            self.parent.show_menu()

        self.video_label = tk.Label(self)
        self.video_label.pack()

        button_frame = tk.Frame(self)
        cancel_button = tk.Button(button_frame, text='Назад', command=self.parent.show_menu)
        cancel_button.pack(side='left')
        submit_button = tk.Button(button_frame, text='Сделать снимок', command=self.take_photo)
        submit_button.pack(side='left')
        button_frame.pack()

        close_button = tk.Button(self, text='Закрыть окно', command=self.parent.destroy)
        close_button.pack()

        self.update_camera()

    def get_image(self):
        """
        Captures an image from the camera and returns it as a PIL.Image object.

        Returns:
            PIL.Image.Image: The captured image.
        """

        _, frame = self.video_capture.read()
        cv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        image = Image.fromarray(cv_image)
        return image

    def update_camera(self):
        """
        Updates the camera feed display at regular intervals.
        """

        image = self.get_image()
        tk_image = ImageTk.PhotoImage(image)
        self.video_label.image = tk_image
        self.video_label.configure(image=tk_image)
        self.video_label.after(10, self.update_camera)

    def take_photo(self):
        """
        Captures a photo and displays the editor frame.
        """

        image = self.get_image()
        self.parent.image = image
        self.parent.show_editor()

    def destroy(self):
        """
        Releases the video capture object and destroys the frame.
        """

        self.video_capture.release()
        super().destroy()
