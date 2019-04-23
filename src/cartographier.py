#/usr/bin/env python3

import re
import os
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
        # Let's keep some useful directory names
        self.data_dir = 'data'

    def lambert932WGPS(self, lambertE, lambertN):
        """
        Convert some gographical units.
        Stolen from a website I didn't remember ..
        """

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
        The folder we want is then :
        shapefiles\\GEOFLA_2-1_DEPARTEMENT_SHP_LAMB93_FXX_2015-12-01\\GEOFLA\\1_DONNEES_LIVRAISON_2015\\GEOFLA_2-1_SHP_LAMB93_FR-ED152\\DEPARTEMENT
        The content of this folder has to be copied to a "shapefile" folder on the base_dir
        """
        try:
            download_data('GEOFLA_2-1_DEPARTEMENT_SHP_LAMB93_FXX_2015-12-01.7z', website='https://wxs-telechargement.ign.fr/oikr5jryiph0iwhw36053ptm/telechargement/inspire/GEOFLA_THEME-DEPARTEMENTS_2015_2$GEOFLA_2-1_DEPARTEMENT_SHP_LAMB93_FXX_2015-12-01/file/')
        except Exception as e:
            download_data('GGEOFLA_2-1_DEPARTEMENT_SHP_LAMB93_FXX_2015-12-01.7z', website='foobar')

    def draw_french_map(self, theme):
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

        # Get departments shape
        shape_file = os.path.join(self.data_dir, 'shapefile', 'DEPARTEMENT.shp')
        shape_data = shapefile.Reader(shape_file)
        shapes = shape_data.shapes()
        records = shape_data.records()

        # Get some lists for plotting
        polys = list()
        departments_order = list()

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
        data = geopandas.GeoDataFrame(geometry=polys)

        # Now we gonna set colors regarding the number of participants for each category of the debate
        with open('{}/departments.json'.format(os.path.join(self.data_dir, theme)), 'r') as handler:
            seen_departments = json.loads(handler.read())

        # And we plot all that. Colors are mapped by the 'value' field
        geopandas.plotting.plot_polygon_collection(
            ax,
            data['geometry'],
            color=None,
            values=[seen_departments[departement] if departement in seen_departments.keys() else 0 for departement in departments_order],
            cmap='YlOrBr')

        # Save figure
        plt.title(theme.replace('_', ' '))
        plt.savefig(os.path.join('maps', '{}.png'.format(theme)))

        return os.path.join('maps', '{}.png'.format(theme))
