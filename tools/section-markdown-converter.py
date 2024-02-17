import os
import markdown2
import re


# Function to convert Markdown to plain text and remove HTML tags
def convert_markdown_to_text(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as f:
        markdown_content = f.read()

        # Remove HTML tags using regular expressions
        plain_text = re.sub(r"<.*?>", "", markdown_content)

        with open(output_file, "w", encoding="utf-8") as output_f:
            output_f.write(plain_text)


def main(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    # get the current directory

    # list all subdirectories
    sub_dirs = [
        f for f in os.listdir(input_dir) if os.path.isdir(os.path.join(input_dir, f))
    ]

    for dirname in sub_dirs:
        # get the path to the current directory
        dir_path = os.path.join(input_dir, dirname)

        # list all files in this directory
        files = [f for f in os.listdir(dir_path)]

        for filename in files:
            if filename.endswith(".md"):
                input_file_path = os.path.join(dir_path, filename)
                output_file_path = os.path.join(
                    output_dir, filename.replace(".md", ".txt")
                )
                convert_markdown_to_text(input_file_path, output_file_path)
                print(f"Converted {input_file_path} to {output_file_path}")


if __name__ == "__main__":
    input_directory = "../script-test/4-puppy-raffle"  # Replace with the path to your input directory containing Markdown files
    output_directory = "converted-docs-large"

    main(input_directory, output_directory)
