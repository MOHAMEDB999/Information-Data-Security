# 🔐 Secure Authentication System

A robust, terminal-based authentication system with progressive lockout mechanisms and permanent ban functionality. Built with Python, this system demonstrates secure password management practices with SHA-256 hashing and salt generation.

![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-production%20ready-brightgreen.svg)

---

## 📋 Table of Contents

- [Features](#-features)
- [Screenshots](#-screenshots)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Usage](#-usage)
- [How It Works](#-how-it-works)
- [Security Features](#-security-features)
- [File Structure](#-file-structure)
- [Configuration](#-configuration)
- [Testing](#-testing)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

### Core Functionality
- **User Registration (Sign Up)** - Create new accounts with validated credentials
- **User Authentication (Sign In)** - Secure login with progressive lockout system
- **Persistent Storage** - User data stored in encrypted format
- **Ban System** - Permanent account bans after excessive failed attempts
- **Colorful UI** - Enhanced terminal interface with color-coded messages

### Security Mechanisms
- ✅ Password hashing with SHA-256
- ✅ Unique salt generation per user (5-digit numeric)
- ✅ Progressive lockout delays (5s → 10s → 15s → 20s)
- ✅ Permanent ban after 12 failed login attempts
- ✅ Input validation for usernames and passwords
- ✅ Ban persistence across program restarts

### User Experience
- 🎨 Color-coded interface (green for success, red for errors, yellow for warnings)
- 📊 Real-time attempt counter during login
- ⏱️ Live countdown timer during lockouts
- 💬 Clear, informative error messages
- 🔄 Persistent program loop (no need to restart)

---

## 🖼️ Screenshots

### Main Menu
```
============================================================
              SECURE AUTHENTICATION SYSTEM
              Version 2.0 - Production Ready
============================================================

╔════════════════════════════════════════════════╗
║              MAIN MENU                         ║
╠════════════════════════════════════════════════╣
║  1 - Sign Up (Create Account)                  ║
║  2 - Sign In (Login)                           ║
║  3 - Exit (Quit Application)                   ║
╚════════════════════════════════════════════════╝

➤ Select an option (1-3):
```

### Sign Up Process
```
==================================================
         SIGN UP - CREATE NEW ACCOUNT
==================================================

Enter username (5 lowercase letters): alice
Enter password (8 chars: a-z, A-Z, 0-9): Test123A

==================================================
✓ Account created successfully!
  Username: alice
  Salt: 45829
==================================================
```

### Sign In with Lockout
```
==================================================
        SIGN IN - LOGIN TO YOUR ACCOUNT
==================================================

Enter username: alice

Level 1 - You have 3 attempts
Password (attempts left: 3): wrongpass
✗ Incorrect password!
Password (attempts left: 2): wrongpass
✗ Incorrect password!
Password (attempts left: 1): wrongpass
✗ Incorrect password! All attempts exhausted.

==================================================
⚠ LOCKOUT: Account locked for 5 seconds
  ⏳ Unlocking in 5s...
✓ Account unlocked! You have 3 new attempts.
```

---

## 📦 Requirements

### System Requirements
- **Operating System**: Windows, macOS, or Linux
- **Python Version**: 3.6 or higher
- **Disk Space**: Minimal (< 1 MB)
- **RAM**: Minimal (< 50 MB)

### Python Dependencies
- **colorama** >= 0.4.4 - For cross-platform colored terminal output

### Hardware Requirements
- Any modern computer capable of running Python
- Terminal/Command Prompt access

### Optional Requirements
- **Git** - For cloning the repository
- **Virtual Environment** - Recommended for dependency isolation

---

## 🚀 Installation

### Method 1: Clone from GitHub (Recommended)

```bash
# Clone the repository
git clone https://github.com/MOHAMEDB999/Information-Data-Security.git

# Navigate to project directory
cd Information-Data-Security

# Install dependencies
pip install colorama
```

### Method 2: Manual Download

1. Download the repository as ZIP from [GitHub](https://github.com/MOHAMEDB999/Information-Data-Security)
2. Extract the ZIP file
3. Open terminal/command prompt in the extracted folder
4. Install dependencies:
```bash
pip install colorama
```

### Method 3: Using Virtual Environment (Recommended for Development)

```bash
# Clone the repository
git clone https://github.com/MOHAMEDB999/Information-Data-Security.git
cd Information-Data-Security

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install colorama

# Run the application
python Information-Data-Security.py
```

### Verify Installation

```bash
# Check Python version
python --version

# Check if colorama is installed
python -c "import colorama; print('Colorama installed successfully!')"

# Run the application
python Information-Data-Security.py
```

You should see the main menu appear with colorful text if everything is installed correctly.

---

## 💻 Usage

### Starting the Application

```bash
python Information-Data-Security.py
```

### Creating an Account (Sign Up)

1. Select option `1` from the main menu
2. Enter a username (exactly 5 lowercase letters)
   - ✅ Valid: `alice`, `bobby`, `admin`
   - ❌ Invalid: `ALICE`, `ali`, `alice1`
3. Enter a password (exactly 8 characters with mixed case and digits)
   - ✅ Valid: `Test123A`, `Pass99Zz`, `Secure1X`
   - ❌ Invalid: `test123a`, `TESTABCD`, `Test12`
4. System generates a unique salt and stores your credentials

### Logging In (Sign In)

1. Select option `2` from the main menu
2. Enter your username
3. Enter your password
4. Track your remaining attempts displayed on screen
5. If successful, you'll see a welcome message

### Exiting the Application

1. Select option `3` from the main menu
2. Application will terminate gracefully

---

## 🔍 How It Works

### Authentication Flow

```
┌─────────────┐
│  Start App  │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  Main Menu  │◄─────────────┐
└──────┬──────┘              │
       │                     │
   ┌───┴───┐                 │
   │       │                 │
   ▼       ▼                 │
┌────┐   ┌────┐              │
│Sign│   │Sign│              │
│ Up │   │ In │              │
└─┬──┘   └─┬──┘              │
  │        │                 │
  │        ▼                 │
  │   ┌──────────┐           │
  │   │Attempt 1 │           │
  │   └────┬─────┘           │
  │        │                 │
  │    ┌───┴────┐            │
  │    │Success?│            │
  │    └───┬────┘            │
  │        │                 │
  │    ┌───┴────┐            │
  │   Yes       No           │
  │    │         │           │
  │    ▼         ▼           │
  │ ┌────┐   ┌────────┐     │
  │ │Auth│   │Lockout │     │
  │ │OK  │   │Cycle   │     │
  │ └────┘   └────┬───┘     │
  │               │         │
  │          ┌────┴─────┐   │
  │          │12 fails? │   │
  │          └────┬─────┘   │
  │               │         │
  │          ┌────┴────┐    │
  │         Yes       No    │
  │          │         │    │
  │          ▼         │    │
  │       ┌─────┐     │    │
  │       │ BAN │     │    │
  │       └─────┘     │    │
  │                   │    │
  └───────────────────┴────┘
```

### Lockout Progression Table

| Level | Attempts Per Level | Lockout Duration | Total Failed Attempts | Action After Failure |
|-------|-------------------|------------------|----------------------|---------------------|
| 1     | 3                 | —                | 0-3                  | 5s lockout          |
| 2     | 3                 | 5 seconds        | 4-6                  | 10s lockout         |
| 3     | 3                 | 10 seconds       | 7-9                  | 15s lockout         |
| 4     | 3                 | 15 seconds       | 10-12                | 20s lockout + BAN   |

### Password Storage Format

Data is stored in `password.txt` using pipe-delimited format:

```
username|salt|password_hash
username|salt|password_hash|BANNED
```

**Example:**
```
alice|45829|7d8e9f2a1b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e
bobby|12345|1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b|BANNED
```

### Hashing Algorithm

```python
# Pseudocode
salt = random_5_digit_number()
password_hash = SHA256(password + salt)
store(username, salt, password_hash)
```

---

## 🛡️ Security Features

### Password Hashing
- **Algorithm**: SHA-256 (256-bit cryptographic hash)
- **Salt**: Unique 5-digit numeric salt per user
- **Format**: `hash = SHA256(password + salt)`

### Input Validation

**Username Rules:**
- Length: Exactly 5 characters
- Character set: Lowercase letters only (a-z)
- Regex pattern: `^[a-z]{5}$`

**Password Rules:**
- Length: Exactly 8 characters
- Must contain:
  - At least 1 lowercase letter (a-z)
  - At least 1 uppercase letter (A-Z)
  - At least 1 digit (0-9)

### Brute Force Protection

The system implements **progressive time-based lockouts**:

1. **Level 1**: 3 attempts → 5-second delay
2. **Level 2**: 3 attempts → 10-second delay
3. **Level 3**: 3 attempts → 15-second delay
4. **Level 4**: 3 attempts → 20-second delay → **PERMANENT BAN**

**Total attempts before ban**: 12 attempts across 4 levels

### Ban Persistence

- Bans are written to `password.txt` with `|BANNED` suffix
- Bans persist even after program restart
- Banned users cannot create new accounts with same username
- No automatic unban mechanism (administrative action required)

---

## 📁 File Structure

```
Information-Data-Security/
│
├── Information-Data-Security.py    # Main application file
├── password.txt                     # User credentials storage (auto-generated)
├── README.md                        # This documentation file
│
└── .gitignore                      # Git ignore file (optional)
```

### File Descriptions

**Information-Data-Security.py**
- Main Python script containing all logic
- Class: `AuthenticationSystem`
- Functions: `main_menu()`, `display_header()`

**password.txt**
- Auto-generated on first run
- Stores user credentials in pipe-delimited format
- Format: `username|salt|hash` or `username|salt|hash|BANNED`

**README.md**
- Complete project documentation
- Installation and usage instructions
- Technical specifications

---

## ⚙️ Configuration

### Customizing Lockout Levels

Edit the `LOCKOUT_LEVELS` constant in `Information-Data-Security.py`:

```python
LOCKOUT_LEVELS = [
    {'attempts': 3, 'delay': 5},    # Level 1: 3 attempts, 5s delay
    {'attempts': 3, 'delay': 10},   # Level 2: 3 attempts, 10s delay
    {'attempts': 3, 'delay': 15},   # Level 3: 3 attempts, 15s delay
    {'attempts': 3, 'delay': 20}    # Level 4: 3 attempts, 20s delay
]
```

**Example - More Lenient System:**
```python
LOCKOUT_LEVELS = [
    {'attempts': 5, 'delay': 3},
    {'attempts': 5, 'delay': 5},
]
# Result: 10 total attempts before ban, shorter delays
```

### Changing Validation Rules

**Username Length (default: 5 characters):**
```python
# In validate_username() method
USERNAME_PATTERN = r'^[a-z]{5}$'  # Change {5} to desired length
```

**Password Length (default: 8 characters):**
```python
# At top of file
PASSWORD_LENGTH = 8  # Change to desired length
```

### Changing Storage File

```python
# At top of file
PASSWORD_FILE = "password.txt"  # Change to your preferred filename
```

---

## 🧪 Testing

### Manual Test Cases

#### Test Case 1: Valid Registration
```
Input:
  Username: alice
  Password: Test123A

Expected: ✓ Account created successfully
```

#### Test Case 2: Invalid Username
```
Input: ALICE (uppercase)
Expected: ✗ Username must be lowercase

Input: ali (too short)
Expected: ✗ Username must be exactly 5 characters

Input: alice1 (contains digit)
Expected: ✗ Username must contain only letters
```

#### Test Case 3: Invalid Password
```
Input: test123a (no uppercase)
Expected: ✗ Password must contain at least one: uppercase letter

Input: TEST123A (no lowercase)
Expected: ✗ Password must contain at least one: lowercase letter

Input: TestABCD (no digit)
Expected: ✗ Password must contain at least one: digit

Input: Test12 (too short)
Expected: ✗ Password must be exactly 8 characters
```

#### Test Case 4: Duplicate Username
```
Input: alice (already exists)
Expected: ✗ Username 'alice' already exists!
```

#### Test Case 5: Successful Login
```
Input:
  Username: alice
  Password: Test123A (correct)

Expected: ✓ LOGIN SUCCESSFUL! WELCOME!
```

#### Test Case 6: Failed Login → Lockout
```
Attempt 1: wrongpass → ✗ Incorrect password!
Attempt 2: wrongpass → ✗ Incorrect password!
Attempt 3: wrongpass → ⚠ LOCKOUT: Account locked for 5 seconds
```

#### Test Case 7: Account Ban
```
Fail all 12 attempts across 4 levels
Expected: ⚠ ACCOUNT PERMANENTLY BANNED
```

#### Test Case 8: Banned Account Login
```
Input: alice (banned account)
Expected: ⚠ THIS ACCOUNT IS PERMANENTLY BANNED
```

### Automated Testing (Optional)

Create `test_auth.py`:

```python
import unittest
from Information-Data-Security import AuthenticationSystem

class TestAuthSystem(unittest.TestCase):
    def setUp(self):
        self.auth = AuthenticationSystem()
    
    def test_username_validation(self):
        valid, msg = self.auth.validate_username("alice")
        self.assertTrue(valid)
        
        valid, msg = self.auth.validate_username("ALICE")
        self.assertFalse(valid)
    
    def test_password_validation(self):
        valid, msg = self.auth.validate_password("Test123A")
        self.assertTrue(valid)
        
        valid, msg = self.auth.validate_password("test123a")
        self.assertFalse(valid)
    
    def test_salt_generation(self):
        salt = self.auth.generate_salt()
        self.assertEqual(len(salt), 5)
        self.assertTrue(salt.isdigit())
    
    def test_password_hashing(self):
        hash1 = self.auth.hash_password("Test123A", "12345")
        hash2 = self.auth.hash_password("Test123A", "12345")
        self.assertEqual(hash1, hash2)  # Same input = same hash
        
        hash3 = self.auth.hash_password("Test123A", "54321")
        self.assertNotEqual(hash1, hash3)  # Different salt = different hash

if __name__ == '__main__':
    unittest.main()
```

Run tests:
```bash
python test_auth.py
```

---

## 🔧 Troubleshooting

### Common Issues

#### Issue 1: `ModuleNotFoundError: No module named 'colorama'`

**Solution:**
```bash
pip install colorama
```

#### Issue 2: Colors not displaying correctly on Windows

**Solution:**
Colorama should handle this automatically. If issues persist:
```bash
# Upgrade colorama
pip install --upgrade colorama

# Or use Windows Terminal instead of CMD
```

#### Issue 3: `password.txt` file not found

**Solution:**
The file is auto-generated. If it's missing:
```bash
# Create it manually (empty file)
touch password.txt

# Or let the program create it on first run
```

#### Issue 4: Permission denied when writing to file

**Solution:**
```bash
# Check file permissions
ls -l password.txt

# Fix permissions (Linux/Mac)
chmod 644 password.txt

# On Windows, check file properties and ensure it's not read-only
```

#### Issue 5: Corrupted `password.txt`

**Solution:**
```bash
# Backup current file
cp password.txt password.txt.backup

# Start fresh
rm password.txt

# Program will create new file on next run
```

#### Issue 6: Account locked but want to reset

**Solution:**
Edit `password.txt` manually:
```bash
# Remove |BANNED from the end of the user's line
# Before: alice|12345|hash|BANNED
# After:  alice|12345|hash
```

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### Reporting Bugs

1. Check existing issues first
2. Create a new issue with:
   - Clear description of the bug
   - Steps to reproduce
   - Expected vs actual behavior
   - System information (OS, Python version)

### Suggesting Enhancements

1. Create an issue with tag `enhancement`
2. Describe the feature and why it's useful
3. Provide examples if possible

### Submitting Pull Requests

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guide
- Add docstrings to all functions
- Include unit tests for new features
- Update README.md if needed

---

## 📈 Future Enhancements

### Planned Features
- [ ] Password strength meter during registration
- [ ] Account recovery via email
- [ ] Two-factor authentication (2FA)
- [ ] Password reset functionality
- [ ] Admin panel for user management
- [ ] Database integration (SQLite/PostgreSQL)
- [ ] GUI version using Tkinter or PyQt
- [ ] Web interface using Flask/Django
- [ ] Password history (prevent reuse)
- [ ] Account lockout notifications
- [ ] Logging and audit trail
- [ ] Rate limiting by IP address

### Security Improvements
- [ ] Upgrade to bcrypt or Argon2 for password hashing
- [ ] Implement key stretching
- [ ] Add CAPTCHA after multiple failures
- [ ] Session management
- [ ] Password expiration policy
- [ ] Encrypted file storage

---

## 📄 License

This project is licensed under the MIT License.

```
MIT License

Copyright (c) 2024 Mohamed Benabdelghani

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 👨‍💻 Author

**Mohamed Benabdelghani**
- GitHub: [@MOHAMEDB999](https://github.com/MOHAMEDB999)
- Email: moha.benabdelghani@gmail.com
- Repository: [Information-Data-Security](https://github.com/MOHAMEDB999/Information-Data-Security)

---

## 🙏 Acknowledgments

- [Colorama](https://github.com/tartley/colorama) - Cross-platform colored terminal text
- Python community for excellent documentation
- Contributors and testers

---

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Troubleshooting](#-troubleshooting) section
2. Search [existing issues](https://github.com/MOHAMEDB999/Information-Data-Security/issues)
3. Create a [new issue](https://github.com/MOHAMEDB999/Information-Data-Security/issues/new)
4. Contact: moha.benabdelghani@gmail.com

---

## ⭐ Show Your Support

If you find this project helpful, please give it a ⭐️ on [GitHub](https://github.com/MOHAMEDB999/Information-Data-Security)!

---

**Last Updated**: November 2024  
**Version**: 2.0  
**Status**: Production Ready
