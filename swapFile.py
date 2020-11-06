def swapFileData():
    file1 = input("Please enter path of 1st file: ")
    file2 = input("Please enter path of 2nd file: ")


    with open(file1, 'r') as data_a:
    data_a = a.read()

	with open(file2, 'r') as data_b:
    data_b = b.read()

    with open(file1, 'w') as data_a:
    a.write(data_b)

    with open(file2, 'w') as data_b:
    b.write(data_a)

swapFileData()