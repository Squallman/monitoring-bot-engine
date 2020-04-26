def default(stores):
    elements = [{'text': store} for store in stores]
    change_location_keyboard = [{'text': 'Change location'}]
    keyboards = __split_array(elements)
    keyboards.append(change_location_keyboard)
    return keyboards


def __split_array(elements):
    result = []
    temp_array = []
    length = len(elements)
    for i in range(0, length):
        element = elements[i]
        if i % 2 == 0:
            temp_array = [element]
            if i == length - 1:
                result.append(temp_array)
        else:
            temp_array.append(element)
            result.append(temp_array)
    return result
