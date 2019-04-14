#/usr/bin/env python3

import re
import json
import math
import shapefile
import geopandas
import cartopy.crs as ccrs
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from pyensae import download_data
from shapely.geometry import Polygon
from matplotlib.colors import Normalize
from pyquickhelper.filehelper import un7zip_files
from matplotlib.collections import LineCollection
from shapely.ops import cascaded_union, unary_union
from cartopy.feature import NaturalEarthFeature, COLORS


class CARTOGRAPHIER(object):
    """"""

    def __init__(self):
        pass

    def lambert932WGPS(self, lambertE, lambertN):
        """"""

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


    def download_french_department_shape(self):
        """
        Will download data about geometric shape of French states.
        The result is manually extracted.
        It returns the absolute path of the .shp file.
        """

        # Download
        try:
            download_data('GEOFLA_2-1_DEPARTEMENT_SHP_LAMB93_FXX_2015-12-01.7z', website='https://wxs-telechargement.ign.fr/oikr5jryiph0iwhw36053ptm/telechargement/inspire/GEOFLA_THEME-DEPARTEMENTS_2015_2$GEOFLA_2-1_DEPARTEMENT_SHP_LAMB93_FXX_2015-12-01/file/')
        except Exception as e:
            download_data('GGEOFLA_2-1_DEPARTEMENT_SHP_LAMB93_FXX_2015-12-01.7z', website='foobar')

        # Extract
        try:
            un7zip_files("GEOFLA_2-1_DEPARTEMENT_SHP_LAMB93_FXX_2015-12-01.7z", where_to="shapefiles")
            departements = 'shapefiles\\GEOFLA_2-1_DEPARTEMENT_SHP_LAMB93_FXX_2015-12-01\\GEOFLA\\1_DONNEES_LIVRAISON_2015\\GEOFLA_2-1_SHP_LAMB93_FR-ED152\\DEPARTEMENT\\DEPARTEMENT.shp'
        except FileNotFoundError as e:
            download_data("DEPARTEMENT.zip")
            departements = "DEPARTEMENT.shp"

        return '/home/emeric/Desktop/GJ_GrandDebat/shapefiles/GEOFLA_2-1_DEPARTEMENT_SHP_LAMB93_FXX_2015-12-01/GEOFLA/1_DONNEES_LIVRAISON_2015/GEOFLA_2-1_SHP_LAMB93_FR-ED152/DEPARTEMENT/DEPARTEMENT.shp'



    def draw_french_map(self):
        """"""

        # Download natural features of France (rivers, mountains, etc)
        resolution = "50m"
        BORDERS = NaturalEarthFeature('cultural', 'admin_0_boundary_lines_land', resolution, edgecolor='black', facecolor='none')
        STATES = NaturalEarthFeature('cultural', 'admin_1_states_provinces_lakes', resolution, edgecolor='black', facecolor='none')
        COASTLINE = NaturalEarthFeature('physical', 'coastline', resolution, edgecolor='black', facecolor='none')
        LAKES = NaturalEarthFeature('physical', 'lakes', resolution, edgecolor='face', facecolor=COLORS['water'])
        LAND = NaturalEarthFeature('physical', 'land', resolution, edgecolor='face', facecolor=COLORS['land'], zorder=-1)
        OCEAN = NaturalEarthFeature('physical', 'ocean', resolution, edgecolor='face', facecolor=COLORS['water'], zorder=-1)
        RIVERS = NaturalEarthFeature('physical', 'rivers_lake_centerlines', resolution, edgecolor=COLORS['water'], facecolor='none')

        # Project these data as basemap
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
        ax.set_title('French map')
        ax.gridlines(crs=projection, draw_labels=True, linewidth=2, color='gray', alpha=0.5, linestyle='--')

        # Get departments shape
        shape_file = self.download_french_department_shape()
        shape_data = shapefile.Reader(shape_file)
        shapes = shape_data.shapes()
        records = shape_data.records()

        # Get some lists for plotting
        polys = list()
        departments_order = list()
        departments_count = list()

        # Draw each as a polygon
        for i, (record, shape) in enumerate(zip(records, shapes)):
            departments_order.append(record[1])
            # Lambert93 coodinates
            geo_points = [self.lambert932WGPS(x,y) for x, y in shape.points]
            if len(shape.parts) == 1:
                poly = Polygon(geo_points)
            else:
                # Fusion polygons if many
                ind = list(shape.parts) + [len(shape.points)]
                pols = [Polygon(geo_points[ind[i]:ind[i+1]]) for i in range(0, len(shape.parts))]
                try:
                    poly = unary_union(pols)
                except Exception as e:
                    print('Merging polygon error: {} ({})'.format(record, e))
                    print([_.length for _ in pols], ind)
                    poly = Polygon(geo_points)
            polys.append(poly)

        # Now we gonna set colors regarding the number of participants for each category of the debate
        with open('data/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS/departments.json', 'r') as handler:
            seen_departments = json.loads(handler.read())
        for departement in departments_order:
            # Get the number of time each has been seen
            try:
                departments_count.append(seen_departments[departement])
            except KeyError:
                departments_count.append(0)

        # Now map colors to values
        colors = list()
        min_count = min(departments_count)
        max_count = max(departments_count)
        norm = Normalize(vmin=min_count, vmax=max_count, clip=True)
        mapper = cm.ScalarMappable(norm=norm, cmap=cm.Greys)

        for value in departments_count:
            colors.append(mapper.to_rgba(value))

        data = geopandas.GeoDataFrame(geometry=polys)
        # cmap -> voir https://matplotlib.org/users/colormaps.html
        #data.plot(ax=ax, cmap='tab20', edgecolor='black');
        # Ou pour définir des couleurs spécifiques.

#        A VERIFIER, LE COUNT EST CHELOU
#        plt.close()
#        plt.bar(departments_order, departments_count)
#        plt.show()
#        exit(0)

        geopandas.plotting.plot_polygon_collection(
            ax,
            data['geometry'],
            facecolor=colors,
            values=None)
        plt.show()


if __name__ == '__main__':
    A = CARTOGRAPHIER()
    A.draw_french_map()
