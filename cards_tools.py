# keep all dict of all name cards
card_list = []


def show_menu():
    """Option Menu"""
    print("*" * 50)
    print("Welcome to [Name Cards Management System] V 1.0")
    print("")
    print("1. Create a new name card")
    print("2. Display all name cards")
    print("3. Search a name card")
    print("")
    print("0. Exit")
    print("*" * 50)


def new_card():
    """Add New Name Card"""
    print("-" * 50)
    print("Add New Name Card")

    # 1. prompt user to enter name card info
    name = input("Please Enter Name:")
    phone = input("Please Enter phone Number:")
    qq = input("Please Input QQ number:")
    email = input("Please enter email:")

    # 2. use the info to create a dict
    card_dict = {"name": name,
                 "phone": phone,
                 "qq": qq,
                 "email": email}

    # 3. add the dict to card_list
    card_list.append(card_dict)
    print(card_list)

    # 4. Display create succeed
    print("%s\'s Name card created success" % name)


def show_all():
    """Display All Name Cards"""
    print("-" * 50)
    print("Display All Name Cards")

    # To identify if there an record exist, if not, prompt the user that there is no record, and return
    if len(card_list) == 0:

        print("There is no record exist, please use option [1] to add new name card")

        return


    # print table head
    for name in ["Name", "Phone", "QQ", "Email"]:
        print(name, end = "\t\t\t")
    else:
        # print break line
        print("")
        print("=" * 50)

    # iterate cart list for card info
    for card_dict in card_list:

        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                        card_dict["phone"],
                                        card_dict["qq"],
                                        card_dict["email"]))


def search_card():
    """Search Name Cards"""
    print("-" * 50)
    print("Search Name Cards")

    # 1. prompt user to enter search name
    find_name = input("Please enter the search name: ")

    # 2. iterate card_list to find the name
    for card_dict in card_list:

        if card_dict["name"] == find_name:

            print("Name\t\tPhone\t\tQQ\t\tEmail")
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                            card_dict["phone"],
                                            card_dict["qq"],
                                            card_dict["email"]))

            # To edit the find_name
            deal_card(card_dict)

            break
    else:

        # the search name doesn't exist
        print("Sorry, %s doesn't exist" % find_name)


def deal_card(find_dict):
    """
    deal with found dict data
    :param find_dict: the dict found
    """
    print(find_dict)

    action_str = input("Please select what to do next: "
                       "[1]Edit [2]Delete [0] Return: ")

    if action_str == "1":

        find_dict["name"] = input_card_info(find_dict["name"], "Name: ")
        find_dict["phone"] = input_card_info(find_dict["phone"], "Phone: ")
        find_dict["qq"] = input_card_info(find_dict["qq"], "QQ: ")
        find_dict["email"] = input_card_info(find_dict["email"], "Email: ")
        print("Edit name Card Successful!")

    elif action_str == "2":

        card_list.remove(find_dict)
        print("Delete Name card successful!")


def input_card_info(dict_value, tip_message):
    """
    deal with found dict data
    :param dict_value: the dict original value
    :param tip_message: the prompt message for user input
    :return: return user input or original value
    """

    # 1. Prompt user to input
    result_str = input(tip_message)

    # 2. if user enter, return result
    if len(result_str) > 0:

        return result_str

    # 3. if user doesn't input data, return original data
    else:
        return dict_value
