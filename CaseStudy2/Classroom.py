#Name: Arittri Ray
#ID: u3312851
#Date: 12 September 2025
#CaseStudy2

room_state = {
    "projector_on" : False,
    "capacity": 3,
    "topic": ""
}

attendance = set()
temp = []

def toggle_projector():     #turns projector ON/OFF
    room_state["projector_on"] = not room_state["projector_on"]
    status = "ON" if room_state["projector_on"] else "OFF"
    print(f"Projector status: {status}")

def set_topic():    #Sets Topic

    topic = input("Enter topic: ")

    if topic:
        room_state["topic"] = topic
        print(f"The Topic is: {topic}")
        if not room_state["projector_on"]:  #Alerts if the projector is OFF while topic is set
            print("Projector is OFF")
    else:
        print("There is NO topic")

def add_student():  #Adds student to attendance set
    if len(attendance) >= room_state["capacity"]:
        print("The Room Is Full! \nStudent Can't Be Added!")        #alerts if room is full
        return

    name = input("Enter Student Name or ID: ").strip()
    if name:
        if name.lower() in attendance:
            print(f"{name.title()} is already in the room.")        #checks if student is already in the room
        else:
            attendance.add(name.lower())
            print(f"{name.title()} added to classroom. Current students in room: {len(attendance)}")
    else:
        print("Name cannot be empty!")


def remove_student():   #removes students
    name = input("Enter student name: ").strip()
    if name.lower() in attendance:       #checks if student is in the room
        attendance.remove(name)
        print(f"{name.title()} has been removed from the room")
    else:
        print(f"{name.title()} is not in the room")

def add_temp():     #adds temperature to temperature log
    try:
        t = float(input("Enter the temperature(°C) : "))
        temp.append(t)
        print(f"Recorded temperature: {t}°C")
        if t < 16 or t > 28:                        #Alerts when temperature is too low or high
            print("Temperature Warning!")
    except ValueError:
        print("Invalid temperature input")

def show_stats():     #shows temperature stats
    if temp:
        low, high, avg = min(temp), max(temp), sum(temp)/len(temp)
        print(f"Temperature stats: \nMin: {low: .2f}°C \nMax: {high: .2f}°C \nAverage = {avg: .2f}°C")
    else:
        print(f"No temperature readings found!")


def show_report():  #shows the status of the room
    print("~"*14 + "Classroom Report" + "~"*14)
    print(f"Projector: {'ON' if room_state['projector_on'] else 'OFF'}")
    print(f"Capacity: {room_state['capacity']}, Current: {len(attendance)}")
    if len(attendance) >= room_state['capacity']:
        print("ROOM FULL!")
    print(f"Topic: {room_state['topic'] if room_state['topic'] else 'Not set'}")
    print("Students:", ", ".join(sorted(attendance)) if attendance else "None")
    show_stats()
    print("~" * 46)


def main():
    while True:
        print("\n")
        print("="*12 + "Smart Classroom Monitor" + "="*12)
        print("1. Toggle Projector\n2. Set Topic\n3. Add Student\n4. Remove Student\n5. Add Temperature\n6. View Temperature Stats\n7. View Report\n8. Exit")

        choice = input("Choose (1-8): ").strip()

        if choice == "1":
            toggle_projector()
        elif choice == "2":
            set_topic()
        elif choice == "3":
            add_student()
        elif choice == "4":
            remove_student()
        elif choice == "5":
            add_temp()
        elif choice == "6":
            show_stats()
        elif choice == "7":
            show_report()
        elif choice == "8":
            break
        else:
            print("Invalid choice. Please select 1-8.")


    if room_state["topic"] and not room_state["projector_on"]:          #Alerts if the topic is set and the projector is OFF
        print("Reminder: projector is OFF but topic is set!")


if __name__ == "__main__":
    main()

