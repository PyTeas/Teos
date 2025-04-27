from PySide6.QtWidgets import QMainWindow, QSplitter, QToolBar
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt

from ui.widgets.folder_tree import FolderTree
from ui.widgets.file_list import FileList

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Teos")
        self.resize(1000, 600)

        self.setup_ui()

    def setup_ui(self):
        splitter = QSplitter(Qt.Horizontal)

        self.folder_tree = FolderTree()
        self.file_list = FileList()

        self.folder_tree.folder_selected.connect(self.file_list.set_path)

        splitter.addWidget(self.folder_tree)
        splitter.addWidget(self.file_list)
        splitter.setSizes([300, 700])

        self.setCentralWidget(splitter)

        self.setup_toolbar()

    def setup_toolbar(self):
        toolbar = QToolBar("Основная панель")
        self.addToolBar(toolbar)

        refresh_action = QAction("Обновить", self)
        refresh_action.triggered.connect(self.refresh)
        toolbar.addAction(refresh_action)

    def refresh(self):
        self.folder_tree.refresh()
        self.file_list.refresh()
