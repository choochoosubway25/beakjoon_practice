import sys


station_inputs = sys.stdin.readline().strip()
station_splits = station_inputs.split('(')
main_station_name = station_splits[0]
sub_station_name = '-'
if len(station_splits) == 2:
    sub_station_name = station_splits[1][:-1]
    main_station_name = main_station_name[:-1]
print(main_station_name)
print(sub_station_name)
