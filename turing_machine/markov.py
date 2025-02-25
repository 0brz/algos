

# 0_01_0_0010_01
# check count zeros is odd/even
def is_even_zeros(str):
    state = "first"
    for t in str:
        print(f"___st={state} t={t}")
        if (state == "first"):
            if (t == '0'):
                state = "second"

        elif (state == "second"):
            if (t == '0'):
                state = "is_even"
        
        elif (state == "is_even"):
            if (t == '0'):
                state = "second"

    print(state)

#is_even_zeros("0_01_0_0010_01")
#is_even_zeros("001")
#is_even_zeros("00_1_00_0")

# summ two values on TAPE
# 101+101_
def summ_two(str):
    left = 0
    pos = 0
    right = 0

    state = "beg"

    # find operation pos
    op_index = 0
    cursor = 0

    left_len = 0
    right_len = 0
    cursor = 0
    while(cursor < len(str)):
        cursor += 1
        if (state == "beg"):
            if (str[cursor] == '+'):
                op_index = cursor-1
                left_len = cursor-2
            elif (str[cursor] == '_'):
                right_len = cursor-1-left_len
                state = "summ"
                cursor -= 1

        if (state == "summ"):
            cursor = -1
            state = "calc_left"
            pos = 0
        elif (state == "calc_left"):
            if (str[cursor] == '1'):
                left += 1*pow(2, pos)
                pos += 1
            elif (str[cursor] == '+'):
                pos = 0
                state = "calc_right"
            elif (str[cursor] == '0'):
                pos += 1
        elif (state == "calc_right"):
            if (str[cursor] == '1'):
                right += 1*pow(2, pos)
                pos += 1
            elif (str[cursor] == '_'):
                state = "ret"
                cursor -= 1
            elif (str[cursor] == '0'):
                pos += 1
        elif (state == "ret"):
            print(f"result of {left} + {right} = {left+right}")
            break

#summ_two("101010010111001+10001001000111_")

