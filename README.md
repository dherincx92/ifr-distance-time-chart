# ifr-distance-time-chart
A utility for pilots who want a more exhaustive crosschart of FAF to MAP distance times

## Motivation
As an IFR student practicing approaches at KRMN, I noticed that Stafford airport does not identify a missed approach point by DME distance; it is one of those few approaches where a pilot has to rely on the FAF to MAP times specified on the approach plate.

An example of the FAF to MAP 5.5NM table for KRMN (do not use for navigation):
| Knots | Min:Sec |
| ---- | ------- |
60 | 5:30
90 | 3:40
120 | 2:45
150 | 2:12
180 | 1:50

## Usage
```
$ python chart.py [-d, --DISTANCES] [-s, --SPEEDS] [-o, --OUTPUT_DIR]
```

```
Named Arguments:
  -d, --DISTANCES
    Range of distances to specify times for. Distances will be created at 0.25nm intervals to help with extrapolation
  -s, --SPEEDS
    Range of speeds to use. Speeds will be created at 5kt intervals to help with extrapolation
  -o, --OUTPUT_DIR
    Output directory to dump crosstab file at
```

## Example

```
$ python chart.py -o /Users/dherincx/Desktop/ -s 60 70 -d 1 3
```

This command will generate a crosstab of groundspeeds between 60-70, _excluding_ 70kts so the final result should yield 2 speed columns, 60kts & 65 kts. Similar logic applies for the distance at each 0.25nm interval.

If not speeds or distances are specified, the command will generate a table with groundspeeds ranging from 60-180 knots and distances from 1-7nm

|  | 60 | 65
| --- | ---- | ----- |
1 | 1:00 | 0:55 
1.25 | 1:15 | 1:09 
1.5 | 1:30 | 1:23
1.75 | 1:45 | 1:36
2 | 2:00 | 1:50
2.25 | 2:15 | 2:04
2.5 | 2:30 | 2:18
2.75 | 2:45 | 2:32



