with open("d:\Python\EngineeringInformationProcessing\lab\doremi.txt", "r") as doremi:
    text = doremi.read()
    with open("d:\Python\EngineeringInformationProcessing\lab\\2022189005.txt", "w") as do2:
        do2.write(text)
        do2.write(text)
with open("d:\Python\EngineeringInformationProcessing\lab\\2022189005.txt", "r") as doremi2:
    print(doremi2.read())
