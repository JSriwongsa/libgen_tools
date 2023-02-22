#!/usr/bin/env python3
# command-line utility to search libgen api for title and author
import argparse
import json
from libgen_api import LibgenSearch

parser = argparse.ArgumentParser(
    description="Command-line utility to parse libgen API search results for author and/or title.")
parser.add_argument("--title", type=str,
                    help="The title of what you would like to search.")
parser.add_argument("--author", type=str,
                    help="The author of the work you would like to search.")

args = parser.parse_args()

s = LibgenSearch()

def format_result(header_line, result, result_count):
    line_seperator = "------------" * 6
    download_links = s.resolve_download_links(result)

    print(header_line)
    print("Result count: {}".format(result_count))
    print(line_seperator)
    print(json.dumps(result, indent=2))
    print(line_seperator)
    print("Download links:")
    print(json.dumps(download_links, indent=2))
    print(line_seperator)


def search_title(title):
    results = s.search_title(title)
    result_count = 0
    for result in results:
        result_count += 1
        header_line = "Title Search {}".format(title)

        format_result(header_line, result, result_count)


def search_author(author):
    results = s.search_author(author)
    result_count = 0
    for result in results:
        result_count += 1
        header_line = "Author Search: {}".format(author)

        format_result(header_line, result, result_count)


if args.title:
    search_title(args.title)
elif args.author:
    search_author(args.author)
else:
    print("Please provide a title or author.")
    exit
