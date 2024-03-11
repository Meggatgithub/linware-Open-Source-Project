import time
import keyboard

def bios_screen():
    print("=============================================")
    print("|        Welcome to Linware BIOS            |")
    print("=============================================")
    print("|  Press F2 to enter BIOS Setup             |")
    print("|  Press F12 to boot from network           |")
    print("|  Press DEL to enter system configuration  |")
    print("=============================================")

def boot_from_network():
    print("Booting from network...")
    time.sleep(2)
    print("Network boot successful!")

def bios_setup():
    print("=============================================")
    print("|          BIOS Setup Configuration         |")
    print("=============================================")
    print("|  1. Change Boot Order                     |")
    print("|  2. Configure Hardware Settings           |")
    print("|  3. Save and Exit BIOS Setup              |")
    print("=============================================")

    while True:
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            print("Changing boot order...")
            time.sleep(2)
            print("Boot order changed successfully!")
        elif choice == "2":
            print("Configuring hardware settings...")
            time.sleep(2)
            print("Hardware settings configured successfully!")
        elif choice == "3":
            print("Saving and exiting BIOS setup...")
            time.sleep(2)
            break
        else:
            print("Invalid choice. Please select a valid option.")

    print("Exiting BIOS setup...")

def system_config():
    print("=============================================")
    print("|      System Configuration Settings        |")
    print("=============================================")
    print("|  1. Set Date and Time                     |")
    print("|  2. Configure Network Settings            |")
    print("|  3. Update System Software                |")
    print("|  4. Exit System Configuration             |")
    print("=============================================")

    while True:
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            print("Setting date and time...")
            time.sleep(2)
            print("Date and time set successfully!")
        elif choice == "2":
            print("Configuring network settings...")
            time.sleep(2)
            print("Network settings configured successfully!")
        elif choice == "3":
            print("Updating system software...")
            time.sleep(2)
            print("System software updated successfully!")
        elif choice == "4":
            print("Exiting System Configuration...")
            time.sleep(2)
            break
        else:
            print("Invalid choice. Please select a valid option.")

    print("Exiting System Configuration...")

# Simulate BIOS screen
bios_screen()

keyboard.add_hotkey('f12', boot_from_network)
keyboard.add_hotkey('f2', bios_setup)
keyboard.add_hotkey('delete', system_config)

keyboard.wait('q')  
