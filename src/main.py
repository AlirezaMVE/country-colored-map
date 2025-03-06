import geopandas as gpd
import matplotlib.pyplot as plt
import os
import requests

def draw_asia_map(shapefile_path):
    """Draw the map of Asia with Iran highlighted."""
    if not os.path.exists(shapefile_path):
        raise FileNotFoundError(f"Shapefile not found: {shapefile_path}")
    
    try:
        # Load the world map data
        world = gpd.read_file(shapefile_path)
    except Exception as e:
        raise RuntimeError(f"Error reading shapefile: {e}")

    # Inspect the columns of the shapefile
    print("Columns in the shapefile:", world.columns)

    # List of Asian countries
    asian_countries = [
        'Afghanistan', 'Armenia', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Bhutan', 
        'Brunei', 'Cambodia', 'China', 'Cyprus', 'Georgia', 'India', 'Indonesia', 
        'Iran', 'Iraq', 'Israel', 'Japan', 'Jordan', 'Kazakhstan', 'Kuwait', 
        'Kyrgyzstan', 'Laos', 'Lebanon', 'Malaysia', 'Maldives', 'Mongolia', 
        'Myanmar', 'Nepal', 'North Korea', 'Oman', 'Pakistan', 'Palestine', 
        'Philippines', 'Qatar', 'Saudi Arabia', 'Singapore', 'South Korea', 
        'Sri Lanka', 'Syria', 'Tajikistan', 'Thailand', 'Timor-Leste', 'Turkey', 
        'Turkmenistan', 'United Arab Emirates', 'Uzbekistan', 'Vietnam', 'Yemen'
    ]

    # Filter for Asia
    asia = world[world['ADMIN'].isin(asian_countries)]

    # Create a plot
    fig, ax = plt.subplots(figsize=(15, 10))

    # Draw the map of Asia
    asia.plot(ax=ax, color='white', edgecolor='black')

    # Highlight Iran
    iran = asia[asia['ADMIN'] == 'Iran']
    iran.plot(ax=ax, color='lightgreen', edgecolor='red', linewidth=2)

    # Set title and show the plot
    ax.set_title('Map of Asia with Iran Highlighted')
    plt.show()

if __name__ == "__main__":
    shapefile_path = 'E:/university/term8/mabahes/asia-map-project/data/ne_110m_admin_0_countries.shp'
    try:
        draw_asia_map(shapefile_path)
    except Exception as e:
        print(f"An error occurred: {e}")
