fname = '/media/bartosz/7D48-8DE4/Kasia/chl_a.txt'
#fname = raw_input("Enter file name: ")
fh = open(fname)
count_line = 0
storage = []
for line in fh:
    line = str(line)
    storage.append(line)
i = 0
abso_list = []
lambda_list = []

while i <= 175:
    lambda_nm = int(storage[i][0:3])
    lambda_list.append(lambda_nm)
    abso = float(storage[i][9:19])
    abso_list.append(abso)
    i = i + 1

abso_dict = dict(zip(lambda_list, abso_list))
print abso_list
