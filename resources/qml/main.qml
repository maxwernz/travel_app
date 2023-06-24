import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    width: 640
    height: 480
    title: qsTr("Hello World")

    Text {
        anchors.centerIn: parent
        text: qsTr("Hello World")
        font.pixelSize: 24
    }
}