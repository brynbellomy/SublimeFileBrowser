import sublime

class FileBrowserState:
    def __init__(self):
        self.marked_files = {}

    def set_marked_files(self, window_id, files):
        self.marked_files[window_id] = files

    def get_marked_files(self, window_id):
        return self.marked_files.get(window_id, [])

file_browser_state = FileBrowserState()

def get_marked_files(window):
    return file_browser_state.get_marked_files(window.id())

def set_marked_files(window, files):
    file_browser_state.set_marked_files(window.id(), files)
