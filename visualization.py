import csv
import matplotlib.pyplot as plt
from matplotlib.dates import YearLocator, DateFormatter
import datetime as dt

industry_name = {
   "Industry_01": "Food industry portfolio",
    "Industry_02": "Beer industry portfolio",
    "Industry_03": "Smoke industry portfolio",
    "Industry_04": "Games industry portfolio",
    "Industry_05": "Books industry portfolio",
    "Industry_06": "Hshld industry portfolio",
    "Industry_07": "Clths industry portfolio",
    "Industry_08": "Hlth industry portfolio",
    "Industry_09": "Chems industry portfolio",
    "Industry_10": "Txtls industry portfolio",
    "Industry_11": "Cnstr industry portfolio",
    "Industry_12": "Steel industry portfolio",
    "Industry_13": "FabPr industry portfolio",
    "Industry_14": "ElcEq industry portfolio",
    "Industry_15": "Autos industry portfolio",
    "Industry_16": "Carry industry portfolio",
    "Industry_17": "Mines industry portfolio",
    "Industry_18": "Coal industry portfolio",
    "Industry_19": "Oil industry portfolio",
    "Industry_20": "Util industry portfolio",
    "Industry_21": "Telcm industry portfolio",
    "Industry_22": "Servs industry portfolio",
    "Industry_23": "BusEq industry portfolio",
    "Industry_24": "Paper industry portfolio",
    "Industry_25": "Trans industry portfolio",
    "Industry_26": "Whlsl industry portfolio",
    "Industry_27": "Rtail industry portfolio",
    "Industry_28": "Meals industry portfolio",
    "Industry_29": "Fin industry portfolio",
    "Industry_30": "Other industry portfolio",
}

cleaned_industry_dataset = {}

with open("nexus.csv") as market_dataset:
    csv_reader = csv.DictReader(market_dataset, delimiter=',')
    date = ""
    for row in csv_reader:
        for key, value in row.items():
            if key == 'Date':
                date = value
                continue
            
            industry_data = cleaned_industry_dataset.setdefault(key, [])
            industry_data.append((date, float(value)))
    
for industry, dataset in cleaned_industry_dataset.items():
    dates = [dt.datetime.strptime(d[0], "%m/%d/%Y") for d in dataset]
    values = [d[1] for d in dataset]

    plt.figure(figsize=(14, 5))
    plt.plot(dates, values, color='skyblue', marker='o', linestyle='-', markersize=5, linewidth=1.5)

    plt.ylim(-16, 16)
    plt.xticks(rotation=45)


    plt.gca().xaxis.set_major_locator(YearLocator())
    plt.gca().xaxis.set_major_formatter(DateFormatter('%Y'))

    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
