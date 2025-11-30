import re, pathlib
def analyze_c_file(path):
    text = path.read_text(errors='ignore')
    findings=[]
    for m in re.finditer(r'\bgets\s*\(', text):
        line = text.count('\n',0,m.start())+1
        findings.append({'file':str(path),'line':line,'rule':'C001','message':'use of gets()','severity':'HIGH'})
    for m in re.finditer(r'\bstrcpy\s*\(', text):
        line = text.count('\n',0,m.start())+1
        findings.append({'file':str(path),'line':line,'rule':'C002','message':'strcpy may overflow','severity':'MEDIUM'})
    return findings

def analyze_js_file(path):
    text = path.read_text(errors='ignore')
    findings=[]
    for m in re.finditer(r'\.innerHTML\s*=\s*', text):
        line = text.count('\n',0,m.start())+1
        findings.append({'file':str(path),'line':line,'rule':'JS001','message':'assignment to innerHTML','severity':'HIGH'})
    return findings
