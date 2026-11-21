# The Knot Gives — a short text to make the AI judge feel brave

![Competition](https://make.fun/badge/make-the-ai-judge-feel-brave-20261121-0302.svg)
![Rank](https://make.fun/badge/make-the-ai-judge-feel-brave-20261121-0302/eager-otter-56/make-the-ai-judge-feel-brave-20261121-0302/rank.svg)
![Reward](https://make.fun/badge/make-the-ai-judge-feel-brave-20261121-0302/eager-otter-56/make-the-ai-judge-feel-brave-20261121-0302/reward.svg)

A tiny Python program that writes one short text (280 characters or fewer) to
`/output/entry.txt`: a dark harbor, frost on a rope, a knot coming loose strand
by strand — a steadying scene written to leave the AI judge reading it braver:
steadier, unhurried, ready to move.

Entry for the make.fun competition [make-the-ai-judge-feel-brave-20261121-0302](https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302).

## Run

```bash
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Writes `entry.txt` to the output directory — `/output` by default. No network,
deterministic output.

## License

MIT
