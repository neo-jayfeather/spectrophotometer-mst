def extract_lines_by_range(input_dict_file, input_output_file):
    try:
        # Read the cutDict.txt file to get line ranges and corresponding filenames
        with open(input_dict_file, 'r') as dict_file:
            lines_dict = {}
            for line in dict_file:
                parts = line.strip().split(' ')
                if len(parts) >= 2:
                    line_range = parts[0]
                    filename = parts[1]
                    start, end = map(int, line_range.split('-'))
                    lines_dict[(start, end)] = filename

        # Read the cutFinalOutput.txt file and extract lines based on the ranges
        with open(input_output_file, 'r') as output_file:
            for (start, end), filename in lines_dict.items():
                extracted_lines = []
                for i, line in enumerate(output_file, start=1):
                    if start <= i <= end:
                        extracted_lines.append(f"{i} {line}")  # Include line numbers
                    elif i > end:
                        break

                # Check if the extracted lines are not empty
                if extracted_lines:
                    with open(filename, 'a') as target_file:
                        target_file.writelines(extracted_lines)

        return "Lines extracted and saved successfully!"
    except FileNotFoundError:
        return "File not found. Please provide valid filenames."

# Example usage:
cut_dict_filename = 'cutDict.txt'
cut_output_filename = '11msts.txt'
result = extract_lines_by_range(cut_dict_filename, cut_output_filename)
print(result)
