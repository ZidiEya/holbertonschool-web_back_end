GitHub repository: holbertonschool-web_back_end
Directory: personal_data

🔐 Features Recap
hash_password(password: str) -> bytes:

Takes a plain password and returns a securely salted and hashed version.

Uses bcrypt.gensalt() for generating a random salt.

is_valid(hashed_password: bytes, password: str) -> bool:

Checks whether a plain password matches a previously hashed password.


🔒 Security Notes
bcrypt is considered very secure for password hashing.

Do not store plain passwords — only store the hash result from hash_password.

You don’t need to store the salt separately — bcrypt embeds it in the hash string.



✅ What You Did Right
Secure Hashing using bcrypt:

The use of bcrypt.gensalt() ensures that each password gets a unique salt.

hashpw and checkpw are standard secure methods.

Good Documentation:

Docstrings are clear and correctly describe the purpose, arguments, and return types.


