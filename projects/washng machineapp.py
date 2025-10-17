class WashingMachine:
    def __init__(s):
        s.mode="Normal"
        s.timer30
        s.water="medium"
        s.spin="normal"
        s.running=False
    def start(s):
        if not s.running:
            s.running=True
            return "Washing Machine Started in {} mode for {} minutes with {} water and {} spin."
        else:
            return "Washing Machine is already running."
    def stop(s):
        if s.running:
            s.running=False
            return "Washing Machine Stopped."
        else:
            return "Washing Machine is not running."
    def set_mode(s):
        s.mode=input("Enter mode (Normal/Delicate/Heavy): ")
        print(f"Mode set to {s.mode}")

    def set_timer(s):
        s.timer=int(input("enter time in minutes: "))
        print(f"Timer set to {s.timer} minutes")
    
    def set_water(s):
        s.water=input("Enter water level (low/medium/high): ")
        print(f"Water level set to {s.water}")
    def set_spin(s):
        s.spin=input("Enter spin speed (low/normal/high): ")
        print(f"Spin speed set to {s.spin}")

    def status(s):
        print("Washing Machine Status:")
        print(f"Running: {s.running}")
        print(f"Mode: {s.mode}")
        print(f"Timer: {s.timer} minutes")
        print(f"Water Level: {s.water}")
        print(f"Spin Speed: {s.spin}")
        print("---------------------------")
    def main():
        wm=WashingMachine()
        while True:
            print("1. Start Washing Machine")
            print("2. Stop Washing Machine")
            print("3. Set Mode")
            print("4. Set Timer")
            print("5. Set Water Level")
            print("6. Set Spin Speed")
            print("7. Check Status")
            print("8. Exit")
            choice=int(input("Enter your choice: "))
            if choice==1:
                print(wm.start())
            elif choice==2:
                print(wm.stop())
            elif choice==3:
                wm.set_mode()
            elif choice==4:
                wm.set_timer()
            elif choice==5:
                wm.set_water()
            elif choice==6:
                wm.set_spin()
            elif choice==7:
                wm.status()
            elif choice==8:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")