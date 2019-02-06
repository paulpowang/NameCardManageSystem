import cards_tools


while True:

    # Display the menu
    cards_tools.show_menu()

    action_str = input("Please enter a number for option: ")
    print("The number you enter is [%s]" % action_str)

    if action_str in ["1" ,"2" ,"3"]:

        # Add name card
        if action_str == "1":
            cards_tools.new_card()
        # Display All
        elif action_str == "2":
            cards_tools.show_all()
        # Search Name Card
        elif action_str == "3":
            cards_tools.search_card()

    elif action_str == "0":  # exit the system

        print("Thank you for using Name Cards Management System.")
        break
    else:
        print("Invalid Input. Please enter again.")
