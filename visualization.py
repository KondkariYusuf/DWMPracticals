import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create sample data
data = {'Student': ['A','B','C','D','E','F','G','H','I','J'],
        'Marks': [45, 67, 89, 55, 72, 34, 90, 60, 78, 50]}
df = pd.DataFrame(data)
print("Original Data:\n", df)

# Step 2: Discretization (Equal Width Binning)
df['Grade'] = pd.cut(df['Marks'], bins=5, labels=['F','D','C','B','A'])
print("\nAfter Discretization:\n", df)

# Step 3: Visualization
plt.figure(figsize=(6,4))
plt.bar(df['Student'], df['Marks'], color='skyblue')
plt.title("Student Marks Visualization")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.show()
