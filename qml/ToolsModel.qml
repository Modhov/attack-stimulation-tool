// ToolsModel.qml
import QtQuick 2.15

ListModel {
    ListElement {
        toolName: "Recon"
        functions: '[{"functionName": "Nmap Scan", "callBack": "nmap_scan", "inputs": [{"placeholder": "Target IP"}]}, \
                     {"functionName": "VirusTotal IP Report", "callBack": "virustotal_ip_report", "inputs": [{"placeholder": "Target IP"}]}, \
                     {"functionName": "Shodan Host Info", "callBack": "shodan_host_info", "inputs": [{"placeholder": "Target IP"}]}, \
                     {"functionName": "Shodan Open Ports", "callBack": "shodan_open_ports", "inputs": [{"placeholder": "Target IP"}]}]'
    }
    ListElement {
        toolName: "Connect"
        functions: '[]'
    }
}
