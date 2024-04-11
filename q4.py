def reformat_date(date_str, input_format, output_format):
    """
    Returns a new date string formatted according to the output date format.

    >>> reformat_date("12/31/1998", "M/D/Y", "D/M/Y")
    '31/12/1998'
    >>> reformat_date("1/2/3", "M/D/Y", "Y/M/D")
    '3/1/2'
    >>> reformat_date("0/200/4", "Y/D/M", "M/Y")
    '4/0'
    >>> reformat_date("3/2", "M/D", "D")
    '2'
    """
    # Split the date string and input date format by '/'
    date_parts = date_str.split('/')
    input_symbols = input_format.split('/')
    output_symbols = output_format.split('/')

    # Create a dictionary to map input symbols to corresponding date parts
    input_map = {'M': date_parts[0], 'D': date_parts[1], 'Y': date_parts[2]}
    
    # Initialize an empty list to store formatted date parts
    formatted_date_parts = []

    # Iterate over output symbols and add the corresponding date part to the formatted list
    for symbol in output_symbols:
        formatted_date_parts.append(input_map[symbol])

    # Join the formatted date parts with '/'
    return '/'.join(formatted_date_parts)


