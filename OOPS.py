#MAKE A UNIVERSTY CLASS OF SECTION , TIMING , STUDENTS , TEACHER

class Universty:
    universty_name = "National textile universty"
    section_name = "bs it 2"
    section_timing = "2pm to 6pm"
    section_teachers = "Naveed sarver,Abu Hurrarah"

    def __init__(self, name):
        self.name = name
        
print(Universty.universty_name)
print(Universty.section_name)
print(Universty.section_timing)
print(Universty.section_teachers)
       
s1 = Universty("Mursaleen")
print(s1.name)

s2 = Universty("Sheran Jutt")
print(s2.name)

s3 = Universty("Raffay")
print(s3.name)