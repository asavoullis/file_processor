import os
import shutil
import argparse


def get_unprocessed_files(in_dir, records_file):
    with open(records_file, "r") as f:
        processed_files = f.read().splitlines()

    files = os.listdir(in_dir)
    unprocessed_files = [f for f in files if f not in processed_files]

    return unprocessed_files


def process_files(in_dir, out_dir, records_file, delete=False):
    unprocessed_files = get_unprocessed_files(in_dir, records_file)

    if not unprocessed_files:
        print("No new files to process.")
        return

    with open(records_file, "a") as f:
        for file_name in unprocessed_files:
            source_path = os.path.join(in_dir, file_name)
            dest_path = os.path.join(out_dir, file_name)

            if delete:
                shutil.move(source_path, dest_path)
                print(f"Moved and deleted file: {file_name}")
            else:
                shutil.copy(source_path, dest_path)
                print(f"Copied file: {file_name}")

            f.write(file_name + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Process files from 'In' directory to 'Out' directory."
    )
    parser.add_argument(
        "--delete",
        action="store_true",
        help="Move and delete files instead of copying them.",
    )
    args = parser.parse_args()

    in_dir = "Files_Folders/In"
    out_dir = "Files_Folders/Out"
    records_file = "Files_Folders/Records/files_added.txt"

    process_files(in_dir, out_dir, records_file, args.delete)
