
'''
The following is the main plot py script to show the probability cloud for the
solution of the wave equation for an electron with no potential energy.

This script takes the colors given by .py, colors that represent either low, mid
or high probability for that point in space

We use montecarlo simulation approach, since we are dealing with finite numbers
'''
import streamlit as st
import numpy as np
import plotly.graph_objects as go
import config
import waveec as we

#We have N numbers of points for each R3 axis, so in total we have N points in R3

N = config.N
L = config.L
#We define the total space in each axis, given an interval, we randomize N numbers in between

@st.cache_data                       #<-------- This for streamlit use
def generate_points(N, L):
    x = np.random.uniform(-L, L, N)
    y = np.random.uniform(-L, L, N)
    z = np.random.uniform(-L, L, N)
    return x, y, z

x, y, z = generate_points(N, L)



#Now we define a finite number of t values, I build it as scalable integers, so
#we need both, a range of t integers between 0 and Tn, and a scale s

Tn = config.Tn
s = config.s
T = [t*s for t in range(0, Tn)]  #<-------- This for streamlit use
st.title("Quantum Probability Cloud")  
# At the end, we will have Tn number of total frames

frames = []

'''
Now we do calculate now the psi value for each point, at each time, filling the
frames array with them, we plot each point x,y,z normal, but the collor changes
acording to the psi value
'''
for t in T:
  
  psi = we.ProbPsi(x,y,z,t)

  frames.append(go.Frame(
      data=[go.Scatter3d(
          x=x,
          y=y,
          z=z,
          customdata=psi,
          mode='markers',
          marker=dict(
              size=2,
              color=psi,
              colorscale='Turbo',
              opacity=0.8
          ),
          hovertemplate=(
                "x: %{x}<br>"
                "y: %{y}<br>"
                "z: %{z}<br>"
                "ψ: %{customdata}<extra></extra>"
            )
      )],
      name=str(t)
  ))


'''
Now we have 'each' frame in the frames array, we are left with defining the
initial frame to show, and creating the time slide
'''
#First, the inital frame

fig = go.Figure(
    data=frames[0].data,
    frames = frames
)
#Then, the slider, we are redrawing the plot each time t changes
steps = []
for i, t in enumerate(T):
    steps.append(dict(
        method="animate",
        args=[[str(t)], {"frame": {"duration": 0, "redraw": True}}],
        label=str(t)
    ))


#final config to plot

fig.update_layout(
    paper_bgcolor="black",
    scene=dict(
        bgcolor="black",
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        zaxis=dict(visible=False),
    ),
    sliders=[dict(
        active=0,
        currentvalue={"prefix": 's ='+str(s)+' t ='},
        steps=steps
    )]
)

#fig.show()                                       #<-------- This for general plotly use

st.plotly_chart(fig, use_container_width=True)   #<-------- This for streamlit use
