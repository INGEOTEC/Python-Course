cdn = "hour"

if cdn[-1] == cdn[3]:
    print("Equal")


a = ""
b = "Good morning"
if a == b[4]:
    print("Equal")
else:
    print("No equal")


a = "Mario"
output = "Hi! " + a
print(output)

a = "Mario"
output = "Hi! {}".format(a)
print(output)


b = 12.346
output = "Hi, {} Value {:.2f}"
print(output.format(a, b))


b = 12.346
output = "Hi, {1} Value {1:.2f}"
print(output.format(a, b))


