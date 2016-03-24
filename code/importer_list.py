import pylab
def file_import(fname):

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

    
    return abso_list



print('Choose file to comparision: ')
fname = '/home/bartosz/project/spectre/data/chl_b.txt'
#fname = raw_input('Enter file name: ')
a = file_import(fname)
fname_2 = '/home/bartosz/project/spectre/data/feo.txt'
#fname_2 = raw_input('Enter file name: ')
b = file_import(fname_2)

y = 0
abs_diff = 0
max_a = max(a)
max_b = max(b)

for i in range(len(a)):
    diff = (a[y]/max_a - b[y]/max_b)**2
    y = y + 1
    abs_diff = abs_diff + diff

print 'Sum of square of difference: ', abs_diff
print 'Sum of square of difference divided by points number: ', abs_diff/len(a)
print 'Points_number: ', len(a)
print 'Maximum of aborbance in first file: ', max(a)
print 'Maximum of aborbance in second file: ', max(b)

# plot creation
# add wavelength as X axis!!!
pylab.figure(1)
pylab.title('First spectrum')
pylab.plot(a)
pylab.show()

pylab.figure(2)
pylab.title('Second spectrum')
pylab.plot(b)
pylab.show()
