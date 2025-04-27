from PySide6.QtWidgets import QTreeView
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QFileSystemModel

class FolderTree(QTreeView):
    folder_selected = Signal(str)

    def __init__(self):
        super().__init__()

        self.model = QFileSystemModel()
        self.model.setRootPath("")
        self.setModel(self.model)

        self.setRootIndex(self.model.index(""))
        self.setHeaderHidden(True)
        self.setAnimated(True)
        self.setIndentation(20)

        self.setColumnHidden(1, True)
        self.setColumnHidden(2, True)
        self.setColumnHidden(3, True)

        self.selectionModel().selectionChanged.connect(self.on_selection_changed)

    def on_selection_changed(self, selected, deselected):
        index = self.selectionModel().currentIndex()
        path = self.model.filePath(index)
        self.folder_selected.emit(path)

    def refresh(self):
        self.model.refresh()
