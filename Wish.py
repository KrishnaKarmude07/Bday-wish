import time
import random
import sys
import os

def type_out(text, delay=0.03):
    """Mimic human typing."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def loading_animation(msg, dots=3, repeat=2):
    for _ in range(repeat):
        for i in range(dots + 1):
            print('\r' + msg + '.' * i + ' ' * (dots - i), end='')
            time.sleep(0.4)
    print()

def fireworks_effect():
    emojis = ["🎉", "🎈", "✨", "💥", "🎊", "🌟"]
    for _ in range(15):
        line = ''.join(random.choice(emojis) for _ in range(random.randint(25, 50)))
        print(line)
        time.sleep(0.2)

def fake_hack():
    print("\n👾 Initiating Operation: Project S-A-K-S-H-I")
    time.sleep(1)
    for i in range(5):
        code_line = f"Injecting surprise module {i+1}/5..."
        type_out(code_line, delay=0.05)
        time.sleep(0.3)
    loading_animation("Accessing Celebration Gateway")
    print("🔓 Access granted: Welcome Commander!")
    time.sleep(1)

def surprise_birthday_message():
    print()
    fireworks_effect()
    print("\n✨🎂 LOADING MESSAGE MODULE 🎂✨\n")
    time.sleep(2)
    
    wishes = [
        "SURPRISEEEEEEEEE!!! 🧨🧨🧨",
        "Wait, WHAT?! SYSTEM ALERT?? 😱",
        "Nope! It's just a BIRTHDAY PARTY in disguise! 😂🎁",
        "\n🎉 HAPPY BIRTHDAY SAKSHI! 🎉",
        "You legend, you sparkle, you sunflower in chaos 😎🌻",
        "Here’s to the most fabulous, crazy, and amazing friend ever!",
        "Let’s make sure the world can hear your laughter today 😄💃",
        "Keep shining, keep being the madness we all love! 💖✨"
    ]
    
    for line in wishes:
        type_out(line, delay=0.06)
        time.sleep(1)

    fireworks_effect()
    type_out("\n🎂 Your system will now self-destruct from too much joy... just kidding! 😜", delay=0.05)
    print("\n💌 With more love than your phone's storage can handle – From your crazy genius friend ❤️")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    fake_hack()
    surprise_birthday_message()

if __name__ == "__main__":
    main()
