
# Filter by Fabrics
def filter():
    df = pd.read_csv(f'/home/taniya/Projects/thredup-scraper-api/data/test_runs/merged_{file_name}.csv')
    df_materials_banned = ~df.Materials.str.contains("Polyester|Polyamide|Polyethylene|Acrylic|No Fabric Content")
    df_materials_banned_removed = df[df_materials_banned]
    df_materials_banned_removed.to_csv(f'/home/taniya/Projects/thredup-scraper-api/data/test_runs/clean_{file_name}.csv', index=False)