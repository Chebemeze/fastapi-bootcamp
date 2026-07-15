import os

#with open("rm.py", "x") as f:
#    f.write("This is a newly created file")
#    print("After creating the file")
#    print(f.read())

try:
    os.path.exists("rm.py")
    os.remove("rm.py")
except Exception:
    print("The file doesn't exist, so we create it now")
    f = open("rm.py", "x")
    f.close()