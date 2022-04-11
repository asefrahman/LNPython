monthConversions = {
"Jan": "January",
"Feb": "February",
"Mar": "March",
0: "December",
True: "Yes"
}

print(monthConversions["Mar"])
print(monthConversions[0])
print(monthConversions.get("Luv"))
print(monthConversions.get("Luv", "Not a valid key"))
print(monthConversions[True])