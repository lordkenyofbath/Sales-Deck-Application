import streamlit as st

# --- Configuration (Minimalist Aesthetic) ---
# Define colors and fonts to maintain the "Minimalist, Professional" look
PRIMARY_DARK = "#1A202C"  # Deep Charcoal
ACCENT_BLUE = "#10497E"   # Dark, Professional Blue
OFF_WHITE = "#F8F8F8"     # Off-White/Light Gray

st.set_page_config(
    page_title="Veritas Analytics Sales Deck",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for Minimalist, Harvard-Style Aesthetic
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Lora:wght@600;700&family=Inter:wght@300;400;700&display=swap');
    
    html, body, [class*="stApp"], .main {{
        font-family: 'Inter', sans-serif;
        background-color: {OFF_WHITE};
        color: {PRIMARY_DARK};
    }}
    h1, h2, h3, .lora {{
        font-family: 'Lora', serif !important;
        color: {PRIMARY_DARK};
    }}
    .accent-blue {{ color: {ACCENT_BLUE}; }}
    .stButton>button {{
        background-color: {ACCENT_BLUE};
        color: white;
        border-radius: 9999px;
        padding: 0.75rem 2rem;
        font-weight: 700;
    }}
    /* Hide Streamlit Header/Footer */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    </style>
""", unsafe_allow_html=True)


# --- 1. SLIDE: The Hook / The Unspoken Problem ---
st.markdown("## 1. The Unspoken Problem", unsafe_allow_html=True)

col1, col2 = st.columns([1, 2])

with col1:
    st.markdown(f'<p class="text-xl text-gray-500 mb-4 lora">The Unspoken Problem</p>', unsafe_allow_html=True)
    
    # The dramatic statistic is key to the Hook
    st.markdown(f"""
        <h1 class="text-8xl font-extrabold tracking-tight lora leading-none accent-blue">85%</h1>
        <h3 class="text-4xl font-light mt-4">of valuable data is never acted upon.</h3>
    """, unsafe_allow_html=True)
    
with col2:
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.image("https://placehold.co/600x400/F8F8F8/1A202C?text=Minimalist+Visual+Metaphor", use_column_width=True)
    st.markdown(f'<p class="text-sm mt-2 text-gray-400">A potential $1.2M in missed opportunity per mid-market client.</p>', unsafe_allow_html=True)


st.markdown("---") # Visual separator between slides

# --- 2. SLIDE: The Conflict / The Status Quo Friction ---
st.markdown("## 2. The Status Quo Friction", unsafe_allow_html=True)

st.markdown(f"""
    <div style='text-align: center;'>
        <p class="text-xl text-gray-500 mb-4 lora">The Status Quo Friction</p>
        <h2 class="text-5xl font-bold mb-12 lora">Data Complexity Creates <span class="accent-blue">Analysis Paralysis.</span></h2>
    </div>
""", unsafe_allow_html=True)

col3, col4, col5 = st.columns(3)

with col3:
    st.markdown(f"""
        <div style="text-align: center; padding: 10px;">
            <span style="font-size: 48px;" role="img" aria-label="Labyrinth Icon">🌀</span>
            <p class="text-lg font-semibold" style="color:{PRIMARY_DARK};">DATA VELOCITY</p>
            <p class="text-sm text-gray-500">Too fast, too hard to process.</p>
        </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
        <div style="text-align: center; padding: 10px;">
            <span style="font-size: 48px;" role="img" aria-label="Wall of Data Icon">🧱</span>
            <p class="text-lg font-semibold" style="color:{PRIMARY_DARK};">DATA VOLUME</p>
            <p class="text-sm text-gray-500">Too much noise, no signal.</p>
        </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown(f"""
        <div style="text-align: center; padding: 10px;">
            <span style="font-size: 48px;" role="img" aria-label="Disconnected Icon">🔗</span>
            <p class="text-lg font-semibold" style="color:{PRIMARY_DARK};">DATA VARIETY</p>
            <p class="text-sm text-gray-500">Disparate sources, zero cohesion.</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")


# --- 3. SLIDE: The Climax / The Veritas Clarity (Solution) ---
st.markdown("## 3. The Veritas Clarity", unsafe_allow_html=True)

st.markdown(f"""
    <div style='text-align: center;'>
        <p class="text-xl text-gray-500 mb-4 lora">The Veritas Clarity</p>
        <h2 class="text-5xl font-extrabold tracking-tight lora mb-8 accent-blue">
            We Translate Complexity into Actionable Intelligence.
        </h2>
    </div>
""", unsafe_allow_html=True)

col6, col7 = st.columns([1, 1])

with col6:
    # Visual Metaphor of Clarity (Replicating the bar chart metaphor from HTML)
    st.markdown(f"""
        <div style="height: 250px; background-color: white; border: 1px solid #ddd; border-radius: 8px; padding: 15px; display: flex; align-items: flex-end; justify-content: space-around;">
            <div style="width: 15%; height: 50%; background-color: {PRIMARY_DARK}; border-radius: 4px;"></div>
            <div style="width: 15%; height: 30%; background-color: {PRIMARY_DARK}; border-radius: 4px;"></div>
            <div style="width: 15%; height: 90%; background-color: #2ECC71; border-radius: 4px; box-shadow: 0 0 10px {ACCENT_BLUE};"></div>
            <div style="width: 15%; height: 60%; background-color: {PRIMARY_DARK}; border-radius: 4px;"></div>
        </div>
        <p style="text-align: center; margin-top: 10px; font-weight: bold; color: {ACCENT_BLUE};">SIGNAL</p>
    """, unsafe_allow_html=True)

with col7:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"""
        <p class="text-lg mt-8 text-gray-600">
            We use proprietary models to cut through the data noise, isolating the single, highest-value action your executive team needs to take right now.
        </p>
        <ul style="list-style-type: disc; margin-left: 20px; padding-top: 15px;">
            <li>**Filter:** Remove 95% of irrelevant data.</li>
            <li>**Focus:** Deliver one clear recommendation.</li>
            <li>**Forecast:** Project ROI within 90 days.</li>
        </ul>
    """, unsafe_allow_html=True)

st.markdown("---")


# --- 4. SLIDE: The Resolution / The Future State (CTA) ---
st.markdown("## 4. The Future State", unsafe_allow_html=True)

st.markdown(f"""
    <div style='text-align: center; padding-top: 20px;'>
        <p class="text-xl text-gray-500 mb-4 lora">The Future State</p>
        <h2 class="text-6xl font-bold tracking-tighter mb-8 lora">
            Insight. Confidence. <span class="accent-blue">Growth.</span>
        </h2>
        
        <div style="max-width: 600px; margin: 30px auto; text-align: left; padding: 20px; background-color: white; border-left: 8px solid {ACCENT_BLUE}; box-shadow: 0 4px 6px rgba(0,0,0,0.1); border-radius: 4px;">
            <p class="text-2xl italic text-gray-600 leading-relaxed">
                "Veritas helped us move beyond reporting and into strategic forecasting."
            </p>
            <p class="text-base font-semibold mt-4 text-primary-dark">- Placeholder Client Testimonial</p>
        </div>
        
        <br>
        <br>
        
    </div>
""", unsafe_allow_html=True)

st.button("Ready to simplify your strategy? Let's connect.")

st.markdown("<br><br><br>", unsafe_allow_html=True)
