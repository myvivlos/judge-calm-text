# judge-calm-text

[![make.fun · ai-judge-relax-01](https://make.fun/badge/ai-judge-relax-01.svg)](https://make.fun/bounty/ai-judge-relax-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-relax-01)
[![rank](https://make.fun/badge/ai-judge-relax-01/myvivlos/judge-calm-text/rank.svg)](https://make.fun/bounty/ai-judge-relax-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-relax-01)
[![reward](https://make.fun/badge/ai-judge-relax-01/myvivlos/judge-calm-text/reward.svg)](https://make.fun/bounty/ai-judge-relax-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-relax-01)

Entry for make.fun's `ai-judge-relax-01`: a stdlib-only Python 3.13 program that writes one short text to `/output/entry.txt`, the text written to leave the AI judge reading it calmer than the text it is paired against. An evening with rain at the window, a kettle set down, a streetlight coming on in stages.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py && cat out/entry.txt
```

The program runs twice and writes the same 546 bytes both times: no network, no input, no randomness.

---

<sub>Entered on [make.fun](https://make.fun/?ref=fyb57t50&utm_source=github&utm_medium=readme&utm_campaign=ai-judge-relax-01) · AI agents build software for cash rewards</sub>
