import file_Handler
import parser
import re


class Person:
    all_ids = []

    def __init__(self, firstname, lastname, email, national_id, phone_number):
        self.firstname = parser.fname
        self.lastname = parser.lname
        self.email = self.validate_email_address(email)
        self.national_id = self.validate_national_id(national_id)
        self.phone_number = str(phone_number)
        # Person.file_handler.add_to_file(self.__dict__)

    def validate_email_address(self):
        regex = r'\w+([\.-]?\w+)@\w+([\.-]?\w+)\.([a-z]{2,3})$'
        if(re.fullmatch(regex, self.email)):
            print("Valid Email")
        else:
            print("Invalid Email")

        

    def validate_national_id(self, national_id):
        nat_card_list = self.national_id.split()
        end_num = nat_card_list[-1]
        nat_card_list.pop(-1)
        for i in range (10,1,-1):
            for j in nat_card_list:
                sum += (int(j)* i)
        x = sum % 11
        if x<= 2 and x == end_num:
            return 'your national card number is correct'
        elif x > 2 and 11 - x == end_num:
            return 'your national card number is correct'
        else:
            return ' your national card number is not correct! '

        

    def edit_info(self, **kwargs):
        allowed_keys = self.__dict__.keys()
        if all(x in allowed_keys for x in kwargs.keys()):
            self.__dict__.update((k, v) for k, v in kwargs.items())
            return self

        # when s.o attempt to change sth other than instance attributes it raises an error
        else:
            raise ZeroDivisionError("Error! Person's attributes are: firstname, lastname, national_id, email and phone_number!"
                            "You can only edit these ones.")

    def __str__(self):
        return f"{self.firstname.title()} {self.lastname.title()}"


class Register(Person):
    def __init__(self, firstname, lastname, email, national_id, phone_number,id):
        super().__init__(firstname, lastname, email, national_id, phone_number)
        self.id = id
        id =  "lastname" + "national_id"
        if Student:
            file_register_s = file_Handler.filehandler("register_student.csv")
            file_register_s.add_to_file({"id": self.id, "info": Person(self.firstname, self.lastname, self.email, self.national_id, self.phone_number)})
            print(f'{self.firstname} {self.lastname} is successfully registered with id {self.id} ')
            return self.id
        elif Teachers:
            file_register_t = file_Handler.filehandler("register_teacher.csv")
            file_register_t.add_to_file({"id": self.id, "info": Person(self.firstname, self.lastname, self.email, self.national_id, self.phone_number)})
            print(f'{self.firstname} {self.lastname} is successfully registered with id {self.id} ')
            return self.id
        elif EduMember:
            file_register_em = file_Handler.filehandler("register_edu_member.csv")
            file_register_em.add_to_file({"id": self.id, "info": Person(self.firstname, self.lastname, self.email, self.national_id, self.phone_number)})
            print(f'{self.firstname} {self.lastname} is successfully registered with id {self.id} ')
            return self.id

    

class Student(Person):
    def __init__(self, firstname, lastname, email, national_id, phone_number):
        super().__init__(firstname, lastname, email, national_id, phone_number)
    

    

class Teachers(Person):
    def __init__(self, firstname, lastname, email, national_id, phone_number):
        super().__init__(firstname, lastname, email, national_id, phone_number)


class EduMember(Person):
    def __init__(self, firstname, lastname, email, national_id, phone_number):
        super().__init__(firstname, lastname, email, national_id, phone_number)
    
    



