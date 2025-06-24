try: 
 file_name="sample.txt"   
 file1=open(file_name,'r')
 reading_files=file1.readlines()
 print(reading_files)
 n=0
 for i in  reading_files:
  print(f"Line {n}:{i}")
  n=n+1
except FileNotFoundError :
    print(f"Error: The file {file_name} was not found")
except Exception as ex:
  print("some thing went wrong : ",ex)
    