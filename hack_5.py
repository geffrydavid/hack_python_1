"""
text: "fooziman" output => "f00z1m@n"
"""

def fn_hack_5():
    result = "fooziman"
    return result[:-7] + "00" + result[3:-4] + "1" + result[5:-2] + "@" + result[-1]

print(fn_hack_5())