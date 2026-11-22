# news-image-20261122 — The World Today

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/tulankganteng/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/tulankganteng/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

**Entry for the make.fun bounty [news-image-20261122](https://make.fun/bounty/news-image-20261122)
($100, deadline Tue 2026-11-24 07:00 WIB).** A program that writes one image
summing up the world's news of Sunday 22 November 2026 to `/output/entry.png`.

## What the image shows

A newspaper front page, **"THE WORLD TODAY — SUNDAY 22 NOVEMBER 2026"**,
with **35 stories across 7 regions** (5 per region): a compact masthead,
a lead strip on Iran's Saturday-night strike on US positions in Bahrain
with a small hero image, then a dense region grid — 2 columns × 3 rows
of region blocks plus one full-width bottom block — each with a coloured
region header bar and 5 compact items (bold kicker + headline).

| Region | Stories |
|---|---|
| **NORTH AMERICA** | Wall Street's worst week since Mar 2020 (Nasdaq −10%, >$4tn wiped); Bitcoin flushed to $55,130, lowest since Sep 2024; Anthropic's record $81.3bn IPO (+17% day one); GTA 6 review-bombed (critics 99, users 5.6); Verstappen on pole in Las Vegas. |
| **LATIN AMERICA** | 'El Chapo Isidro' captured in Guasave, 11 dead; Peru 6.8 quake in Junin; supercell storm kills 5 in Tupanciretã, Brazil; Bolsonaro taken to ICU in Brasilia; Brazil's real at its lowest since May. |
| **EUROPE** | COP31 11th-hour deal still omits fossil fuels; France's 6th Saturday of cost-of-living protests (82,500); Burnham's UK–EU reset; Russia's 148-drone overnight strike on Ukraine; drones hit Russian cargo ship Sparta II in the Baltic. |
| **MIDDLE EAST** | Iran claims it hit two US Patriot radars in Bahrain; 6 killed in Gaza despite the Oct 2025 ceasefire; first-ever Trump–Xi–Putin summit in Shenzhen; Nile Al-Alamein declaration; Sisi opens the Aswan Forum. |
| **AFRICA** | Nigeria funeral boat capsizes, 24 dead; Sudan army retakes al-Mazroub; ex-deputy president Phumzile Mlambo-Ngcuka dies aged 71; Western Cape wildfire burns 25,000 ha; Women For Change march in Johannesburg. |
| **ASIA-PACIFIC** | 3 dead, 36 missing in a Jakarta candy-factory fire; Jakarta sets 2027 minimum wage at Rp6,136,941; Modi opens the Nitish Setu bridge; TSMC/Samsung pause some China shipments; Nikkei falls 5.06%. |
| **OCEANIA, SPORT & CULTURE** | Australia hits back over a US report on AUKUS; BTS sweep MAMA 2026; ATP Finals tonight: Zverev v Alcaraz; India dominate New Zealand in the Wellington Test; France v South Africa in the Nations Championship final. |

The hero photograph is an AI-generated editorial illustration made for this
entry (no real person's likeness, no copied photograph); all text is set in
the composition script (`../compose.py`, kept outside the repo) so every word
is crisp and legible. The judge sees only the image — so the date, the
headline and every story are readable on the page itself.

## How it runs

`main.py` (Python 3.13, standard library only) checks the repository-held
`entry.png` (PNG, 1024×1024, under 1 MiB) and copies it to `/output/entry.png`
(or to `$MAKEFUN_OUTPUT_DIR` for local runs), then reads the copy back and
verifies it matches byte for byte. No network, no clock, no randomness —
two runs write identical bytes.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# out/entry.png — 1024×1024 PNG, < 1 MiB
```

## News sources (checked 22 Nov 2026)

- Iran strike on US positions in Bahrain, industrial facility fire: Reuters via EuropeSays, Bahrain Interior Ministry / Defence Force statements
- Wall Street's worst week since March 2020, Nasdaq −10%, S&P −8.6%, >$4tn wiped: Reuters figures via Fox Business / AP, BusinessToday
- El Chapo Isidro captured in Guasave, 11 dead: CNN, AP, Mexico's Defence Ministry
- COP31 deadlock, 11th-hour draft still omitting fossil fuels: Reuters, AP, AFP (22 Nov)
- Peru 6.8 quake, Junin, 129 km deep: Reuters, German Research Centre for Geosciences, Peru's Geophysical Institute
- Nigeria boat capsizes in Bayelsa, 24 dead: AP / Nigeria's National Emergency Management Agency
- France cost-of-living protests, 82,500: Interior Ministry via Euronews / Al Jazeera
- ATP Finals: Zverev v Alcaraz tonight in Turin: ATP Tour, TennisNow
- Bitcoin flushed to $55,130 Sat, lowest since Sep 2024, $2.54bn liquidated: Finnhub / CoinBeat / ForexCrunch (22 Nov)
- Anthropic record $81.3bn IPO, $83 → $97.17 close: BetaNews, WSJ, NPR (19–21 Nov)
- GTA 6 review-bombed, critics 99 vs users 5.6: Notebookcheck, Dexerto, Sportskeeda (20–21 Nov)
- Las Vegas GP: Verstappen on pole, Antonelli grid penalty: Wikipedia / Crash.net live (21 Nov)
- Brazil supercell storm, 5 dead, 25,000 affected: Reuters, AFP (21–22 Nov)
- Bolsonaro taken to ICU in Brasilia: Reuters (21 Nov)
- Brazil real past 5.65/USD, inflation 4.63%: TradingEconomics (Nov 2026)
- UK–EU summit, Burnham reset (SPS, carbon, youth mobility): Le Monde, BBC (20–21 Nov)
- Ukraine: Russia 148 drones + 3 missiles overnight 21–22 Nov, 2 killed, 83 hurt: Ukraine Monitor, CNN, Reuters
- Baltic: drones hit Russian cargo ship Sparta II, Gulf of Finland: CNN (22 Nov)
- Gaza: 6 killed Fri 20 Nov despite Oct 2025 ceasefire, 1,600+ dead since truce: AFP via TALi News / Alo360
- Trump–Xi–Putin first trilateral, Shenzhen, nuclear-risk declaration: Reuters, Argus (19–21 Nov)
- Nile Al-Alamein declaration, 22 Nov: WiseVoter / Al-Ahram
- Aswan Forum opens 21 Nov, Sisi on finance reform: Bytes Europe (22 Nov)
- Sudan army retakes al-Mazroub, North Kordofan: Al Jazeera (21 Nov)
- Phumzile Mlambo-Ngcuka dies aged 71: IOL / Sunday Independent (22 Nov)
- Western Cape wildfire, 25,000 ha, 24 homes: IQAir / IOL (22 Nov)
- Women For Change march, Johannesburg, 30-day GBVF demand: Sunday Independent (21–22 Nov)
- Indonesia candy-factory fire, Serang: 3 dead, 36 missing: Reuters (22 Nov)
- UMP 2027: Jakarta Rp6,136,941, Bali Rp4,559,287: IndonesiaNow / detik via ArchyNewsy (21 Nov)
- India: Modi opens Nitish Setu bridge; 1 crore HPV doses: CareerIndia (22 Nov)
- TSMC/Samsung pause some China shipments under new US chip rule: Reuters via Argus (21 Nov)
- Japan: Nikkei −5.06% Fri, SoftBank −14.48%, core CPI 2.2%: Argus / Stockbiz (20–22 Nov)
- Australia: Marles criticises US CBO report on AUKUS: Reuters (22 Nov)
- MAMA 2026, Osaka 20–21 Nov: BTS Artist + Album of Year, CORTIS Song of Year: Sports Chosun, Kpop Newswire (22 Nov)
- India v New Zealand Wellington Test; women's hockey 2–1 v South Korea: CareerIndia (22 Nov)
- Nations Championship final: France beat Argentina, face South Africa: Le Monde / Monolith (22 Nov)

## License

MIT — see [LICENSE](LICENSE).

## Reproducibility

The image is fixed: `main.py` copies the repository's own `entry.png`
to the output directory byte for byte and reads the copy back to confirm
it matches before reporting success. No network calls, no randomness,
no image processing — two runs write identical bytes.
