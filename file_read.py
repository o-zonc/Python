in_file = open("d:\Python\EngineeringInformationProcessing\lab\서문.txt", "r", encoding="utf-8")
mytext = in_file.read()
in_file.close()

print(mytext)
print("len(mytext)=",len(mytext))
print("mytext[:6]=",mytext[:6])
print("mytext[:14]",mytext[:14])