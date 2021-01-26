def condition(row):
    '''
    Args:
        row (int): Individual entry for specified column
    Returns:
        val (int): If number equals 0 returns  
                   Else return 1
     '''
    if row == 0:
        val = 0
    else:
        val = 1
    return val


def roundup(row):
    '''
    Args:
        row (int): values in row equal to specified numbers
    Return:
        row (int): If value meets criteria add .25 and return new value
    '''
    if row == 0.75:
        row += .25
    elif row == 1.25:
        row += .25
    elif row == 1.75:
        row += .25
    elif row == 2.25:
        row += .25
    elif row == 2.75:
        row += .25
    elif row == 3.25:
        row += .25
    else:
        row == row
    return row