# Forensics - Registry Furensics 

### Core Concepts:

- **Windows Registry:** acts as a "brain" for the Windows OS, storing all the information and configurations it needs to function effectively.
- **Hives:** separate files (like `SYSTEM`, `SECURITY`, `SOFTWARE`, `SAM`, `NTUSER.DAT`) that store specific configuration settings.
- **Registry Editor:** a built-in tool used to view registry data, organizing hives into root keys (e.g., `HKEY_LOCAL_MACHINE`, `HKEY_CURRENT_USER`).
- **Registry Forensics:** the process of extracting and analyzing evidence from the registry to construct an incident timeline.



 **Q1) What application was installed on the dispatch-srv01 before the abnormal activity started?** 
 
 - `DroneManager Update`


**Q2) What is the full path where the user launched the application (found in question 1) from?**

- `C:\Users\dispatch.admin\Downloads\DroneManager_Setup.exe`


**Q3) Which value was added by the application to maintain persistence on startup?**

- `"C:\Program Files\DroneManager\dronehelper.exe" --background`




