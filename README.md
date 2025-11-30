# BSS — Big Security Solution

BSS (Big Security Solution) is an advanced Static Application Security Testing (SAST) toolkit
designed to find common and complex security issues in Python, C, and JavaScript projects.
This repository is a polished, production-grade demo including:
- AST-based Python analysis
- Heuristic C/JS checks + C-accelerated scanner
- Rule engine with YAML rules
- JSON + styled HTML reporting
- Pre-commit integration, CI workflow, and Docker support
- Tests and example vulnerabilities

## Quickstart (Docker)
```bash
git clone <repo-url>
cd bss_full
docker build -t bss-sast -f docker/Dockerfile .
docker run --rm -v $(pwd):/app bss-sast python3 sast.py scan tests --json report.json --html report.html
```

## Goals
- Provide a solid baseline SAST tool that is easy to extend
- Demonstrate production patterns: CI, tests, packaging, native helpers
- Be recruiter- and engineering-manager-friendly

## License
MIT
