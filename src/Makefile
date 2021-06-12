all:
	$(info NOT SUPPORTED)
	$(info Please choose according to your machine)
	$(info Options: noprotection || sgterm || sgrandom )
	exit -1
noprotection:
	$(info Building binaries without any protection)
	$(warning Disabling ASLR)
	sudo sh -c "echo 0 > /proc/sys/kernel/randomize_va_space"
	gcc -m32 -g -no-pie -fno-stack-protector -z execstack -z norelro challenge-1.c -o binary-1-no-protection
	gcc -m32 -g -no-pie -fno-stack-protector -z execstack -z norelro challenge-2.c -o binary-2-no-protection
	gcc -m32 -g -no-pie -fno-stack-protector -z execstack -z norelro challenge-3.c -o binary-3-no-protection
	gcc -m32 -g -no-pie -fno-stack-protector -z execstack -z norelro challenge-4.c -o binary-4-no-protection
	gcc -m32 -g -no-pie -fno-stack-protector -z execstack -z norelro challenge-5.c -o binary-5-no-protection
sgterm:
	$(info Building binaries with StackGuard11 terminator canary)
	gcc challenge-1.c -g -o binary-1-SG11-terminator
	gcc challenge-2.c -g -o binary-2-SG11-terminator
	gcc challenge-3.c -g -o binary-3-SG11-terminator
	gcc challenge-4.c -g -o binary-4-SG11-terminator
	gcc challenge-5.c -g -o binary-5-SG11-terminator
sgrandom:
	$(info Building binaries with StackGuard12 random canary)
	gcc challenge-1.c -g -o binary-1-SG12-random
	gcc challenge-2.c -g -o binary-2-SG12-random
	gcc challenge-3.c -g -o binary-3-SG12-random
	gcc challenge-4.c -g -o binary-4-SG12-random
	gcc challenge-5.c -g -o binary-5-SG12-random
