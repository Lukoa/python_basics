import termios
import sys
import tty

def input_password(prompt):
    print(prompt, end='', flush=True)
    old_settings=termios.tcgetattr(sys.stdin)

    try:
        tty.setraw(sys.stdin.fileno())
        password=''
        while True:
            ch=sys.stdin.read(1)
            if ch=='\r' or ch=='\n':
                break
            if ch=='\03':
                raise KeyboardInterrupt
            sys.stdout.write('.')
            sys.stdout.flush()
        print()
        return password
    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
 
name=input('Enter your username: '.lower())
user_name=name.lower() + '.eagles'
password=input_password('Enter your password: ')
print(f'{user_name}, {password} is your password')