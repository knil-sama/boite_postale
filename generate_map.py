"""
    Take a post-office box file and generate a Folium map 
"""
# -*- coding: utf-8 -*-

from pandas import DataFrame, read_csv, isnull
import folium
from io import open
from tqdm import tqdm

def main():
    """
        Main function
        1) Open boite_postale.csv file
        2) Convert to DataFrame
        3) Create folium object
        4) Create and add marker
        5) Generate map
    """
    with open("boite_postale.csv",encoding="utf-8") as boite_postale_file:
        boite_postale_dataframe = read_csv(boite_postale_file,sep=";")
    #restrain on Paris area for optimisation of display
    boite_postale_dataframe = boite_postale_dataframe[boite_postale_dataframe["co_postal"].str.startswith("75")]
    map_folium = folium.Map(location=[48.8566, 2.3522], zoom_start=12)
    for index,row in tqdm(boite_postale_dataframe.iterrows(),total=len(boite_postale_dataframe)):
        #some value can be missing
        if(isnull(row["latlong"]) == False):
            folium.Marker(location=row["latlong"].split(","),popup=row["co_mup"]).add_to(map_folium)
    map_folium.save("index.html")


if __name__ == "__main__":
    main()

