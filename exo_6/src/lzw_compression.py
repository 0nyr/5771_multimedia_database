

def encode(input_string: str) -> list[int]:
    """
    Encode a given string using the LZW algorithm.
    The encoding should be provided, here we are only going to support ASCII encoding.
    """

    # build table (dictionary) with all ASCII characters
    
    # convert int to ascii character
    table = {chr(i): i for i in range(256)}

    # initialize variables
    result: list[int] = []
    window: str = ""

    # loop through input string
    for char in input_string:
        window += char

        # if window is in table, keep current window for next iteration
        # if window is not in table, add window to table and output code for beginning of window
        if window not in table:
            last_char = window[-1]
            remaining_window = window[:-1]

            result.append(table[remaining_window])
            table[window] = len(table)
            window = last_char

    # encode last
    if window:
        result.append(table[window])
    
    return result


def decode(input_list: list[int]) -> str:
    """
    Decode a given list of integers using the LZW algorithm.
    The decoding should be provided, here we are only going to support ASCII encoding.
    """
    # build table (dictionary) with all ASCII characters
    table = {i: chr(i) for i in range(256)}

    # initialize variables
    result: str = ""
    last_decoded_string: str = ""

    # loop through input list
    for code in input_list:
        # get decoded string
        current_decoded = table[code]

        # build table
        window = last_decoded_string + current_decoded[0] # first character of the current decoded string
        if window not in table.values():
            table[len(table)] = window

        # we always have the code in the table since we are building it as we go
        last_decoded_string = current_decoded
        result += current_decoded
        
    return result


def main():

    input_strings = [
        "MISSISSIPISS",
        "TOBEORNOTTOBEORTOBEORNOT",
        "BABAABAAAABABAAABAAAAABABAAAAA",
    ]
    for string in input_strings:
        print("string:", string)

        result = encode(string)
        print("result:", result)

        decoded_string = decode(result)
        print("decoded_string:", decoded_string)

        assert decoded_string == string
        print()



if __name__ == "__main__":
    main()