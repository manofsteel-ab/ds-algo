import sys


class ErrorMessage:
    INVALID_STRING = "Invalid string"
    INVALID_ARGUMENT = "Invalid string"
    INVALID_TYPE = "Invalid argument type"
    MISSING_PARAM = "{0} is missing"
    MAX_ARG_LIMIT = " Only two arguments are allowed"


class CustomFormatter:

    @classmethod
    def validate_arguments(cls, args=[]):
        args_len = len(args)
        if args_len == 1:
            return cls.format(ErrorMessage.MISSING_PARAM, "both argument")

        if args_len == 2:
            return cls.format(
                ErrorMessage.MISSING_PARAM, "argument2"
            )
        if args_len > 3:
            return ErrorMessage.MAX_ARG_LIMIT
        return None

    @classmethod
    def validate_string(cls, string):
        """
        If string is none or empty return false other wise return true
        :param string:
        :return:
        """
        if string is None:
            return ErrorMessage.INVALID_STRING
        if type(string) != str:
            return ErrorMessage.INVALID_TYPE

        return None

    @classmethod
    def format(cls, place_holder_string, substitutions, replace_within="{}"):
        """
        Format given place_holder_string, using format_with string
        :param place_holder_string: string with placeholder
        :param substitutions: comma separated substitution word
        :param replace_within: replace character withing given
        :return: formatted string
        """

        # place_holder_string can not be empty

        if cls.validate_string(place_holder_string):
            return cls.validate_string(place_holder_string)

        if cls.validate_string(substitutions):
            return cls.validate_string(substitutions)

        substitution_list = substitutions.split(',')
        substitution_dict = {str(v): k for v, k in enumerate(substitution_list)}
        formatted_string = ""
        sz = len(place_holder_string)
        index = 0
        while index < sz:
            char = place_holder_string[index]
            if not substitution_list:
                break
            if char not in [replace_within[0]]:
                formatted_string += char
            if char == replace_within[0]:
                next_closing = place_holder_string.find(
                    replace_within[1], index + 1
                )
                in_between_str = place_holder_string[index+1: next_closing]
                if substitution_dict.get(in_between_str):
                    formatted_string += substitution_dict.get(in_between_str)
                    index = next_closing
                else:
                    formatted_string += char
            index += 1
        return formatted_string


argumentList = sys.argv

text_file = open("abhishek_yadav_output.txt", "a")

text_file.write("Input\n")
text_file.write(str(argumentList)[1:-1] + "\n")
argument_validation = CustomFormatter.validate_arguments(argumentList)
if argument_validation:
    text_file.write("Output\n")
    text_file.write(argument_validation + "\n\n")
else:

    text_file.write("Output\n")
    ans = CustomFormatter.format(argumentList[1], argumentList[2])
    text_file.write(ans + "\n\n")
