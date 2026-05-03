# 🌌 Real-Time Sky Map Simulation (Sumatera Barat)

This project visualizes a **real-time sky map** using Python, showing the positions of:

* 🌞 Sun
* 🌙 Moon
* ⭐ Selected constellations (Crux & Orion Belt)

The simulation is based on real astronomical calculations using `astropy`, and it updates dynamically over time.

---

## 🚀 Features

* Real-time sky movement simulation
* Interactive controls (pause, rewind, fast-forward)
* Day/night background switching
* Polar sky map (observer-based view)
* Constellation visualization with connecting lines

---

## 📦 Requirements

Install the required libraries:

```bash
pip install numpy matplotlib astropy
```

---

## ▶️ How to Run

```bash
python control_time_sky_map.py
```

The simulation window will open automatically.

---

## 🎮 Controls

| Key       | Action                    |
| --------- | ------------------------- |
| Space     | Pause / Resume simulation |
| → (Right) | Fast-forward (10 minutes) |
| ← (Left)  | Rewind (10 minutes)       |

---

## 🧭 How to Read the Sky Map

This is the **most important part** 👇

### 🌐 1. Map Projection (Polar View)

* The map is displayed in a **circular (polar) format**
* You are standing at the center, looking up at the sky

---

### 📍 2. Distance from Center = Altitude

* **Center (0 radius)** → directly overhead (**zenith**)
* **Edge (radius = 90°)** → horizon

So:

* Objects near center = high in the sky
* Objects near edge = close to horizon

---

### 🧭 3. Direction (Azimuth)

The circle represents compass directions:

| Label | Meaning         |
| ----- | --------------- |
| U     | Utara (North)   |
| T     | Timur (East)    |
| S     | Selatan (South) |
| B     | Barat (West)    |

Intermediate labels:

* TL = Timur Laut (NE)
* TG = Tenggara (SE)
* BD = Barat Daya (SW)
* BL = Barat Laut (NW)

➡️ Rotation is **clockwise**, like a compass.

---

### 🌞 4. Sun Behavior

* Appears **only when above horizon**
* Yellow dot labeled "SUN"
* Background changes:

  * 🌅 Blue → Day
  * 🌌 Black → Night

---

### 🌙 5. Moon Behavior

* Appears when above horizon
* White dot labeled "MOON"

---

### ⭐ 6. Constellations

Currently included:

* **Crux (Southern Cross)**
* **Orion Belt**

How they are shown:

* White dots = stars
* Blue lines = constellation shape

They only appear when **visible above horizon**

---

### ⏱️ 7. Time System

Displayed at top:

```
Sky Map Sumbar (RUNNING)
2026-05-03 XX:XX:XX UTC
```

* Time updates automatically
* You can control it using arrow keys

---

## 🧠 How It Works (Behind the Scenes)

* Uses `astropy` to convert:

  * Right Ascension (RA)
  * Declination (Dec)
    ➡️ into **Altitude & Azimuth** based on your location

* Location is set to:

```python
lat = -0.45
lon = 100.60
```

(Sumatera Barat)

---

## 🔧 Customization Ideas

You can extend this project by:

* Adding more constellations ⭐
* Simulating planets 🪐
* Adding star brightness (magnitude)
* Changing observer location 🌍
* Adding Milky Way background

---

## 📁 Source Code

Main script: control_time_sky_map.py

---

## 🌟 Summary

This project turns real astronomical data into an **interactive sky simulation**, helping you understand:

* How the sky moves
* Where celestial objects appear
* How to read a real sky map