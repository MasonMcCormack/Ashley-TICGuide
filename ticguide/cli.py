import argparse

import ticguide


def main():

    parser = argparse.ArgumentParser(
                                     description='ticguide: quick + painless TESS observing information',
                                     prog'ticguide',
    )
    parser.add_argument('--version',
                        action='version',
                        version="%(prog)s {}".format(tiguide.__version__),
                        help="print version number and exit",
    )

    main_parser = argparse.ArgumentParser(add_help=False)

    main_parser.add_argument('--file', '--in', '--input', 
                             metavar='path', 
                             help="input list of targets (requires csv with 'tic' column of integer type)", 
                             dest='input', 
                             default='todo.csv',
    )
    main_parser.add_argument('--out', '--output',
                              metavar='path', 
                             help='path to save the observed TESS table for all targets', 
                             dest='output', 
                             default='all_observed.csv',
    )
    main_parser.add_argument('--path', 
                             metavar='path', 
                             help='path to directory', 
                             type=str, 
                             dest='path', 
                             default=os.path.join(os.path.abspath(os.getcwd()),''),
    )
    main_parser.add_argument('-s', '--save', 
                             help='disable the saving of output files', 
                             dest='save', 
                             default=True, 
                             action='store_false',
    )
    main_parser.add_argument('--star', '--stars', '--tic', 
                             metavar='star', 
                             help='TESS Input Catalog (TIC) IDs', 
                             type=int, 
                             dest='stars', 
                             nargs='*', 
                             default=None,
    )
    main_parser.add_argument('-t', '--total', 
                             help='include total sectors per target per cadence', 
                             dest='total', 
                             default=True, 
                             action='store_false',
    )
    main_parser.add_argument('-v', '--verbose', 
                             help='turn off verbose output', 
                             dest='verbose', 
                             default=True, 
                             action='store_false',
    )

    main_parser.set_defaults(func=ticguide.pipeline)

    args = main_parser.parse_args()
    args.func(args)



if __name__ == '__main__':

    main()