import os
import shutil


def get_unprocessed_files(in_dir, records_file):
    with open(records_file, "r") as f:
        processed_files = f.read().splitlines()

    files = os.listdir(in_dir)
    unprocessed_files = [f for f in files if f not in processed_files]

    return unprocessed_files


def process_files(in_dir, out_dir, records_file):
    unprocessed_files = get_unprocessed_files(in_dir, records_file)

    if not unprocessed_files:
        print("No new files to process.")
        return

    with open(records_file, "a") as f:
        for file_name in unprocessed_files:
            source_path = os.path.join(in_dir, file_name)
            dest_path = os.path.join(out_dir, file_name)
            shutil.move(source_path, dest_path)
            f.write(file_name + "\n")
            print(f"Processed file: {file_name}")


if __name__ == "__main__":
    in_dir = "Files_Folders/In"
    out_dir = "Files_Folders/Out"
    records_file = "Files_Folders/Records/files_added.txt"

    process_files(in_dir, out_dir, records_file)
