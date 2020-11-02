def arithmetic_arranger(problems, show_answer=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    first_row = ''
    second_row = ''
    third_row = ''
    fourth_row = ''

    for problem in problems:
        [number_one, sign, number_two] = problem.split()

        validation_result = validate_problem(number_one, number_two, sign)
        if len(validation_result) > 0:
            return validation_result

        row_length = max(len(number_one), len(number_two)) + 2

        first_row += left_pad(number_one, length=row_length) + ' ' * 4
        second_row += sign + left_pad(number_two, length=row_length - 1) + ' ' * 4
        third_row += left_pad('', length=row_length, pad='-') + ' ' * 4

        answer = get_answer(number_one, number_two, sign)
        fourth_row += left_pad(answer, length=row_length) + ' ' * 4

    return format_result(first_row, second_row, third_row, fourth_row, show_answer)


def left_pad(text, length=4, pad=' '):
    return pad * (length - len(text)) + text


def get_answer(number_one, number_two, sign):
    if sign == '+':
        return str(int(number_one) + int(number_two))

    return str(int(number_one) - int(number_two))


def validate_problem(number_one, number_two, sign):
    if sign not in ['+', '-']:
        return "Error: Operator must be '+' or '-'."

    if len(number_one) > 4 or len(number_two) > 4:
        return 'Error: Numbers cannot be more than four digits.'

    if not number_one.isnumeric() or not number_two.isnumeric():
        return 'Error: Numbers must only contain digits.'

    return ''


def format_result(first_row, second_row, third_row, fourth_row, show_answer):
    result = first_row.rstrip() + '\n' + second_row.rstrip() + '\n' + third_row.rstrip()
    if show_answer:
        result += '\n' + fourth_row.rstrip()
    return result
