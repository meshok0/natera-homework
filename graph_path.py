#! /usr/bin/env python3
import sys
import argparse
import json

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", nargs="?", default="-", metavar="INPUT_FILE", type=argparse.FileType("r"),
        help="path to the input file with graph in JSON format (read from stdin if omitted)")
    parser.add_argument("--start", "-s", required=True, type=str, help="start vertex")
    parser.add_argument("--end", "-e", required=True, type=str, help="end vertex")
    args = parser.parse_args()


    graph = json.load(args.input)
    start = args.start
    end = args.end

    path = find_path(graph, start, end)
    
    print(json.dumps(path))


def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
      return path
    if start not in graph:
      return None
    for node in graph[start]:
      if node not in path:
        newpath = find_path(graph, node, end, path)
        if newpath: return newpath
    return None
        
if __name__ == "__main__":
    main()