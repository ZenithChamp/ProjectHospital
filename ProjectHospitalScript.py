import pickle
from tabulate import tabulate
import os
file = open(r"user_dir.dat", "ab+")
file.close()
file = open(r"emp_master.dat", "ab+")
file.close()
file = open(r"patient_dir.dat", "ab+")
file.close()
file = open(r"inventory_dir.dat", "ab+")
file.close()
cur_uid = ''

def register_new():
    username = input("Enter name: ")
    uid = input("Enter UID: ")
    users = []
    if os.path.getsize("user_dir.dat") > 0:
        with open("user_dir.dat", "rb") as f:
            try:
                while True:
                    x = pickle.load(f)
                    users.append(x)
            except EOFError:
                pass
    for user in users:
        if user["uid"] == uid:
            print("\033[0;31mUID already exists!\033[0m")
            print("1. Exit")
            print("2. Try a different UID")
            ch = input("\033[0;31mEnter your choice: \033[0m")
            if ch == "1":
                return
            elif ch == "2":
                return register_new()
    while True:
        pwd = input("Enter your password: ")
        pwd_ch = input("Re-enter your password: ")
        if pwd == pwd_ch:
            new_user = {"uid": uid, "name": username, "password": pwd}
            with open("user_dir.dat", "ab") as f:
                pickle.dump(new_user, f)
            print("\033[0;32mRegistered successfully!\033[0m")
            break
        else:
            print("\033[0;31mPassword mismatch! Try again.\033[0m")


def login():
    global cur_uid
    if os.path.getsize("user_dir.dat") == 0:
        print("\033[0;31mDirectory empty! Please register first.\033[0m")
        register_new()
    uid = input("Enter your UID: ")
    users = []
    with open("user_dir.dat", "rb") as f:
        try:
            while True:
                users.append(pickle.load(f))
        except EOFError:
            pass
    for user in users:
        if user["uid"] == uid:
            cur_uid = uid
            for i in range(5):
                pwd = input("Enter your password: ")
                if user["password"] == pwd:
                    print("\033[0;32mLogged in successfully!\033[0m")
                    print(f"\033[0;32mWelcome back {user["name"]}!\033[0m")
                    return menu()
                else:
                    print(f"\033[0;31mWrong password! {4 - i} tries left.\033[0m")
            print("\033[0;31mToo many failed attempts. Try again later.\033[0m")
            return None
    else:
        print("\033[0;31mUsername not found!\033[0m")
        ch = input("Register as new user? (y/n): ")
        if ch in "Yy":
            return register_new()
        elif ch in "Nn":
            return None
        return None

def ui_1():
    print("Welcome to Diptayan Memorial Hospital")
    print("1. Administrator login")
    print("2. Register new admin account")
    print("3. Employee login")
    print("4. Exit")
    ch0 = input("\033[0;32mEnter your choice: \033[0m")
    if ch0 == "1":
        login()
    elif ch0 == "2":
        register_new()
    elif ch0 == "3":
        emp_login()
    elif ch0 == "4":
        exit()

def menu():
    print("\033[1;33mWhat do you want to work on?\033[0m")
    print("1. Employee Management")
    print("2. Patient Management")
    print("3. Inventory Management")
    print("4. Pharmacy Management")
    print("5. Change password")
    print("6. Remove account")
    print("7. Logout")
    ch = input("\033[0;36mEnter your choice: \033[0m")
    if ch == "1":
        return employee_management()
    elif ch == "2":
        return patient_management()
    elif ch == "3":
        return inventory_management()
    elif ch == "4":
        return pharmacy_management()
    elif ch == "5":
        return change_password()
    elif ch == "6":
        return remove_account()
    elif ch == "7":
        ch = input("\033[0;33mConfirm logout? (y/n) \033[0m")
        if ch in "Yy":
            print("\033[0;34mLogged out! \033[0m")
            return ui_1()
        elif ch in "Nn":
            return menu()
        return menu()
    else:
        return menu()

def emp_login():
        global cur_uid
        uid = input("Enter your UID: ")
        emplist = []
        with open("emp_master.dat", "rb") as f:
            try:
                while True:
                    emplist.append(pickle.load(f))
            except EOFError:
                pass
        for emp in emplist:
            if emp["empid"] == uid:
                cur_uid = uid
                for i in range(5):
                    pwd = input("Enter your password: ")
                    if emp["password"] == pwd:
                        print("\033[0;32mLogged in successfully!\033[0m")
                        print(f"\033[0;32mWelcome back {emp["name"]}!\033[0m")
                        return emp_menu()
                    else:
                        print(f"\033[0;31mWrong password! {4 - i} tries left.\033[0m")
                print("\033[0;31mToo many failed attempts. Try again later.\033[0m")
                return None
        else:
            print("\033[0;31mUsername not found!\033[0m")
            return None
def emp_menu():
    print("\033[1;33mWhat do you want to work on?\033[0m")
    print("1. Patient Management")
    print("2. Inventory Management")
    print("3. Pharmacy Management")
    print("4. Change password")
    print("5. Logout")
    ch = input("\033[0;36mEnter your choice: \033[0m")
    if ch == "1":
        return patient_management()
    elif ch == "2":
        return inventory_management()
    elif ch == "3":
        return pharmacy_management()
    elif ch == "4":
        return change_password_emp()
    elif ch == "5":
        ch = input("\033[0;33mConfirm logout? (y/n) \033[0m")
        if ch in "Yy":
            print("\033[0;34mLogged out! \033[0m")
            return ui_1()
        elif ch in "Nn":
            return emp_menu()
        return emp_menu()
    else:
        return emp_menu()
    
def change_password_emp():
    emplist = []
    with open("emp_master.dat", "rb") as f:
        try:
            while True:
                emplist.append(pickle.load(f))
        except EOFError:
            pass
    for emp in emplist:
        if emp["empid"] == cur_uid:
            while True:
                new_password = input("Enter new password: ")
                if new_password == emp["password"]:
                    print("\033[0;33mNew and old passwords cannot be same!\033[0m")
                    continue
                else:
                    new_password_check = input("Re-enter new password: ")
                    if new_password_check == new_password:
                        emp["password"] = new_password
                        print("\033[0;32mPassword changed successfully!\033[0m")
                        break
                    else:
                        print("\033[0;31mPassword mismatch! Try again. \033[0m")
                        continue
    with open("emp_master.dat", "wb") as f:
        for emp in emplist:
            pickle.dump(emp, f)
    return emp_menu()

def employee_management():
    print("\033[0;36Employee Management: \033[0m")
    print("1. Create new entry")
    print("2. Remove employee")
    print("3. View all entries")
    print("4. Back")
    ch = input("\033[0;36mEnter your choice: \033[0m")
    if ch == "1":
        empid = input("Enter employee ID: ")
        emplist = []
        if os.path.getsize("emp_master.dat") >=0:
            with open("emp_master.dat", "rb") as f:
                try:
                    while True:
                        emplist.append(pickle.load(f))
                except EOFError:
                    pass
        for emp in emplist:
            if emp["empid"] == empid:
                print("\033[0;3m2Employee ID already exists!\033[0m")

        b=0
        while b==0:
            spec = input("Enter employee specification (Cardiologist/Neurologist/Nephrologist/Orthologist/Gynocologist/Surgeon/Medicine & Put N/A IF EMPLOYEE IS NOT DOCTOR): ")
            if spec=="Cardiologist" or spec=="Neurologist" or spec=="Nephrologist" or spec=="Orthologist" or spec=="Gynocologist" or spec=="Surgeon" or spec=="Medicinal" or spec=="N/A":
                b=b+1
                break
            else:
                print("Not proper speciality chosen")
                continue
        name1 = input("Enter employee name: ")
        a=0
        while a==0:
            desig = input("Enter employee designation: ")
            if desig=="Doctor" or desig=="Nurse" or desig=="Janitor" or desig=="Receptionist":
                a=a+1
                break
            else:
                print("Not proper designation chosen")
                continue
        new_entry = {"empid": empid, "name": name1, "designation": desig, "specialty": spec}
        with open("emp_master.dat", "ab+") as f:
            try:
                pickle.dump(new_entry, f)
                f.flush()
            except EOFError:
                pass
        return employee_management()
    elif ch == "2":
        emplist = []
        with open("emp_master.dat", "rb") as f:
            try:
                while True:
                    emplist.append(pickle.load(f))
            except EOFError:
                pass
        em=input("Enter employee ID of employee to be removed: ")
        for e in emplist:
            if e["empid"] == em:
                ch = input("Are you sure you want to remove the account? (y/n): ")
                if ch in "Yy":
                    emplist.remove(e)
                else:
                    return employee_management()
        with open("emp_master.dat", "wb") as f:
            for e in emplist:
                pickle.dump(e, f)
                print("\033[0;33mEmployee removed successfully!\033[0m")
        return employee_management()
    elif ch == "3":
        emplist=[]
        with open("emp_master.dat","rb") as f:
            try:
                while True:
                    emplist.append(pickle.load(f))
            except EOFError:
                pass
        data=[]
        for e in emplist:
            d1=[e["empid"], e["name"] ,e["designation"], e["specialty"]]
            data.append(d1)
        headers= ["Employee ID", "Name", "Designation", "Speciality"]
        print(tabulate(data, headers=headers, tablefmt="grid"))
        return employee_management()
    elif ch == "4":
        return menu()



def patient_management():
    print ("\033[0;36Patient Management: \033[0m")
    print("1. Create new entry")
    print("2. Remove patients")
    print("3. Change ward type")
    print("4. Change doctors")
    print("5. View all entries")
    print("6. Back")
    ch = input("\033[0;36mEnter your choice: \033[0m")
    if ch == "1":
        patid = input("Enter patient ID: ")
        patlist = []
        if os.path.getsize("patient_dir.dat") >= 0:
            with open("patient_dir.dat", "rb") as f:
                try:
                    while True:
                        patlist.append(pickle.load(f))
                except EOFError:
                    pass
        for pat in patlist:
            if pat["patid"] == patid:
                print("\033[0;32mPatient ID already exists!\033[0m")

        name1 = input("Enter patient name: ")
        Ano = int(input("Enter AADHAR number: "))
        Pno = int(input("Enter PhoneNO: "))
        Age = int(input("Enter Age: "))
        Gender = input("Enter Gender (M/F): ")
        BG = input("Enter Blood Group: ")
        DOA = input("Enter Date of Admission: ")
        g= 0
        while g == 0:
            WT = input("Enter type of ward (ICU/ITU/ICCU/A&E/SURGICAL/GERIARTRIC/MATERNITY/ONCOLOGY/GENERAL)")
            if WT == "ICU" or WT == "ITU" or WT == "ICCU" or WT == "A&E" or WT == "SURGICAL" or WT == "GERIATRIC" or WT == "MATERNITY" or WT == "ONCOLOGY" or WT == "GENERAL":
                g = g + 1
                break
            else:
                print("Not proper ward chosen (Capitalise all letters if you are choosing one from options")
                continue
        b = 0
        while b == 0:
            Field = input("Enter type of Doctor needed(Cardiologist/Neurologist/Nephrologist/Orthologist/Gynocologist/Surgeon/Medicine): ")
            if Field == "Cardiologist" or Field == "Neurologist" or Field == "Nephrologist" or Field == "Orthologist" or Field== "Gynocologist" or Field== "Surgeon" or Field == "Medicinal":
                b = b + 1
                break
            else:
                print("Branch not chosen properly (Capitalise (1st letter if you are choosing one from options)")
                continue
        c=0
        while c==0 :
            Doc_ID = input("Enter doctor id: ")
            emplist=[]
            with open("emp_master.dat", "rb") as t:
                try:
                    while True:
                        emplist.append(pickle.load(t))
                except EOFError:
                    pass
                for emp in emplist:
                    if Doc_ID == emp["empid"]:
                        if emp["designation"]=="Doctor":
                            if emp["specialty"]== Field:
                                c=c+1
                                break
                            else:
                                print("Doctor chosen is not of proper field")
                        else:
                            print("Employee chosen is not a doctor")
                    else:
                        print(" ID chosen is not registered")
            t.close()

        new_entry = {"PatientId": patid, "name": name1, "AADHAR number": Ano, "Phone no": Pno, "Age": Age, "Gender": Gender, "Blood Group": BG, "Date of Admission": DOA, "WardType": WT, "Dis": Field, "Doctor Appointed": Doc_ID}
        with open("patient_dir.dat", "ab+") as f:
            try:
                pickle.dump(new_entry, f)
                f.flush()
            except EOFError:
                pass
        return patient_management()
    elif ch == "2":
        patlist = []
        with open("patient_dir.dat", "rb") as f:
            try:
                while True:
                    patlist.append(pickle.load(f))
            except EOFError:
                pass
        p=input("Enter employee ID of employee to be removed: ")
        for pat in patlist:
            if pat["PatientId"] == p:
                ch = input("Are you sure you want to remove the account? (y/n): ")
                if ch in "Yy":
                    patlist.remove(pat)
                else:
                    return patient_management()
        with open("patient_dir.dat", "wb") as f:
            for pat in patlist:
                pickle.dump(pat, f)
                print("\033[0;33mPatient removed successfully!\033[0m")
        return patient_management()
    elif ch == "3":
        patlist = []
        with open("patient_dir.dat", "rb") as f:
            try:
                while True:
                    patlist.append(pickle.load(f))
            except EOFError:
                pass
        p=int(input("Enter patient id of the patient whose ward type is to be changed"))
        for pat in patlist:
            if pat["PatientId"] == p:
                while True:
                    new_wt = input("Enter new ward type: ")
                    if new_wt == pat["WardType"]:
                        print("\033[0;33mNew and old ward types cannot be same!\033[0m")
                        continue
                    else:
                        pat["WardType"] = new_wt
        with open("patient_dir.dat", "wb") as f:
            for pat in patlist:
                pickle.dump(pat, f)
        return patient_management()

    elif ch == "4":
        patlist = []
        with open("patient_dir.dat", "rb") as f:
            try:
                while True:
                    patlist.append(pickle.load(f))
            except EOFError:
                pass
        p = int(input("Enter patient id of the patient whose doc is to be changed"))
        for pat in patlist:
            if pat["PatientId"] == p:
                while True:
                    while c == 0:
                        new_Doc_ID = input("Enter doctor id")
                        emplist = []
                        with open("emp_master.dat", "rb") as t:
                            try:
                                while True:
                                    emplist.append(pickle.load(t))
                            except EOFError:
                                pass
                            for emp in emplist:
                                if new_Doc_ID == emp["empid"]:
                                    if emp["designation"] == "Doctor":
                                        if emp["specialty"] == pat["Dis"]:
                                            if new_Doc_ID != pat["Doctor Appointed"]:
                                                pat["Doctor Appointed"] = new_Doc_ID
                                                c = c + 1
                                                break
                                            else:
                                                print("\033[0;33mNew and old ward types cannot be same!\033[0m")
                                                continue
                                        else:
                                            print("Doctor chosen is not of proper field")
                                    else:
                                        print("Employee chosen is not a doctor")
                                else:
                                    print(" ID chosen is not registered")
                        t.close()
        with open("patient_dir.dat", "wb") as f:
            for pat in patlist:
                pickle.dump(pat, f)
        return patient_management()
    elif ch == "5":
        patlist = []
        with open("patient_dir.dat", "rb") as f:
            try:
                while True:
                    patlist.append(pickle.load(f))
            except EOFError:
                pass
        data = []
        for p in patlist:
            d1 = [p["PatientId"], p["name"], p["AADHAR number"], p["Phone no"], p["Age"], p["Gender"], p["Blood Group"], p["Date of Admission"], p["WardType"], p["Dis"], p["Doctor Appointed"]]
            data.append(d1)
        headers = ["Patient ID", "Name", "AADHAR No", "Phone No", "Age", "Gender", "Blood Group", "D0A", "WT", "ConditionType", "DocID"]
        print(tabulate(data, headers=headers, tablefmt="grid"))
        return patient_management()
    elif ch == "6":
        return menu()

def inventory_management():
    print("\033[0;Inventory Management: \033[0m")
    print("1. Add ward or no of beds available in the ward")
    print("2. Make one less bed filled in a ward")
    print("3. View all entries")
    print("4. Back")
    ch = input("\033[0;36mEnter your choice: \033[0m")
    if ch == "1":
        wardNo = input("Enter ward no: ")
        wardlist = []
        if os.path.getsize("inventory_dir.dat") >=0:
            with open("inventory_dir.dat", "rb") as f:
                try:
                    while True:
                        wardlist.append(pickle.load(f))
                except EOFError:
                    pass
        for ward in wardlist:
            if ward["WardNo"] == wardNo:
                if ward["Con"]=="Contagious":
                    print("WARD IS CONTAGIOUS!! TAKE CAUTION BEFORE ADDING NEW PATIENTS HERE!!")
                ward["nob"]=ward["nob"]+1
                print("\033[0;32mWard Updated!\033[0m")
                with open("inventory_dir.dat", "ab+") as f:
                    try:
                        pickle.dump(ward, f)
                        f.flush()
                    except EOFError:
                        pass
                return inventory_management()

        type = input("Enter ward type: ")
        BedAvailable = input("Enter no of beds available in the ward: ")
        filled = input("Enter whether ward is filled or not: ")
        con=input("Enter whether ward is contagious: ")
        new_entry = {"WardNo": wardNo, "WT": type, "nob": BedAvailable, "BF": filled, "Con": con}
        with open("inventory_dir.dat", "ab+") as f:
            try:
                pickle.dump(new_entry, f)
                f.flush()
            except EOFError:
                pass
        return inventory_management()
    elif ch == "2":
        wardlist = []
        with open("inventory_dir.dat", "rb") as f:
            try:
                while True:
                    wardlist.append(pickle.load(f))
            except EOFError:
                pass
        wt=input("Enter item ID of item to be removed: ")
        for w in wardlist:
            if w["WardNo"] == wt:
                w["nob"]=i["nob"]-1
                with open("inventory_dir.dat.dat", "wb") as f:
                    for w in wardlist:
                        pickle.dump(w, f)
                        print("\033[0;33mWard updated!\033[0m")
                return inventory_management()
    elif ch == "3":
        wardlist=[]
        with open("inventory_dir.dat","rb") as f:
            try:
                while True:
                    wardlist.append(pickle.load(f))
            except EOFError:
                pass
        data=[]
        for w in wardlist:
            d1=[w["WardNo"], w["WT"] ,i["nob"], i["BF"], i["Con"]]
            data.append(d1)
        headers= ["WardNo", "WardType", "No of Beds available", "Ward Full/NotFull", "Contagious"]
        print(tabulate(data, headers=headers, tablefmt="grid"))
        return inventory_management()
    elif ch == "4":
        return menu()



def pharmacy_management():
    print("\033[0;36Pharmacy Management: \033[0m")
    print("1. Add item")
    print("2. Remove item")
    print("3. View all entries")
    print("4. Back")
    ch = input("\033[0;36mEnter your choice: \033[0m")
    if ch == "1":
        itemid = input("Enter item ID: ")
        itemlist = []
        if os.path.getsize("pharmacy_dir.dat") >=0:
            with open("pharmacy_dir.dat", "rb") as f:
                try:
                    while True:
                        itemlist.append(pickle.load(f))
                except EOFError:
                    pass
        for item in itemlist:
            if item["Itemid"] == itemid:
                item["quantity"]=item["quantity"]+1
                print("\033[0;32mItem Updated!\033[0m")
                with open("pharmacy_dir.dat", "ab+") as f:
                    try:
                        pickle.dump(item, f)
                        f.flush()
                    except EOFError:
                        pass
                return pharmacy_management()

        name1 = input("Enter item name: ")
        expdate = input("Enter exp date of item: ")
        quantity = int(input("Enter item quantity: "))
        price=float(input("Enter item price: "))
        new_entry = {"Itemid": itemid, "name": name1, "Expdate": expdate, "quantity": quantity, "price": price}
        with open("pharmacy_dir.dat", "ab+") as f:
            try:
                pickle.dump(new_entry, f)
                f.flush()
            except EOFError:
                pass
        return pharmacy_management()
    elif ch == "2":
        itemlist = []
        with open("pharmacy_dir.dat", "rb") as f:
            try:
                while True:
                    itemlist.append(pickle.load(f))
            except EOFError:
                pass
        it=input("Enter item ID of item to be removed: ")
        for i in itemlist:
            if i["Itemid"] == it:
                i["quantity"]=i["quantity"]-1
                with open("pharmacy_dir.dat", "wb") as f:
                    for i in itemlist:
                        pickle.dump(i, f)
                        print("\033[0;33mItem updated!\033[0m")
                return pharmacy_management()
                if i["quantity"] == 0:
                    itemlist.remove(i)
                else:
                    return pharmacy_management()
        with open("pharmacy_dir.dat", "wb") as f:
            for i in itemlist:
                pickle.dump(i, f)
                print("\033[0;33mItem removed successfully!\033[0m")
        return pharmacy_management()
    elif ch == "3":
        itemlist=[]
        with open("pharmacy_dir.dat","rb") as f:
            try:
                while True:
                    itemlist.append(pickle.load(f))
            except EOFError:
                pass
        data=[]
        for i in itemlist:
            d1=[i["Itemid"], i["name"] ,i["Expdate"], i["quantity"], i["price"]]
            data.append(d1)
        headers= ["Item ID", "Name", "Exp.Date", "Quantity", "Price"]
        print(tabulate(data, headers=headers, tablefmt="grid"))
        return pharmacy_management()
    elif ch == "4":
        return menu()


def change_password():
    users = []
    with open("user_dir.dat", "rb") as f:
        try:
            while True:
                users.append(pickle.load(f))
        except EOFError:
            pass
    for user in users:
        if user["uid"] == cur_uid:
            while True:
                new_password = input("Enter new password: ")
                if new_password == user["password"]:
                    print("\033[0;33mNew and old passwords cannot be same!\033[0m")
                    continue
                else:
                    new_password_check = input("Re-enter new password: ")
                    if new_password_check == new_password:
                        user["password"] = new_password
                        print("\033[0;32mPassword changed successfully!\033[0m")
                        break
                    else:
                        print("\033[0;31mPassword mismatch! Try again. \033[0m")
                        continue
    with open("user_dir.dat", "wb") as f:
        for user in users:
            pickle.dump(user, f)
    return menu()

def remove_account():
    users = []
    with open("user_dir.dat", "rb") as f:
        try:
            while True:
                users.append(pickle.load(f))
        except EOFError:
            pass
    for user in users:
        if user["uid"] == cur_uid:
            ch = input("Are you sure you want to remove the account? (y/n): ")
            if ch in "Yy":
                users.remove(user)
            else:
                return menu()
    with open("user_dir.dat", "wb") as f:
        for user in users:
            pickle.dump(user, f)
            print("\033[0;33mUser removed successfully!\033[0m")
    return ui_1()



while True:
    ui_1()



