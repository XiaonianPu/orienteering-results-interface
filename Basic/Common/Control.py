import xml.etree.ElementTree as ET


class Control:
    def __init__(self, control_xml: ET.Element) -> None:
        super().__init__()
        self.number = control_xml.find("./Id").text
        self.x = control_xml.find("./MapPosition").attrib["x"]
        self.y = control_xml.find("./MapPosition").attrib["y"]
