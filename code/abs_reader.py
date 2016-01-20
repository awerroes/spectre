#odczytuje absorbancje i zapisuje ja jako liste
fname = '/media/bartosz/7D48-8DE4/Kasia/chl_a.txt'
#fname = raw_input("Enter file name: ")
fh = open(fname)
count_line = 0
storage = []
for line in fh:
    count_line = count_line + 1
    if count_line >= 20 and count_line <= 195:
        line = str(line)
        storage.append(line)
i = 0
abso_list = []
while i <= 175:
    lambda_nm = storage[i][0:3]
    abso = float(storage[i][9:19])
    abso_list.append(abso)
    i = i + 1
print abso_list
