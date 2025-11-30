#!/usr/bin/env python3
"""BSS CLI entrypoint"""
import argparse
from scanner import scan_paths
from report import write_report, print_summary
import pkg_resources

__version__ = "0.1.0"

def main():
    ap = argparse.ArgumentParser(prog="bss-sast")
    ap.add_argument("--version", action="store_true", help="print version and exit")
    ap.add_argument("--quiet", action="store_true", help="minimal output")
    sub = ap.add_subparsers(dest="cmd")
    sc = sub.add_parser("scan", help="Scan files or directories")
    sc.add_argument("paths", nargs="+")
    sc.add_argument("--json", help="Write JSON report", default="bss_report.json")
    sc.add_argument("--html", help="Write HTML report", default="bss_report.html")
    sc.add_argument("--threads", type=int, default=4)
    sc.add_argument("--min-severity", choices=["LOW","MEDIUM","HIGH"], default="LOW")
    args = ap.parse_args()
    if args.version:
        print(__version__); return
    if args.cmd == "scan":
        findings = scan_paths(args.paths, threads=args.threads)
        write_report(findings, args.json, args.html)
        if not args.quiet:
            print_summary(findings)
    else:
        ap.print_help()

if __name__ == '__main__':
    main()
