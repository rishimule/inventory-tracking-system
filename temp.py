class item():

    def __init__(self,type,location,sr_no,department):
        self.type = type
        self.location = location
        self.sr_no = sr_no
        self.department = department

    def __str__(self):

        strin = "The item {} is at location '{}' .".format(self.sr_no,self.location)
