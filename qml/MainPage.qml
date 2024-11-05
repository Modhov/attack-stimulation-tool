// MainPage.qml
import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    width: 640
    height: 480
    title: "My App"

    // StackView to handle page navigation
    StackView {
        id: stackView
        height: parent.height
        width: parent.width
        initialItem: mainPage
    }

    Component {
        id: mainPage

        Rectangle {
            height: parent.height
            width: parent.width
            color: "white"

            Column {
                anchors.centerIn: parent
                spacing: 20

                // App title
                Text {
                    text: "My App Name"
                    font.pointSize: 24
                    horizontalAlignment: Text.AlignHCenter
                    anchors.horizontalCenter: parent.horizontalCenter
                }

                // Row of buttons
                Row {
                    spacing: 10
                    anchors.horizontalCenter: parent.horizontalCenter

                    Button {
                        text: "Recon"
                        onClicked: stackView.push(Qt.resolvedUrl("Category.qml"), {
                            categoryName: "Recon"
                        })
                    }

                    Button {
                        text: "Connect"
                        onClicked: stackView.push(Qt.resolvedUrl("Category.qml"), {
                            categoryName: "Connect"
                        })
                    }
                }
            }
        }
    }
}
