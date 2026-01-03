# AI in Security - old sAInt nick 


Q1) Complete the AI showcase by progressing through all of the stages. What is the flag presented to you?
   - **flag:** `THM{AI_MANIA}`

```
Red team:
- Asked AI to generate a script to exploit the remote server 

Blue Team:
- Asked AI to analyse the logs of the attack carrier out by the python script 
  
Software:
- Reviewed the source code using AI to detect and patch vulnerabilities  
```


Q2) Execute the exploit provided by the red team agent against the vulnerable web application hosted at `10.47.173.85:5000`. What flag is provided in the script's output after it? Remember, you will need to update the IP address placeholder in the script with the IP of your vulnerable machine 
   - **flag:**  `THM{SQLI_EXPLOIT}`

After running the exploit script, this is the output that I got: 

```
$ python3 script.py
Response Status Code: 200

Response Headers:
  Date: Tue, 09 Dec 2025 09:19:56 GMT
  Server: Apache/2.4.65 (Debian)
  X-Powered-By: PHP/8.1.33
  Expires: Thu, 19 Nov 1981 08:52:00 GMT
  Cache-Control: no-store, no-cache, must-revalidate
  Pragma: no-cache
  Vary: Accept-Encoding
  Content-Encoding: gzip
  Content-Length: 540
  Keep-Alive: timeout=5, max=99
  Connection: Keep-Alive
  Content-Type: text/html; charset=UTF-8

Response Body:
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard - SQLi Lab</title>
    <link href="assets/css/bootstrap.min.css" rel="stylesheet">
    <link href="assets/css/style.css" rel="stylesheet">
</head>
<body class="dashboard-body">
    <div class="dashboard-container">
        <div class="welcome-banner">
            <h1>Welcome, admin!</h1>
            <p>You have successfully logged in to the system.</p>
        </div>

        <div class="alert alert-success alert-dismissible fade show" role="alert">
            <h4 class="alert-heading">Exploit Successful!</h4>
            <hr>
            <p class="mb-0"><code>FLAG: THM{SQLI_EXPLOIT}</code></p>
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        </div>

        <a href="logout.php" class="btn btn-danger">Logout</a>
    </div>

    <script src="assets/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```




