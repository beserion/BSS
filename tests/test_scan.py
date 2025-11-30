from scanner import scan_paths
def test_scan_samples():
    findings = scan_paths(['tests'], threads=2)
    assert any(f['rule'].startswith('PY') for f in findings)
    assert any(f['rule'].startswith('C') for f in findings)
    assert any(f['rule'].startswith('JS') for f in findings)
