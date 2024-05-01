#Jay Gaines
#4/30/2024

def getDatesWorked():
    fromDate = input("Please enter a start date in the following format MM/DD/YYYY: ")
    endDate = input("Please enter the end date in the following format MM/DD/YYYY: ")
    return fromDate, endDate

def getEmpName():
    empName = input("ENter employee name: ")
    return empName

def getHoursWorked():
    hours = float(input("Enter hours: "))
    return hours

def getHourlyRate():
    hourlyRate = float(input("Enter hourly rate: "))
    return hourlyRate

def getTaxRate():
    taxRate = float(input("Enter tax rate: "))
    return taxRate

def CalcTaxAndNetPay(hours, hourlyRate, taxRate):
    gPay = hours * hourlyRate
    incomeTax = gPay * taxRate
    netPay = gPay - incomeTax
    return gPay, incomeTax, netPay

def printInfo(empDetailList):
    totalEmployees = 0
    totalHours = 0.00
    totalGrossPay = 0.00
    totalTax = 0.00
    totalNetPay = 0.00
    for empList in empDetailList:
        fromDate = empList[0]
        endDate = empList[1]
        empName = empList[2]
        hours = empList[3]
        hourlyRate = empList[4]
        taxRate = empList[5]
        grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyRate, taxRate)
        print(fromDate, endDate, empName, f"{hours:,.2f}", f"{hourlyRate:,.2f}", f"{grosspay:,.2f}", f"{taxRate:,.1%}", f"{incometax:,.2f}", f"{netpay:.2f}")
        totalEmployees += 1
        totalHours += hours
        totalGrossPay += grosspay
        totalTax += incometax
        totalNetPay += netpay
        empTotals["totEmp"] = totalEmployees
        empTotals["totHours"] = totalHours
        empTotals["totGross"] = totalGrossPay
        empTotals["totTax"] = totalTax
        empTotals["totNet"] = totalNetPay
        
def printTotals(empTotals):
    print(f'Total Number of Employees: {empTotals["totEmp"]}')
    print(f'Total hours for Employees: {empTotals["totHours"]}')
    print(f'Total gross pay for employees: {empTotals["totGross"]}')
    print(f'Total tax for employees: {empTotals["totTax"]}')
    print(f'Total net paay of employees: {empTotals["totNet"]}')
    
if __name__ == "__main__":
    empDetailList = []
    empTotals = {}
    while True:
        empName = getEmpName()
        if (empName.lower() == "end"):
            break
        fromDate, endDate = getDatesWorked()
        hours = getHoursWorked()
        hourlyRate = getHourlyRate()
        taxRate = getTaxRate()
        empDetail = []
        empDetail.insert(0, fromDate)
        empDetail.insert(1, endDate)
        empDetail.insert(2, empName)
        empDetail.insert(3, hours)
        empDetail.insert(4, hourlyRate)
        empDetail.insert(5, taxRate)
        empDetailList.append(empDetail)
        
    printInfo(empDetailList)
    printTotals(empTotals)
    

    
        
    
