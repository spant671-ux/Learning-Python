p = open(r'main.py')
print(p.read())

r = open("file.txt", "w")
r.write("Hello, this is a file made by w commamnd and written by write command.")
r.close()
