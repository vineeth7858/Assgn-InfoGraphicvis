import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


def format_plot(ax, color):
    """
    Formats the appearance of a matplotlib plot by customizing borders and ticks.

    Parameters:
    - ax (matplotlib.axes.Axes): The axes object to be formatted.
    - color (str): The color for the plot borders and ticks.

    Returns:
    None

    """
    # Add border and set ticks inside
    for spine in ax.spines.values():
        spine.set_edgecolor(color)
        spine.set_linewidth(2)
    
    ax.tick_params(direction='in', length=6, width=2)


# Read and prepare data
df_bar = pd.read_csv('Carrier.csv')
df_bar = df_bar.set_index('Country Name').transpose().reset_index()
df_bar.rename(columns={'index': 'Year', 'United Kingdom': 'Departures'}, 
              inplace=True)
df_bar['Year'] = df_bar['Year'].astype(str)

df_area = pd.read_csv('Elec_Cons.csv')

df_radar = pd.read_csv('PortTraffic.csv')
yrs_radar = df_radar['Year'].astype(str).tolist()
d_rad = df_radar['Data'].tolist()
a_rad = np.linspace(0, 2 * np.pi, len(d_rad), endpoint=False)
a_rad = a_rad.tolist()
d_rad += d_rad[:1]
a_rad += a_rad[:1]
df_line = pd.read_csv('Broadband.csv')
df_line.set_index('Country Name', inplace=True)
df_line = df_line.T

# Define color scheme
color_bar = 'lightpink'  
color_area_fill = 'lightblue'  
color_area_line = '#3182bd'  
color_radar_fill = '#74c476'
color_radar_line = '#31a354'
color_line = '#6baed6' 
background_color = 'lightblue'

# Create figure and GridSpec layout
fig = plt.figure(figsize=(20, 24))
gs = gridspec.GridSpec(5, 2, height_ratios=[3, 3, 3, 2, 1])

# Main title
plt.suptitle(
    "Analyzing the Impact on UK's Energy Consumption, Air Travel, and Trade (1970-2022)",
    fontsize=25, fontweight='bold', y=0.96, color='blue')

# Bar Chart for Air Transport
p0 = plt.subplot(gs[0, :])
p0.bar(df_bar['Year'], df_bar['Departures'], color=color_bar)
p0.set_title('Air Transport, Registered Carrier Departures Worldwide (United Kingdom)',
              fontsize=18, fontweight='bold', pad=20)
p0.set_xlabel('Year', fontsize=14, fontweight='bold')
p0.set_ylabel('Departures', fontsize=14, fontweight='bold')
p0.grid(axis='y', linestyle='--', alpha=0.7)

# Area chart for Electricity Consumption
p1 = plt.subplot(gs[1, 0])
p1.fill_between(df_area['Year'], df_area['Data'], color=color_area_fill, alpha=0.4)
p1.plot(df_area['Year'], df_area['Data'], color=color_area_line, alpha=0.6)
p1.set_title('Electric Power Consumption (kWh per capita) Over Years',
              fontsize=18, fontweight='bold', pad=20)
p1.set_xlabel('Year', fontsize=14, fontweight='bold')
p1.set_ylabel('Electric Power Consumption (kWh per capita)',
               fontsize=14, fontweight='bold')
p1.grid(True)

# Radar chart for Port Traffic
p2 = plt.subplot(gs[1, 1], polar=True)
p2.fill(a_rad, d_rad, color=color_radar_fill, alpha=0.25)
p2.plot(a_rad, d_rad, color=color_radar_line, linewidth=2)
p2.set_xticks(a_rad[:-1])
p2.set_xticklabels(yrs_radar)
p2.set_title('Container Port Traffic (TEU: 20 foot equivalent units)',
              fontsize=18, fontweight='bold', pad=20)

# Line plot for Broadband Subscriptions
p3 = plt.subplot(gs[2, :])
p3.plot(df_line.index, df_line.iloc[:, 0], color=color_line, linewidth=3)
p3.set_title('Fixed Broadband Subscriptions in the United Kingdom (per 100 people)',
              fontsize=18, fontweight='bold', pad=20)
p3.set_xlabel('Year', fontsize=14, fontweight='bold')
p3.set_ylabel('Subscriptions per 100 people', fontsize=14, fontweight='bold')

# Format each plot
format_plot(p1, 'black')
format_plot(p2, 'black')
format_plot(p3, 'black')
format_plot(p0, 'black')

# Adjust space between plots
plt.subplots_adjust(wspace=10, hspace=10)

# Set background color for the entire figure
fig.patch.set_facecolor(background_color)

# Enhance X-ticks
for idx in [p1, p2, p3, p0]:
    idx.tick_params(axis='x', labelsize=12)
    idx.tick_params(axis='y', labelsize=12)
    for label in idx.get_xticklabels():
        label.set_fontweight('bold')

# Text block setup
summarytext = plt.subplot(gs[3, :])
summarytext.axis('off')
summarycontent = (
    "• Electric power consumption per capita in the UK increased by approximately "
    "162.87% over the time span provided, which does not align with the 31.31% decrease "
    "in air carrier departures from 1970 to 2020, indicating other factors may have "
    "influenced the rise in energy use.\n"
    "• The massive increase in broadband subscriptions by 46,059.71% from 2000 to 2022 "
    "suggests a shift toward digital services, which may contribute to more energy-efficient "
    "consumption patterns and a reduced growth rate in per capita energy use.\n"
    "• The 44.12% rise in port traffic from 2000 to 2020 implies growing global trade "
    "activities, which generally drive up energy demand, reflecting a possible correlation "
    "with the increased energy consumption over the same period.\n"
    "• The surge in digital connectivity, as shown by the growth in broadband subscriptions, "
    "could be inversely related to the 31.31% decrease in air travel, as enhanced online "
    "communication might reduce the necessity for travel."
)

summarytext.text(0, 0.5, summarycontent,
             ha='left', va='center', fontsize=25, color='blue', wrap=True)

# Add name and ID
studentdtls = plt.subplot(gs[4, :])
studentdtls.axis('off')
studentdtls.text(0.95, 0.5, "Name:Naredla Vineeth Kumar \n ID:22091863 ", ha="right", fontsize=18, fontweight = 'bold', color='blue')

# Adjust layout
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()