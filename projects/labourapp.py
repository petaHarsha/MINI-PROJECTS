class Labourapp:
    def __init__(s):
        s.labours=[]
    def add(s,n,a,sk,w):
        s.labours.append({"name":n,"age":a,"skill":sk,"wage":w,"days":0})
    def work(s,n):
        for l in s.labours:
            if l['name']==n:
                l['days']+=1
                print(f"{n} worked for a day. Total days worked: {l['days']}")
                return
    def salary(s,n):
        for l in s.labours:
            if l['name']==n:
                pay=l['wage']*l['days']
                print(f"{n}'s total salary for {l['days']} days is: ${pay}")
                return
    def view(s):
        for i,l in enumerate(s.labours,1):
            print(f"{i}. Name: {l['name']}, Age: {l['age']}, Skill: {l['skill']}, Wage: ${l['wage']}/day, Days Worked: {l['days']}")
    def remove(s,n):
        s.labours=[l for l in s.labours if l['name']!=n]
def main():
    app=Labourapp()
    while True:
        print("1. Add Labour")
        print("2. Record Work Day")
        print("3. Calculate Salary")
        print("4. View Labours")
        print("5. Remove Labour")
        print("6. Exit")
        choice=int(input("Enter your choice: "))
        if choice==1:
            name=input("Enter labour name: ")
            age=int(input("Enter labour age: "))
            skill=input("Enter labour skill: ")
            wage=float(input("Enter labour wage per day: "))
            app.add(name,age,skill,wage)
        elif choice==2:
            name=input("Enter labour name to record work day: ")
            app.work(name)
        elif choice==3:
            name=input("Enter labour name to calculate salary: ")
            app.salary(name)
        elif choice==4:
            app.view()
        elif choice==5:
            name=input("Enter labour name to remove: ")
            app.remove(name)
        elif choice==6:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
