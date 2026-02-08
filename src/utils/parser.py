import argparse

parser = argparse.ArgumentParser(description="report script")
parser.add_argument("--files", dest="files", nargs="+", required=True)
parser.add_argument("--report", dest="avg", required=True)
