EXERCISE3:
pending_registrations = []
pending_registrations.append("Sarah")
pending_registrations.append("Assu")
pending_registrations.append("Suba")
print("Total Registrations:", len(pending_registrations))
pending_registrations.pop(1)
print(pending_registrations)

EXERCISE4:

citizens = [
    {"city":"Chennai","name":"Sarah"},
    {"city":"Madurai","name":"Assu"},
    {"city":"Chennai","name":"Suba"}
]

for citizen in citizens:
    if citizen["city"] == "Chennai":
        print(citizen["name"])
