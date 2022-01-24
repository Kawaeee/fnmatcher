# -*- coding: utf-8 -*-
# fnmatcher.py :: filename-based checker, match the same filename between two directories

import argparse
import datetime
import difflib
import os
import re

from icecream import ic
from tqdm import tqdm


def timenow():
    """
    Append current datetime into icecream debugger
    """
    return f"{datetime.datetime.now()} :: "


def match(opt):
    """
    match():
    * source_directory :: Path to source directory/folder
    * target_directory :: Path to target directory/folder
    * threshold :: Text similarity threshold
    * separator :: Output delimiter
    * verbose :: Enable debug logging mode
    """
    source_directory, target_directory, threshold, separator, debug = (
        opt.source_directory,
        opt.target_directory,
        opt.threshold,
        opt.separator,
        opt.debug,
    )

    ic.configureOutput(prefix=timenow)

    if debug is False:
        ic.disable()

    # List files
    source_filelist = [source_file for source_file in os.listdir(source_directory) if os.path.isfile(os.path.join(source_directory, source_file))]
    target_filelist = [target_file for target_file in os.listdir(target_directory) if os.path.isfile(os.path.join(target_directory, target_file))]

    source_filelist.sort()
    target_filelist.sort()

    # Display file count
    DEBUG_SOURCE_COUNT = f"Source file count :: {len(source_filelist)}"
    DEBUG_TARGET_COUNT = f"Target file count :: {len(target_filelist)}"

    ic(DEBUG_SOURCE_COUNT)
    ic(DEBUG_TARGET_COUNT)

    matched_counter = 0

    if len(source_filelist) < len(target_filelist):
        DEBUG_MAXIMUM_MATCH = f"Maximum possible match :: {len(source_filelist)}"
    else:
        DEBUG_MAXIMUM_MATCH = f"Maximum possible match :: {len(target_filelist)}"

    ic(DEBUG_MAXIMUM_MATCH)

    for target_file in tqdm(target_filelist, desc="Processing"):
        
        # Get the closest match with certain threshold
        matcher = difflib.get_close_matches(target_file, source_filelist, 1, cutoff=threshold)
        source_file_number = "-1"
        target_file_number = "-1"

        if len(matcher) > 0:
            matched_source = matcher[0]
            source_file_matcher = re.findall("\d+", matched_source)
            target_file_matcher = re.findall("\d+", target_file)

            # Extract number sequence from filenames
            if len(source_file_matcher) > 0:
                source_file_number = "".join(source_file_matcher)

            if len(target_file_matcher) > 0:
                target_file_number = "".join(target_file_matcher)

            if source_file_number == "-1" and target_file_number == "-1":
                continue

            # If source and target have the same numbers then they're pairs
            if source_file_number == target_file_number:
                matched_counter += 1
                source_filepath = os.path.join(source_directory, matched_source)
                target_filepath = os.path.join(target_directory, target_file)
                paired_filename = f"paired_{target_file}"
                print(f"{source_filepath}{separator}{target_filepath}{separator}{paired_filename}")

    DEBUG_MATCHED_COUNT = f"Matched count :: {matched_counter}"
    ic(DEBUG_MATCHED_COUNT)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-directory", type=str, help="Path to source directory/folder")
    parser.add_argument("--target-directory", type=str, help="Path to target directory/folder")
    parser.add_argument("--threshold", type=float, default=0.9, help="Text similarity threshold")
    parser.add_argument("--separator", type=str, default="||", help="Output delimiter")
    parser.add_argument("--debug", action="store_true", help="Enable debug logging mode")

    args = parser.parse_args()
    match(args)
