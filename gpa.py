numOfModule = int(input("Số môn\n"))
totalScore, totalCredit = 0, 0

for i in range(1, numOfModule+1):
    moduleScore = float(input("Điểm môn {0}\n".format(i)))
    moduleCredit = int(input("Tín chỉ môn {0}\n".format(i)))
    totalScore += moduleScore*moduleCredit
    totalCredit += moduleCredit

print(totalScore/totalCredit)