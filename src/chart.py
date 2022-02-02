"""
Generating a crosstab of groundspeed and distance times for IFR
non-precision approaches. Omitting logging and such stuff since this is
simple project

author: Derek Herincx, derek663@gmail.com
last_updated: 02/01/2022
"""
import argparse
import os

import numpy as np
import pandas as pd

def main(args_dict, speed_interval=5, dst_interval=0.25):
    if not os.path.isdir(args_dict['output_dir']):
        raise OSError("Specified output directory doesn't exist")

    speeds = args_dict['speeds']
    dsts = args_dict['distances']

    approach_speeds = list(range(speeds[0], speeds[1], speed_interval))
    distances = np.arange(dsts[0], dsts[1], dst_interval)

    def format_minutes(mins):
        """Returns decimal minutes as MM:SS
        """
        if mins < 1:
            whole_mins = "00"
            remainder_mins = int(mins * 60)
        else:
            whole_mins = int(mins)
            remainder_mins = int((mins % whole_mins) * 60)
        return f"{whole_mins}:{remainder_mins}"

    df = pd.DataFrame(columns=approach_speeds, index=distances)

    for dist in distances:
        for speed in approach_speeds:
            df.loc[dist, speed] = (dist/speed) * 60

    # formatting of final dataframe output
    df = df.applymap(format_minutes)
    df.columns = [f"{col}kts" for col in df]
    df.index = [f"{i}nm" for i in df.index]

    output_dir = os.path.join(args_dict['output_dir'], 'ifr_distance_time.csv')
    df.to_csv(output_dir, index=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='A small utility for IFR pilots looking to generate '
        'a more complete crosstab of groundspeeds & distances to a MAP'
    )
    parser.add_argument(
        '-d',
        '--distances',
        type=int,
        nargs='+',
        required=False,
        default=[1, 7],
        help="Specify a range of distances separated by a space"
    )
    parser.add_argument(
        '-s',
        '--speeds',
        type=int,
        nargs='+',
        required=False,
        default=[60, 185],
        help="Specify a range of groundspeeds, separated by a space"
    )
    parser.add_argument(
        '-o',
        '--output_dir',
        type=str,
        required=True,
        help="Output directory to dump file at"
    )
    args_dict = vars(parser.parse_args())

    main(args_dict)
