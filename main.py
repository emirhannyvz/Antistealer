import subprocess
import os
import ctypes
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QTextEdit, QDesktopWidget
from PyQt5.QtCore import Qt
import sys

def get_critical_paths():
    local_app_data = os.environ.get('LOCALAPPDATA', '')
    app_data = os.environ.get('APPDATA', '')

    paths = {
        'Discord': os.path.join(app_data, 'Discord'),
        'Discord Canary': os.path.join(app_data, 'discordcanary'),
        'Discord PTB': os.path.join(app_data, 'discordptb'),
        'Discord Development': os.path.join(app_data, 'discorddevelopment'),
        'Chrome': os.path.join(local_app_data, 'Google', 'Chrome', 'User Data', 'Default'),
        'Edge': os.path.join(local_app_data, 'Microsoft', 'Edge', 'User Data', 'Default'),
        'Opera': os.path.join(app_data, 'Opera Software', 'Opera Stable'),
        'Opera GX': os.path.join(app_data, 'Opera Software', 'Opera GX Stable'),
        'Brave': os.path.join(local_app_data, 'BraveSoftware', 'Brave-Browser', 'User Data', 'Default')
    }
    return paths

critical_files = [
    'Local State', 'Login Data', 'Web Data', 'History', 'Cookies', 'Local Storage',
    'Local Storage/leveldb', 'Session Storage', 'IndexedDB', 'Network', 'Extension Cookies',
    'Preferences', 'Secure Preferences', 'desktop-settings.json', 'settings.json'
]

def lock_file(path):
    try:
        if not os.path.exists(path):
            return False
        
        if os.path.isdir(path):
            cmds = [
                ['icacls', path, '/deny', 'Everyone:(OI)(CI)(F)', '/T'],
                ['icacls', path, '/deny', 'Users:(OI)(CI)(F)', '/T'],
                ['icacls', path, '/inheritance:d']
            ]
        else:
            cmds = [
                ['icacls', path, '/deny', 'Everyone:(F)'],
                ['icacls', path, '/deny', 'Users:(F)'],
                ['icacls', path, '/inheritance:d']
            ]
        
        for cmd in cmds:
            subprocess.run(cmd, check=True, capture_output=True, text=True)
        
        return True
    except Exception as e:
        return False

def unlock_file(path):
    try:
        if not os.path.exists(path):
            return False
            
        cmds = [
            ['icacls', path, '/reset', '/T'],
            ['icacls', path, '/grant', 'Everyone:(OI)(CI)F', '/T']
        ]
        
        for cmd in cmds:
            subprocess.run(cmd, check=True, capture_output=True, text=True)
            
        return True
    except Exception as e:
        return False

# GUI
class AntiRATUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("AntiSteal - @mehdikamber / @emirhannyvz")
        self.resize(600, 400)
        self.center()

        self.setStyleSheet("background-color: #EAEAEA; color: #333333;")
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()

        self.status_bar = QLabel("STATUS: Ready", self)
        self.status_bar.setStyleSheet("""
            border: 1px solid #CCCCCC;
            background-color: #D6D6D6;
            padding: 10px;
            font-size: 14px;
            border-radius: 5px;
        """)
        self.status_bar.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.status_bar)

        self.console_messages = QTextEdit(self)
        self.console_messages.setPlaceholderText("discord.gg/bank")
        self.console_messages.setStyleSheet("""
            border: 1px solid #CCCCCC;
            background-color: #F7F7F7;
            color: #333333;
            font-size: 14px;
            padding: 5px;
            border-radius: 5px;
        """)
        self.console_messages.setReadOnly(True)
        self.console_messages.setContextMenuPolicy(Qt.NoContextMenu)
        self.console_messages.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.console_messages.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        main_layout.addWidget(self.console_messages)

        button_layout = QHBoxLayout()

        lock_button = QPushButton("Lock Files")
        lock_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: #FFFFFF;
                font-size: 14px;
                padding: 10px;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #45A049;
            }
        """)
        lock_button.clicked.connect(self.on_lock_button_clicked)
        button_layout.addWidget(lock_button)

        unlock_button = QPushButton("Unlock Files")
        unlock_button.setStyleSheet("""
            QPushButton {
                background-color: #F44336;
                color: #FFFFFF;
                font-size: 14px;
                padding: 10px;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #D32F2F;
            }
        """)
        unlock_button.clicked.connect(self.on_unlock_button_clicked)
        button_layout.addWidget(unlock_button)

        main_layout.addLayout(button_layout)
        central_widget.setLayout(main_layout)

    def on_lock_button_clicked(self):
        self.console_messages.append("Initializing file lock...")
        QTimer.singleShot(2000, self.lock_files)

    def lock_files(self):
        self.console_messages.append("Locking files...")
        paths = get_critical_paths()

        for app, base_path in paths.items():
            if os.path.exists(base_path):
                self.console_messages.append(f"Locking files for {app}...")
                for file in critical_files:
                    full_path = os.path.join(base_path, file)
                    if lock_file(full_path):
                        self.console_messages.append(f"Locked: {full_path}")
                    else:
                        self.console_messages.append(f"Failed to lock: {full_path}")

        self.console_messages.append("All files locked.")

    def on_unlock_button_clicked(self):
        self.console_messages.append("Initializing file unlock...")
        QTimer.singleShot(2000, self.unlock_files)

    def unlock_files(self):
        self.console_messages.append("Unlocking files...")
        paths = get_critical_paths()

        for app, base_path in paths.items():
            if os.path.exists(base_path):
                self.console_messages.append(f"Unlocking files for {app}...")
                for file in critical_files:
                    full_path = os.path.join(base_path, file)
                    if unlock_file(full_path):
                        self.console_messages.append(f"Unlocked: {full_path}")
                    else:
                        self.console_messages.append(f"Failed to unlock: {full_path}")

        self.console_messages.append("All files unlocked.")

    def center(self):
        frame_geometry = self.frameGeometry()
        screen_center = QDesktopWidget().availableGeometry().center()
        frame_geometry.moveCenter(screen_center)
        self.move(frame_geometry.topLeft())

# Main program entry point
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AntiRATUI()
    window.show()
    sys.exit(app.exec_())
