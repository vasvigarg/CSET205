class Flight:
    def __init__(self, p_id, process, start_time, priority):
        self.p_id = p_id
        self.process = process
        self.start_time = start_time
        self.priority = priority

    def __str__(self):
        return f"{self.p_id} {self.process} {self.start_time} {self.priority}"


def sort_flight_data(flights, sort_param):
    if sort_param == 1:
        flights.sort(key=lambda x: x.p_id)
    elif sort_param == 2:
        flights.sort(key=lambda x: x.start_time)
    elif sort_param == 3:
        flights.sort(key=lambda x: x.priority)
    else:
        print("Invalid sorting parameter. Please choose 1, 2, or 3.")
        return

    for flight in flights:
        print(flight)


# Main program
flights = [
    Flight("P1", "VSCode", 100, "MID"),
    Flight("P23", "Eclipse", 234, "MID"),
    Flight("P93", "Chrome", 189, "High"),
    Flight("P42", "JDK 9", 9, "High"),
    Flight("P9", "CMD", 7, "High"),
    Flight("P87", "NotePad", 23, "Low")
]

sort_param = int(input("Choose the sorting parameter:\n1. Sort by P_ID\n2. Sort by Start Time\n3. Sort by Priority\n"))

sort_flight_data(flights, sort_param)
