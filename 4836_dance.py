import sys

while True:
    dance_str = str(sys.stdin.readline().strip())
    if dance_str == '':
        break
    dance_form = dance_str.split()
    errors = set()
    moving_count = len(dance_form)
    dip_allow = set()
    is_hop_contained = True
    dip_error = set()
    # prepare for check the rule 1
    for i in range(moving_count):
        moving = dance_form[i]
        if moving == 'jiggle':
            dip_allow.add(i+1)
            dip_allow.add(i+2)
        elif moving == 'twirl':
            is_hop_contained = False
            dip_allow.add(i-1)
    # check the rules
    # check the length
    if moving_count < 3:
        errors.add(2)
    dip_count = 0
    for i in range(moving_count):
        moving = dance_form[i]
        # check the rule 4
        if i == 0:
            if moving == 'jiggle':
                errors.add(4)
        # check the rule 2
        if i == moving_count - 3 or i == moving_count - 1:
            if moving != 'clap':
                errors.add(2)
        elif i == moving_count - 2:
            if moving != 'stomp':
                errors.add(2)
        # check the rule 1
        if moving == 'dip':
            dip_count += 1
            if i not in dip_allow:
                errors.add(1)
                dip_error.add(i)
        # check the rule 3
        if moving == 'hop':
            is_hop_contained = True
    if not is_hop_contained:
        errors.add(3)
    # check the rule 5
    if dip_count < 1:
        errors.add(5)

    # mark the dip error
    for j in dip_error:
        dance_form[j] = dance_form[j].upper()

    # print result
    errors_list = list(errors)
    errors_list.sort()
    result_part = 'form '
    error_count = len(errors_list)
    if error_count == 0:
        result_part += 'ok'
    elif error_count == 1:
        result_part += f'error {errors_list[0]}'
    else:
        result_part += 'errors '
        for k in range(error_count - 1):
            result_part += f'{errors_list[k]}, '
        result_part = result_part[:-2]
        result_part += f' and {errors_list[-1]}'
    result_part += ': '
    result_part += ' '.join(dance_form)
    print(result_part)
