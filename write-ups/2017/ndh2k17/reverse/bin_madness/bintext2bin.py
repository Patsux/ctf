import struct
import sys

if (len(sys.argv) < 2):
	print("Please set arguments %%u <file>")
	sys.exit(-1)

f = open(sys.argv[1], 'r')

# Replace the '\n' to remove 80-chars columns
data = f.read().replace("\n", "")

# Reverse bit
data = data.replace("1", "2").replace("0", "1").replace("2", "0")

data_str = ""
for i in range(0, len(data) // 8):
	byte = data[i*8:i*8+8]
	data_str = data_str + str(hex(int(byte, 2))) + " "

# Write the output file
f_out = open("out.bin", "wb")
data_list = data_str.split(' ')[:-1]
for i in data_list:
		f_out.write(struct.pack("B", int(i, 16)))

f.close()
f_out.close()
