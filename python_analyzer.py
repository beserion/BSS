import ast, pathlib, re

SECRET_REGEX = re.compile(r'[A-Za-z0-9_]{20,}')

def analyze_python_file(path):
    text = path.read_text()
    try:
        tree = ast.parse(text, filename=str(path))
    except Exception:
        return [{'file':str(path),'line':0,'rule':'PY_PARSE_ERR','message':'parse error','severity':'HIGH'}]
    findings=[]
    for node in ast.walk(tree):
        # eval
        if isinstance(node, ast.Call):
            func = node.func
            name = getattr(func, 'id', None) or getattr(func, 'attr', None)
            if name == 'eval':
                findings.append({'file':str(path),'line':node.lineno,'rule':'PY001','message':'use of eval()','severity':'HIGH'})
            # subprocess with shell=True
            if getattr(func, 'id', '') == 'Popen' or getattr(func, 'id', '') == 'run':
                for kw in getattr(node, 'keywords', []):
                    if kw.arg == 'shell' and getattr(kw.value, 'value', False) == True:
                        findings.append({'file':str(path),'line':node.lineno,'rule':'PY003','message':'subprocess with shell=True','severity':'HIGH'})
        # literal secrets
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            s = node.value
            if SECRET_REGEX.search(s):
                findings.append({'file':str(path),'line':getattr(node,'lineno',0),'rule':'PY002','message':'possible hardcoded secret','severity':'MEDIUM'})
    return findings
