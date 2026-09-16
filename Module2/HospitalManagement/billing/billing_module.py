'''4. Billing Package

Create a package named "billing".

Create module:
billing_module.py


Implement:


generate_bill()


Take:

- Patient ID
- Consultation Charges
- Medicine Cost
- Test Charges


Calculate total amount:

Total Bill = Consultation Charges + Medicine Cost + Test Charges


Display complete bill.'''
def generate_bill():
    total_bill=0
    id=input("Patient ID:")
    c_charges=int(input("Consultation Charges: "))
    m_cost=int(input("Medicine Cost:"))
    t_charges=int(input("Test Charges:"))
    total_bill=c_charges+m_cost+t_charges
    print("-------Total Bill-----------")
    print("Patient ID",id)
    print("Consultation Charges: ",c_charges)
    print("Medicine Cost:",m_cost)
    print("Test Charges: ",t_charges)
    print("Total Bill: ",total_bill)
    print("------------------------------")




