# Public signal sheets

Edit, then run `./build/build.sh`: it redraws the four PNGs in the live repo and rebuilds the page.
One `## <sheet>` section per sheet, YAML inside; `## defaults` applies to every sheet unless a sheet sets the same key.
Numbers are always computed; you pick which ones show and how they are labelled.

- `tiles`: up to 4, in order. `rows`: any order; delete a line to hide it. Keep labels in double quotes; `\n` inside one is a line break.
- Label placeholders: `{year}` (last year), `{since}` (first year), `{ctx}` (the correlation factors' names).
- Figure keys: `ytd` · `held_sharpe` · `max_dd` · `calmar` · `vol` · `peak_gross` · `sharpe_vol_calmar` · `days_in_market` ·
  `episodes` · `trades` · `gross` · `correlation` · `breakeven` · `note` (text-only row).
- Fixed in code, not here: no gate shading or timing, no lots, no thresholds, no $ cost (the masking).

## defaults

```yaml
footnote: Hypothetical backtest, net of modelled trading costs
tiles:
  - ytd: "P&L {year} YTD\n% of equity"
  - held_sharpe: "Sharpe, held days\nnet of costs"
  - max_dd: "Max drawdown\n% of equity"
  - calmar: "Calmar\nall days"
rows:
  - sharpe_vol_calmar: "Sharpe, all days · realized vol · Calmar"
  - days_in_market: "Days in market, since {since}"
  - episodes: "Held episodes · hit rate"
  - gross: "Gross / equity, held days: median · p90"
  - correlation: "Correlation: {ctx}"
```

## vx_combined_regime

```yaml
title: VIX Spot/Futures Basis
level: VIX futures term structure, M1 − M2
rows:
  - sharpe_vol_calmar: "Sharpe, all days · realized vol · Calmar"
  - trades: "Trades · hit rate · win rate"
  - days_in_market: "Days in market, since {since}"
  - gross: "Gross / equity, held days: median · p90"
  - correlation: "Correlation: {ctx}"
```

## crack_regime

```yaml
title: WTI Crack Spread
level: 3:2:1 crack spread
```

## rates_rv_regime_5y

```yaml
title: US/EU Rates Relative Value
level: US 5y − German 5y yield, bp
```

## core_trend_regime

```yaml
title: Macro Trend
level: Diversified macro basket, equal weight
rows:
  - sharpe_vol_calmar: "Sharpe, all days · realized vol · Calmar"
  - days_in_market: "Days in market, since {since}"
  - episodes: "Leg episodes · hit rate"
  - gross: "Gross / equity, held days: median · p90"
  - correlation: "Correlation: {ctx}"
```
