# fnmatcher

``fnmatcher`` is filename-based checker, match the same filename between two directories.

## Installation

- Clone this repository

```git
git clone https://github.com/Kawaeee/fnmatcher.git
```

- Install required packages

```bash
pip install -r requirements.txt
```

## Usage

```python  
usage: fnmatcher.py [-h] [--source-directory SOURCE_DIRECTORY]
                    [--target-directory TARGET_DIRECTORY]
                    [--threshold THRESHOLD] [--separator SEPARATOR] [--debug]

optional arguments:
  -h, --help            show this help message and exit
  --source-directory SOURCE_DIRECTORY
                        Path to source directory/folder (default: None)
  --target-directory TARGET_DIRECTORY
                        Path to target directory/folder (default: None)
  --threshold THRESHOLD
                        Text similarity threshold (default: 0.9)
  --separator SEPARATOR
                        Output delimiter (default: ||)
  --debug               Enable debug logging mode (default: False
```
