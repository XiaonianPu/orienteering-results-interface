from Network import Database


class Competitor:
    def __init__(self, competitor_id,  firstname, lastname, club_name, cat_name, chip_no) -> None:
        super().__init__()
        self.chip_no = chip_no
        self.lastname = lastname
        self.firstname = firstname
        self.cat_name = cat_name
        self.club_name = club_name
        self.competitor_id = competitor_id

    @staticmethod
    def request_by_chip(chip_no, stage):
        db, cursor = Database.connect()
        sql = 'select ID, CLUBID, CATEGORYID, FIRSTNAME, LASTNAME from OEVCOMPETITOR where CHIPNUMBER{0}=?'.format(stage)
        cursor.execute(sql, (chip_no,))
        res = cursor.fetchone()
        club_id = cat_id = competitor_id = firstname = lastname = None
        if res is not None:
            competitor_id = res[0]
            club_id = res[1]
            cat_id = res[2]
            firstname = res[3]
            lastname = res[4]
        else:
            raise Exception("No records")

        club_name = None
        if club_id is not None:
            sql = 'select LONGNAME from OEVCLUB where ID=?'
            cursor.execute(sql, (club_id,))
            res = cursor.fetchone()
            club_name = res[0]

        cat_name = None
        if cat_id is not None:
            sql = 'select CATEGORYNAME from OEVCATEGORY where ID=?'
            cursor.execute(sql, (cat_id,))
            res = cursor.fetchone()
            cat_name = res[0]
        Database.close()
        return Competitor(competitor_id, firstname, lastname,club_name, cat_name, chip_no)
