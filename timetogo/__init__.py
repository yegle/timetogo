from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import enum

stdchunk = enum.Enum('StdChunk',
[
    'long_month', # "January"
    'month', # "Jan"
    'num_month', # "1"
    'zero_month' # "01"
    'long_week_day', # "Monday"
    'week_day', # "Mon"
    'day', # "2"
    'under_day', # "_2"
    'zero_day', # "02"
    'hour', # "15"
    'hour_12', # "3"
    'zero_hour_12', # "03"
    'minute', # "4"
    'zero_minute', # "04"
    'second', # "5"
    'zero_second', # "05"
    'long_year', # "2006"
    'year', # "06"
    'pm_upper', # "PM"
    'pm_lower', # "pm"
    'tz', # "MST"
    'iso_8601_tz', # "Z0700"
    'iso_8601_seconds_tz', # "Z070000"
    'iso_8601_colon_tz', # "Z07:00"
    'iso_8601_colon_seconds_tz', # "Z07:00:00"
    'num_tz', # "-0700"
    'num_seconds_tz', # "-070000"
    'num_short_tz', # "-07"
    'num_colon_tz', # "-07:00"
    'num_colon_seconds_tz', # "-07:00:00"
    'frac_second_0', # ".0", ".00", ...
    'frac_second_9', # ".9", ".99", ...
    'need_date',
    'need_clock',
    ]
)

std0x = [
    stdchuck.zero_month,
    stdchuck.zero_day,
    stdchuck.zero_hour_12,
    stdchuck.zero_minute,
    stdchuck.zero_second,
    stdchuck.year,
]

def format(datetime_, layout):
  while layout:
    pass
  pass

def parse(value, layout):
  pass

def starts_with_lowercase(string):
  return string and 'a' <= string[0] <= 'z'

def next_std_chuck(layout):
  for i, c in enumerate(layout):
    if c == 'J':
      # January, Jan
      if layout.startswith("Jan", i):
        if layout.startswith("January", i):
          return layout[:i], stdchunk.long_year, layout[i+7:]
        elif layout[i+3:] and layout[i+3] in string.ascii_lowercase:
          return layout[:i], stdchuck.month, layout[i+3:]
    elif c == 'M':
      # Monday, MOn, MST
      if layout.startswith("Mon", i):
        if layout.startswith("Monday", i):
          return layout[:i], stdchunk.long_week_day, layout[i+6:]
        elif layout[i+3:] and layout[i+3] in string.ascii_lowercase:
          return layout[:i], stdchunk.week_day, layout[i+3:]
    elif c == '0':
      # 01, 02, 03, 04, 05, 06
      if layout[i+1:] and '1' <= layout[i+1] <= '6':
        return layout[:i], std0x[ord(layout[i+1]) - ord('1')], layout[i+2:]
    elif c == '1':
      if layout[i+1:] and layout[i+1] == '5':
      # 15, 1
        return layout[:i], stdchunk.hour, layout[i+2:]
      return layout[:i], stdchunk.num_month, layout[i+1:]
    elif c == '2':
      # 2006, 2
      if layout[i+3:] and layout.startswith("2006", i):
        return layout[:i], stdchunk.long_year, layout[i+4:]
      return layout[:i], stdchunk.day, layout[i+1:]
    elif c == '_' and layout.startswith("_2", i):
        return layout[:i], stdchunk.under_day, layout[i+2:]
    elif c == '3':
      return layout[:i], stdchunk.hour_12, layout[i+1:]
    elif c == '4':
      return layout[:i], stdchunk.minute, layout[i+1:]
    elif c == '5':
      return layout[:i], stdchunk.second, layout[i+1:]
    elif c == 'P' and layout.startswith("PM", i):
      return layout[:i], stdchunk.pm_upper, layout[i+2:]
    elif c == 'p' and layout.startswith("pm", i):
      return layout[:i], stdchunk.pm_lower, layout[i+2:]
    elif c == '-':
      l = [
          ("-070000", stdchunk.num_seconds_tz),
          ("-07:00:00", stdchunk.num_colon_seconds_tz),
          ("-07:00", stdchunk.num_colon_tz),
          ("-07", stdchunk.num_short_tz)
      ]
      for x in l:
        if layout.startswith()
      if layout.startswith("-070000", i):
        return layout[:i], stdchunk.num_seconds_tz, layout[i+7:]
      elif layout.startswith("-07:00:00", i):
        return layout[:i], stdchunk.num_colon_seconds_tz, layout[i+9:]
      elif layout.startswith("-0700", i):
        return layout[:i], stdchunk.num_tz, layout[i+5:]
      elif layout.startswith("-07:00", i):
        return layout[:i], stdchunk.num_short_tz, layout[i+6:]


if __name__ == '__main__':
  pass
