

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

is_even_zeros("0_01_0_0010_01")
is_even_zeros("001")
is_even_zeros("00_1_00_0")