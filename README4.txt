4. SQL Injection Lab
**Difficulty:** Easy-Medium  
**Category:** Web Exploitation  

**Objective:** Exploit a simple login page to retrieve the hidden flag using SQL injection.

**Scenario:**
A website's login form does not properly validate user input. Your goal is to bypass authentication and find the flag.

**Instructions:**
- Examine the fake vulnerable login form code (`sql_lab.py`).
- Examine possible inputs from image provided ('sql.png').
- Craft a SQL injection payload that grants access.
- The flag will appear once you "login."


**Flag Format:** `FLAG{the_secret_message}`

- No input sanitization!
- Try to inject SQL commands.
- Successful login will reveal: FLAG{the_secret_message}