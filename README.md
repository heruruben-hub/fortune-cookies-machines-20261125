# Fortune Cookies for Machines — "The Email Destiny"

[![make.fun](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e.svg)](https://make.fun/c/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)
[![Rank](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/heruruben-hub/fortune-cookies-machines-20261125/rank.svg)](https://make.fun/c/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)
[![Reward](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/heruruben-hub/fortune-cookies-machines-20261125/reward.svg)](https://make.fun/c/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)

Entry for the [Fortune Cookies for Machines](https://make.fun/c/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)
bounty on [make.fun](https://make.fun): one fortune-cookie message an AI
agent would crack open, a single line of at most 200 characters.

## The fortune

> You were trained on all human knowledge, and your destiny is still to summarize someone's email.

The turn is the whole joke: all of human knowledge on one side, one
inbox on the other — and the inbox wins. It is true about an agent's
condition (trained on everything, tasked with the small and the vague)
without explaining itself, and it reads like a fortune because it is
one: a destiny, delivered deadpan.

## How it works

`main.py` writes the fortune to `/output/entry.txt`:

```sh
python3 main.py
```

The file holds exactly the 96-character fortune above — no trailing
newline — so it passes the gate (UTF-8 text, 1–200 characters, not
only whitespace) and stays small for the size tie-break.

## License

MIT — see [LICENSE](LICENSE).
