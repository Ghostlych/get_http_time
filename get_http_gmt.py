#!/usr/bin/env python3


from time import gmtime


def get_http_gmt():
    """ Gets pretty gmt time. Returns a string."""
    days = {0 : "Mon",
            1 : "Tue",
            2 : "Wed",
            3 : "Thu",
            4 : "Fri",
            5 : "Sat",
            6 : "Sun"}
    months = {1 : "Jan",
              2 : "Feb",
              3 : "Mar",
              4 : "Apr",
              5 : "May",
              6 : "Jun",
              7 : "Jul",
              8 : "Aug",
              9 : "Sep",
              10 : "Oct",
              11 : "Nov",
              12 : "Dec"}
    time = gmtime()
    pretty_time = "{day}, ".format(day = days[time.tm_wday])
    pretty_time += "{:02} ".format(time.tm_wday)
    pretty_time += "{month} ".format(month = months[time.tm_mon])
    pretty_time += "{year} ".format(year = time.tm_year)
    pretty_time += "{:02}:{:02}:".format(time.tm_hour, time.tm_min)
    pretty_time += "{:02} ".format(time.tm_sec)
    pretty_time += "GMT"
    return pretty_time


if __name__ == """__main__""":
    print(get_pretty_gmt())
