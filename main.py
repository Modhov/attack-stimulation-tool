# main.py
import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtQml import QQmlApplicationEngine

def main():
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()

    # Load the main QML file
    engine.load("qml/MainPage.qml")

    # Check if the QML file loaded successfully
    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
