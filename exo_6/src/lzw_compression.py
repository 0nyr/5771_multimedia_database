

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
            print("new entry: <", window, len(table), ">")
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
    # WARN: need to take the first value out of input_list
    init_value = input_list[0]
    result: str = "" + table[init_value]
    last_decoded_string: str = result

    # loop through input list
    for code in input_list[1:]:
        # get decoded string
        if code in table:
            current_decoded = table[code]
        else:
            # corner case explained:
            #   source: https://github.com/amycardoso/lzw-text-file-compression/blob/master/lzw.py by Amy Cardoso
            #   Bit is not in the dictionary
            #   Get the last character printed + the first position of the last character printed
            #   because we must decode bits that are not present in the dictionary, so we have to guess what it represents, for example:
            #   let's say bit 37768 is not in the dictionary, so we get the last character printed, for example it was 'uh'
            #   and we take it 'uh' plus its first position 'u', resulting in 'uhu', which is the representation of bit 37768
            #   the only case where this can happen is if the substring starts and ends with the same character ("uhuhu").
            current_decoded = last_decoded_string + last_decoded_string[0] # corner case

        # build table
        window = last_decoded_string + current_decoded[0] # first character of the current decoded string
        if window not in table.values():
            print("code:", code, "new entry: <", len(table), window, ">")
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