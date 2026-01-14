import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import seaborn as sns

graph_padding_factor = 0.10

graph_dir = "graphs"
os.makedirs(graph_dir, exist_ok=True)


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
    "Industry_11": "Cnstr industry portfolio", # Construction
    "Industry_12": "Steel industry portfolio",
    "Industry_13": "FabPr industry portfolio", # Fabric
    "Industry_14": "ElcEq industry portfolio", # Electrical Equipment
    "Industry_15": "Autos industry portfolio",
    "Industry_16": "Carry industry portfolio",
    "Industry_17": "Mines industry portfolio",
    "Industry_18": "Coal industry portfolio",
    "Industry_19": "Oil industry portfolio",
    "Industry_20": "Util industry portfolio",
    "Industry_21": "Telcm industry portfolio",
    "Industry_22": "Servs industry portfolio",
    "Industry_23": "BusEq industry portfolio", # Business Equipment
    "Industry_24": "Paper industry portfolio",
    "Industry_25": "Trans industry portfolio", # Transport
    "Industry_26": "Whlsl industry portfolio", # Wholesale
    "Industry_27": "Rtail industry portfolio",
    "Industry_28": "Meals industry portfolio",
    "Industry_29": "Fin industry portfolio",
    "Industry_30": "Other industry portfolio",
}

industry_dataframe = pd.read_csv("nexus.csv", index_col="Date", parse_dates=True)

# Visualizing the monthly returns
for column in industry_dataframe.columns:
    plt.figure(figsize=(14, 5))

    industry_dataframe[column].plot(
        color="skyblue", marker="o", linestyle="-", markersize=5, linewidth=1.5
    )

    data_points = industry_dataframe[column].values

    limit = np.max(np.abs(data_points)) * (1 + graph_padding_factor)
    plt.ylim(-limit, limit)
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.tight_layout()

    file_path = os.path.join(graph_dir, f"{column}.png")
    plt.savefig(file_path)
    plt.close()

# Finding correlations
industry_correlation_matrix = industry_dataframe.drop(
    columns=["Mkt_RF", "Term_Spread", "VIX"]
).corr()

plt.figure(figsize=(16, 12))

sns.heatmap(industry_correlation_matrix, annot=False, cmap="YlOrRd", linewidths=0.5)
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(os.path.join(graph_dir, "industry_correlation_heatmap.png"))
plt.close()

pairs = industry_correlation_matrix.unstack().sort_values(ascending=False)
strong_correlations = pairs[pairs < 1].drop_duplicates()
print(strong_correlations)
