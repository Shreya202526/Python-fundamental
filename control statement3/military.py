age=int(input("Enter Age:"))
bmi=int(input("Enter BMI:"))
runtime=int(input("Enter Running Time:"))
medical=input("Enter Medical:")
if 18<age<25:
    if 18<bmi<25:
        if runtime<=15:
            if medical=="fit":
                print("Selected")
            else:
                print("Medical Rejected")    
        else:
            print("Physical fail")
    else:
        print("BMI fail")        
elif 26<age<30:
   if runtime<=14 and medical=="fit":
       print("Conditional Selection") 
   else:
       print("Rejected")
elif age>30 or age<18:
    print("Not Eligible")              

                         