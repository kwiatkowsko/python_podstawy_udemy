while True:
    filesizeStr = input("Enter the max file size (MB): ")

    if filesizeStr.isdecimal():
        filesizeInt = int(filesizeStr)
        break

print("The max size is %d" % (filesizeInt))

print("Size in KB is %d" % (filesizeInt *1024))