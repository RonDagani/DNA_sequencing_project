import os
import subprocess
import sys

def run(command):
    print(f"\nRunning: {command}")
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print("Error running command.")
        sys.exit(1)

# -------- Config --------
FASTQ_FILENAME = "E.raw.fastq"
FILTERED_FASTQ = "filtered.fastq"
MIN_QUALITY = 7
MIN_LENGTH = 500
# ------------------------

os.makedirs("QC_before", exist_ok=True)
os.makedirs("QC_after", exist_ok=True)

print("\nGenerating QC report for raw data...")
run(f"NanoPlot --fastq {FASTQ_FILENAME} -o QC_before")

print("\nFiltering reads by quality and length...")
run(f"cat {FASTQ_FILENAME} | NanoFilt -q {MIN_QUALITY} -l {MIN_LENGTH} > {FILTERED_FASTQ}")

print("\nGenerating QC report for filtered data...")
run(f"NanoPlot --fastq {FILTERED_FASTQ} -o QC_after")

print("\nDone. Reports saved in 'QC_before' and 'QC_after'.")
