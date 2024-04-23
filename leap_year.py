def is_leap(year):
    leap = False
    if year % 4 != 0:
        return leap
    elif year % 100 == 0:
        if year % 400 != 0:
            return leap
        else:
            return True
    else:
        return True
    return leap


year = int(input())
print(is_leap(year))