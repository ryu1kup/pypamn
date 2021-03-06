# pypamn
A python script to process and to merge nSort output files for XENONnT nVeto MC.

## dependencies
pypamn depends on of course ROOT, and additionally on the following packages.

- numpy
- pandas
- uproot

You can install easily these packages with the command

```
$ pip3 install -r requirements.txt
```

## usage
pypamn can be run from your command line.
Even if there are multiple nSort output files or only one output file, pypamn can process them/it with the same command

```
$ python3 pamn.py -i /path/to/nSort_output_dir/*_Sort.root [options]
```

where options are additional parameters to be given to pypamn;

- `-o, --output [OUTPUT_FILENAME]` ... The output filename. Currently csv and pickle are supported, which extensions are `.csv` and `.pkl` respectively.
- `-v, --verbose [VERBOSE_LEVEL]` ... The verbosity level.

pypamn can also understand a text file listing the paths to input files with the same option as the above.

```
$ python3 pamn.py -i /path/to/input.txt [options]
```

You can also check how to run pypamn with the command

```
$ python3 pamn.py --help
```

## output
pypamn creates a csv or a pickle as the output file, which has the columns shown in the following table.

| Column Name | Unit | Type   | Description |
|-------------|------|--------|-------------|
| NR          |      | float  | Nuclear recoil parameter, which is 1 if the largest S2 scatter in TPC is nuclear recoil. |
| Ed          | keV  | float  | Energy deposition by the largest S2 scatter in TPC.  |
| secondS2    | phe  | float  | The second largest S2.  |
| pri         |      | string | The name of the primary particle. |
| ns          |      | int    | Scatter times of the incident particle. |
| fv          |      | float  | Fiducial volume parameter, which is less than 1 if the largest S2 scatter in TPC is in 4t fiducial volume. |
| nhits       |      | int    | Number of nVeto PMTs which have hit over the threshold (0.5 phe).  |
