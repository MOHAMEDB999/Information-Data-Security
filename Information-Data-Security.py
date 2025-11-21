import hashlib
import random
import re
import time
import os
from colorama import Fore, Back, Style, init

# Initialize colorama for cross-platform color support
init(autoreset=True)

# Constants
PASSWORD_FILE = "password.txt"
USERNAME_PATTERN = r'^[a-z]{5}$'
PASSWORD_LENGTH = 8
SALT_LENGTH = 5

# Lockout configuration
LOCKOUT_LEVELS = [
    {'attempts': 3, 'delay': 5},
    {'attempts': 3, 'delay': 10},
    {'attempts': 3, 'delay': 15},
    {'attempts': 3, 'delay': 20}
]


class AuthenticationSystem:
    """Main authentication system class"""

    def __init__(self):
        self.password_file = PASSWORD_FILE
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        """Create password file if it doesn't exist"""
        if not os.path.exists(self.password_file):
            open(self.password_file, 'w').close()

    @staticmethod
    def generate_salt():
        """Generate a random 5-digit salt"""
        return str(random.randint(10000, 99999))

    @staticmethod
    def hash_password(password, salt):
        """Hash password with salt using SHA256"""
        return hashlib.sha256((password + salt).encode()).hexdigest()

    @staticmethod
    def validate_username(username):
        """
        Validate username format
        Rules: Exactly 5 lowercase letters (a-z)
        """
        if not username:
            return False, "Username cannot be empty"

        if not re.match(USERNAME_PATTERN, username):
            if len(username) != 5:
                return False, "Username must be exactly 5 characters"
            if not username.isalpha():
                return False, "Username must contain only letters"
            if not username.islower():
                return False, "Username must be lowercase"
            return False, "Username must be exactly 5 lowercase letters"

        return True, "Valid"

    @staticmethod
    def validate_password(password):
        """
        Validate password format
        Rules: Exactly 8 characters with lowercase, uppercase, and digits
        """
        if not password:
            return False, "Password cannot be empty"

        if len(password) != PASSWORD_LENGTH:
            return False, f"Password must be exactly {PASSWORD_LENGTH} characters"

        has_lower = bool(re.search(r'[a-z]', password))
        has_upper = bool(re.search(r'[A-Z]', password))
        has_digit = bool(re.search(r'[0-9]', password))

        missing = []
        if not has_lower:
            missing.append("lowercase letter")
        if not has_upper:
            missing.append("uppercase letter")
        if not has_digit:
            missing.append("digit")

        if missing:
            return False, f"Password must contain at least one: {', '.join(missing)}"

        return True, "Valid"

    def load_users(self):
        """Load all users from password file"""
        users = {}
        try:
            with open(self.password_file, 'r') as f:
                for line_num, line in enumerate(f, 1):
                    line = line.strip()
                    if not line:
                        continue

                    parts = line.split('|')
                    if len(parts) == 3:
                        username, salt, hash_pwd = parts
                        users[username] = {
                            'salt': salt,
                            'hash': hash_pwd,
                            'banned': False
                        }
                    elif len(parts) == 4 and parts[3] == 'BANNED':
                        username, salt, hash_pwd, _ = parts
                        users[username] = {
                            'salt': salt,
                            'hash': hash_pwd,
                            'banned': True
                        }
                    else:
                        print(f"{Fore.YELLOW}⚠ Warning: Malformed line {line_num} in password file{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}✗ Error loading users: {e}{Style.RESET_ALL}")

        return users

    def save_user(self, username, salt, hash_pwd):
        """Save a new user to the password file"""
        try:
            with open(self.password_file, 'a') as f:
                f.write(f"{username}|{salt}|{hash_pwd}\n")
            return True
        except Exception as e:
            print(f"{Fore.RED}✗ Error saving user: {e}{Style.RESET_ALL}")
            return False

    def mark_as_banned(self, username):
        """Mark a user as permanently banned"""
        users = self.load_users()
        if username not in users:
            return False

        users[username]['banned'] = True

        try:
            with open(self.password_file, 'w') as f:
                for user, data in users.items():
                    if data['banned']:
                        f.write(f"{user}|{data['salt']}|{data['hash']}|BANNED\n")
                    else:
                        f.write(f"{user}|{data['salt']}|{data['hash']}\n")
            return True
        except Exception as e:
            print(f"{Fore.RED}✗ Error banning user: {e}{Style.RESET_ALL}")
            return False

    def signup(self):
        """User registration process"""
        print(f"\n{Fore.CYAN}{'=' * 50}")
        print(f"{Fore.CYAN}{'SIGN UP - CREATE NEW ACCOUNT':^50}")
        print(f"{Fore.CYAN}{'=' * 50}{Style.RESET_ALL}")

        # Username input loop
        while True:
            username = input(f"\n{Fore.YELLOW}Enter username (5 lowercase letters): {Style.RESET_ALL}").strip()

            is_valid, message = self.validate_username(username)
            if not is_valid:
                print(f"{Fore.RED}✗ {message}{Style.RESET_ALL}")
                continue

            users = self.load_users()
            if username in users:
                print(f"{Fore.RED}✗ Username '{username}' already exists!{Style.RESET_ALL}")
                continue

            break

        # Password input loop
        while True:
            password = input(f"{Fore.YELLOW}Enter password (8 chars: a-z, A-Z, 0-9): {Style.RESET_ALL}").strip()

            is_valid, message = self.validate_password(password)
            if not is_valid:
                print(f"{Fore.RED}✗ {message}{Style.RESET_ALL}")
                continue

            break

        # Generate salt and hash password
        salt = self.generate_salt()
        hash_pwd = self.hash_password(password, salt)

        # Save user
        if self.save_user(username, salt, hash_pwd):
            print(f"\n{Fore.GREEN}{'=' * 50}")
            print(f"{Fore.GREEN}✓ Account created successfully!{Style.RESET_ALL}")
            print(f"{Fore.GREEN}  Username: {Fore.WHITE}{username}{Style.RESET_ALL}")
            print(f"{Fore.GREEN}  Salt: {Fore.WHITE}{salt}{Style.RESET_ALL}")
            print(f"{Fore.GREEN}{'=' * 50}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}✗ Failed to create account{Style.RESET_ALL}")

    def signin(self):
        """User login process with progressive lockout"""
        print(f"\n{Fore.CYAN}{'=' * 50}")
        print(f"{Fore.CYAN}{'SIGN IN - LOGIN TO YOUR ACCOUNT':^50}")
        print(f"{Fore.CYAN}{'=' * 50}{Style.RESET_ALL}")

        username = input(f"\n{Fore.YELLOW}Enter username: {Style.RESET_ALL}").strip()

        users = self.load_users()

        # Check if user exists
        if username not in users:
            print(f"{Fore.RED}✗ User '{username}' not found!{Style.RESET_ALL}")
            return

        # Check if user is banned
        if users[username]['banned']:
            print(f"\n{Fore.RED}{Back.WHITE} ⚠ THIS ACCOUNT IS PERMANENTLY BANNED ⚠ {Style.RESET_ALL}")
            print(f"{Fore.RED}Contact administrator for assistance.{Style.RESET_ALL}\n")
            return

        salt = users[username]['salt']
        correct_hash = users[username]['hash']

        current_level = 0

        # Main authentication loop
        while current_level < len(LOCKOUT_LEVELS):
            level_config = LOCKOUT_LEVELS[current_level]
            attempts_remaining = level_config['attempts']

            print(f"\n{Fore.CYAN}Level {current_level + 1} - You have {attempts_remaining} attempts{Style.RESET_ALL}")

            # Attempt loop for current level
            for attempt in range(level_config['attempts']):
                attempts_remaining = level_config['attempts'] - attempt

                password = input(
                    f"{Fore.YELLOW}Password {Fore.MAGENTA}(attempts left: {attempts_remaining}){Fore.YELLOW}: {Style.RESET_ALL}"
                ).strip()

                input_hash = self.hash_password(password, salt)

                # Successful login
                if input_hash == correct_hash:
                    print(f"\n{Fore.GREEN}{Back.BLACK}{'=' * 50}")
                    print(f"{Fore.GREEN}{Back.BLACK}{'✓ LOGIN SUCCESSFUL! WELCOME!':^50}")
                    print(f"{Fore.GREEN}{Back.BLACK}{'=' * 50}{Style.RESET_ALL}\n")
                    return

                # Failed attempt
                if attempts_remaining > 1:
                    print(f"{Fore.RED}✗ Incorrect password!{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}✗ Incorrect password! All attempts exhausted.{Style.RESET_ALL}")

            # All attempts for this level failed
            delay = level_config['delay']

            # Check if this is the last level
            if current_level == len(LOCKOUT_LEVELS) - 1:
                print(f"\n{Fore.RED}{'=' * 50}")
                print(f"{Fore.RED}⚠ LOCKOUT: Account locked for {delay} seconds{Style.RESET_ALL}")

                for remaining in range(delay, 0, -1):
                    print(f"{Fore.YELLOW}  ⏳ Unlocking in {remaining}s...{Style.RESET_ALL}", end='\r')
                    time.sleep(1)
                print()

                print(f"\n{Fore.RED}{Back.WHITE}{'=' * 50}")
                print(f"{Fore.RED}{Back.WHITE}{' ⚠ ACCOUNT PERMANENTLY BANNED ⚠ ':^50}")
                print(f"{Fore.RED}{Back.WHITE}{'Too many failed login attempts!':^50}")
                print(f"{Fore.RED}{Back.WHITE}{'=' * 50}{Style.RESET_ALL}\n")

                self.mark_as_banned(username)
                return
            else:
                # Apply lockout delay
                print(f"\n{Fore.RED}{'=' * 50}")
                print(f"{Fore.RED}⚠ LOCKOUT: Account locked for {delay} seconds{Style.RESET_ALL}")

                for remaining in range(delay, 0, -1):
                    print(f"{Fore.YELLOW}  ⏳ Unlocking in {remaining}s...{Style.RESET_ALL}", end='\r')
                    time.sleep(1)
                print()

                current_level += 1
                next_attempts = LOCKOUT_LEVELS[current_level]['attempts']
                print(f"{Fore.GREEN}✓ Account unlocked! You have {next_attempts} new attempts.{Style.RESET_ALL}")


def display_header():
    """Display application header"""
    print(f"\n{Fore.CYAN}{Back.BLACK}{'=' * 60}")
    print(f"{Fore.YELLOW}{Back.BLACK}{'SECURE AUTHENTICATION SYSTEM':^60}")
    print(f"{Fore.WHITE}{Back.BLACK}{'Version 2.0 - Production Ready':^60}")
    print(f"{Fore.CYAN}{Back.BLACK}{'=' * 60}{Style.RESET_ALL}\n")


def main_menu():
    """Main application loop"""
    auth_system = AuthenticationSystem()
    display_header()

    while True:
        print(f"\n{Fore.GREEN}╔{'═' * 48}╗")
        print(f"{Fore.GREEN}║{Fore.YELLOW}{'MAIN MENU':^48}{Fore.GREEN}║")
        print(f"{Fore.GREEN}╠{'═' * 48}╣")
        print(f"{Fore.GREEN}║  {Fore.CYAN}1{Fore.WHITE} - Sign Up (Create Account)                   {Fore.GREEN}║")
        print(f"{Fore.GREEN}║  {Fore.CYAN}2{Fore.WHITE} - Sign In (Login)                            {Fore.GREEN}║")
        print(f"{Fore.GREEN}║  {Fore.CYAN}3{Fore.WHITE} - Exit (Quit Application)                    {Fore.GREEN}║")
        print(f"{Fore.GREEN}╚{'═' * 48}╝{Style.RESET_ALL}")

        choice = input(f"\n{Fore.MAGENTA}➤ Select an option (1-3): {Style.RESET_ALL}").strip()

        if choice == '1':
            auth_system.signup()
        elif choice == '2':
            auth_system.signin()
        elif choice == '3':
            print(f"\n{Fore.YELLOW}{'=' * 50}")
            print(f"{Fore.YELLOW}Thank you for using our system. Goodbye!{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}{'=' * 50}{Style.RESET_ALL}\n")
            break
        else:
            print(f"{Fore.RED}✗ Invalid option! Please choose 1, 2, or 3.{Style.RESET_ALL}")


if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print(f"\n\n{Fore.YELLOW}Program interrupted by user. Exiting...{Style.RESET_ALL}\n")
    except Exception as e:
        print(f"\n{Fore.RED}✗ Unexpected error: {e}{Style.RESET_ALL}\n")