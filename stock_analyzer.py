import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import seaborn as sns
import warnings

# --- 1. CONFIGURATION ---
warnings.filterwarnings('ignore') 
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

class StockAnalyzer:
    def __init__(self):
        self.ticker_symbol = ""
        self.stock = None
        self.data_store = {} 
        self.analysis_report = []

    def get_user_input(self):
        raw_name = input("\nEnter Stock Name : ").strip().upper()
        
        # NSE Extension Logic
        if not raw_name.endswith(".NS") and not raw_name.endswith(".BO"):
            self.ticker_symbol = f"{raw_name}.NS"
        else:
            self.ticker_symbol = raw_name
            
        print(f"\n[INFO] Fetching data for {self.ticker_symbol}...")
        self.stock = yf.Ticker(self.ticker_symbol)

    def fetch_financial_data(self):
        """Fetches data safely. If one part fails, others will still work."""
        
        # Helper function to fetch safely
        def safe_fetch(fetch_func, name):
            try:
                print(f"... Fetching {name}")
                data = fetch_func()
                if data is not None and not data.empty:
                    return data
                return pd.DataFrame(["Data Unavailable"])
            except Exception as e:
                return pd.DataFrame([f"Error fetching data: {str(e)}"])

        # 1. Quarterly Results
        self.data_store['Quarterly Results'] = safe_fetch(lambda: self.stock.quarterly_financials, "Quarterly Results")

        # 2. Profit & Loss
        self.data_store['Profit & Loss'] = safe_fetch(lambda: self.stock.financials, "Profit & Loss")

        # 3. Balance Sheet
        self.data_store['Balance Sheet'] = safe_fetch(lambda: self.stock.balance_sheet, "Balance Sheet")

        # 4. Cash Flow
        self.data_store['Cash Flow'] = safe_fetch(lambda: self.stock.cashflow, "Cash Flow")

        # 5. Shareholding
        print("... Fetching Shareholding Pattern")
        try:
            major = self.stock.major_holders
            if major is not None and not major.empty:
                self.data_store['Major Investors'] = major
            
            inst = self.stock.institutional_holders
            if inst is not None and not inst.empty:
                self.data_store['Institutional Investors'] = inst
        except Exception:
            print("[WARN] Shareholding data structure changed, skipping this part.")

    def calculate_ratios(self):
        print("... Calculating Key Ratios")
        try:
            info = self.stock.info
            ratios = {
                "Metric": [
                    "Current Price", "Market Cap", "Trailing P/E", "Forward P/E",
                    "PEG Ratio", "Price to Book (P/B)", "Return on Equity (ROE)",
                    "Debt to Equity", "Dividend Yield", "52 Week High", "52 Week Low"
                ],
                "Value": [
                    info.get('currentPrice', 'N/A'), info.get('marketCap', 'N/A'), 
                    info.get('trailingPE', 'N/A'), info.get('forwardPE', 'N/A'),
                    info.get('pegRatio', 'N/A'), info.get('priceToBook', 'N/A'), 
                    info.get('returnOnEquity', 'N/A'), info.get('debtToEquity', 'N/A'), 
                    info.get('dividendYield', 'N/A'), info.get('fiftyTwoWeekHigh', 'N/A'), 
                    info.get('fiftyTwoWeekLow', 'N/A')
                ]
            }
            self.data_store['Key Ratios'] = pd.DataFrame(ratios)
        except Exception as e:
            self.data_store['Key Ratios'] = pd.DataFrame([f"Error: {str(e)}"])

    def perform_analysis(self):
        print("... Running AI Analysis Logic")
        try:
            info = self.stock.info
            pros = []
            cons = []
            
            # 1. Valuation Check
            pe = info.get('trailingPE')
            if pe and isinstance(pe, (int, float)):
                if pe < 20: pros.append("Stock is Undervalued (Low P/E).")
                elif pe > 50: cons.append("Stock is Overvalued (High P/E).")
            
            # 2. Debt Check
            de = info.get('debtToEquity')
            if de and isinstance(de, (int, float)):
                if de < 50: pros.append("Company has Low Debt.") 
                elif de > 200: cons.append("Company has High Debt.")

            # 3. Profitability (ROE)
            roe = info.get('returnOnEquity')
            if roe and isinstance(roe, (int, float)):
                if roe > 0.15: pros.append("Excellent ROE (>15%).")
                elif roe < 0.05: cons.append("Poor ROE (<5%).")

            # 4. Earnings
            eps = info.get('trailingEps')
            if eps and isinstance(eps, (int, float)) and eps < 0:
                cons.append("Company is currently in LOSS (Negative EPS).")

            # Formatting
            max_len = max(len(pros), len(cons)) if (pros or cons) else 1
            pros += [""] * (max_len - len(pros))
            cons += [""] * (max_len - len(cons))
            
            # Verdict Logic
            score = len([p for p in pros if p]) - len([c for c in cons if c])
            if score >= 2: verdict = "STRONG BUY / POSITIVE"
            elif score <= -2: verdict = "SELL / RISKY"
            else: verdict = "NEUTRAL / HOLD"
            
            summary = pd.DataFrame({
                "ANALYSIS SUMMARY": [f"FINAL VERDICT: {verdict}"], 
                " ": [""]
            })
            details = pd.DataFrame({"PROS": pros, "CONS": cons})
            
            self.data_store['Final Analysis'] = pd.concat([summary, details], ignore_index=True)
            
        except Exception as e:
            self.data_store['Final Analysis'] = pd.DataFrame([f"Analysis Failed: {str(e)}"])

    def export_to_excel(self):
        filename = f"{self.ticker_symbol}_Fundamental_Report.xlsx"
        print(f"\n[INFO] Saving Excel Report: {filename}")
        
        try:
            with pd.ExcelWriter(filename, engine='xlsxwriter') as writer:
                
                sheets_order = [
                    'Key Ratios', 
                    'Quarterly Results', 
                    'Profit & Loss', 
                    'Balance Sheet', 
                    'Cash Flow', 
                    'Major Investors', 
                    'Institutional Investors',
                    'Final Analysis'
                ]
                
                for sheet_name in sheets_order:
                    if sheet_name in self.data_store:
                        df = self.data_store[sheet_name]
                        df.to_excel(writer, sheet_name=sheet_name)
                        
                        # Formatting
                        worksheet = writer.sheets[sheet_name]
                        worksheet.set_column(0, 0, 30) 
                        worksheet.set_column(1, 10, 18)
                        
            print("✅ Report Generated Successfully (Analysis is in the LAST Sheet).")
        except Exception as e:
            print(f"❌ Excel Save Error: {e}")

class InteractiveChart:
    def __init__(self, ticker_symbol):
        self.ticker = yf.Ticker(ticker_symbol)
        self.symbol = ticker_symbol
        self.fig, self.ax1 = plt.subplots(figsize=(12, 7))
        self.ax2 = self.ax1.twinx()
        plt.subplots_adjust(bottom=0.2)
        
        self.update_chart('1y')
        self.create_buttons()
        
    def update_chart(self, period):
        print(f"[GRAPH] Updating chart: {period}")
        try:
            df = self.ticker.history(period=period)
            self.ax1.clear()
            self.ax2.clear()
            
            if df.empty:
                print("No data for graph.")
                return

            self.ax1.bar(df.index, df['Volume'], color='#B0C4DE', alpha=0.5, label='Volume')
            self.ax1.set_ylabel("Volume")
            
            sns.lineplot(x=df.index, y=df['Close'], ax=self.ax2, color='#2E86C1', linewidth=2)
            self.ax2.set_ylabel("Price (INR)")
            
            self.ax1.set_title(f"{self.symbol} - {period.upper()}", fontsize=14, fontweight='bold')
            plt.draw()
        except Exception as e:
            print(f"Graph Error: {e}")

    def create_buttons(self):
        buttons_info = [
            ('1M', '1mo', 0.1), ('6M', '6mo', 0.2), 
            ('1Y', '1y', 0.3), ('3Y', '3y', 0.4), 
            ('5Y', '5y', 0.5), ('MAX', 'max', 0.6)
        ]
        self.buttons = []
        for label, period, x_pos in buttons_info:
            ax_btn = plt.axes([x_pos, 0.05, 0.08, 0.075])
            btn = Button(ax_btn, label)
            btn.on_clicked(lambda event, p=period: self.update_chart(p))
            self.buttons.append(btn)

if __name__ == "__main__":
    try:
        app = StockAnalyzer()
        app.get_user_input()
        app.fetch_financial_data()
        app.calculate_ratios()
        app.perform_analysis()
        app.export_to_excel()
        
        print("\n[INFO] Opening Interactive Graph...")
        chart = InteractiveChart(app.ticker_symbol)
        plt.show()
        
    except Exception as e:
        print(f"\n[CRITICAL ERROR] {e}")