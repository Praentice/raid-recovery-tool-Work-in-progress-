# RAID recovery tool
This CLI tool allows you to retrieve data as a whole disk image from faulty RAID arrays (Supported RAID : 0 and 5).
## Install
```
pip install -r requirements.txt
```
### Running the tool
```
./main.py -f path/to/first/file path/to/second/file -r 0 #Recover faulty RAID 0 array
./main.py -f path/to/first/file path/to/second/file path/to/third/file -r 5 -o custom_output #Recover faulty RAID 0 array and output the result to a disk image called "custom_output"

```
## Documentation
### Recovery from RAID 0
You need at least two disk files to recover the data from a faulty RAID 0 array.
### Recovery from RAID 5
You need at least three disk files to recover the data from a fault RAID 5 array.
If you only have 2 disks from a faulty RAID 5 array, you can generate the third file by XORING the two another files.
You'll need the following tool to do this : https://github.com/Praentice/xor-raid
### Mandatory flags
| Flag        | Description                               |
|-------------|-------------------------------------------|
| -r / --raid | Specify the type of the faulty RAID array |
| -f / --file | Absolute path to the disk image files     |
### Optional flags
| Flag           | Description                                                                       |
|----------------|-----------------------------------------------------------------------------------|
| -o / --output  | Specify a name for the output file (Without this flag, default name is "output".) |
| -s / --sector  | Specify size of sector in bytes (Default value is 512)                            |
| -v / --version | Print the version of tool and exit                                                |
## Credits

This tool was created by Prantice and is provided for free under GNU License.


