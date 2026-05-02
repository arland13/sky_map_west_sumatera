import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from astropy.coordinates import SkyCoord, EarthLocation, AltAz, get_sun, get_body
from astropy.time import Time
import astropy.units as u

# 📍 Lokasi: Sumatera Barat
location = EarthLocation(lat=-0.45 * u.deg, lon=100.60 * u.deg, height=0 * u.m)

# ⭐ Data Rasi Bintang
constellations = {
    "Crux": {"stars": SkyCoord(ra=[186.6, 191.9, 187.8, 183.8]*u.deg, dec=[-63.1, -59.7, -57.1, -58.8]*u.deg), "edges": [(0, 2), (1, 3)]},
    "Orion Belt": {"stars": SkyCoord(ra=[84.05, 83.00, 81.9]*u.deg, dec=[-1.2, -0.3, 1.9]*u.deg), "edges": [(0, 1), (1, 2)]}
}

# 🕹️ Variabel Kontrol
current_time = Time.now()
is_paused = False
time_step = 1 * u.minute # Kecepatan jalan normal

def run_realtime_sky():
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(8, 9))
    fig.subplots_adjust(top=0.82)
    
    def on_key(event):
        global is_paused, current_time
        if event.key == ' ':
            is_paused = not is_paused
        elif event.key == 'right':
            current_time += 10 * u.minute
        elif event.key == 'left':
            current_time -= 10 * u.minute

    fig.canvas.mpl_connect('key_press_event', on_key)

    def update(frame):
        global current_time
        if not is_paused:
            current_time += time_step
        
        ax.clear()
        altaz_frame = AltAz(obstime=current_time, location=location)

        # 🌌 Background & Sun Check
        sun = get_sun(current_time).transform_to(altaz_frame)
        bg_color = "#1a2a6c" if sun.alt.degree > 0 else "#000000"
        fig.patch.set_facecolor(bg_color)
        ax.set_facecolor(bg_color)

        # --- Plot Rasi ---
        for name, data in constellations.items():
            c_alt = data["stars"].transform_to(altaz_frame)
            if any(c_alt.alt.degree > 0):
                az, r = c_alt.az.radian, 90 - c_alt.alt.degree
                ax.scatter(az, r, color="white", s=30, zorder=5)
                for e in data["edges"]:
                    ax.plot([az[e[0]], az[e[1]]], [r[e[0]], r[e[1]]], color="skyblue", lw=1, alpha=0.5)

        # --- Plot Matahari & Bulan ---
        if sun.alt.degree > 0:
            ax.scatter(sun.az.radian, 90 - sun.alt.degree, color="yellow", s=300, zorder=10)
            ax.text(sun.az.radian, 90 - sun.alt.degree, " SUN", color="yellow", fontweight='bold')

        moon = get_body("moon", current_time).transform_to(altaz_frame)
        if moon.alt.degree > 0:
            ax.scatter(moon.az.radian, 90 - moon.alt.degree, color="#ecf0f1", s=150, zorder=9)
            ax.text(moon.az.radian, 90 - moon.alt.degree, " MOON", color="white")

        # 🛠️ Layout
        ax.set_ylim(0, 90)
        ax.set_theta_zero_location("N")
        ax.set_theta_direction(-1)
        ax.set_xticklabels(['U', 'TL', 'T', 'TG', 'S', 'BD', 'B', 'BL'], color="white")
        ax.grid(True, color="white", alpha=0.1)
        
        status = "PAUSED" if is_paused else "RUNNING"
        ax.set_title(f"Sky Map Sumbar ({status})\n{current_time.iso[:-7]} UTC\n[Space]: Pause | [Arrows]: Rewind/Fast-Forward", 
                     color="white", pad=40)

    ani = FuncAnimation(fig, update, interval=100, cache_frame_data=False)
    plt.show()

if __name__ == "__main__":
    run_realtime_sky()
