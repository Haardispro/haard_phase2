
Description:
this is most definitely going to ring some bells for those who attended the "router hijacking" workshop L0L

This is how the tree looked after unzipping the required files: 
```
.
├── formwear
│   ├── fwu_ver
│   ├── hw_ver
│   └── rootfs
├── formwear.zip
└── README.md
```

Static analysis: 
```
➜  ~/Documents/recruitment/haard_phase2/hardware/formwear/formwear git:(main) ✗ file rootfs
rootfs: Squashfs filesystem, little endian, version 4.0, zlib compressed, 10936182 bytes, 910 inodes, blocksize: 131072 bytes, created: Sun Oct  1 07:02:43 2023
➜  ~/Documents/recruitment/haard_phase2/hardware/formwear/formwear git:(main) ✗ cat fwu_ver
3.0.5
➜  ~/Documents/recruitment/haard_phase2/hardware/formwear/formwear git:(main) ✗ cat hw_ver
X1
```

As we can see, the `rootfs` is a Squashfs filesystem, which is quite common for routers. 
Next step would be to mount rootfs on my system and examine its contents.   

Commands used:  
```
> sudo mkdir /mnt/mounted
> sudo mount rootfs /mnt/mounted
```

Contents of `rootfs`: 
```
➜  /mnt/mounted ls
bin  config  dev  etc  home  image  lib  mnt  overlay  proc  run  sbin  sys  tmp  usr  var
```

- The `bin` folder contains all binaries required by the system, such as `echo`, `grep` etc. 
- The `dev` folder contains device files, which are special files that provide an interface to hardware devices and resources on the system.
- The `etc` folder contains system wide config files, so my best bet to find the flag would be in this folder. 

```
➜  /mnt/mounted/etc ls
config                 insdrv.sh                     protocols              scripts
config_default_hs.xml  irf                           radvd.conf             services
config_default.xml     mdev.conf                     ramfs.img              setprmt_reject
cups                   modules-load.d                rc_boot_dsp            shells
default                multiap.conf                  rc_log_dsp             simplecfgservice.xml
dhclient-script        omci_custom_opt.conf          rc_reset_dsp           smb.conf
dnsmasq.conf           omci_ignore_mib_tbl_10g.conf  resolv.conf            TZ
ethertypes             omci_ignore_mib_tbl.conf      rtk_tr142.sh           version
fstab                  omci_mib.cfg                  run_customized_sdk.sh  version_info
group                  orf                           runoam.sh              wscd.conf
inetd.conf             passwd                        runomci.sh
init.d                 ppp                           runsdk.sh
inittab                profile                       samba
```

My main aim here, is to find the super user password, which ultimately is the flag. 

Usually, password is stored in `/etc/shadow` file, in the form of a hash. Here, there's no `shadow` file, considering this is a file system from  a router. 
Here, config files are stored in `.xml` format. 

On grepping `PASSWORD` from `config_default.xml`, I got the flag.

```
➜  /mnt/mounted/etc grep "PASSWORD" config_default.xml
<Value Name="USER_PASSWORD" Value="user"/>
<Value Name="RS_PASSWORD" Value=""/>
<Value Name="ACCOUNT_RS_PASSWORD" Value=""/>
<Value Name="WLAN1_RS_PASSWORD" Value=""/>
<Value Name="WLAN1_ACCOUNT_RS_PASSWORD" Value=""/>
<Value Name="SUSER_PASSWORD" Value="HTB{N0w_Y0u_C4n_L0g1n}"/>
<Value Name="CWMP_ACS_PASSWORD" Value="password"/>
<Value Name="CWMP_CONREQ_PASSWORD" Value=""/>
<Value Name="CWMP_CERT_PASSWORD" Value="client"/>
```

**flag:** `HTB{N0w_Y0u_C4n_L0g1n}`


 
