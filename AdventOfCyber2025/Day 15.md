# Web Attack Forensics - Drone Alone

### Investigation Steps:

- **Suspicious Requests:** Search Apache access logs for indicators like `cmd.exe`, `PowerShell`, and `Invoke-Expression`.
- **Vulnerability Identification:** Pinpoint command injection attempts targeting the vulnerable CGI script (`hello.bat`).
- **Process Spawning:** Analyze **Sysmon logs** to determine what child processes Apache spawned.
- **Confirmation:** Observing `cmd.exe` running `whoami` confirms the attacker gained interactive command execution.
- **Payload Verification:** Search for `PowerShell` traces using `-EncodedCommand`, `enc`, or `Base64` strings. If no results are found, the encoded payloads did not successfully execute.

**Q1) What is the reconnaissance executable file name?**

 - `whoami.exe`


 **Q2) What executable did the attacker attempt to run through the command injection?**

- `powershell.exe`


