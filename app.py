import plotly.graph_objects as go
import plotly.io as pio
import pandas as pd 
import chart_studio.tools as tls
import chart_studio.plotly as py

#hide the plotly logo
config = {'displaylogo': False}

#Create Dataframe for the visuals
df = pd.read_excel("/Users/niqtoliver/Desktop/ACES/aces_household_challenges_visualization/data.xlsx", sheet_name="Sheet1")


fig = go.Figure()
fig.add_trace(go.Bar(
        x=df.data_values,
        y=df.breakdown[0:3],
        orientation="h",
        ))

fig.update_traces( selector=dict(type='bar'))


cols =["data_values"]

statewide = [list(df[item][0:4]) for item in cols]
asian = [list(df[item][4:8])  for item in cols]
black = [list(df[item][8:12])  for item in cols]
hispa = [list(df[item][12:16])  for item in cols]
white = [list(df[item][16:20])  for item in cols]
female = [list(df[item][20:24])  for item in cols]
male = [list(df[item][24:28])  for item in cols]
lgbt = [list(df[item][28:32])  for item in cols]
unsure = [list(df[item][32:36])  for item in cols]
hetero = [list(df[item][36:40])  for item in cols]

# Chart should display only the chart for the specified button, and can toggle between other charts, going back to the original 
dropdown1 =  dict(method = "update", 
                args = [{'x': statewide}],
                label = "Statewide")

dropdown2 =  dict(method = "update",
                args = [{'x': asian}],
                label = "Asian")

dropdown3 =  dict(method = "update",
                args = [{'x': black}],
                label = "Black")

dropdown4 =  dict(method = "update",
                args = [{'x': hispa}],
                label = "Hispanic")

dropdown5 =  dict(method = "update",
                args = [{'x': white}],
                label = "White")

dropdown6 =  dict(method = "update",
                args = [{'x': female}],
                label = "Female")
dropdown7 =  dict(method = "update",
                args = [{'x': male}],
                label = "Male")

dropdown8 =  dict(method = "update",
                args = [{'x': lgbt}],
                label = "Gay/Lesbian/Bisexual")

dropdown9 =  dict(method = "update",
                args = [{'x': unsure}],
                label = "Unsure")

dropdown10 =  dict(method = "update",
                args = [{'x': hetero}],
                label = "Heterosexual")

fig.update_layout(height=450,bargap=0.2, title="Child Abuse", title_x=0.5,
                  updatemenus=[dict(active=0,
                                    buttons=[dropdown1, dropdown2, dropdown3, dropdown4,
                                             dropdown5, dropdown6, dropdown7 ,dropdown8 ,
                                             dropdown9, dropdown10])
                               
                              ])

# fig.show(config=config)

# fig.write_html("index.html", auto_open=True)

pio.write_html(fig, config=config, file='index.html', auto_open=True)