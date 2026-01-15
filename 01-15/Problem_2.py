from abc import ABC, abstractmethod
# ----------BASE CLASS -----------
# abc -> abstract base class 
class Patient(ABC):
    def __init__(self,patient_id,name,age,admission_date):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.admission_date = admission_date
    
    @abstractmethod
    def calculate_bill(self):
        pass

# ----------------INpatient class ---------------------------
class InPatient(Patient):
    def __init__(self, patient_id, name, age, admission_date,room_type,no_of_days,daily_room_charge,doctor_fee):
        super().__init__(patient_id,name,age,admission_date)
        self.room_type = room_type
        self.no_of_days = no_of_days
        self.daily_room_charge = daily_room_charge
        self.doctor_fee = doctor_fee
    def calculate_bill(self):
        room_cost = self.no_of_days*self.daily_room_charge
        total = room_cost+self.doctor_fee
        icu_charge = 0
        senior_discount = 0
        # ICU chargets 
        if self.room_type.upper() =="ICU":
            icu_charge = total*0.20
            total = total +icu_charge
        if self.age>=60:
            senior_discount = total*0.10
            total = total-senior_discount
        self.display_bill(room_cost,icu_charge,senior_discount,total)
    
    def display_bill(self,room_cost,icu_charge,senior_discount,total):
        print("\n-------------IN-PATIENT BILL-------------")
        print(f"Patient ID          : {self.patient_id}")
        print(f"Name          : {self.name}")
        print(f"age          : {self.age}")
        print(f"room type          : {self.room_type}")
        print(f"Days Admitted          : {self.no_of_days}")
        print(f"Room charges          : {self.daily_room_charge}")
        print(f"ICU extra charges          : {icu_charge}")
        print(f"Senior discount          : {senior_discount}")
        print(f"doctor fees          : {self.doctor_fee}")
        print(f"Total payable          : {total}")
