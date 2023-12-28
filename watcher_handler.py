from watchdog.events import FileSystemEventHandler


class MyHandler(FileSystemEventHandler):
    # patterns = ["*.jpg", "*.jpeg"]

    def __init__(self, func, arg1, arg2, arg3, arg4):
        self.func = func
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.arg4 = arg4

    def on_created(self, event):
        # This method will be called when a new file is created
        print(f"New file {event.src_path} has been created.")
        # Call your function here with the required arguments
        self.func(self.arg1, self.arg2, self.arg3, self.arg4)
