import os
import shutil
import argparse


class FileProcessor:
    # Initialize input, output and records file paths
    def __init__(self, in_directory: str, out_directory: str, records_file: str):
        self.in_directory = in_directory
        self.out_directory = out_directory
        self.records_file = records_file

        # Ensure required paths exist
        os.makedirs(self.in_directory, exist_ok=True)
        os.makedirs(self.out_directory, exist_ok=True)
        os.makedirs(os.path.dirname(self.records_file), exist_ok=True)

        # Create records file if it doesn't exist
        if not os.path.exists(self.records_file):
            open(self.records_file, "w").close()

    def get_processed_files(self) -> set:
        """
        Read the records file and return a set of already processed file names.
        """
        with open(self.records_file, "r") as file:
            return set(file.read().strip().splitlines())

    def process_files(self, delete_after_process: bool = False):
        """
        Process files by moving unprocessed files to the output directory,
        updating the records file and optionally deleting the original files.
        """
        processed_files = self.get_processed_files()
        files_to_process = [
            f
            for f in os.listdir(self.in_directory)
            if os.path.isfile(os.path.join(self.in_directory, f))
        ]

        for file_name in files_to_process:
            file_path = os.path.join(self.in_directory, file_name)

            # Process only if the file has not been recorded
            if file_name not in processed_files:
                shutil.move(file_path, os.path.join(self.out_directory, file_name))
                print(f"Processed and moved file: {file_name}")

                # Record the processed file
                with open(self.records_file, "a") as record_file:
                    record_file.write(file_name + "\n")

                # Optionally delete the original file
                if delete_after_process:
                    try:
                        os.remove(file_path)
                        print(f"Deleted original file: {file_name}")
                    except FileNotFoundError:
                        print(f"File not found for deletion: {file_name}")

    def clear_in_directory(self):
        """
        Delete all files in the input directory.
        """
        for file_name in os.listdir(self.in_directory):
            file_path = os.path.join(self.in_directory, file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Deleted file: {file_name}")

    def clear_records_file(self):
        """
        Clear the contents of the records file.
        """
        open(self.records_file, "w").close()
        print("Cleared records file.")


def main():
    # Uncomment these lines for hardcoded actions instead of using CLI
    # processor = FileProcessor(in_directory, out_directory, records_file)
    # processor.process_files(delete_after_process=False)  # Process without deletion
    # processor.clear_records_file()  # Clear records file if needed

    # to avoid hardcoding the arguments and paths and instead use CLI
    parser = argparse.ArgumentParser(
        description="Process files from input to output directory."
    )
    parser.add_argument(
        "--in_directory", required=True, help="Path to the input directory."
    )
    parser.add_argument(
        "--out_directory", required=True, help="Path to the output directory."
    )
    parser.add_argument(
        "--records_file", required=True, help="Path to the records file."
    )
    parser.add_argument(
        "--delete_after",
        action="store_true",
        help="Delete files from input directory after processing.",
    )
    parser.add_argument(
        "--clear_records", action="store_true", help="Clear the records file."
    )

    args = parser.parse_args()

    processor = FileProcessor(args.in_directory, args.out_directory, args.records_file)

    if args.clear_records:
        processor.clear_records_file()
    else:
        processor.process_files(delete_after_process=args.delete_after)


if __name__ == "__main__":
    main()

    # examples how to run the script in CLI
    # python file_processor.py --in_directory "Files_Folders/In" --out_directory "Files_Folders/Out" --records_file "Files_Folders/Records/files_added.txt" --delete_after
    # python file_processor.py --in_directory "./dummy" --out_directory "./dummy" --records_file "./Files_Folders/Records/files_added.txt" --clear_records
