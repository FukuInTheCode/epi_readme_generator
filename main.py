import sys


# Function to generate Markdown table from input
def generate_markdown_table(input_text):
    # Split the input into lines
    lines = input_text.strip().split("||")

    # Initialize the table header
    table = "| Test | Status |\n| --- | --- |"

    lines = [line for line in lines if line != ""]
    start = 6 if "warning" not in lines else 8
    # Iterate through the lines and add rows to the table
    for i in range(start, len(lines), 2):
        test_name = lines[i]
        result = lines[i + 1]
        if result != "PASSED" and "Crash" not in result:
            result = "FAILURE"
        elif "Crash" in result:
            result = "Crash"
        table += f"\n| {test_name} | {result} |"

    return f"### {lines[0]} ({lines[1]})\n" + table


if __name__ == "__main__":
    # Check if the script was provided with the expected number of command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python script.py 'input_text'")
        sys.exit(1)

    # Get the input from the command line argument
    user_input = sys.argv[1]

    # Generate Markdown table
    markdown_table = generate_markdown_table(user_input)

    # Print or save the generated table
    print(markdown_table)
