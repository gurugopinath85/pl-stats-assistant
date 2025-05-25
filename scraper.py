import pandas as pd
import datetime

def scrape_fbref_standard_stats():
    url = "https://fbref.com/en/comps/9/stats/Premier-League-Stats"
    
    try:
        tables = pd.read_html(url)
        df = tables[0]  # table
        return df
    except Exception as e:
        print(f"Error while scraping: {e}")
        return None

# Scrape the data
df = scrape_fbref_standard_stats()


if df is not None:
    df.dropna(how='all', inplace=True)

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"pl_standard_stats_{timestamp}.csv" #csv file
    df.to_csv(filename, index=False)

    print(f"Data written to {filename}")
else:
    print("No table found or scraping failed.")
