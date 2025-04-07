#ProcessData.py
#Name: Tim Weixelman
#Date:4-6
#Assignment: Lab 8

import random

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  #Process each line of the input file and output to the CSV file

  for line in inFile:
    data = line.split()
    first = data[0]
    last = data[1]
    idNum = data[3]
    major = data[6]
    year = data[5]

    student_id = makeID(first, last, idNum)
    shortMajor = major_short(major)
    shortYear = abbreviated_year(year)
    output = last+"," + first + "," + student_id + "," + shortMajor + "-" + shortYear + "\n"
    outFile.write(output)
    print(student_id)


  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()
def major_short(major):
  return major[:3]
def makeID(first, last, idNum):
  idLen = len(idNum)
  while len(last) < 5:
    last = last + "X"
  id = first[0] + last + idNum[idLen -3: ]

  return id
def abbreviated_year(year):
  if "Freshman" in year:
    return "FR"
  if "Sophomore" in year:
    return "SO"
  if "Junior" in year:
    return "JR"
  if "Senior" in year:
    return "SR"

if __name__ == '__main__':
  main()
