import QtQuick 2.15
import QtQuick.Controls 2.15

Rectangle {
    width: parent.width
    height: parent.height
    color: "white"

    property string categoryName: "" // Set this from MainPage
    property string selectedFunction: "" // Holds the selected function name
    property var selectedFunctionData: [] // Holds parsed functions for the selected tool
    property var inputFields: [] // Dynamically updated based on the selected function

    ToolsModel {
        id: categoryList
    }

    Component.onCompleted: {
        // Find matching category functions based on categoryName
        for (let i = 0; i < categoryList.count; i++) {
            if (categoryList.get(i).toolName === categoryName) {
                selectedFunctionData = JSON.parse(categoryList.get(i).functions);
                for(let j = 0; j < selectedFunctionData.length; j++){
                    console.log(selectedFunctionData[j].functionName)
                }
                break;
            }
        }
    }

    Column {
        padding: 4
        anchors.fill: parent
        spacing: 8
        // ToolNavigator {
        //     toolName: categoryName
        //     onNavigateBack: stackView.pop()
        // }

        Row {
            width: parent.width
            height: parent.height - y

            // Left panel for tool and function list
            Rectangle {
                width: parent.width * 0.3
                height: parent.height
                color: "#ffffff"

                ListView {
                    spacing: 8
                    anchors.fill: parent
                    model: selectedFunctionData

                    delegate: Button {
                        text: modelData.functionName
                        width: 150
                        height: 40

                        background: Rectangle {
                            implicitWidth: 100
                            implicitHeight: 40
                            color: parent.hovered ? "#eee" : "#fff"
                        }

                        contentItem: Text {
                            text: modelData.functionName
                            color: "#000"
                            font.pixelSize: 15
                            font.family: "Arial"
                            font.weight: Font.Thin
                            horizontalAlignment: Text.AlignHCenter
                            verticalAlignment: Text.AlignVCenter
                        }
                        onClicked: {
                            selectedFunction = modelData.functionName
                            inputFields = modelData.inputs
                        }
                    }
                }
            }

            // Right panel for dynamic inputs and outputs
            Rectangle {
                width: parent.width * 0.7
                height: parent.height
                color: "#ffffff"

                Column {
                    anchors.fill: parent
                    padding: 20
                    spacing: 10

                    Text {
                        text: selectedFunction ? "Function: " + selectedFunction : "Select a function"
                        font.pointSize: 20
                        font.bold: true
                    }

                    // Dynamic input fields section
                    Repeater {
                        id: repeater
                        model: inputFields
                        delegate: TextInput {
                            width: parent.width * 0.8
                            Text {
                                text: modelData.placeholder // Placeholder for each input
                                color: "#aaa"
                                visible: !parent.text && !parent.activeFocus // <----------- ;-)
                            }
                        }
                    }

                    Button {
                        text: "Run " + selectedFunction
                        visible: selectedFunction !== "" // Enable only if a function is selected
                        onClicked: {
                            function getAllFuncs(obj) {
                                let methods = new Set()
                                while (obj = Reflect.getPrototypeOf(obj)) {
                                    let keys = Reflect.ownKeys(obj)
                                    keys.forEach((k) => methods.add(k));
                                }
                                return methods.values();
                            }
                            var inputs = [];
                            for (let i = 0; i < inputFields.length; i++) {
                                let input = repeater.itemAt(i);
                                inputs.push(input ? input.text : "");
                            }

                            console.log("Running function:", selectedFunction, "with inputs:", inputs);

                            for (let j = 0; j < selectedFunctionData.length; j++) {
                                if (selectedFunctionData[j].functionName === selectedFunction) {
                                    console.log("Executing:", selectedFunction);
                                    let result = reconFunctions[selectedFunctionData[j].callBack](...inputs);
                                    console.log("Result:", result);
                                    outputArea.text = result;
                                }
                            }
                        }
                    }

                    // Output section
                    ScrollView {
                        width: parent.width * 0.9
                        height: parent.height - y - 4

                        TextArea {
                            id: outputArea
                            padding: 8
                            background: Rectangle {
                                color: "black"
                                radius: 4
                            }
                            readOnly: true
                            font.family: "monospace"
                            text: "Output will be displayed here."
                            wrapMode: TextEdit.Wrap // Allows text wrapping in the output area
                        }
                    }
                }
            }
        }
    }
}
