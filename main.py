# main.py
import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QObject, Slot
import NetworkScanner
import VirusTotal
import ShodanExtension


class ReconFunctions(QObject):
    @Slot(result=list)
    def list_functions(self):
        # Use dir() and filter to get only the callable methods
        return [attr for attr in dir(self) if callable(getattr(self, attr)) and not attr.startswith("_")]

    @Slot(str, result=str)
    def nmap_scan(self, target):
        return str(NetworkScanner.scan_network(target))

    @Slot(str, result=str)
    def virustotal_ip_report(self, target):
        return VirusTotal.format_report(VirusTotal.get_ip_report(target))

    @Slot(str, result=str)
    def shodan_host_info(self, target):
        return ShodanExtension.get_host_info(target)

    @Slot(str, result=str)
    def shodan_open_ports(self, target):
        return ShodanExtension.get_open_ports(target)


def main():
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()

    recon_functions = ReconFunctions()
    engine.rootContext().setContextProperty("reconFunctions", recon_functions)

    # Load the main QML file
    engine.load("qml/MainPage.qml")

    # Check if the QML file loaded successfully
    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
