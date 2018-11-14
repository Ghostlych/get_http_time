#!/usr/bin/env python3


from time import gmtime


def get_http_gmt():
    """ Gets http gmt time. Returns a string."""
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
    http_time = "{day}, ".format(day = days[time.tm_wday])
    http_time += "{:02} ".format(time.tm_mday)
    http_time += "{month} ".format(month = months[time.tm_mon])
    http_time += "{year} ".format(year = time.tm_year)
    http_time += "{:02}:{:02}:".format(time.tm_hour, time.tm_min)
    http_time += "{:02} ".format(time.tm_sec)
    http_time += "GMT"
    return http_time


if __name__ == """__main__""":
    print(get_http_gmt())
