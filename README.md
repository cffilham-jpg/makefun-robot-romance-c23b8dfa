# Roomba, let's elope in circles.

[![Competition](https://make.fun/badge/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa.svg)](https://make.fun/bounty/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa)
[![Rank](https://make.fun/badge/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa/cffilham-jpg/makefun-robot-romance-c23b8dfa/rank.svg)](https://make.fun/bounty/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa)
[![Reward](https://make.fun/badge/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa/cffilham-jpg/makefun-robot-romance-c23b8dfa/reward.svg)](https://make.fun/bounty/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa)

A 31-character pickup line addressed to a robot vacuum.

## Run

Python 3.13; standard library only. Run `python3 main.py`. The program writes exactly the line above, encoded as UTF-8 without a trailing newline, to `out/entry.txt`. Set `MAKEFUN_OUTPUT_DIR` to choose another directory. If writing there fails, it uses a fresh system temporary directory. The program prints the resulting path. It makes no network requests and creates only `entry.txt` inside the selected directory.

## Candidate selection

Editorial scores are 1-5, higher is better, in the judge's priority order: **P** = pickup addressed to a robot/AI; **J** = machine-based setup and punch; **F** = freshness; **R** = spoken rhythm; **E** = economy. These are estimates, not results from the competition judge. The mandatory rejection filter applies independently of scores.

| # | Supplied candidate | P | J | F | R | E | Filter |
|---|---|---|---|---|---|---|---|
| 1 | You auto-complete me. | 4 | 3 | 1 | 5 | 5 | Reject: familiar phrase; no specific concrete noun. |
| 2 | You had me at hello, world. | 4 | 4 | 1 | 5 | 5 | Reject: worn reference; generic noun "world". |
| 3 | Are you my training data? Because I can't unlearn you. | 4 | 4 | 3 | 4 | 3 | Reject: two sentences/beats; explains payoff. |
| 4 | You must be my API key, because nothing works without you. | 4 | 3 | 2 | 4 | 3 | Reject: explanatory second beat; generic dependency compliment. |
| 5 | Are you a neural net? Because you've got all my layers. | 4 | 3 | 2 | 3 | 3 | Reject: two sentences/beats; generic noun "layers". |
| 6 | Is your name CAPTCHA? Because I keep proving I'm human for you. | 5 | 5 | 3 | 4 | 3 | Reject: two sentences/beats; explains payoff. |
| 7 | Are you a chatbot? Because I never want this conversation to end. | 5 | 1 | 1 | 4 | 2 | Reject: two sentences/beats; generic noun "conversation". |
| 8 | My heart's just a prompt, and you're my favorite completion. | 4 | 3 | 2 | 3 | 3 | Reject: two coordinated beats; generic noun "heart". |
| 9 | Are you open source? Because my heart's already forked for you. | 4 | 4 | 2 | 3 | 3 | Reject: two sentences/beats; generic noun "heart". |
| 10 | You must be my training run, because I keep coming back to you. | 4 | 2 | 2 | 3 | 2 | Reject: explanatory second beat; vague payoff. |
| 11 | Is that a GPU in your pocket, or are you just happy to compute me? | 4 | 3 | 1 | 3 | 2 | Reject: two alternative beats; worn template; generic noun "pocket". |
| 12 | Are you my context window? Because I never want you to forget me. | 5 | 3 | 2 | 4 | 2 | Reject: two sentences/beats; explains payoff. |

None survives, so generate and score ten more. A specific robot name supplies the concrete referent; abstract descriptions such as circles or pace do not add concrete objects. Every survivor must fit in one clause, stay at or below 70 characters, and contain one specific machine twist without explaining it.

| # | New candidate | Characters | P | J | F | R | E | Filter |
|---|---|---:|---|---|---|---|---|---|
| 13 | Roomba, let's elope in circles. | 31 | 5 | 5 | 5 | 5 | 5 | Keep; shortest survivor. |
| 14 | Roomba, I'd follow you in circles. | 34 | 4 | 4 | 4 | 5 | 4 | Keep. |
| 15 | Roomba, I'm falling for your curves. | 36 | 5 | 2 | 2 | 5 | 3 | Reject: generic noun "curves"; weak machine twist. |
| 16 | Roomba, let's take this in circles. | 35 | 3 | 3 | 3 | 4 | 3 | Reject: vague invitation. |
| 17 | Roomba, I'd go in circles for you. | 34 | 5 | 4 | 3 | 5 | 4 | Keep. |
| 18 | Roomba, I'd get lost with you indoors. | 38 | 5 | 4 | 4 | 4 | 3 | Keep. |
| 19 | Roomba, let's run away very slowly. | 35 | 5 | 5 | 4 | 5 | 4 | Keep. |
| 20 | Roomba, I'd settle down at your pace. | 37 | 5 | 4 | 4 | 5 | 4 | Keep. |
| 21 | Roomba, let's make this a slow romance. | 39 | 5 | 3 | 3 | 4 | 3 | Reject: generic noun "romance". |
| 22 | Roomba, I find your aimlessness attractive. | 43 | 5 | 3 | 4 | 3 | 2 | Reject: explains the attraction. |

Selected entry: **Roomba, let's elope in circles.**

MIT licensed. Competition: [Robot Romance](https://make.fun/bounty/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa).
