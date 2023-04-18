import webbrowser
gender = input("What is your gender? (Type 'M' for male, 'F' for female): ")
url = ""

if gender.upper() == 'M':
    print("Please select from the following options:")
    print("1. Shirts")
    print("2. Jeans")
    print("3. Shoes")
    choice = int(input("Enter your choice (1-3): "))

    if choice == 1:
        print("Select type of shirt:")
        print("1. Casual")
        print("2. Formal")
        print("3. Striped")
        print("4. Printed")
        shirt_choice = int(input("Enter your choice (1-4): "))

        if shirt_choice == 1:
            webbrowser.open("https://www.myntra.com/men-casual-shirts")
        elif shirt_choice == 2:
            webbrowser.open("https://www.myntra.com/men-formal-shirts")
        elif shirt_choice == 3:
            webbrowser.open("https://www.myntra.com/men-striped-shirts")
        elif shirt_choice == 4:
            webbrowser.open("https://www.myntra.com/men-printed-shirts")
        else:
            print("Invalid choice.")

    elif choice == 2:
        print("Select type of jeans:")
        print("1. Skinny")
        print("2. Straight")
        print("3. Ripped")
        print("4. High-waisted")
        jeans_choice = int(input("Enter your choice (1-4): "))

        if jeans_choice == 1:
            webbrowser.open("https://www.myntra.com/men-skinny-jeans")
        elif jeans_choice == 2:
            webbrowser.open("https://www.myntra.com/men-straight-jeans")
        elif jeans_choice == 3:
            webbrowser.open("https://www.myntra.com/men-ripped-jeans")
        elif jeans_choice == 4:
            webbrowser.open("https://www.myntra.com/men-high-waisted-jeans")
        else:
            print("Invalid choice.")

    elif choice == 3:
        print("Select type of shoes:")
        print("1. Sneakers")
        print("2. Boots")
        print("3. Flats")
        shoes_choice = int(input("Enter your choice (1-3): "))

        if shoes_choice == 1:
            webbrowser.open("https://www.myntra.com/men-sneakers")
        elif shoes_choice == 2:
            webbrowser.open("https://www.myntra.com/men-boots")
        elif shoes_choice == 3:
            webbrowser.open("https://www.myntra.com/men-flats")
        else:
            print("Invalid choice.")

    else:
        print("Invalid choice.")

elif gender.upper() == 'F':
    print("Please select from the following options:")
    print("1. Tops")
    print("2. Jeans")
    print("3. Shoes")
    choice = int(input("Enter your choice (1-3): "))

    if choice == 1:
        print("Select type of top:")
        print("1. Casual")
        print("2. Formal")
        print("3. Floral")
        print("4. Lace")
        top_choice = int(input("Enter your choice (1-4): "))

        if top_choice == 1:
             webbrowser.open("https://www.myntra.com/women-casual-tops")
        elif top_choice == 2:
             webbrowser.open("https://www.myntra.com/women-formal-tops")
        elif top_choice == 3:
             webbrowser.open("https://www.myntra.com/women-floral-tops")
        elif top_choice == 4:
             webbrowser.open("https://www.myntra.com/women-lace-tops")

    elif choice == 2:
        print("Select type of jeans:")
        print("1. Skinny")
        print("2. Straight")
        print("3. Ripped")
        print("4. High-waisted")
        top_choice = int(input("Enter your choice (1-4): "))


        if top_choice == 1:
             webbrowser.open("https://www.myntra.com/women-skinny-jeans")
        elif top_choice == 2:
             webbrowser.open("https://www.myntra.com/women-straight-jeans")
        elif top_choice == 3:
             webbrowser.open("https://www.myntra.com/women-ripped-jeans")
        elif top_choice == 4:
             webbrowser.open("https://www.myntra.com/women-high-waisted-jeans")

    elif choice == 3:
        print("Select type of shoes:")
        print("1. Sneakers")
        print("2. Boots")
        print("3. Heels")
        print("4. Flats")
        shoes_choice = int(input("Enter your choice (1-4): "))

        if shoes_choice == 1:
            webbrowser.open("https://www.myntra.com/women-sneakers")
        elif shoes_choice == 2:
            webbrowser.open("https://www.myntra.com/women-boots")
        elif shoes_choice == 3:
            webbrowser.open("https://www.myntra.com/women-heels")
        elif shoes_choice == 4:
            webbrowser.open("https://www.myntra.com/women-flats")
        else:
            print("Invalid choice.")
    else:
        print("Invalid choice.")

        webbrowser.open(myntra_url)