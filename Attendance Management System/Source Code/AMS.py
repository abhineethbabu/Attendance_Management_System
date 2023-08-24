import pandas as pd
import smtplib
from email.message import EmailMessage


#function for automated email
def email_alert(subject, body, to):

  msg = EmailMessage()
  msg.set_content(body)
  
  msg['subject'] = subject
  msg['to'] = to
  msg['from'] = "python.attendance@gmail.com"

  user = "name@email.com"
  password = "****************"

  server = smtplib.SMTP("smtp.gmail.com", 587)
  server.starttls()
  server.login(user, password)
  server.send_message(msg)

  server.quit()



class attendance:

    def __init__(self, name, roll):

        self.name=name
        self.roll=roll


    def takeattendance(self):

        while(True):

            self.take=input(f"{self.roll} - {self.name} : ")

            if(self.take=='p' or self.take=='P' or self.take=='A' or self.take=='a'):

                if(self.take=='P' or self.take=='p'):

                    att_list.append(self.take.upper())
                    break

                elif(self.take=='A' or self.take=='a'):

                    absent_list.append(self.roll)
                    att_list.append(self.take.upper())
                    break

            elif(not(self.take=='P' or self.take=='P' or self.take=='a' or self.take=='A')):

                print("\nInvalid input, Please Enter again")

#function to take attendance
def stud_attendance():

    date=input("\nEnter date:")

    for i in range(len(name_list)):

        att_list1.append(attendance(name_list[i], roll_list[i]))


    for i in range(len(roll_list)):

        att_list1[i].takeattendance()

    
    data[date]=att_list

#function to modify attendance
def modify():
    while(True):


        mod=input("\nDo you want to make any modifications (Yes/No): ")

        if(mod.lower()=="no"):
            break

        elif(mod.lower()=="yes"):

            date=input("\nEnter required date(DD/MM/YYYY): ")

            while(True):


                change=input("\nEnter roll number (0 to exit): ")

                if(change=="0"):
                    break

                else:
                   
                    data.loc[data[data['Roll No']==change.upper()].index.tolist(),date] = input("Enter modified attendance: ")

            break



name_list=[]
roll_list=[]
absent_list=[]
att_list1=[]
att_list=[]

#reading csv file with pandas lib
data=pd.read_csv("C:/Users/abhia/OneDrive/Desktop/PYTHON PROJECT/STUD_data1.csv")

#storing values of names and roll number in array
roll_list=data["Roll No"].values
name_list=data["Name"].values
data=pd.DataFrame(data)


#starting screen
print("\n\n ------> WELCOME TO PYTHON ATTENDANCE MANAGEMNT SYSTEM <------ \n\n ")

while(True):

    print("\n\n\n1)Take Attendance\n2)Modify Attendance\n3)EXIT\n")

    choice=int(input("\nEnter your choice: "))

    if(choice==1):

        stud_attendance()
    
    elif(choice==2):

        modify()

    elif(choice==3):
        break

    else:
        print("\nINVALID CHOICE!!")




#For calling email function providing each students email
for i in range(0,len(absent_list)):

    email_alert("ABSENCE ALERT","You have been marked absent for todays class", f'{absent_list[i].lower()}@iiitk.ac.in')



#to store the edited value and save the csv file
data.to_csv(r"C:\Users\abhia\OneDrive\Desktop\PYTHON PROJECT\STUD_data1.csv", index=False)
print(data)

