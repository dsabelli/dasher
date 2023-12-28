from watchdog.events import FileSystemEventHandler


class MyHandler(FileSystemEventHandler):
    def __init__(self, func, arg1, arg2, arg3, arg4):
        self.func = func
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.arg4 = arg4

    def on_any_event(self, event):
        self.func(self.arg1, self.arg2, self.arg3, self.arg4)
