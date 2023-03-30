
import termios
import sys
import tty

def masked_input(prompt):
    """
    Reads input from the user and masks it with dots.
    """
    print(prompt, end='', flush=True)
    old_settings = termios.tcgetattr(sys.stdin)
    try:
        tty.setraw(sys.stdin.fileno())
        password = ''
        while True:
            ch = sys.stdin.read(1)
            if ch == '\r' or ch == '\n':
                break
            if ch == '\x03':  # Ctrl-C
                raise KeyboardInterrupt
            password += ch
            sys.stdout.write('*')
            sys.stdout.flush()
        print()  # Move to next line
        return password
    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

name = input('Enter your user name: ')
password = masked_input('Enter your password: ')
secret = len(password) * '*'
print(secret)
