#/usr/bin/env python3

import cartopy.crs as ccrs
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import shapefile
import geopandas
from shapely.geometry import Polygon
from shapely.ops import cascaded_union, unary_union


class prout():
    def __init__(self):
        pass


if __name__ == '__main__':

    import math

    def lambert932WGPS(lambertE, lambertN):

        class constantes:
            GRS80E = 0.081819191042816
            LONG_0 = 3
            XS = 700000
            YS = 12655612.0499
            n = 0.7256077650532670
            C = 11754255.4261

        delX = lambertE - constantes.XS
        delY = lambertN - constantes.YS
        gamma = math.atan(-delX / delY)
        R = math.sqrt(delX * delX + delY * delY)
        latiso = math.log(constantes.C / R) / constantes.n
        sinPhiit0 = math.tanh(latiso + constantes.GRS80E * math.atanh(constantes.GRS80E * math.sin(1)))
        sinPhiit1 = math.tanh(latiso + constantes.GRS80E * math.atanh(constantes.GRS80E * sinPhiit0))
        sinPhiit2 = math.tanh(latiso + constantes.GRS80E * math.atanh(constantes.GRS80E * sinPhiit1))
        sinPhiit3 = math.tanh(latiso + constantes.GRS80E * math.atanh(constantes.GRS80E * sinPhiit2))
        sinPhiit4 = math.tanh(latiso + constantes.GRS80E * math.atanh(constantes.GRS80E * sinPhiit3))
        sinPhiit5 = math.tanh(latiso + constantes.GRS80E * math.atanh(constantes.GRS80E * sinPhiit4))
        sinPhiit6 = math.tanh(latiso + constantes.GRS80E * math.atanh(constantes.GRS80E * sinPhiit5))

        longRad = math.asin(sinPhiit6)
        latRad = gamma / constantes.n + constantes.LONG_0 / 180 * math.pi

        longitude = latRad / math.pi * 180
        latitude = longRad / math.pi * 180

        return longitude, latitude

    from pyensae import download_data

    try:
        download_data("GEOFLA_2-1_DEPARTEMENT_SHP_LAMB93_FXX_2015-12-01.7z",
                      website="https://wxs-telechargement.ign.fr/oikr5jryiph0iwhw36053ptm/telechargement/inspire/" + \
                              "GEOFLA_THEME-DEPARTEMENTS_2015_2$GEOFLA_2-1_DEPARTEMENT_SHP_LAMB93_FXX_2015-12-01/file/")
    except Exception as e:
        # au cas le site n'est pas accessible
        download_data("GGEOFLA_2-1_DEPARTEMENT_SHP_LAMB93_FXX_2015-12-01.7z", website="xd")

    from pyquickhelper.filehelper import un7zip_files
    try:
        un7zip_files("GEOFLA_2-1_DEPARTEMENT_SHP_LAMB93_FXX_2015-12-01.7z", where_to="shapefiles")
        departements = 'shapefiles\\GEOFLA_2-1_DEPARTEMENT_SHP_LAMB93_FXX_2015-12-01\\GEOFLA\\1_DONNEES_LIVRAISON_2015\\' + \
                       'GEOFLA_2-1_SHP_LAMB93_FR-ED152\\DEPARTEMENT\\DEPARTEMENT.shp'
    except FileNotFoundError as e:
        # Il est possible que cette instruction ne fonctionne pas.
        # Dans ce cas, on prendra une copie de ce fichier.
        import warnings
        warnings.warn("Plan B parce que " + str(e))
        download_data("DEPARTEMENT.zip")
        departements = "DEPARTEMENT.shp"

#    if not os.path.exists(departements):
#        raise FileNotFoundError("Impossible de trouver '{0}'".format(departements))

    from cartopy.feature import NaturalEarthFeature, COLORS
    resolution = "50m"
    BORDERS = NaturalEarthFeature('cultural', 'admin_0_boundary_lines_land',
                                  resolution, edgecolor='black', facecolor='none')
    STATES = NaturalEarthFeature('cultural', 'admin_1_states_provinces_lakes',
                                 resolution, edgecolor='black', facecolor='none')
    COASTLINE = NaturalEarthFeature('physical', 'coastline', resolution,
                                    edgecolor='black', facecolor='none')
    LAKES = NaturalEarthFeature('physical', 'lakes', resolution,
                                edgecolor='face',
                                facecolor=COLORS['water'])
    LAND = NaturalEarthFeature('physical', 'land', resolution,
                               edgecolor='face',
                               facecolor=COLORS['land'], zorder=-1)
    OCEAN = NaturalEarthFeature('physical', 'ocean', resolution,
                                edgecolor='face',
                                facecolor=COLORS['water'], zorder=-1)
    RIVERS = NaturalEarthFeature('physical', 'rivers_lake_centerlines', resolution,
                                 edgecolor=COLORS['water'],
                                 facecolor='none')

    projection = ccrs.PlateCarree()
    fig = plt.figure(figsize=(12, 12))
    ax = fig.add_subplot(1, 1, 1, projection=projection)
    ax.add_feature(BORDERS)
    ax.add_feature(LAKES)
    ax.add_feature(LAND)
    ax.add_feature(OCEAN)
    ax.add_feature(RIVERS)
    ax.add_feature(COASTLINE)
    ax.set_extent([-5, 12, 40, 54])
    ax.set_title("Europe")
    ax.gridlines(crs=projection, draw_labels=True,
                 linewidth=2, color='gray', alpha=0.5, linestyle='--')

    print('----'*10)
    print(departements)
    print('----'*10)

    #shp = departements
    shp = "/home/emeric/Desktop/GJ_GrandDebat/shapefiles/GEOFLA_2-1_DEPARTEMENT_SHP_LAMB93_FXX_2015-12-01/GEOFLA/1_DONNEES_LIVRAISON_2015/GEOFLA_2-1_SHP_LAMB93_FR-ED152/DEPARTEMENT/DEPARTEMENT.shp"
    r = shapefile.Reader(shp)
    shapes = r.shapes()
    records = r.records()

    polys = []
    for i, (record, shape) in enumerate(zip(records, shapes)):
        # les coordonnées sont en Lambert 93
        if i == 0:
            print(record, shape.parts)
        geo_points = [lambert932WGPS(x,y) for x, y in shape.points]
        if len(shape.parts) == 1:
            # Un seul polygone
            poly = Polygon(geo_points)
        else:
            # Il faut les fusionner.
            ind = list(shape.parts) + [len(shape.points)]
            pols = [Polygon(geo_points[ind[i]:ind[i+1]]) for i in range(0, len(shape.parts))]
            try:
                poly = unary_union(pols)
            except Exception as e:
                print("Cannot merge: ", record)
                print([_.length for _ in pols], ind)
                poly = Polygon(geo_points)
        polys.append(poly)

    data = geopandas.GeoDataFrame(geometry=polys)
    # cmap -> voir https://matplotlib.org/users/colormaps.html
    data.plot(ax=ax, cmap='tab20', edgecolor='black');
    # Ou pour définir des couleurs spécifiques.
    # geopandas.plotting.plot_polygon_collection(ax, data['geometry'], facecolor=data['colors'], values=None)
    plt.show()
