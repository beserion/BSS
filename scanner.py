# scanner.py
import os, json, pathlib
from concurrent.futures import ThreadPoolExecutor, as_completed
from rules import RULES
from python_analyzer import analyze_python_file
from c_js_analyzer import analyze_c_file, analyze_js_file

SEVERITY_ORDER = {'LOW':0,'MEDIUM':1,'HIGH':2}

def discover_files(paths):
    exts = {'.py','.c','.h','.js','.jsx'}
    files=[]
    for p in paths:
        ppath = pathlib.Path(p)
        if ppath.is_file() and ppath.suffix in exts:
            files.append(ppath)
        elif ppath.is_dir():
            for f in ppath.rglob('*'):
                if f.is_file() and f.suffix in exts:
                    files.append(f)
    return files

def scan_file(path):
    s = str(path)
    if s.endswith('.py'):
        return analyze_python_file(path)
    elif s.endswith('.c') or s.endswith('.h'):
        return analyze_c_file(path)
    elif s.endswith('.js') or s.endswith('.jsx'):
        return analyze_js_file(path)
    return []

def scan_paths(paths, threads=4, min_severity='LOW'):
    files = discover_files(paths)
    findings=[]
    with ThreadPoolExecutor(max_workers=threads) as ex:
        futures = {ex.submit(scan_file, f): f for f in files}
        for fut in as_completed(futures):
            try:
                res = fut.result()
                if res:
                    findings.extend(res)
            except Exception as e:
                findings.append({'file': str(futures[fut]), 'line':0, 'rule':'scanner-error','message':str(e),'severity':'HIGH'})
    return findings
