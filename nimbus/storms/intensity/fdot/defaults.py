import os

from nimbus.storms.intensity import IntensityCurve
from nimbus.data import data


abs_path = os.path.abspath(__file__)
dir_name = os.path.dirname(abs_path)

zone01tuples = data.tuples_from_csv(dir_name + "/csv/zone01.csv")
zone02tuples = data.tuples_from_csv(dir_name + "/csv/zone02.csv")
zone03tuples = data.tuples_from_csv(dir_name + "/csv/zone03.csv")
zone04tuples = data.tuples_from_csv(dir_name + "/csv/zone04.csv")
zone05tuples = data.tuples_from_csv(dir_name + "/csv/zone05.csv")
zone06tuples = data.tuples_from_csv(dir_name + "/csv/zone06.csv")
zone07tuples = data.tuples_from_csv(dir_name + "/csv/zone07.csv")
zone08tuples = data.tuples_from_csv(dir_name + "/csv/zone08.csv")
zone09tuples = data.tuples_from_csv(dir_name + "/csv/zone09.csv")
zone10tuples = data.tuples_from_csv(dir_name + "/csv/zone10.csv")
zone11tuples = data.tuples_from_csv(dir_name + "/csv/zone11.csv")

zone01_02year = IntensityCurve("FDOT ZONE 01 02-YEAR", zone01tuples[0][0], zone01tuples[0][1:len(zone01tuples)])
zone01_03year = IntensityCurve("FDOT ZONE 01 03-YEAR", zone01tuples[1][0], zone01tuples[1][1:len(zone01tuples)])
zone01_05year = IntensityCurve("FDOT ZONE 01 05-YEAR", zone01tuples[2][0], zone01tuples[2][1:len(zone01tuples)])
zone01_10year = IntensityCurve("FDOT ZONE 01 10-YEAR", zone01tuples[3][0], zone01tuples[3][1:len(zone01tuples)])
zone01_25year = IntensityCurve("FDOT ZONE 01 25-YEAR", zone01tuples[4][0], zone01tuples[4][1:len(zone01tuples)])
zone01_50year = IntensityCurve("FDOT ZONE 01 50-YEAR", zone01tuples[5][0], zone01tuples[5][1:len(zone01tuples)])

zone02_02year = IntensityCurve("FDOT ZONE 02 02-YEAR", zone02tuples[0][0], zone02tuples[0][1:len(zone02tuples)])
zone02_03year = IntensityCurve("FDOT ZONE 02 03-YEAR", zone02tuples[1][0], zone02tuples[1][1:len(zone02tuples)])
zone02_05year = IntensityCurve("FDOT ZONE 02 05-YEAR", zone02tuples[2][0], zone02tuples[2][1:len(zone02tuples)])
zone02_10year = IntensityCurve("FDOT ZONE 02 10-YEAR", zone02tuples[3][0], zone02tuples[3][1:len(zone02tuples)])
zone02_25year = IntensityCurve("FDOT ZONE 02 25-YEAR", zone02tuples[4][0], zone02tuples[4][1:len(zone02tuples)])
zone02_50year = IntensityCurve("FDOT ZONE 02 50-YEAR", zone02tuples[5][0], zone02tuples[5][1:len(zone02tuples)])

zone03_02year = IntensityCurve("FDOT ZONE 03 02-YEAR", zone03tuples[0][0], zone03tuples[0][1:len(zone03tuples)])
zone03_03year = IntensityCurve("FDOT ZONE 03 03-YEAR", zone03tuples[1][0], zone03tuples[1][1:len(zone03tuples)])
zone03_05year = IntensityCurve("FDOT ZONE 03 05-YEAR", zone03tuples[2][0], zone03tuples[2][1:len(zone03tuples)])
zone03_10year = IntensityCurve("FDOT ZONE 03 10-YEAR", zone03tuples[3][0], zone03tuples[3][1:len(zone03tuples)])
zone03_25year = IntensityCurve("FDOT ZONE 03 25-YEAR", zone03tuples[4][0], zone03tuples[4][1:len(zone03tuples)])
zone03_50year = IntensityCurve("FDOT ZONE 03 50-YEAR", zone03tuples[5][0], zone03tuples[5][1:len(zone03tuples)])

zone04_02year = IntensityCurve("FDOT ZONE 04 02-YEAR", zone04tuples[0][0], zone04tuples[0][1:len(zone04tuples)])
zone04_03year = IntensityCurve("FDOT ZONE 04 03-YEAR", zone04tuples[1][0], zone04tuples[1][1:len(zone04tuples)])
zone04_05year = IntensityCurve("FDOT ZONE 04 05-YEAR", zone04tuples[2][0], zone04tuples[2][1:len(zone04tuples)])
zone04_10year = IntensityCurve("FDOT ZONE 04 10-YEAR", zone04tuples[3][0], zone04tuples[3][1:len(zone04tuples)])
zone04_25year = IntensityCurve("FDOT ZONE 04 25-YEAR", zone04tuples[4][0], zone04tuples[4][1:len(zone04tuples)])
zone04_50year = IntensityCurve("FDOT ZONE 04 50-YEAR", zone04tuples[5][0], zone04tuples[5][1:len(zone04tuples)])

zone05_02year = IntensityCurve("FDOT ZONE 05 02-YEAR", zone05tuples[0][0], zone05tuples[0][1:len(zone05tuples)])
zone05_03year = IntensityCurve("FDOT ZONE 05 03-YEAR", zone05tuples[1][0], zone05tuples[1][1:len(zone05tuples)])
zone05_05year = IntensityCurve("FDOT ZONE 05 05-YEAR", zone05tuples[2][0], zone05tuples[2][1:len(zone05tuples)])
zone05_10year = IntensityCurve("FDOT ZONE 05 10-YEAR", zone05tuples[3][0], zone05tuples[3][1:len(zone05tuples)])
zone05_25year = IntensityCurve("FDOT ZONE 05 25-YEAR", zone05tuples[4][0], zone05tuples[4][1:len(zone05tuples)])
zone05_50year = IntensityCurve("FDOT ZONE 05 50-YEAR", zone05tuples[5][0], zone05tuples[5][1:len(zone05tuples)])

zone06_02year = IntensityCurve("FDOT ZONE 06 02-YEAR", zone06tuples[0][0], zone06tuples[0][1:len(zone06tuples)])
zone06_03year = IntensityCurve("FDOT ZONE 06 03-YEAR", zone06tuples[1][0], zone06tuples[1][1:len(zone06tuples)])
zone06_05year = IntensityCurve("FDOT ZONE 06 05-YEAR", zone06tuples[2][0], zone06tuples[2][1:len(zone06tuples)])
zone06_10year = IntensityCurve("FDOT ZONE 06 10-YEAR", zone06tuples[3][0], zone06tuples[3][1:len(zone06tuples)])
zone06_25year = IntensityCurve("FDOT ZONE 06 25-YEAR", zone06tuples[4][0], zone06tuples[4][1:len(zone06tuples)])
zone06_50year = IntensityCurve("FDOT ZONE 06 50-YEAR", zone06tuples[5][0], zone06tuples[5][1:len(zone06tuples)])

zone07_02year = IntensityCurve("FDOT ZONE 07 02-YEAR", zone07tuples[0][0], zone07tuples[0][1:len(zone07tuples)])
zone07_03year = IntensityCurve("FDOT ZONE 07 03-YEAR", zone07tuples[1][0], zone07tuples[1][1:len(zone07tuples)])
zone07_05year = IntensityCurve("FDOT ZONE 07 05-YEAR", zone07tuples[2][0], zone07tuples[2][1:len(zone07tuples)])
zone07_10year = IntensityCurve("FDOT ZONE 07 10-YEAR", zone07tuples[3][0], zone07tuples[3][1:len(zone07tuples)])
zone07_25year = IntensityCurve("FDOT ZONE 07 25-YEAR", zone07tuples[4][0], zone07tuples[4][1:len(zone07tuples)])
zone07_50year = IntensityCurve("FDOT ZONE 07 50-YEAR", zone07tuples[5][0], zone07tuples[5][1:len(zone07tuples)])

zone08_02year = IntensityCurve("FDOT ZONE 08 02-YEAR", zone08tuples[0][0], zone08tuples[0][1:len(zone08tuples)])
zone08_03year = IntensityCurve("FDOT ZONE 08 03-YEAR", zone08tuples[1][0], zone08tuples[1][1:len(zone08tuples)])
zone08_05year = IntensityCurve("FDOT ZONE 08 05-YEAR", zone08tuples[2][0], zone08tuples[2][1:len(zone08tuples)])
zone08_10year = IntensityCurve("FDOT ZONE 08 10-YEAR", zone08tuples[3][0], zone08tuples[3][1:len(zone08tuples)])
zone08_25year = IntensityCurve("FDOT ZONE 08 25-YEAR", zone08tuples[4][0], zone08tuples[4][1:len(zone08tuples)])
zone08_50year = IntensityCurve("FDOT ZONE 08 50-YEAR", zone08tuples[5][0], zone08tuples[5][1:len(zone08tuples)])

zone09_02year = IntensityCurve("FDOT ZONE 09 02-YEAR", zone09tuples[0][0], zone09tuples[0][1:len(zone09tuples)])
zone09_03year = IntensityCurve("FDOT ZONE 09 03-YEAR", zone09tuples[1][0], zone09tuples[1][1:len(zone09tuples)])
zone09_05year = IntensityCurve("FDOT ZONE 09 05-YEAR", zone09tuples[2][0], zone09tuples[2][1:len(zone09tuples)])
zone09_10year = IntensityCurve("FDOT ZONE 09 10-YEAR", zone09tuples[3][0], zone09tuples[3][1:len(zone09tuples)])
zone09_25year = IntensityCurve("FDOT ZONE 09 25-YEAR", zone09tuples[4][0], zone09tuples[4][1:len(zone09tuples)])
zone09_50year = IntensityCurve("FDOT ZONE 09 50-YEAR", zone09tuples[5][0], zone09tuples[5][1:len(zone09tuples)])

zone10_02year = IntensityCurve("FDOT ZONE 10 02-YEAR", zone10tuples[0][0], zone10tuples[0][1:len(zone10tuples)])
zone10_03year = IntensityCurve("FDOT ZONE 10 03-YEAR", zone10tuples[1][0], zone10tuples[1][1:len(zone10tuples)])
zone10_05year = IntensityCurve("FDOT ZONE 10 05-YEAR", zone10tuples[2][0], zone10tuples[2][1:len(zone10tuples)])
zone10_10year = IntensityCurve("FDOT ZONE 10 10-YEAR", zone10tuples[3][0], zone10tuples[3][1:len(zone10tuples)])
zone10_25year = IntensityCurve("FDOT ZONE 10 25-YEAR", zone10tuples[4][0], zone10tuples[4][1:len(zone10tuples)])
zone10_50year = IntensityCurve("FDOT ZONE 10 50-YEAR", zone10tuples[5][0], zone10tuples[5][1:len(zone10tuples)])

zone11_02year = IntensityCurve("FDOT ZONE 11 02-YEAR", zone11tuples[0][0], zone11tuples[0][1:len(zone11tuples)])
zone11_03year = IntensityCurve("FDOT ZONE 11 03-YEAR", zone11tuples[1][0], zone11tuples[1][1:len(zone11tuples)])
zone11_05year = IntensityCurve("FDOT ZONE 11 05-YEAR", zone11tuples[2][0], zone11tuples[2][1:len(zone11tuples)])
zone11_10year = IntensityCurve("FDOT ZONE 11 10-YEAR", zone11tuples[3][0], zone11tuples[3][1:len(zone11tuples)])
zone11_25year = IntensityCurve("FDOT ZONE 11 25-YEAR", zone11tuples[4][0], zone11tuples[4][1:len(zone11tuples)])
zone11_50year = IntensityCurve("FDOT ZONE 11 50-YEAR", zone11tuples[5][0], zone11tuples[5][1:len(zone11tuples)])

defaults_list = [
    zone01_02year, zone01_03year, zone01_05year, zone01_10year, zone01_25year, zone01_50year,
    zone02_02year, zone02_03year, zone02_05year, zone02_10year, zone02_25year, zone02_50year,
    zone03_02year, zone03_03year, zone03_05year, zone03_10year, zone03_25year, zone03_50year,
    zone04_02year, zone04_03year, zone04_05year, zone04_10year, zone04_25year, zone04_50year,
    zone05_02year, zone05_03year, zone05_05year, zone05_10year, zone05_25year, zone05_50year,
    zone06_02year, zone06_03year, zone06_05year, zone06_10year, zone06_25year, zone06_50year,
    zone07_02year, zone07_03year, zone07_05year, zone07_10year, zone07_25year, zone07_50year,
    zone08_02year, zone08_03year, zone08_05year, zone08_10year, zone08_25year, zone08_50year,
    zone09_02year, zone09_03year, zone09_05year, zone09_10year, zone09_25year, zone09_50year,
    zone10_02year, zone10_03year, zone10_05year, zone10_10year, zone10_25year, zone10_50year,
    zone11_02year, zone11_03year, zone11_05year, zone11_10year, zone11_25year, zone11_50year,
]

