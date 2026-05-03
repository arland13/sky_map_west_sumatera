import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from astropy.coordinates import SkyCoord, EarthLocation, AltAz, get_sun, get_body
from astropy.time import Time
import astropy.units as u

# 📍 Lokasi: Sumatera Barat
location = EarthLocation(lat=-0.45 * u.deg, lon=100.60 * u.deg, height=0 * u.m)

# ⭐ Data Rasi Bintang (expanded)
constellations = {
    "Crux": {
        "stars": SkyCoord(
            ra=[186.6, 191.9, 187.8, 183.8]*u.deg,
            dec=[-63.1, -59.7, -57.1, -58.8]*u.deg
        ),
        "edges": [(0, 2), (1, 3)]
    },

    "Orion": {
        "stars": SkyCoord(
            ra=[83.8, 78.6, 88.8, 81.3, 84.0, 85.2, 86.9]*u.deg,
            dec=[-5.4, -8.2, 7.4, 6.3, -1.2, -0.3, 1.9]*u.deg
        ),
        "edges": [(0,1), (1,2), (2,3), (3,0), (4,5), (5,6)]
    },

    "Scorpius": {
        "stars": SkyCoord(
            ra=[247.3, 241.4, 239.7, 252.5, 263.4]*u.deg,
            dec=[-26.4, -22.6, -19.8, -34.0, -37.1]*u.deg
        ),
        "edges": [(0,1), (1,2), (2,3), (3,4)]
    },

    "Ursa Major": {
        "stars": SkyCoord(
            ra=[165, 165, 178, 183, 193, 200, 210]*u.deg,
            dec=[56, 61, 53, 57, 55, 60, 54]*u.deg
        ),
        "edges": [(0,1), (1,2), (2,3), (3,4), (4,5), (5,6)]
    },

    "Cassiopeia": {
        "stars": SkyCoord(
            ra=[10, 20, 30, 40, 50]*u.deg,
            dec=[60, 58, 62, 59, 61]*u.deg
        ),
        "edges": [(0,1), (1,2), (2,3), (3,4)]
    }
}

# 🌟 Generate background stars
num_stars = 1000
star_ra = np.random.uniform(0, 360, num_stars) * u.deg
star_dec = np.random.uniform(-90, 90, num_stars) * u.deg
star_coords = SkyCoord(ra=star_ra, dec=star_dec)

# brightness simulation
star_sizes = np.random.uniform(1, 6, num_stars)

# 🕹️ Control variables
current_time = Time.now()
is_paused = False
time_step = 1 * u.minute


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

        # 🌞 Sun (for day/night)
        sun = get_sun(current_time).transform_to(altaz_frame)
        is_day = sun.alt.degree > 0

        bg_color = "#1a2a6c" if is_day else "#000000"
        fig.patch.set_facecolor(bg_color)
        ax.set_facecolor(bg_color)

        # 🌌 Background stars (only visible at night)
        if not is_day:
            bg_altaz = star_coords.transform_to(altaz_frame)

            visible = bg_altaz.alt.degree > 0
            az = bg_altaz.az.radian[visible]
            r = 90 - bg_altaz.alt.degree[visible]

            ax.scatter(
                az,
                r,
                s=star_sizes[visible],
                color="white",
                alpha=0.6,
                zorder=1
            )

        # ⭐ Constellations
        for name, data in constellations.items():
            c_alt = data["stars"].transform_to(altaz_frame)

            visible = c_alt.alt.degree > 0
            if any(visible):
                az = c_alt.az.radian
                r = 90 - c_alt.alt.degree

                ax.scatter(az, r, color="white", s=40, zorder=5)

                for e in data["edges"]:
                    ax.plot(
                        [az[e[0]], az[e[1]]],
                        [r[e[0]], r[e[1]]],
                        color="cyan",
                        lw=1.5,
                        alpha=0.7
                    )

                # label
                ax.text(
                    np.mean(az),
                    np.mean(r),
                    f" {name}",
                    color="lightblue",
                    fontsize=8
                )

        # 🌞 Sun
        if sun.alt.degree > 0:
            ax.scatter(sun.az.radian, 90 - sun.alt.degree,
                       color="yellow", s=300, zorder=10)
            ax.text(sun.az.radian, 90 - sun.alt.degree,
                    " SUN", color="yellow", fontweight='bold')

        # 🌙 Moon
        moon = get_body("moon", current_time).transform_to(altaz_frame)
        if moon.alt.degree > 0:
            ax.scatter(moon.az.radian, 90 - moon.alt.degree,
                       color="#ecf0f1", s=150, zorder=9)
            ax.text(moon.az.radian, 90 - moon.alt.degree,
                    " MOON", color="white")

        # 🧭 Layout
        ax.set_ylim(0, 90)
        ax.set_theta_zero_location("N")
        ax.set_theta_direction(-1)
        ax.set_xticklabels(['U', 'TL', 'T', 'TG', 'S', 'BD', 'B', 'BL'], color="white")
        ax.grid(True, color="white", alpha=0.1)

        status = "PAUSED" if is_paused else "RUNNING"

        ax.set_title(
            f"Sky Map Sumbar ({status})\n"
            f"{current_time.iso[:-7]} UTC\n"
            "[Space]: Pause | [← →]: Time Control",
            color="white",
            pad=40
        )

    ani = FuncAnimation(fig, update, interval=100, cache_frame_data=False)
    plt.show()


if __name__ == "__main__":
    run_realtime_sky()