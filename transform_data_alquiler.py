import pandas as pd
import distance
from collections import defaultdict

#madrid open datasets use Windows encoding (mbcs)
polygon_df = pd.read_csv("./data/shapefiles/Districts/900FAULURU/PolygonConverted.csv", sep=',', encoding = "mbcs")
polygon_df = polygon_df[polygon_df["DESBDT"].str[:3] == "079"]
districts = pd.Series(polygon_df["DESBDT"].unique())
districts = districts.map(lambda x: x.encode('utf-8'))
polygon_df.to_csv("./data/shapefiles/Districts/900FAULURU/PolygonConverted_transformed.csv", sep=',', index=False, encoding="utf-8")


price_df = pd.read_csv("./data/historico-precios-alquiler.csv", sep=',', decimal=',')
price_df.rename(columns = {"distrito" : "District"}, inplace = True)
price_df.drop(["2q 2006", "4q 2006"], axis=1, inplace = True)
price_df.iloc[:,1:] = price_df.iloc[:,1:].astype(float)
price_df.insert(0, "Country", "Spain")
price_df.insert(1, "City", "Madrid")

lev_pairs = {}
for dis in price_df["District"]:
    lev = float("inf")
    join_name = dis
    for dis_join in districts:
        #perform levenshtein ignoring the first 6 positions (corresponding to the numeric code), and up to the length of the original string since some are compound names (e.g.:Moncloa should match Moncloa-Aravaca)
        new_lev = distance.levenshtein(dis,dis_join[7:7+len(dis)])
        if new_lev < lev:
            lev = new_lev
            join_name = dis_join
    lev_pairs[dis] = join_name

price_df.insert(3, "District_join", "")
price_df["District_join"] = price_df["District"].map(lambda x: lev_pairs[x])

year_col_idx = defaultdict(list)
init_year_idx = 4
col_list = price_df.columns.values.tolist()[init_year_idx:]
enum_col_list = enumerate(col_list)
for x,y in enum_col_list:
    year_col_idx[y[-4:]].append(x + init_year_idx)

col_idx_delete = []
for key in sorted(year_col_idx):
    values = year_col_idx[key]
    col_idx_delete += values
    price_df[key] = price_df.iloc[:, values].mean(axis = 1)

price_df.drop(price_df.columns[col_idx_delete], axis=1, inplace = True)

transformed_col_names = map(lambda x: x[-4:], col_list)
transformed_col_names = list(set(transformed_col_names))
transformed = pd.melt(price_df, id_vars=["Country","City","District","District_join"], value_vars=sorted(transformed_col_names), var_name="Year", value_name="Price/m2")

transformed.to_csv("./data/historic_rent_price.csv", sep=',', index=False, decimal=',')
