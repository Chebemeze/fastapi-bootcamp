""" A basic market calculator for market women in mile 1
   
   It gives her a total breakdown for Rice, Beans, and Garri

"""

def get_user_input(food_price_or_kg, is_float = False):
    """ Handles the price of goods and kilogram of goods entered by the market woman
    It ensurs that the right value type for price and kilogram are entered by the market woman

    Args:
        food_price_or_kg: This is either the price of the goods or the kilogram
        entered by the woman.

        is_float: specifies the type of input the market woman wants (Float or integer)

    Raises:
        ValueError: whenever an unexpected value is entered by a user it raises a ValueError

    Return:
        reply: return back either an integer or float

    Example:
        >>> from basic_market_calculator import get_user_input
        >>> rice_price = get_user_input("What's the price of Rice?")
            What's the price of Rice? Eben
        >>> print(rice_price)
            Eben
    """
    while True:
        try:
            if is_float:
                reply = float(input(f"{food_price_or_kg}: "))
            else:
                reply = int(input(f"{food_price_or_kg}: "))
            return reply
        except ValueError as e:
            print(f"{e}, Kindly enter a valid number")

def main():
    while True:
        user_reply = input("Welcome to Market Bill calculator, Enter Y to continue or N to quit: ")
        reply = user_reply.lower()
        if reply.lower() == "n":
            break
        elif reply == "y":
            rice_price = get_user_input("What's the price of Rice?")
            kg_rice = get_user_input("How many kg of Rice?", is_float = True)

            beans_price = get_user_input("What's the price of Beans?")
            kg_beans = get_user_input("How many kg of Beans?", is_float = True)

            garri_price = get_user_input("What's the price of Garri?")
            kg_garri = get_user_input("How many kg of Garri?", is_float = True)

            goods = {"Rice": [kg_rice, rice_price], "Beans": [kg_beans, beans_price], "Garri": [kg_garri, garri_price]}
            total = 0
            answer_list = []

            for key, value in goods.items():
                each_list = f"{key}: {value[0]}kg x N{value[1]} = N{(value[0]*value[1]):.2f}"
                answer_list.append(each_list)
                total += value[0] * value[1]

            left_and_right_dash = (len(answer_list[0]) - 13)//2
            print()
            print(f"{left_and_right_dash * '-'} MARKET BILL {left_and_right_dash * '-'}")
            for i in answer_list:
                print(i)
            print(len(answer_list[0]) * '-')
            print(f"\nTOTAL TO PAY: N{total:.2f}")
            break
        else:
            break

if __name__ == "__main__":
    main()