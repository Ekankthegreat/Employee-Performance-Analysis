# Email: 24f1001581@ds.study.iitm.ac.in

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set seed for reproducibility
np.random.seed(42)

# Generate synthetic dataset
departments = ["Sales", "HR", "Finance", "IT", "Operations", "Marketing"]
regions = ["North America", "Latin America", "Europe", "Asia Pacific", "Africa"]

data = {
    "employee_id": [f"EMP{i:03d}" for i in range(1, 101)],
    "department": np.random.choice(departments, 100),
    "region": np.random.choice(regions, 100),
    "performance_score": np.random.uniform(60, 95, 100).round(2),
    "years_experience": np.random.randint(1, 20, 100),
    "satisfaction_rating": np.random.uniform(2.5, 5.0, 100).round(1)
}

df = pd.DataFrame(data)

# Save dataset
df.to_csv("employee_data.csv", index=False)

# ✅ Frequency count for Operations department
ops_count = df[df["department"] == "Operations"].shape[0]
print("Frequency count for Operations department:", ops_count)

# ✅ Histogram of departments
plt.figure(figsize=(8, 6))
sns.histplot(df["department"], discrete=True, palette="Set2")
plt.title("Employee Distribution by Department")
plt.xlabel("Department")
plt.ylabel("Count")
plt.tight_layout()

# Save chart
plt.savefig("chart.png", dpi=100)

# ✅ Generate HTML report
html_output = f"""
<html>
<head><title>Employee Performance Visualization</title></head>
<body>
<h2>Employee Distribution Analysis</h2>
<p><b>Email:</b> 24f1001581@ds.study.iitm.ac.in</p>
<p>Frequency count for Operations department: {ops_count}</p>
<img src="chart.png" alt="Histogram">
</body>
</html>
"""

with open("employee_analysis.html", "w") as f:
    f.write(html_output)
