import xml.etree.ElementTree as ET


class Course:
    def __init__(self, course_xml: ET.Element) -> None:
        super().__init__()
        self.name = course_xml.find("./Name").text
        self.length = int(course_xml.find("./Length").text)
        self.climb = int(course_xml.find("./Climb").text)
        self.start = course_xml.find("./CourseControl[@type='Start']/Control")
        self.finish = course_xml.find("./CourseControl[@type='Finish']/Control")
        self.control_list = list(
            map(lambda control: int(control[0].text), course_xml.findall("./CourseControl[@type='Control']")))
