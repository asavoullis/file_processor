# File Processor Tool

## Overview
This tool automates file processing tasks by moving unprocessed files from an input directory to an output directory, maintaining a record of processed files, and optionally clearing directories or the record file.

## Features
- **Process Files:** Moves files from the input directory to the output directory if they haven't been processed.
- **Delete After Processing:** Optionally deletes files from the input directory after processing.
- **Clear Input Directory:** Deletes all files in the input directory.
- **Clear Records File:** Resets the contents of the records file to track new processing.

## Usage
### Command-Line Arguments
| Argument         | Description                                                | Required | Example                                         |
|------------------|------------------------------------------------------------|----------|-------------------------------------------------|
| `--in_directory` | Path to the input directory.                               | Yes      | `./Files_Folders/In`                            |
| `--out_directory`| Path to the output directory.                              | Yes      | `./Files_Folders/Out`                           |
| `--records_file` | Path to the file that tracks processed files.             | Yes      | `./Files_Folders/Records/files_added.txt`       |
| `--delete_after` | Deletes files from input directory after processing.      | No       | `--delete_after`                                |
| `--clear_records`| Clears the contents of the records file.                  | No       | `--clear_records`                               |

### Examples
#### Process Files Without Deletion
```bash
python file_processor.py --in_directory "./Files_Folders/In" --out_directory "./Files_Folders/Out" --records_file "./Files_Folders/Records/files_added.txt"
```

#### Process Files and Delete Originals
```bash
python file_processor.py --in_directory "./Files_Folders/In" --out_directory "./Files_Folders/Out" --records_file "./Files_Folders/Records/files_added.txt" --delete_after
```

#### Clear Records File
```bash
python file_processor.py --in_directory "./dummy" --out_directory "./dummy" --records_file "./Files_Folders/Records/files_added.txt" --clear_records
```

## Setup
1. Clone the repository:
   ```bash
   git clone file_processor.git
   ```

2. Navigate to the project directory:
   ```bash
   cd file_processor
   ```

3. Install required dependencies if any (none for now).

## Project Structure
```
file_processor/
├── file_processor.py   # Main script
├── Files_Folders/      # Sample directories for input/output
│   ├── In/
│   ├── Out/
│   └── Records/
└── README.md           # Documentation
```

## Repository Name Suggestion
**file-processor**

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License.

