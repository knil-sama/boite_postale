"""
    Take a post-office box file and generate a Folium map 
"""
# -*- coding: utf-8 -*-

from pandas import DataFrame, read_csv, isnull
import folium
from folium.plugins import MarkerCluster
from io import open

MARKER_CLUSTER = MarkerCluster()

def create_single_marker(row):
    address = " ".join([row["VA_NO_VOIE"], row["LB_EXTENSION"], row["LB_VOIE_EXT"]])
    content_popup = "adresse : %s" % address
    # need to create a different icon for each marker
    icon = folium.features.CustomIcon(
        "https://raw.githubusercontent.com/knil-sama/boite_postale/master/small_boite_aux_lettres_cropped.png",
        icon_size=(28, 28),
    )
    folium.Marker(
        location=row["Latlong"].split(","), icon=icon, popup=content_popup
    ).add_to(MARKER_CLUSTER)


def main():
    """
        Main function
        1) Open boite_postale.csv file
        2) Convert to DataFrame
        3) Create folium object
        4) Create and add marker
        5) Generate map
    """
    with open("boite_postale.csv", encoding="utf-8") as boite_postale_file:
        boite_postale_dataframe = read_csv(boite_postale_file, sep=";", dtype="str")
    # restrain on Paris area for optimisation of display
    boite_postale_dataframe = boite_postale_dataframe[
        boite_postale_dataframe["CO_POSTAL"].str.startswith("75")
    ]
    boite_postale_dataframe.fillna(
        value={"VA_NO_VOIE": "", "LB_EXTENSION": "", "LB_VOIE_EXT": ""}, inplace=True
    )
    map_folium = folium.Map(location=[48.8566, 2.3522], zoom_start=12)
    # remove missing coordinates
    boite_postale_dataframe = boite_postale_dataframe[
        ~isnull(boite_postale_dataframe.Latlong)
    ]
    boite_postale_dataframe.apply(create_single_marker, axis="columns")
    map_folium.add_child(MARKER_CLUSTER)
    map_folium.save("build/index.html")


if __name__ == "__main__":
    main()
