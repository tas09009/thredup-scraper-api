import glob
import pandas as pd
import os, re



file_name = "coats"
# product = '61% Cotton, 36% Acrylic, 3% Other'


df = pd.read_csv(f'/home/taniya/Projects/thredup-scraper-api/data/test_runs/merged_{file_name}.csv')
df_materials_banned = ~df.Materials.str.contains("Polyester|Polyamide|Polyethylene|Polymide|Acrylic|Synthetic|No Fabric Content")
df_materials_banned_removed = df[df_materials_banned]
df_materials_banned_removed.to_csv(f'/home/taniya/Projects/thredup-scraper-api/data/test_runs/clean_{file_name}.csv', index=False)

