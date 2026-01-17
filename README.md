# BSS

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
git clone https://github.com/beserion/BSS.git
cd BSS
docker build -t bss-sast -f docker/Dockerfile .
docker run --rm -v $(pwd):/app bss-sast python3 sast.py scan tests --json report.json --html report.html
```

## Goals
- Provide a solid baseline SAST tool that is easy to extend
- Demonstrate production patterns: CI, tests, packaging, native helpers
- Be recruiter- and engineering-manager-friendly

## License
MIT

- minor update @ 2026-01-14 03:48:48.131695
- minor update @ 2026-01-14 03:48:58.744169
- minor update @ 2026-01-14 03:49:01.058650
- minor update @ 2026-01-14 03:49:10.967845
- minor update @ 2026-01-14 03:49:16.265177
- minor update @ 2026-01-14 03:49:26.584334
- minor update @ 2026-01-14 06:36:34.202012
- minor update @ 2026-01-14 06:36:43.903667
- minor update @ 2026-01-14 06:36:53.197114
- minor update @ 2026-01-14 06:36:57.499561
- minor update @ 2026-01-14 06:37:06.091712
- minor update @ 2026-01-14 10:27:34.190160
- minor update @ 2026-01-14 10:28:19.109362
- minor update @ 2026-01-14 16:32:46.967341
- minor update @ 2026-01-15 22:23:21.682616
- minor update @ 2026-01-16 03:40:39.375836
- minor update @ 2026-01-16 03:40:45.028750
- minor update @ 2026-01-16 03:40:47.321243
- minor update @ 2026-01-16 06:36:07.488100
- minor update @ 2026-01-16 06:36:15.925669
- minor update @ 2026-01-16 06:36:22.435710
- minor update @ 2026-01-16 20:23:15.531447
- minor update @ 2026-01-16 20:23:31.154659
- minor update @ 2026-01-16 20:23:34.449788
- minor update @ 2026-01-16 20:23:44.748450
- minor update @ 2026-01-17 03:23:41.266490
- minor update @ 2026-01-17 03:23:50.599878
- minor update @ 2026-01-17 03:24:04.179598
- minor update @ 2026-01-17 03:24:23.769753