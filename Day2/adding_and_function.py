ADDING:
citizens = ["sarah"]
citizens.append("assu")
citizens.insert(0, "suba")
print(citizens)

FUNCTION WITH LIST:
def show_citizens(citizen_list):
    print("Total Citizens:", len(citizen_list))

    for citizen in citizen_list:
        print("-", citizen)

my_citizens = ["Assu", "Sarah", "Suba"]

show_citizens(my_citizens)
