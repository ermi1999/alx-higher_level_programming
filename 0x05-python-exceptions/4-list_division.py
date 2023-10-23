#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    result = []
    while (i < list_length):
        try:
            temp = my_list_1[i] / my_list_2[i]
            i += 1
        except ZeroDivisionError:
            print("division by 0")
            i += 1
        except TypeError:
            print("wrong type")
            i += 1
        except IndexError:
            print("out of range")
            i += 1
        finally:
            result.append(temp)
    return result
