'''
Week 03 | Data types & Data structures
'''

#Exercise 1-5 
student_num = [1,2,3,4,5,6,7,8,9,10]
student_name = ["Zihan","Pair","Namjai","Peter","Aomsin","Im","Tigger","Jay","Tangman","Winston"]
print("Number","Name",sep = '\t')
print((student_num[0]),(student_name[0]),sep = '\t')
print((student_num[1]),(student_name[1]),sep = '\t')
print((student_num[2]),(student_name[2]),sep = '\t')
print((student_num[3]),(student_name[3]),sep = '\t')
print((student_num[4]),(student_name[4]),sep = '\t')
print((student_num[5]),(student_name[5]),sep = '\t')
print((student_num[6]),(student_name[6]),sep = '\t')
print((student_num[7]),(student_name[7]),sep = '\t')
print((student_num[8]),(student_name[8]),sep = '\t')
print((student_num[9]),(student_name[9]),sep = '\t')

print(student_name[0])
print(student_name[-1])
print(student_name[4])
print(student_name[3])

#Exercise 6 
list1 = [0,1,2,'a','b','c']
print(list1[0])

#Exercise 7 
list2 = ['ant','bird','cat','dog','eagle']
list2[3] = "duck"
print(list2)

#Exercise 8 
list5 = [1,2,3,4,5,'a','f']
print(len(list5))

#Exercise 9 
listy = []
text1 = input("input any string: ")
text2 = input("input any string: ")
text3 = input("input any string: ")
listy.append(text1)
listy.append(text2)
listy.append(text3)
print(listy)

#Exercise 10 
list4 = [0,4,2,3,1]
list4.sort()
print(list4)

#Exercise 11 
listx = ["VISIONAI","CHATAI","GAMEAI"]
model4 = input("Enter the name of the 4th model: ")
model5 = input("Enter the name of the 5th model: ")
listx.append(model4)
listx.append(model5)

print(listx)
