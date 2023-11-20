import os

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.0")
    while True:
        s = input("Enter what do you want to Speak: ")
        if s == "ex17":
            break
        s = ''.join(c for c in s if c.isalpha() or c.isspace())

        comm = f"PowerShell -Command "f"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{s}');"
        os.system(comm)
