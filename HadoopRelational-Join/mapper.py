
import sys
for line in sys.stdin:
  try:
    EmployeeID="-1"
    Name="-1"
    Salary="-1"
    Country="-1"
    Passcode="-1"
    line=line.strip( )
    words=line.split(",")

    if(len(words)==4):
      EmployeeID=words[0]
      Salary=words[1]
      Country=words[2]
      Passcode=words[3]
    elif (len(words) == 5):
      EmployeeID = words[0]
      Salary = words[1]
      Salary_dec=words[2]
      Salary=Salary+","+Salary_dec
      Country = words[3]
      Passcode = words[4]
    elif (len(words) == 6):
      EmployeeID = words[0]
      Salary = words[1]
      Salary_dec = words[2]
      Salary = Salary + "," + Salary_dec
      Country = words[3]
      Country_dec = words[4]
      Country = Country + "," + Country_dec
      Passcode = words[5]
    else:
      EmployeeID=words[0]
      Name=words[1]
    if(EmployeeID!="-1" and EmployeeID!="Employee ID"):
      print("%s\t%s\t%s\t%s\t%s"%(EmployeeID,Name,Salary,Country,Passcode))
    # print("%s|%s" % (EmployeeID,value))
    # yield(EmployeeID,value)
  except:
    pass
