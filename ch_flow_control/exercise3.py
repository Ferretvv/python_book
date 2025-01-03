# Without running the following code, what does it print? Why?

def bar_code_scanner(serial):
    match serial:
        case '123':
            print('Product1')
        case '113':
            print('Product2')
        case '142':
            print('Product3')
        case _:
            print('Product not found!')

bar_code_scanner('113')
bar_code_scanner(142)

# Prints Product2 then prints Product not found!
# bar_coe_scanner('113') matches case '123' and bar_coe_scanner(142) does not match any case (case_)