#coding=utf-8
import random

class RD(object):
    def __init__(self,dr):
        self.driver = dr

    def rd_email(self):
        try:
            rd_list = []
            for i in range(5):
                register_email = "".join(random.sample("abcdefghijklmnopqrst",8))+ "."+"1" +"_"+ "2"+"@chacuo.net"
                rd_list.append(register_email)
            rd_email = rd_list[random.randrange(0,len(rd_list))]
            # print(rd_email)
            return rd_email

        except Exception as e:
            return  e

    def rd_name(self):
        try:
            name_list = []
            for i in range(5):
                register_name = "".join(random.sample("abcdefghopqrstuvwxyzABCDEFG._-",5))+ " "+"_test"
                name_list.append(register_name)
            rd_name = name_list[random.randrange(0,len(name_list))]
            # print(rd_name)
            return rd_name

        except Exception as e:
            return e

    def return_password(self):
        return  "123456"

    def return_short_password(self):
        return  "12345"

    def return_login_email(self):
        return  "Sunny_hongtest@patazon.net","Sunny123"

    def return_city(self):

        city_list =["Cheyenne","Chicago" ,"Cincinati","Columbia(SC)","Dallas","Des Moines","Detroit","Dover(DE)","Frankfort(KY)","Hartford(AL)"
                    ,"Helena(MT)","Houston","Indianapolis","Jackson(MS)","Providence(RI)","Raleigh","Richmond(VA)"
                    ,"Sacramento","Salem(OR)","Salt Lake City","San Francisco","Santa Fe(NM)","Seattle","Springfield(IL)"
                    ,"St Louis","St Louis","St Paul","Tallahassee","Topeka","Trenton(NJ)","Washington D. C.","Alaska"
                    ,"Annapolis","Augusta(ME)","Austin(TX)","Bismarck","Boise","Boston","Lincoln(NE)","Los Angeles"
                    ,"New Orleans"]

        rd_city= city_list[random.randrange(0,len(city_list))]
        return rd_city



# a = RD()
# a.return_city()