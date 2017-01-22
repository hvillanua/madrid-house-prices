import pandas as pd

price_df = pd.read_csv("./data/prices_per_year.csv", sep=',')
transformed = pd.melt(price_df, id_vars=["Country","City","District","Neighborhood","Neighborhood_lookup","Subdivision","Lat","Lon"], value_vars=["2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016"], var_name="Year", value_name="Price/m2")
transformed.to_csv("./data/prices_per_year_transformed.csv", sep=',', index=False)
