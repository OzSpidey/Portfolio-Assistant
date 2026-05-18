# Portfolio AI Assistant

> A zero-install, AI-powered stock portfolio dashboard that lives in a single HTML file — live prices, smart charts, a rebalancing tool, and a streaming AI chat that knows your exact holdings.

![Dark dashboard with holdings table, allocation charts, and AI chat sidebar](https://img.shields.io/badge/status-live-brightgreen) ![License MIT](https://img.shields.io/badge/license-MIT-blue) ![No build step](https://img.shields.io/badge/build%20step-none-success) ![Powered by Groq](https://img.shields.io/badge/LLM-Groq%20%7C%20Llama%203.3%2070B-orange) ![10 Tabs](https://img.shields.io/badge/tabs-10%20quant%20tools-purple)

---

## Why This Beats Every Other Portfolio Tracker

Most portfolio tools are either bloated SaaS apps that need an account, or bare-bones spreadsheets with no intelligence. This one is different:

- **No account. No install. No server.** Open one HTML file and you're live in seconds.
- **Real market data** — prices refresh automatically every 60 seconds straight from Yahoo Finance.
- **An AI that knows your actual portfolio** — not generic financial advice, but answers specific to your holdings, weights, and gain/loss figures.
- **Everything in one screen** — holdings, charts, watchlist, rebalancing, and AI chat, all at a glance.

---

## Features

### Live Portfolio Dashboard
Track all your positions in one table. For each holding you see:
- Current price, current value, avg cost basis
- Unrealized gain/loss in $ and %
- Today's dollar change per position
- Portfolio weight (% of total)

Color-coded green/red throughout. The top bar always shows your live total value, cumulative gain/loss, and day change.

### Live Market Prices
Prices are fetched from Yahoo Finance's free API — no key needed. Auto-refreshes every 60 seconds. Manual refresh button available. Shows the last-updated timestamp so you always know how fresh the data is.

### Interactive Charts (Chart.js)
Three charts available in the Charts tab:
- **Allocation by position** — donut chart showing portfolio weight per ticker
- **Allocation by sector** — donut chart grouping holdings by sector
- **Gain/Loss bar chart** — side-by-side bars showing unrealized P&L per position at a glance

### AI Portfolio Chat (Streaming)
A chat sidebar powered by **Llama 3.3 70B via Groq** with full portfolio context injected as the system prompt. Every response streams in token-by-token.

Pre-built suggested prompts to get started instantly:
- *"Am I too concentrated in any sector?"*
- *"Give me rebalancing suggestions"*
- *"What are my riskiest positions?"*
- *"Identify tax-loss harvesting opportunities"*
- *"Summarize my portfolio performance"*

Because the AI has your exact numbers — share prices, weights, gain/loss figures — it gives you specific, actionable analysis rather than generic advice.

### Watchlist with Price Alerts
Add any ticker with a target buy price. When the price drops to or at/below your target, the row lights up with a **BUY ALERT** badge. Refreshes every 60 seconds automatically.

### Rebalancing Tool
Set a target % allocation per holding using sliders (or hit **Equal Weight** to split evenly). The tool calculates:
- How far each position has drifted from target
- Whether to buy or sell, how many shares, and the exact dollar amount

No math required — just set your targets and hit Calculate.

### Risk Analytics ⚡
Institutional-grade risk metrics computed from 90 days of live price history:
- **Sharpe & Sortino ratios** — risk-adjusted return, with and without downside-only penalty
- **Annualized Volatility** — realized vol from daily returns
- **Max Drawdown** — worst peak-to-trough loss over the window
- **VaR & CVaR (95%)** — historical Value-at-Risk and Conditional VaR (expected shortfall)
- **Beta vs SPY** — market sensitivity of the full portfolio
- **Correlation heatmap** — full pairwise Pearson correlation matrix, color-coded

### Monte Carlo Simulation
Runs 500 correlated Geometric Brownian Motion paths using Cholesky decomposition of the realized covariance matrix. Shows a fan chart with P5 / P50 / P95 outcome bands over a 252-day horizon. The bottom panel displays summary statistics: expected value, median, and worst-case 5th-percentile outcome.

### Efficient Frontier
Samples 2,000 random portfolios using Dirichlet-like weight draws and plots them on a return vs. volatility scatter chart colored by Sharpe ratio. Automatically annotates the **minimum volatility** and **maximum Sharpe** portfolios with their exact weightings — no convex optimizer needed.

### Rolling Metrics
30-day rolling windows of three key metrics charted over time:
- **Rolling Sharpe** — how risk-adjusted performance has evolved
- **Rolling Volatility** — annualized realized vol through the window
- **Rolling Beta vs SPY** — how market sensitivity has shifted

Useful for spotting regime changes and whether your edge is stable.

### Black-Scholes Options Calculator
Full European options pricing engine in the browser:
- Input any ticker (auto-fills live price), strike, expiry, vol, risk-free rate
- Outputs **Call and Put prices** plus the complete Greeks: **Delta, Gamma, Theta, Vega, Rho**
- Greeks update instantly as you adjust inputs — no submit required

Built to practice quant interview questions and price real options on your holdings.

### Performance Attribution
Breaks down your portfolio's return over the last 90 days position-by-position and compares it to SPY. For each holding, shows:
- **Contribution** = start weight × period return
- **SPY benchmark return** for the same period
- Side-by-side bar chart of each position's alpha vs. benchmark

Instantly shows you which positions drove outperformance and which dragged returns.

---

## Tech Stack

| Layer | Technology |
|---|---|
| UI Framework | [Tailwind CSS](https://tailwindcss.com) via CDN |
| Charts | [Chart.js 4.4](https://www.chartjs.org) via cdnjs |
| Market Data | [Yahoo Finance Chart API](https://query1.finance.yahoo.com) (free, no key) |
| AI Model | [Llama 3.3 70B Versatile](https://groq.com) via Groq |
| AI Streaming | Groq OpenAI-compatible API + `ReadableStream` / SSE |
| Runtime | Vanilla JavaScript — no framework, no build step |
| Launcher | Python 3 + `python-dotenv` + `webbrowser` |

---

## Getting Started

### Prerequisites
- Python 3.8+
- A free Groq API key — get one at [console.groq.com](https://console.groq.com) (takes 30 seconds)

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
Open `.env` and replace `your_groq_api_key_here` with your actual key:
```
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxx
```

### 4. Run it
```bash
python run_portfolio.py
```

The launcher reads your key from `.env`, injects it into the HTML, and opens the app in your default browser automatically. No server, no localhost, no terminal stays running.

---

## How the Launcher Works

`run_portfolio.py` does three things:
1. Reads `GROQ_API_KEY` from `.env`
2. Injects it into `portfolio_assistant.html` (replacing a placeholder)
3. Writes a temp file and opens it in your browser via `webbrowser.open()`

This keeps secrets out of the HTML (which you can safely commit) and out of git entirely.

---

## Sample Holdings (Pre-loaded)

The app opens with 6 real positions so it's immediately useful:

| Ticker | Shares | Avg Cost | Sector |
|---|---|---|---|
| AAPL | 10 | $150 | Technology |
| MSFT | 5 | $280 | Technology |
| NVDA | 3 | $400 | Technology |
| GOOGL | 4 | $130 | Communication Services |
| BRK-B | 8 | $320 | Financials |
| VTI | 20 | $200 | ETF/Diversified |

Replace these with your own holdings using the **Add Position** form in the Holdings tab.

---

## License

MIT — use it, fork it, build on it.
