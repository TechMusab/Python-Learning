light ="red"

if light == "green":
    print("Go")
elif light == "yellow":
    print("Slow Down")
else:
    print("Stop")

#grades
marks=int(input("Enter your marks: "))
if marks >= 90:
    print("A+")
elif marks >= 80 and marks < 90:
    print("A")
elif marks >= 70 and marks < 80:
    print("B")
elif marks >= 60 and marks < 70:
    print("C")
elif marks >= 50 and marks < 60:
    print("D")
else:
    print("F")



