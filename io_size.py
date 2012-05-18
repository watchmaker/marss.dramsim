# use this script with "grep io_buffer_size err > tmp" to compute the total IO buffer size
infile = open('tmp', 'r')
lines = infile.readlines()
vals = [int(i.split()[2]) for i in lines]
print sum(vals)
