# longread_plots
A collection of plots for long read sequencing FastQ files from devices like Oxford Nanopore's MinION and PromethION.
# Dependencies
```bash
pip install --user --upgrade pandas seaborn
```

Note that matplot lib >= 3.0.0 is needed.
Python >= 3.5 is therfore recommended, otherwise plots might be corrupted.

# Installation

From PyPi:
```bash
pip3 install --user lrplots
```

From the release tar.gz:
```bash
python3 setup.py install --user
```


# Usage
With the pip3 installation it should be in your PATH and you should be able to just call:
```bash
lrplot example.fastq
```

If the command can't be found, pip3 installed it in a path that is not in your PATH variable.
You can then find it with:
```bash
find ~ -name lrplot
```
or
```bash
find /usr/local -name lrplot
```
Then either add the containing directory to your PATH or just use the full path.

You can also call it like a script with python3 (or whatever your python3 is called):
```bash
python3 bin/lrplots example.fastq
```

# Output

<p align="center">
<a name="screenshot">
<img src="https://raw.githubusercontent.com/ahcm/longread_plots/master/doc/images/20180416_1422_EWolf_9948_susscrofa-albacore-2.2.5-FLO-PRO001-SQK-LSK109.fastq-lrplots.png" width="800px">
  </a>
</p>
