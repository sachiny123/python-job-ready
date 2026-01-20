value = input("Enter any value: ")

# Try to detect the type
if value.isdigit():
    print("Data type: int")
elif value.replace(".", "", 1).isdigit():
    print("Data type: float")
elif value.lower() in ["true", "false"]:
    print("Data type: bool")
else:
    print("Data type: string")
