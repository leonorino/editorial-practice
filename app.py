import tkinter as tk
import frames


class App(tk.Tk):
    """
    Main application class.

    Attributes:
        current_frame (tkinter.Frame): The currently displayed frame.
        edited_image (PIL.Image.Image): The image currently being edited.

    Methods:
        recenter(): Centers the application window on the screen.
        resize(): Resizes the application window.
        get_required_size(): Returns the required size of the application window.
        show_menu(): Displays the menu frame.
        show_camera(): Displays the camera frame.
        show_editor(): Displays the editor frame.
    """

    def __init__(self):
        """
        Initializes the application window and sets the title.
        """

        super().__init__()
        self.title('Редактор')

        self.current_frame = None
        self.edited_image = None

        self.show_menu()
        self.recenter()

    def recenter(self):
        """
        Centers the application window on the screen based on the required size.
        """

        width, height = self.get_required_size()

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.geometry(f'{width}x{height}+{x}+{y}')

    def resize(self):
        """
        Resizes the application window based on the required size.
        """

        width, height = self.get_required_size()
        self.geometry(f'{width}x{height}')

    def get_required_size(self):
        """
        Returns the required size of the application window.

        Returns:
            tuple: The required width and height of the application window.
        """

        self.update_idletasks()

        if self.current_frame is None:
            width = self.winfo_width()
            height = self.winfo_height()
        else:
            width = self.current_frame.winfo_reqwidth()
            height = self.current_frame.winfo_reqheight()

        return (width, height)

    def show_menu(self):
        """
        Displays the menu frame and centers the application window.
        """

        if self.current_frame is not None:
            self.current_frame.destroy()

        self.current_frame = frames.MenuFrame(self)
        self.current_frame.pack()
        self.recenter()

    def show_camera(self):
        """
        Displays the camera frame and centers the application window.
        """

        if self.current_frame is not None:
            self.current_frame.destroy()

        self.current_frame = frames.CameraFrame(self)
        self.current_frame.pack()
        self.recenter()

    def show_editor(self):
        """
        Displays the editor frame and centers the application window.
        """

        if self.current_frame is not None:
            self.current_frame.destroy()

        self.current_frame = frames.EditorFrame(self)
        self.current_frame.pack()

        self.recenter()
