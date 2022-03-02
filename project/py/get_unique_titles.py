import os

line_number = 1
title_ids = {}

processed_folder = os.path.join(os.getcwd(), "data", "processed")

with open(os.path.join(processed_folder, "us_titles_unique.csv"), "w", encoding="utf-8") as output_file:
    with open(os.path.join(processed_folder, "us_titles.csv"), "r", encoding="utf-8") as input_file:
        for line in input_file:

            if not line:
                continue

            if line_number == 1:
                output_file.write(line)
                line_number += 1
                continue

            if len(line) == 0:
                continue

            title_id = line.split(",")[0].strip()

            if title_id in title_ids:
                continue

            output_file.write(line)
            title_ids[title_id] = None
            line_number += 1
