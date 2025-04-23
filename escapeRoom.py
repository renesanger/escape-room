import time
import random
import sys

SECRET_PIN = "9337"
FINAL_MESSAGE = "📝 Look under the brown panel underneath the desktop."

def slow_print(text, delay=0.02, end="\n"):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print(end=end)

def glitch_effect(lines=10, intense=False):
    chars = "01"
    for _ in range(lines):
        line = ''.join(random.choice(chars) for _ in range(random.randint(50, 80)))
        color = "\033[91m" if intense else "\033[92m"
        reset = "\033[0m"
        print(f"{color}{line}{reset}")
        time.sleep(0.01 if intense else 0.02)

def error_glitch(attempts):
    slow_print(f"\n❌ ATTEMPT #{attempts}: SYSTEM ERROR DETECTED...", delay=0.04)
    glitch_effect(3, intense=True)
    slow_print("⚠️ MALFUNCTION IN SECTOR 7B — CODE DUMP:", delay=0.03)
    glitch_effect(4, intense=True)
    slow_print("Attempting memory patch...", delay=0.03)
    time.sleep(0.5)

def invalid_input_glitch(attempts):
    slow_print(f"\n❌ ATTEMPT #{attempts}: INVALID INPUT FORMAT!", delay=0.04)
    glitch_effect(2, intense=True)
    slow_print("💥 CRITICAL FORMAT ERROR — NUMERIC SEQUENCE REQUIRED", delay=0.03)
    glitch_effect(3, intense=True)
    slow_print("System restoring previous input state...\n", delay=0.03)
    time.sleep(0.5)

def require_begin_command():
    slow_print("🔐 Secure Terminal Lockdown Initiated", delay=0.04)
    time.sleep(0.5)
    slow_print("Type 'BEGIN' to initiate boot sequence...\n", delay=0.04)

    while True:
        user_input = input("🔁 Command: ").strip().lower()
        if user_input == "begin":
            slow_print("\n✅ Command accepted. Initiating boot sequence...\n", delay=0.04)
            glitch_effect(3)
            break
        else:
            slow_print("⛔ Invalid command. Please type 'BEGIN' to proceed.\n", delay=0.03)

def main():
    require_begin_command()

    attempts = 0
    slow_print("📂 Loading secure system profile...", delay=0.04)
    time.sleep(1)
    glitch_effect(3)
    slow_print("\nVictor D Ciet's Laptop")
    slow_print("Enter pin\n")

    while True:
        pin_input = input("🔢 PIN: ")

        attempts += 1

        if len(pin_input) != 4 or not pin_input.isdigit():
            invalid_input_glitch(attempts)
            continue

        if pin_input == SECRET_PIN:
            print("\n✅ Access Granted!\n")
            glitch_effect(3)
            slow_print(FINAL_MESSAGE, delay=0.05)
            break
        else:
            error_glitch(attempts)

if __name__ == "__main__":
    main()
