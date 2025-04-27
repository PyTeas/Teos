from PySide6.QtWidgets import QListView
from PySide6.QtWidgets import QFileSystemModel

class FileList(QListView):
    def __init__(self):
        super().__init__()

        self.model = QFileSystemModel()
        self.model.setRootPath("")
        self.setModel(self.model)

    def set_path(self, path):
        self.setRootIndex(self.model.setRootPath(path))

    def refresh(self):
        self.model.refresh()
