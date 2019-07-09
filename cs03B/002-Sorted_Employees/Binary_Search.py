@classmethod
def binary_search_for_last_name(cls, data, key_last_nm,
                                first_index, last_index):
    # exhuasted search
    if first_index > last_index:
        return cls.NOT_FOUND

    middle_index = int((first_index + last_index) / 2)

    result = Student.compare_strings_ignore_case(
        key_last_nm,
        data[middle_index].get_last_name()
    )

    # < 0 means key before middle index
    if result < 0:
        return cls.binary_search_for_last_name(
            data, key_last_nm, first_index, middle_index - 1)

    # > 0 means key after middle index
    if result > 0:
        return cls.binary_search_for_last_name(
            data, key_last_nm, middle_index + 1, last_index)

    # else key IS in middle index position, i.e., found him
    return middle_index