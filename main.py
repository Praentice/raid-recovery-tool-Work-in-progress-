#!/usr/bin/python3
import argparse
import sys
import os
VERSION=1.0

def writeOutput(binaryOutput,outputNameFile):
    filename = "output"
    if outputNameFile != None:
        filename = outputNameFile
    open(filename, 'wb').write(binaryOutput)

def recoverRAID0(disks,sectorSize):
    if len(disks) > 1: #Check if we have at least, 2 disk images for the recovery
        print(disks,sectorSize)
    else:
        print("You need to specify at least 2 disk images for RAID 0.")
        exit(1)

def recoverRAID5(disks,sectorSize):
    if len(disks) > 2: #Check if we have at least, 3 disk images for the recovery
        print(disks, sectorSize)
    else:
        print("You need to specify at least 3 disk images for RAID 5.")
        exit(1)

def getOptions():
    parser = argparse.ArgumentParser(add_help=True, formatter_class=argparse.RawTextHelpFormatter,description=
    """
    RAID Recovery tool                    
    This CLI tool allows you to recover data in form of a disk image from faulty RAID 0 and 5 array.
    """,
    epilog=
    """
    Created by Prantice with love <3
    """,
    )
    parser.version = "The current version is {}".format(VERSION)
    parser.add_argument('-f', "--file", required=True,help="""Absolute path to the disk images file (Mandatory)""",nargs=*)
    parser.add_argument('-r', "--raid", required=False,help="""Specify version of RAID to recover (Mandatory)""", )
    parser.add_argument('-s', "--sector", required=False,type=int,default=512,help="""Specify size of sector in bytes (Default value is 512) (Optionnal)""", )
    parser.add_argument('-o', "--output", required=False,help="""Rename the output file (Default name is output) (Optionnal)""", )
    parser.add_argument('-v', '--version', action='version', help='print the version and exit')
    args = vars(parser.parse_args())
    return args

if __name__ == '__main__':
    args = getOptions()
    if (args['raid'] == 0):
        output = recoverRAID0(args['file'],args['sector'])
    elif (args['raid'] == 5):
        output = recoverRAID5(args['file'],args['sector'])
    writeOutput(output,args['output'])






