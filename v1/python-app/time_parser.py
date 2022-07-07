def time_parser(x):
    if isinstance(x, list):
        days_grammar = "Day" if (int(x[3])==1) else "Days"
        hours_grammar = "Hour" if (int(x[2])==1) else "Hours"
        minutes_grammar = "Minute" if (int(x[1])==1) else "Minutes"
        seconds_grammar = "Second" if (int(x[0])==1) else "Seconds"
        days_final = f"{int(x[3])} {days_grammar}, " if (int(x[3])>0) else ""
        hours_final = f"{int(x[2])} {hours_grammar}, " if (int(x[2])>0) else ""
        minutes_final = f"{int(x[1])} {minutes_grammar}, " if (int(x[1])>0) else ""
        seconds_final = f"{int(x[0])} {seconds_grammar}" if (int(x[0])>0) else ""
        return days_final+hours_final+minutes_final+seconds_final
    elif isinstance(x, int) or isinstance(x, float):
        return  time_parser([x%60, (x//60)%60, ((x//60)//60)%60, (((x//60)//60)//24)%24])