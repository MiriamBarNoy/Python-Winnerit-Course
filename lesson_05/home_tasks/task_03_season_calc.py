month_to_check =input("please enter a month to check : ")

match month_to_check.upper():
    case "JANUARY" | "FEBRUARY" | "DECEMBER":
        print("Winter month")
    case "MARCH" | "APRIL" | "MAY":
        print("Spring month")
    case "JUNE" | "JULY" | "AUGUST":
        print("Summer month")
    case "SEPTEMBER" | "OCTOBER" | "NOVEMBER":
        print("Autumn month")
    case _:
        print("invalid month")