def crypto(i,j):

		return (((i >> 6) | (4 * i)) ^ j ) & 0xff


a = [0x99,0xb0,0x87,0x9e,0x70,0xe8,0x41,0x44,0x05,0x04,0x8b,0x9a,0x74,0xbc,0x55,0x58,0xb5,0x61,0x8e,0x36,0xac,0x09,0x59,0xe5,0x61,0xdd,0x3e,0x3f,0xb9,0x15,0xed,0xd5]

flag = 'f'

num = 1
while num < len(a):

	for i in range(0x20,0x7f):

		c = []

		for j in range(len(flag)):
			c.append(crypto(ord(flag[j]),j))
		c.append(crypto(i,num))	



		for l in range(4):
			for m in range(1,len(c)):

				v3 = c[m-1] | c[m]
				v1 = ( v3 & ( 0xffffffff - (c[m] & c[m-1]) )) & 0xff
				c[m] = v1

		if c[num] == a[num]:

			print chr(i)
			flag += chr(i)
			num += 1
			break

print flag






