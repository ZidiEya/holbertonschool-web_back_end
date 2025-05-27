                                                     Basic_authentication


Objective
Add a Basic Authentication mechanism so that users must provide a valid email/password (encoded in base64) in the Authorization header to access certain endpoints.


📚 GENERAL KNOWLEDGE
✅ What is Authentication?
Authentication is the process of verifying the identity of a user or system. In web applications, it's used to ensure that users accessing resources are who they claim to be (e.g., via username/password).

✅ What is Base64?
Base64 is a binary-to-text encoding scheme that converts binary data into an ASCII string format using a 64-character alphabet. It’s commonly used to encode data that needs to be stored and transferred over media that are designed to deal with text.

Example:
python
Copier
Modifier
import base64

text = "HelloWorld"
encoded = base64.b64encode(text.encode())
print(encoded.decode())  # Output: SGVsbG9Xb3JsZA==
✅ What is Basic Authentication?
Basic Authentication is a simple HTTP authentication scheme built into the HTTP protocol.

The client sends the username and password, encoded in Base64, in the Authorization header.

Format:

bash
Copier
Modifier
Authorization: Basic <base64 encoded 'username:password'>
✅ How to send the Authorization header (example with curl):
bash
Copier
Modifier
curl -H "Authorization: Basic $(echo -n 'my_email@example.com:my_password' | base64)" http://localhost:5000/api/v1/users/me
🛠️ PROJECT REQUIREMENTS CHECKLIST
✅ Python Environment
Ubuntu 20.04

Python 3.9

Make sure all Python scripts begin with:

python
Copier
Modifier
#!/usr/bin/env python3
✅ Files and Formatting
All files must end with a newline (\n)

Use pycodestyle==2.5:

bash
Copier
Modifier
pip install pycodestyle==2.5
pycodestyle your_script.py
All files must be executable:

bash
Copier
Modifier
chmod +x your_script.py
✅ File Length Check
Check file length with:

bash
Copier
Modifier
wc your_script.py


