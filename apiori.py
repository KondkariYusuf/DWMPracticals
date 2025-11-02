import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# Step 1: Create sample transactions
dataset = [
    ['Milk','Bread','Butter'],
    ['Milk','Bread'],
    ['Milk','Cookies'],
    ['Bread','Butter'],
    ['Milk','Bread','Butter','Cookies']
]

# Step 2: Convert to one-hot encoded DataFrame
from mlxtend.preprocessing import TransactionEncoder
te = TransactionEncoder()
te_data = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_data, columns=te.columns_)
print("Dataset:\n", df)

# Step 3: Apply Apriori
frequent = apriori(df, min_support=0.4, use_colnames=True)
print("\nFrequent Itemsets:\n", frequent)

# Step 4: Generate Association Rules
rules = association_rules(frequent, metric="confidence", min_threshold=0.6)
print("\nAssociation Rules:\n", rules[['antecedents','consequents','support','confidence','lift']])
