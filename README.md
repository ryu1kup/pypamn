# (py)pamn
A python scripts to process and to merge nSort output files for XENONnT nVeto MC.

# dependencies
pamn depends on of course ROOT, and additionally on the following packages

- numpy
- pandas
- uproot

# usage
pamn can be run from your command line.
Even if there are multiple nSort output files or only one output files, pamn can process them/it as well with the command

```
$ python3 pamn.py -i /path/to/nSort_output_dir/*_Sort.root [options]
```

where options are additional parameters to be given to pypamn;

- `-o, --output [OUTPUT_FILENAME]` ... The output filename. You need to specify the extension `.csv`.
- `-c, --chunksize [CHUNKSIZE]` ... The number of rows to be processed at one time.
- `-v, --verbose [VERBOSE_LEVEL]` ... The verbosity level.

You can also check how to run pamn with the command

```
$ python3 pamn.py --help
```

# output
pamn creates a CSV output fil, which has the columns shown in the following table.

| Column Name | Unit | Description |
|-------------|------|-------------|
| NR          |      | Nuclear recoil parameter, which is 1 if the largest S2 scatter in TPC is nuclear recoil. |
| Ed          | keV  | Energy deposition by the largest S2 scatter in TPC.  |
| secondS2    | phe  | The second largest S2.  |
| pri         |      | The name of the primary particle. |
| ns          |      | Scatter times of the incident particle. |
| fv          |      | Fiducial volume parameter, which is less than 1 if the largest S2 scatter in TPC is in 4t fiducial volume. |
| nhits       |      | Number of nVeto PMTs which have hit over the threshold (0.5 phe).  |
