def arithmetic_arranger(problems, display_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    first_operands = []
    second_operands = []
    operators = []
    answers = []
    for problem in problems:
        parts = problem.split()
        if parts[1] not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        if not (parts[0].isdigit() and parts[2].isdigit()):
            return 'Error: Numbers must only contain digits.'
        if len(parts[0]) > 4 or len(parts[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        first_operands.append(parts[0])
        operators.append(parts[1])
        second_operands.append(parts[2])
        if parts[1] == '+':
            answers.append(str(int(parts[0]) + int(parts[2])))
        elif parts[1] == '-':
            answers.append(str(int(parts[0]) - int(parts[2])))

    first_line = ""
    second_line = ""
    dashes = ""
    answer_line = ""

    for i in range(len(problems)):
        length = max(len(first_operands[i]), len(second_operands[i])) + 2
        first_line += first_operands[i].rjust(length)
        second_line += operators[i] + second_operands[i].rjust(length - 1)
        dashes += "-" * length
        answer_line += answers[i].rjust(length)
        if i < len(problems) - 1:
            first_line += "    "
            second_line += "    "
            dashes += "    "
            answer_line += "    "

    if display_answers:
        arranged_problems = first_line + "\n" + second_line + "\n" + dashes + "\n" + answer_line
    else:
        arranged_problems = first_line + "\n" + second_line + "\n" + dashes

    return arranged_problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')