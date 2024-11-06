// MainPage.qml
import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    width: 640
    height: 480
    title: "NetScan"

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
                    text: "NetScan"
                    font.pointSize: 24
                    horizontalAlignment: Text.AlignHCenter
                    anchors.horizontalCenter: parent.horizontalCenter
                }

                // Row of buttons
                Row {
                    spacing: 10
                    anchors.horizontalCenter: parent.horizontalCenter

                    Button {
                        text: "Start Scanning"
                        width: 200
                        height: 40


                        // Button styling to avoid continuous updates
                        background: Rectangle {
                            implicitWidth: 200
                            implicitHeight: 40
                            color: parent.hovered ? "#111" : "#000"
                            border.color: "black"
                            radius: 5
                        }

                        contentItem: Text {
                            text: "Start Scanning >"
                            color: "#fff"
                            font.pixelSize: 15
                            font.family: "monospace"
                            font.weight: Font.Thin
                            horizontalAlignment: Text.AlignHCenter
                            verticalAlignment: Text.AlignVCenter
                        }

                        onClicked: stackView.push(Qt.resolvedUrl("Category.qml"), {
                            categoryName: "Recon"
                        })
                    }
                }
            }
        }
    }
}
