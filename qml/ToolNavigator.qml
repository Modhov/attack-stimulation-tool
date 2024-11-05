// qml/ToolNavigator.qml
import QtQuick 2.15
import QtQuick.Controls 2.15

Row {
    id: navigator
    // anchors.left: parent.left
    // anchors.top: parent.top
    anchors.margins: 10
    spacing: 10

    property string toolName: "Tool Name"

    signal navigateBack()

    Button {
        text: "Back"
        onClicked: navigator.navigateBack()
    }

    Text {
        text: toolName
        font.pointSize: 16
    }
}
