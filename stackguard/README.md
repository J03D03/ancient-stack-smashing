# StackGuard Installation Instructions
If you want to compile other challenges with [StackGuard](https://gcc.gnu.org/pub/gcc/summit/2003/Stackguard.pdf) you can follow these instructions.

---

## Install Red Hat 5.2
We need ancient packages (~1998) to install the patched version of `gcc-2.7.2.3`.
Follow [these instructions](https://github.com/J03D03/redhat-5.2) to install Red Hat 5.2.  
Afterwards you can choose between one of the following two packages.

1. Get gcc-2.7.2.3-11SG.i386.rpm (terminator canary)
Download gcc-StackGuard to the host machine with `wget https://web.archive.org/web/20000818164605/http://www.cse.ogi.edu/DISC/projects/immunix/StackGuard/RPMS/gcc-2.7.2.3-11SG.i386.rpm`

2. Get gcc-2.7.2.3-14_SGc2_SG12.i386.rpm (random canary)
Download gcc-StackGuard to the host machine with `wget https://web.archive.org/web/20000818164605/http://www.immunix.org/StackGuard/gcc-2.7.2.3-14_SGc2_SG12.i386.rpm`

## Install gcc-2.7.2.3-* (StackGuard)
1. Start RH52 `qemu-system-i386 -hda redhat52-SG11.img -m 256 -vga cirrus -net nic,model=ne2k_pci -net user `
2. Login with `root` `<password>`
3. Transfer `gcc-2.7.2.3-*` to the virtual machine running RH52. Use `ftp` or `nc`.
4. Uninstall current gcc-2.7.2.3 `rpm -e gcc`
5. Install `gcc-2.7.2.3-*` with `rpm -i gcc-2.7.2.3-11SG.i386.rpm` or `rpm -i gcc-2.7.2.3-14_SGc2_SG12.i386.rpm`
