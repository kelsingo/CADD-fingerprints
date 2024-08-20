'''
Usage:
    python ~/convert_mdtraj.py
'''

import argparse
import mdtraj as md

# def convert(input_file, output_file):
#     parser = argparse.ArgumentParser(description="Convert input file extension to output file extention by using mdtraj.")
#     parser.add_argument(input_file, '-i',
#                         default="trajectory.h5",
#                         help='The input file. Default is trajectory.h5.')
#     parser.add_argument(output_file, '-o',
#                         default='trajectory.dcd',
#                         help='The output file. Default is trajectory.dcd.')
#     args = parser.parse_args()

#     traj = md.load(args.input_file)
#     traj.save(args.output_file)



parser = argparse.ArgumentParser(description="Convert input file extension to output file extention by using mdtraj.")
parser.add_argument('--input_file', '-i',
                    default="1hp8.cif",
                    help='The input file. Default is trajectory.h5.')
parser.add_argument('--output_file', '-o',
                    default='trajectory.dcd',
                    help='The output file. Default is trajectory.dcd.')
args = parser.parse_args()


traj = md.load(args.input_file)
traj.save(args.output_file)
