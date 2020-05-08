import sys
isCurrentSalaryMapping=False
isCurrentNameMapping=False

currentPasscode=""
currentSalary=""
currentCountry=""

for line in sys.stdin:
  line=line.strip()
  # line=line.split("|")
  try:
    EmployeeID,Name,Salary,Country,Passcode=line.split("\t")
    if(Name=="-1"):

      currentSalary=Salary
      currentCountry=Country
      currentPasscode=Passcode
      isCurrentSalaryMapping=True

    else:
      currentName=Name
      isCurrentNameMapping=True


    if isCurrentSalaryMapping and  isCurrentNameMapping:

      currentKey='%s,%s,%s,%s,%s'%(EmployeeID,currentName,currentSalary,currentCountry,currentPasscode)
      isCurrentSalaryMapping=False
      isCurrentNameMapping=False
      print('%s'%(currentKey))

  except:
    pass

