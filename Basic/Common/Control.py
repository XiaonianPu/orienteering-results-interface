import time
import xml.etree.ElementTree as ET
# from Network import Database


class Control:
    def __init__(self, control_xml: ET.Element, competition_id=None, pk_control_id=None) -> None:
        super().__init__()
        self.competition_id = competition_id
        self.control_number = control_xml.find("./Id").text
        self.control_pos_x = control_xml.find("./MapPosition").attrib["x"]
        self.control_pos_y = control_xml.find("./MapPosition").attrib["y"]
        self.pk_control_id = int(time.time()*10**6) if pk_control_id is None else pk_control_id
