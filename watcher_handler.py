from watchdog.events import FileSystemEventHandler


class MyHandler(FileSystemEventHandler):
    def __init__(self, func, arg1, arg2, arg3, arg4, arg5):
        self.func = func
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.arg4 = arg4
        self.arg5 = arg5

    def on_created(self, event):
        if self.arg5==0:
            self.func(self.arg1, self.arg2, self.arg3, self.arg4)

    def on_modified(self, event):
        if self.arg5==1:
            self.func(self.arg1, self.arg2, self.arg3, self.arg4)
