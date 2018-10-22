# longread_plots
A collection of plots for long read sequencing FastQ files from devices like Oxford Nanopore's MinION and PromethION.
# Dependencies
```bash
pip install --user --upgrade pandas seaborn
```

Note that matplot lib >= 3.0.0 is would be nice to have.
Python >= 3.5 is therfore recommended.

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
```bash
python3 bin/lrplots example.fastq
```

# Output

<p align="center">
<a name="screenshot">
<img src="https://raw.githubusercontent.com/ahcm/longread_plots/master/doc/images/20180416_1422_EWolf_9948_susscrofa-albacore-2.2.5-FLO-PRO001-SQK-LSK109.fastq-lrplots.png" width="800px">
  </a>
</p>
