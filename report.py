import json, pathlib
from jinja2 import Template

HTML_TMPL = """<!doctype html>
<html><head><meta charset='utf-8'><title>BSS Report</title>
<style>
body { font-family: Arial, sans-serif; padding: 20px; }
table { border-collapse: collapse; width: 100%; }
th, td { border: 1px solid #ddd; padding: 8px; }
th { background: #f4f4f4; }
.HIGH { background: #ffcccc; }
.MEDIUM { background: #fff0b3; }
.LOW { background: #e7f7e7; }
</style>
</head><body>
<h1>BSS — Scan Report</h1>
<p>Findings: {{findings|length}}</p>
<table><tr><th>File</th><th>Line</th><th>Rule</th><th>Severity</th><th>Message</th></tr>
{% for f in findings %}
  <tr class="{{f.severity}}">
    <td>{{f.file}}</td><td>{{f.line}}</td><td>{{f.rule}}</td><td>{{f.severity}}</td><td>{{f.message}}</td>
  </tr>
{% endfor %}
</table>
</body></html>"""

def write_report(findings, json_path, html_path):
    pathlib.Path(json_path).write_text(json.dumps(findings, indent=2))
    tpl = Template(HTML_TMPL)
    pathlib.Path(html_path).write_text(tpl.render(findings=findings))

def print_summary(findings):
    counts = {}
    for f in findings:
        counts[f.get('severity','UNKNOWN')] = counts.get(f.get('severity','UNKNOWN'),0)+1
    print('Scan summary:')
    for k,v in counts.items():
        print(f'  {k}: {v}')
    print(f'  Total: {len(findings)}')
