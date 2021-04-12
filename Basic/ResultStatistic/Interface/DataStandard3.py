import xml.etree.ElementTree as ET
from Basic.Common.Control import Control
from Basic.Common.Course import Course


class DS3:

    def __init__(self, xml_path) -> None:
        self.event_id = None
        self.competition_id = None
        self.path = xml_path
        self.et = ET.parse(self.path)
        self.root_node = self.et.getroot()
        self.course_xml_list = self.root_node.findall("./RaceCourseData/Course")
        self.control_xml_list = self.root_node.findall("./RaceCourseData/Control")
        self.course_list = []
        self.control_list = []
        self.parse_control()
        self.parse_course()

    def parse_course(self):
        for course in self.course_xml_list:
            self.course_list.append(Course(course))

    def parse_control(self):
        for control in self.control_xml_list:
            self.control_list.append(Control(control))
            pass

    def upload(self,competition_id, event_id=None):
        pass








