# class AddmissionForm:

#     def __init__(self):
#         print("Hello World!")

#     pass



# std1 = AddmissionForm()



class AddmissionForm:

    def __init__(self, name, cnic):
        self.name = name
        self.cnic = cnic

    
    def show_detail(self):

        print(f"Your Name is: {self.name} and Your Cnic is: {self.cnic}")



std1 = AddmissionForm("Jawad", "0000")
std2 = AddmissionForm("Ahmad", "1111")



std1.show_detail()

std2.show_detail()



