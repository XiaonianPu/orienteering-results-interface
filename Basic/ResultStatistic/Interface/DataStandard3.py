import xml.etree.ElementTree as ET
from Struct.My.Control import Control
from Struct.My.Course import Course

_NS = "{http://www.orienteering.org/datastandard/3.0}"

class DS3:

    def __init__(self, xml_path) -> None:
        self.event_id = None
        self.competition_id = None
        self.path = xml_path
        self.et = ET.parse(self.path)
        self.root_node = self.et.getroot()
        self.course_xml_list = self.root_node.findall("./RaceCourseData/Course")
        self.control_xml_list = self.root_node.findall("./RaceCourseData/Control")
        self.course_list:[Course] = []
        self.control_list:[Control] = []
        self.parse_control()
        self.parse_course()

    def parse_course(self):
        for course in self.course_xml_list:
            self.course_list.append(Course(course))

    def parse_control(self):
        for control in self.control_xml_list:
            self.control_list.append(Control(control))
            pass

    def upload(self, competition_id=None):
        for course in self.course_list:
            course.create()
        for control in self.control_list:
            pass