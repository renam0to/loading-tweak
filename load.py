import time

def loading_screen():
    print("Loading, please wait...")
    for i in range(1, 51):  # Loop from 1 to 100
        time.sleep(0.05)  # Simulate loading delay
        print(f"\rProgress: {i}%", end="")  # Update progress on the same line
    inpat = input("\nCLICK 'ENTER' TO CONTINUE")
    for z in range(51,101):
        time.sleep(0.05)
        print(f"\rtest {z}%", end="")


loading_screen()

print("\rhey there!")