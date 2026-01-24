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
- minor update @ 2026-01-17 03:24:33.065468
- minor update @ 2026-01-17 03:24:36.361099
- minor update @ 2026-01-17 11:18:08.211822
- minor update @ 2026-01-17 11:18:12.835925
- minor update @ 2026-01-17 16:25:33.725582
- minor update @ 2026-01-17 16:25:40.984029
- minor update @ 2026-01-17 16:25:49.251536
- minor update @ 2026-01-18 03:50:39.057121
- minor update @ 2026-01-18 03:50:49.788394
- minor update @ 2026-01-18 03:51:09.346188
- minor update @ 2026-01-18 03:51:17.627293
- minor update @ 2026-01-18 03:51:24.902775
- minor update @ 2026-01-18 03:51:30.195209
- minor update @ 2026-01-18 03:51:40.753848
- minor update @ 2026-01-18 07:20:33.142859
- minor update @ 2026-01-18 07:20:36.416326
- minor update @ 2026-01-18 07:20:41.673571
- minor update @ 2026-01-18 07:20:47.926300
- minor update @ 2026-01-18 07:20:58.172229
- minor update @ 2026-01-18 07:21:02.418695
- minor update @ 2026-01-18 07:21:05.661269
- minor update @ 2026-01-19 04:53:14.281185
- minor update @ 2026-01-19 04:53:22.620699
- minor update @ 2026-01-19 04:53:42.523237
- minor update @ 2026-01-19 04:53:46.827362
- minor update @ 2026-01-19 04:53:54.117557
- minor update @ 2026-01-19 04:54:07.707233
- minor update @ 2026-01-19 04:54:14.019523
- minor update @ 2026-01-19 04:54:26.631486
- minor update @ 2026-01-19 16:32:00.851838
- minor update @ 2026-01-20 08:34:34.746936
- minor update @ 2026-01-20 08:34:51.925737
- minor update @ 2026-01-20 08:34:55.449632
- minor update @ 2026-01-20 13:49:11.723138
- minor update @ 2026-01-20 13:49:21.991294
- minor update @ 2026-01-20 13:49:30.256144
- minor update @ 2026-01-20 15:32:37.484097
- minor update @ 2026-01-20 15:32:40.279542
- minor update @ 2026-01-21 18:44:26.855180
- minor update @ 2026-01-21 18:44:43.731088
- minor update @ 2026-01-21 18:44:50.010861
- minor update @ 2026-01-21 18:45:12.873676
- minor update @ 2026-01-22 03:49:17.715278
- minor update @ 2026-01-22 03:49:34.247838
- minor update @ 2026-01-22 03:49:40.541908
- minor update @ 2026-01-22 03:49:50.831857
- minor update @ 2026-01-22 03:49:58.125910
- minor update @ 2026-01-23 08:32:39.513774
- minor update @ 2026-01-23 08:32:55.625141
- minor update @ 2026-01-23 08:32:59.292897
- minor update @ 2026-01-23 08:33:02.801071
- minor update @ 2026-01-23 08:33:13.360633
- minor update @ 2026-01-23 13:43:28.223020
- minor update @ 2026-01-23 13:43:42.762377
- minor update @ 2026-01-24 03:27:48.257766
- minor update @ 2026-01-24 03:28:06.296240
- minor update @ 2026-01-24 03:28:39.164622
- minor update @ 2026-01-24 05:22:46.322330
- minor update @ 2026-01-24 05:22:49.621059
- minor update @ 2026-01-24 05:22:59.888510
- minor update @ 2026-01-24 05:23:08.175281
- minor update @ 2026-01-24 09:22:16.766431
- minor update @ 2026-01-24 09:22:32.879551
- minor update @ 2026-01-24 12:43:05.009692
- minor update @ 2026-01-24 12:43:09.675610
- minor update @ 2026-01-24 12:43:30.540844