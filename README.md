# Portfolio AI Assistant

> A zero-install, AI-powered quantitative portfolio dashboard that lives in a **single HTML file** — live prices, institutional-grade risk analytics, Monte Carlo simulation, an efficient frontier optimizer, rolling metrics, Black-Scholes options pricing, performance attribution, and a streaming AI chat that knows your exact holdings.

![status](https://img.shields.io/badge/status-live-brightgreen)
![license](https://img.shields.io/badge/license-MIT-blue)
![build](https://img.shields.io/badge/build%20step-none-success)
![LLM](https://img.shields.io/badge/LLM-Groq%20%7C%20Llama%203.3%2070B-orange)
![tabs](https://img.shields.io/badge/tabs-10%20quant%20tools-purple)
![data](https://img.shields.io/badge/market%20data-Yahoo%20Finance-blue)

---

## Why This Beats Every Other Portfolio Tracker

Most portfolio tools are either bloated SaaS apps that need an account, or bare-bones spreadsheets with no intelligence. This one is different:

- **No account. No install. No server.** Open one HTML file and you're live in seconds.
- **Real market data** — prices refresh automatically every 60 seconds straight from Yahoo Finance.
- **An AI that knows your actual portfolio** — not generic financial advice, but answers specific to your holdings, weights, and gain/loss figures.
- **Quant-grade analytics in the browser** — the same metrics a risk desk uses (VaR, CVaR, Sortino, Beta, Cholesky-correlated Monte Carlo) run entirely client-side with no backend.
- **10 tools in one screen** — from a simple P&L table all the way to options Greeks and the efficient frontier.

---

## Tab Overview

| # | Tab | What It Does |
|---|-----|-------------|
| 1 | **Holdings** | Live P&L table with cost basis, unrealized gains, weights, day change |
| 2 | **Charts** | Allocation donut by position, allocation donut by sector, gain/loss bar chart |
| 3 | **Watchlist** | Track any ticker with a target buy price — lights up with BUY ALERT when triggered |
| 4 | **Rebalance** | Slider-based target allocations → exact buy/sell orders in shares and dollars |
| 5 | **Risk ⚡** | Sharpe, Sortino, VaR, CVaR, Max Drawdown, Beta, full correlation heatmap |
| 6 | **Monte Carlo** | 500 correlated GBM paths, Cholesky covariance, P5/P50/P95 fan chart |
| 7 | **Frontier** | Markowitz efficient frontier via 2,000-portfolio random sampling, Sharpe-colored |
| 8 | **Rolling** | 30-day rolling Sharpe, realized vol, and Beta vs SPY over time |
| 9 | **Options** | Black-Scholes call/put pricer with full Greeks: Δ, Γ, Θ, V, ρ |
| 10 | **Attribution** | Position-level return contribution vs SPY benchmark, 90-day window |

---

## Features In Detail

### 1. Live Portfolio Dashboard

The Holdings tab is your home screen. Every row is a live position:

| Column | Description |
|--------|-------------|
| Ticker | Symbol, linked to sector tag |
| Shares | Number of shares held |
| Avg Cost | Your average cost basis per share |
| Current Price | Live from Yahoo Finance, auto-refreshes every 60s |
| Current Value | `shares × price` |
| Unrealized P&L | `(price − cost) × shares`, shown in $ and % |
| Day Change | `(price − prevClose) × shares` in $ |
| Weight | Position value ÷ total portfolio value |

The top bar always shows your live **total value**, **cumulative gain/loss**, and **day change** so you see the full picture at a glance. Everything is color-coded green/red.

---

### 2. Interactive Charts

Three Chart.js charts in the Charts tab:

- **Allocation by Position** — donut chart showing each ticker's weight in the portfolio
- **Allocation by Sector** — same data grouped by sector (Technology, Financials, ETF, etc.)
- **Gain/Loss Bar Chart** — side-by-side bars of unrealized P&L per position, making outliers immediately obvious

---

### 3. AI Portfolio Chat (Streaming)

A persistent chat sidebar powered by **Llama 3.3 70B via Groq**. The entire portfolio state — every ticker, shares, cost basis, current price, unrealized gain/loss, weight, sector — is injected as the system prompt before every message. Responses stream in token-by-token via SSE.

Pre-built prompts to get started immediately:
- *"Am I too concentrated in any sector?"*
- *"Give me rebalancing suggestions"*
- *"What are my riskiest positions?"*
- *"Identify tax-loss harvesting opportunities"*
- *"Summarize my portfolio performance"*

Because the model has your exact numbers, it gives specific, actionable analysis — not generic disclaimers.

---

### 4. Watchlist with Price Alerts

Add any ticker alongside a target buy price. The watchlist auto-refreshes every 60 seconds. When a stock's live price drops to or below your target, the row highlights with a **BUY ALERT** badge. Useful for tracking names you want to enter on a pullback without setting brokerage alerts.

---

### 5. Rebalancing Tool

Set a target % allocation per holding using sliders, or hit **Equal Weight** to distribute evenly. Click **Calculate** and the tool outputs a full order list:

- Drift from target (current weight vs. desired weight)
- Direction: **BUY** or **SELL**
- Number of shares to trade
- Exact dollar amount of each trade

All math assumes current live prices — no manual updates needed.

---

### 6. Risk Analytics ⚡

All metrics are computed from **90 days of daily closing prices** fetched from Yahoo Finance. No third-party risk service, no API key — pure browser math.

#### Sharpe Ratio
```
Sharpe = (R_p − R_f) / σ_p
```
Where `R_p` is the annualized portfolio return (geometric), `R_f` is the risk-free rate (default 4.5% = approximate T-bill yield), and `σ_p` is annualized standard deviation of daily returns (`σ_daily × √252`).

#### Sortino Ratio
```
Sortino = (R_p − R_f) / σ_downside
```
Same as Sharpe but the denominator only counts days where the portfolio return was negative — penalizing downside risk rather than total volatility. A higher Sortino than Sharpe means your positive days have more variance than your negative days, which is good.

#### Annualized Volatility
```
σ_annual = std(daily_returns) × √252
```
Realized volatility from the 90-day sample. Shown as a percentage.

#### Maximum Drawdown
```
MDD = max over t of (peak_t − trough_t) / peak_t
```
Scans the full 90-day cumulative return series to find the worst peak-to-trough loss. A drawdown of -18% means at some point the portfolio fell 18% from its previous high within the window.

#### Value at Risk (VaR 95%) — Historical Simulation
```
VaR_95 = −percentile(daily_returns, 5)
```
The loss you would not expect to exceed on 95% of trading days, based on the actual historical distribution of returns. No normality assumption — uses the empirical 5th percentile directly.

#### Conditional VaR / Expected Shortfall (CVaR 95%)
```
CVaR_95 = −mean(returns where return < −VaR_95)
```
The average loss on the worst 5% of days. Also called Expected Shortfall. CVaR is considered a more coherent risk measure than VaR because it accounts for the magnitude of tail losses, not just the cutoff point.

#### Beta vs SPY
```
β = Cov(R_portfolio, R_SPY) / Var(R_SPY)
```
Computed from daily returns of the full portfolio (weighted sum) vs. SPY over the same 90-day window. Beta > 1 means the portfolio amplifies market moves; Beta < 1 means it dampens them.

#### Correlation Heatmap
Full pairwise Pearson correlation matrix across all holdings. Each cell shows `Corr(R_i, R_j)` computed from daily returns. Colored from deep red (−1, perfect inverse) through white (0, uncorrelated) to deep green (+1, perfect co-movement). High inter-portfolio correlation means less diversification benefit than the number of positions suggests.

---

### 7. Monte Carlo Simulation

Models future portfolio value using **correlated Geometric Brownian Motion** — the same framework used in institutional risk systems.

#### How It Works

**Step 1 — Estimate parameters from history**

For each asset `i`, compute:
- `μ_i` = mean daily log-return (annualized: `× 252`)
- `σ_i` = standard deviation of daily log-returns (annualized: `× √252`)

**Step 2 — Build the covariance matrix**

```
Σ_{ij} = Corr(R_i, R_j) × σ_i × σ_j
```

**Step 3 — Cholesky decomposition**

Factor `Σ = L Lᵀ` where `L` is lower-triangular. This lets us transform independent standard normal draws into correlated ones:

```
z_correlated = L × z_independent
```

where `z_independent ~ N(0,1)` per asset per time step, generated via the **Box-Muller transform**:
```
z = √(−2 ln U₁) × cos(2π U₂),   U₁, U₂ ~ Uniform(0,1)
```

**Step 4 — Simulate GBM paths**

For each of 500 simulations and each of 252 time steps:
```
S_{t+1} = S_t × exp((μ − σ²/2)Δt + σ√Δt × z_correlated)
```

Portfolio value is the weighted sum across all assets at each step.

**Step 5 — Summarize**

Extracts P5, P50, P95 envelope at each time step. Displays:
- Fan chart with shaded confidence band
- Final-day expected value (P50), downside (P5), and upside (P95) in dollars

---

### 8. Efficient Frontier

Approximates the **Markowitz mean-variance efficient frontier** using random portfolio sampling — no quadratic programming required.

#### How It Works

**Step 1 — Sample random portfolios**

Generate 2,000 weight vectors using a Dirichlet-like approach:
```
w_i = −log(U_i) / Σ_j (−log(U_j)),   U_i ~ Uniform(0,1)
```
This produces uniformly distributed weight vectors that sum to 1 with all weights positive.

**Step 2 — Compute portfolio metrics for each**

For each weight vector `w`:
```
R_p  = wᵀ μ                              (expected annual return)
σ_p  = √(wᵀ Σ w)                         (annual volatility)
Sharpe = (R_p − R_f) / σ_p
```

**Step 3 — Plot and annotate**

- Each portfolio is a point on a return vs. volatility scatter chart
- Points are colored by Sharpe ratio (dark = low, bright = high)
- The **minimum volatility** portfolio (leftmost point) and **maximum Sharpe** portfolio (tangency point) are auto-annotated with their exact per-ticker weightings

The upper-left envelope of the scatter cloud is the efficient frontier — any portfolio below it has the same risk for less return, or the same return for more risk.

---

### 9. Rolling Metrics

Computes three risk metrics over a sliding **30-day window** across the full 90-day history, creating a time-series that shows how each metric has evolved:

| Metric | What A Change Means |
|--------|-------------------|
| **Rolling Sharpe** | Rising = improving risk-adjusted return; falling = deteriorating edge |
| **Rolling Volatility** | Spike = a volatility regime change or news event |
| **Rolling Beta vs SPY** | Rising = portfolio becoming more market-sensitive over time |

All three are plotted as line charts with date labels on the x-axis. Useful for detecting whether strong risk-adjusted performance is structural or a recent artifact.

---

### 10. Black-Scholes Options Calculator

A full **European options pricing engine** running entirely in the browser. Input fields:

| Input | Description |
|-------|-------------|
| Ticker | Auto-fills the current live price |
| Spot Price (S) | Current underlying price |
| Strike Price (K) | Option strike |
| Time to Expiry (T) | In years (e.g. 0.25 = 3 months) |
| Implied Volatility (σ) | As a decimal (e.g. 0.30 = 30%) |
| Risk-Free Rate (r) | As a decimal (e.g. 0.045 = 4.5%) |

#### Black-Scholes Formula

```
d₁ = [ln(S/K) + (r + σ²/2)T] / (σ√T)
d₂ = d₁ − σ√T

Call = S × N(d₁) − K × e^(−rT) × N(d₂)
Put  = K × e^(−rT) × N(−d₂) − S × N(−d₁)
```

`N(x)` is the standard normal CDF, approximated using the Abramowitz & Stegun polynomial with error < 7.5×10⁻⁸.

#### The Greeks

| Greek | Formula | Interpretation |
|-------|---------|----------------|
| **Delta (Δ)** | `N(d₁)` for call, `N(d₁)−1` for put | $ change in option per $1 move in underlying |
| **Gamma (Γ)** | `N'(d₁) / (S σ √T)` | Rate of change of Delta per $1 move — curvature |
| **Theta (Θ)** | `−[S N'(d₁) σ / (2√T)] − rK e^(−rT) N(d₂)` | Time decay: $ lost per day |
| **Vega (V)** | `S N'(d₁) √T` | $ change per 1% move in implied vol |
| **Rho (ρ)** | `KT e^(−rT) N(d₂)` for call | $ change per 1% move in risk-free rate |

All Greeks update instantly as inputs change. Built to practice quant interview derivations and price real options on your existing holdings.

---

### 11. Performance Attribution

Breaks down total portfolio return over the 90-day window **position by position** and compares each holding to the SPY benchmark over the same period.

#### Method (Brinson-style simplified)

For each holding `i` over the 90-day window:
```
Period Return_i = (P_end − P_start) / P_start
Start Weight_i  = position value at start / total portfolio value at start
Contribution_i  = Start Weight_i × Period Return_i
```

The benchmark contribution is the same calculation applied to SPY.

The tab displays:
- A bar chart with each position's contribution side-by-side with SPY's weighted contribution
- Whether each position added to or subtracted from relative performance
- Exact numbers: start weight, period return, contribution in percentage points

Green bars above the SPY line = alpha generators. Red bars below = drag on relative performance.

---

## Tech Stack

| Layer | Technology | Detail |
|---|---|---|
| UI Framework | [Tailwind CSS](https://tailwindcss.com) via CDN | Dark theme, utility-first, zero build step |
| Charts | [Chart.js 4.4](https://www.chartjs.org) via cdnjs | Donut, bar, scatter, and line charts |
| Market Data | [Yahoo Finance v8 API](https://query1.finance.yahoo.com) | Free, no key — live prices + 90-day OHLCV history |
| AI Model | [Llama 3.3 70B Versatile](https://groq.com) via Groq | State-of-the-art open model, free tier available |
| AI Streaming | Groq OpenAI-compatible API + `ReadableStream` / SSE | Token-by-token streaming in the browser |
| Quant Math | Vanilla JS | Cholesky, Box-Muller, Black-Scholes, Pearson correlation — no libraries |
| Runtime | Vanilla JavaScript | No React, no bundler, no build step — just open the file |
| Launcher | Python 3 + `python-dotenv` + `webbrowser` | Injects API key at runtime, never commits it |

---

## Getting Started

### Prerequisites
- Python 3.8+
- A free Groq API key — get one at [console.groq.com](https://console.groq.com) (takes 30 seconds, no credit card)

### 1. Clone the repo
```bash
git clone https://github.com/OzSpidey/portfolio-ai-assistant.git
cd portfolio-ai-assistant
```

### 2. Install the one Python dependency
```bash
pip install python-dotenv
```

### 3. Add your Groq API key
```bash
cp .env.example .env
```
Open `.env` and replace the placeholder with your actual key:
```
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxx
```

### 4. Run it
```bash
python run_portfolio.py
```

The launcher reads your key from `.env`, injects it into the HTML, writes a temp file, and opens the app in your default browser automatically. No server, no localhost, no terminal stays running after launch.

---

## How the Launcher Works

`run_portfolio.py` does exactly three things:
1. Reads `GROQ_API_KEY` from `.env` via `python-dotenv`
2. Replaces the `__GROQ_KEY__` placeholder in `portfolio_assistant.html` with the real key in memory
3. Writes a temp file (`tmp_portfolio_*.html`) and opens it via `webbrowser.open()`

The HTML file you commit contains only `__GROQ_KEY__` — the real key never touches git. The temp file is listed in `.gitignore` and deleted on the next run.

---

## Sample Holdings (Pre-loaded)

The app opens with 6 real positions so every tab is immediately populated and useful:

| Ticker | Shares | Avg Cost | Sector |
|---|---|---|---|
| AAPL | 10 | $150 | Technology |
| MSFT | 5 | $280 | Technology |
| NVDA | 3 | $400 | Technology |
| GOOGL | 4 | $130 | Communication Services |
| BRK-B | 8 | $320 | Financials |
| VTI | 20 | $200 | ETF/Diversified |

Replace these with your own holdings using the **Add Position** form in the Holdings tab. All 10 tabs update automatically.

---

## Quant Interview Prep

The analytics tabs cover concepts that appear regularly in quant researcher and quant developer interviews:

| Topic | Where in the App |
|-------|-----------------|
| Sharpe / Sortino ratio derivation | Risk ⚡ tab |
| VaR vs CVaR / Expected Shortfall | Risk ⚡ tab |
| Cholesky decomposition of covariance | Monte Carlo tab |
| Geometric Brownian Motion | Monte Carlo tab |
| Box-Muller transform | Monte Carlo (implementation detail) |
| Markowitz mean-variance optimization | Efficient Frontier tab |
| Black-Scholes PDE solution | Options tab |
| Delta, Gamma, Theta, Vega, Rho | Options tab |
| Performance attribution / Brinson model | Attribution tab |
| Rolling Sharpe / regime detection | Rolling Metrics tab |

Every formula shown above is implemented from scratch in vanilla JavaScript — no math libraries.

---

## License

MIT — use it, fork it, build on it.
