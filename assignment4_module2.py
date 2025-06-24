try:
    idea= input("Enter Text to write to the files:")
    file1=open("output.txt",'w')
    file1.write(idea)
    file1.close()
    print("Data successfully written to output.txt")

    edit_idea=input("Enter additional text to append:")
    file2=open("output.txt",'a')
    file2.write(edit_idea)
    file2.close()
    print("Data syccessfully appended.")

    print("Final content of output.txt:")
    file3=open("output.txt",'r')
    print(file3.read())
    file3.close()
except Exception as ex:
    print("Error found ",ex)
    