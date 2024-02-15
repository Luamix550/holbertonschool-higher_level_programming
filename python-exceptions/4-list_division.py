#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError("out of range")
            try:
                quotient = my_list_1[i] / my_list_2[i]
            except ZeroDivisionError:
                print("division by 0")
                quotient = 0
            except TypeError:
                print("wrong type")
                quotient = 0
        except IndexError as e:
            print(e)
            break
        finally:
            result.append(quotient)
    return result
