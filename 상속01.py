class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber

    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))

class Student(Person):
    #재정의(덮어쓰기: overriding)
    def __init__(self, name, phoneNumber, subject, studentID):
        #키워드가 없을경우 명시적으로 부모 클래스 생성자 호출
        # Person.__init__(self, name, phoneNumber)
        self.name = name
        self.phoneNumber = phoneNumber
        self.subject = subject
        self.studentID = studentID

    #상속받은 메소드 재정의
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))
        print("Info(Subject:{0}, StudentID: {1})".format(self.subject, self.studentID))


p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "컴공", "991122")
p.printInfo()
s.printInfo()
# print(p.__dict__)
# print(s.__dict__)


