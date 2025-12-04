# simulator.py

import time
import string
from itertools import product

# ---------- LOGIN SYSTEM ----------

def check_login(stored_password: str, entered_password: str) -> bool:
    """
    Compare entered password with stored password.
    """
    return stored_password == entered_password


# ---------- LOAD WORDLIST FROM FILE ----------

def load_wordlist(filename: str) -> list:
    """
    Load passwords from a text file (one per line).
    Returns a list of strings.

    Example wordlist.txt:
        123456
        password
        qwerty
        admin
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            # Strip newlines and ignore empty lines
            words = [line.strip() for line in file.readlines() if line.strip()]
            if not words:
                print(f"⚠ Wordlist file '{filename}' is empty.")
            return words
    except FileNotFoundError:
        print(f"❌ Wordlist file '{filename}' not found in current folder.")
        print("   Make sure 'wordlist.txt' is in the same folder as simulator.py.")
        return []


# ---------- BRUTE FORCE: WORDLIST ----------

def brute_force_with_wordlist(stored_password: str, guesses: list) -> None:
    """
    Simulate a brute-force attack using a provided wordlist.
    """
    print("\n=== Brute Force (Wordlist) ===")
    print(f"Total guesses in wordlist: {len(guesses)}")

    attempts = 0
    start_time = time.time()

    for guess in guesses:
        attempts += 1
        print(f"Trying: {guess} (attempt #{attempts})")
        if check_login(stored_password, guess):
            end_time = time.time()
            duration = end_time - start_time
            print("\n💥 Password cracked using wordlist!")
            print(f"✅ Correct password: {guess}")
            print(f"📌 Total attempts: {attempts}")
            print(f"⏱ Time taken: {duration:.4f} seconds")
            return

    end_time = time.time()
    duration = end_time - start_time
    print("\n❌ Password NOT found in the wordlist.")
    print(f"📌 Total attempts: {attempts}")
    print(f"⏱ Time taken: {duration:.4f} seconds")


# ---------- BRUTE FORCE: ALL COMBINATIONS ----------

def generate_combinations(charset: str, max_length: int):
    """
    Generator that yields all possible strings up to max_length
    using characters from charset.
    """
    for length in range(1, max_length + 1):
        for combo in product(charset, repeat=length):
            yield "".join(combo)


def brute_force_full(stored_password: str, charset: str, max_length: int) -> None:
    """
    Try all possible combinations from the given charset up to max_length.
    WARNING: grows very fast, only use for short passwords and small charsets.
    """
    print("\n=== Brute Force (Full Search) ===")
    print(f"Character set: {charset}")
    print(f"Max length: {max_length}")

    attempts = 0
    start_time = time.time()

    for guess in generate_combinations(charset, max_length):
        attempts += 1
        # Uncomment next line if you want to see each guess (will be very spammy)
        # print(f"Trying: {guess} (attempt #{attempts})")

        if check_login(stored_password, guess):
            end_time = time.time()
            duration = end_time - start_time
            print("\n💥 Password cracked by full brute force!")
            print(f"✅ Correct password: {guess}")
            print(f"📌 Total attempts: {attempts}")
            print(f"⏱ Time taken: {duration:.4f} seconds")
            return

    end_time = time.time()
    duration = end_time - start_time
    print("\n❌ Password NOT found within given charset/length.")
    print(f"📌 Total attempts: {attempts}")
    print(f"⏱ Time taken: {duration:.4f} seconds")


# ---------- DEFENSE: ACCOUNT LOCKOUT ----------

def simulated_login_with_lockout(stored_password: str, max_attempts: int = 5):
    """
    Simulate a normal login system with account lockout after some failed attempts.
    """
    print("\n=== Login with Account Lockout Defense ===")
    attempts = 0

    while attempts < max_attempts:
        entered = input("Enter password: ")
        attempts += 1

        if check_login(stored_password, entered):
            print("✅ Login successful!")
            return
        else:
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"❌ Wrong password. Remaining attempts: {remaining}")
            else:
                print("❌ Wrong password.")

    print("\n🚫 Account locked due to too many failed attempts!")


# ---------- MAIN MENU ----------

def main():
    print("=== Brute Force Attack Simulator ===")
    print("Educational use only. Do NOT use this on real systems.\n")

    # Ask user to set a fake password for the demo
    stored_password = input("Set a password for the fake account (e.g. abc, 1234, P@ssw0rd): ")

    while True:
        print("\n--- Menu ---")
        print("1) Try normal login (no attack)")
        print("2) Brute force using wordlist.txt")
        print("3) Full brute force over a small charset")
        print("4) Simulate login with account lockout defense")
        print("5) Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            # Normal manual login
            entered = input("Enter password: ")
            if check_login(stored_password, entered):
                print("✅ Login successful!")
            else:
                print("❌ Login failed.")

        elif choice == "2":
            # Wordlist attack using external file
            print("\nLoading wordlist from 'wordlist.txt'...")
            wordlist = load_wordlist("wordlist.txt")
            if not wordlist:
                print("⚠ Cannot run wordlist attack without a valid wordlist.")
            else:
                brute_force_with_wordlist(stored_password, wordlist)

        elif choice == "3":
            # Full brute-force attack
            print("\n⚠ WARNING: Full brute force grows VERY fast.")
            print("Use a very small charset and short password (like 'abc', charset='abc', length=3).")

            print("\nChoose charset:")
            print("1) Digits (0-9)")
            print("2) Lowercase letters (a-z)")
            print("3) Digits + lowercase (0-9 + a-z)")
            print("4) Custom charset")

            charset_option = input("Option (1-4): ")

            if charset_option == "1":
                charset = string.digits
            elif charset_option == "2":
                charset = string.ascii_lowercase
            elif charset_option == "3":
                charset = string.digits + string.ascii_lowercase
            else:
                charset = input("Enter custom characters to use (e.g. abc123): ")

            try:
                max_length = int(input("Enter maximum password length to try (e.g. 3): "))
            except ValueError:
                print("Invalid number. Using length 3.")
                max_length = 3

            brute_force_full(stored_password, charset, max_length)

        elif choice == "4":
            # Login system with lockout
            simulated_login_with_lockout(stored_password)

        elif choice == "5":
            print("Exiting. Bye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
