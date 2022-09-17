import os
Directory = os.listdir()
listcsv = []
for file in Directory:
    if file.endswith('.csv'):
        listcsv.append(file)
stu_dur = {}
for fl in listcsv:
    f = open(fl,mode = 'r', encoding = 'utf-8')
    data = f.readlines()  #getting list of lines in the file
    for i in data:
        if (i!=data[0]):
            stu = i.split(",")
            name = stu[0]
            dur = int(stu[1])
            if name not in stu_dur:
                stu_dur[name] = [dur]
            else:
                stu_dur[name].append(dur)
        f.close()


file = open("cs101-students.txt","w")
l = list(stu_dur.keys())
l.sort()
for i in l:
    file.write(i)
    file.write("\n")
file.close()

#attendance with durations
file1 = open("cs101-students-att.txt","w")
for i in stu_dur:
    file1.write(str([i,len(stu_dur[i]),stu_dur[i]]))
    file1.write("\n")
file1.close()




import math_module as math
durations = []
for i in stu_dur:
    durations.append(stu_dur[i])
print(math.Histogram(durations))










        
    
    
