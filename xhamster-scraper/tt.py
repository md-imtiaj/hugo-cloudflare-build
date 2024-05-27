#If hours is 0, omit it.
#If minutes is less than 10, pad it with a leading zero.
#Always show seconds as two digits if there are minutes.
#If there are only seconds, show 00:SS.

def seconds_to_hms(seconds):
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    if hours > 0:
        return f"{hours}:{minutes:02}:{seconds:02}"
    elif minutes > 0:
        return f"{minutes:02}:{seconds:02}"
    else:
        return f"00:{seconds:02}"


a = [1,2,3]
print(a[1:])
