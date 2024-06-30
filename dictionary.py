# They are used to store data values in key: value pairs

mycars = {
    "brand" : "ford",
    "model" : "mustang",
    "year" : "2023"
}
print(mycars)
# removing an item from dictionary

newcars = mycars.pop("brand")
print(mycars)
print(newcars)
