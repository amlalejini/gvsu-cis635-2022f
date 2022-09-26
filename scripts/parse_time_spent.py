import argparse, csv

def read_csv(file_path):
    content = None
    with open(file_path, "r") as fp:
        content = fp.read().strip().split("\n")
    header = content[0].split(",")
    content = content[1:]
    lines = [{header[i]: l[i] for i in range(len(header))} for l in csv.reader(content, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True)]
    return lines

def main():
    # Process inputs.
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file", "-i", type=str, help="File to open to process.")
    parser.add_argument("--output_file", "-o", type=str, help="Output file.")
    args = parser.parse_args()
    # Load data from input file
    data = read_csv(args.input_file)
    # Reformat data into long-format
    out_lines = []
    for line in data:
        week = line["week"]
        times = line["time_spent"]
        times = times.strip("[]").split(",")
        for t in times:
            info = {
                "week": week,
                "time_spent": t
            }
            out_lines.append(info)
    # Write out reformatted data
    heading = list(out_lines[0].keys())
    heading.sort()
    out_content = ",".join(heading) + "\n"
    out_content += "\n".join([",".join([line[field] for field in heading]) for line in out_lines])
    with open(args.output_file, "w") as fp:
        fp.write(out_content)






if __name__ == "__main__":
    main()