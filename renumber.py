def replace_first_item(filename, new_filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        with open(new_filename, 'w') as new_file:
            for line in lines:
                items = line.strip().split(' ')
                if items:
                    try:
                        first_item = int(items[0])
                        new_first_item = first_item + 38
                        items[0] = str(new_first_item)
                        new_line = ' '.join(items) + '\n'
                        new_file.write(new_line)
                    except ValueError:
                        # Skip lines where the first item is not a valid integer
                        new_file.write(line)
                else:
                    # Skip empty lines
                    new_file.write(line)
        
        return f"Successfully created a new file '{new_filename}' with updated content!"
    except FileNotFoundError:
        return "File not found. Please provide valid filenames."

# Example usage:
input_filename = 'cutFinalOuput.txt'
output_filename = 'newOutput.txt'
result = replace_first_item(input_filename, output_filename)
print(result)
