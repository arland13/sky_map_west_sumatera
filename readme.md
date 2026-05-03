# 🌌 Real-Time Sky Map Simulation (Sumatera Barat)

This project visualizes a **real-time sky map** using Python, showing the positions of:

* 🌞 Sun
* 🌙 Moon
* ⭐ Constellations (Crux, Orion, Scorpius, Ursa Major, Cassiopeia)
* 🌌 Background stars (1000+ randomly generated stars)

The simulation is powered by real astronomical calculations using `astropy`, and it updates dynamically over time.

---

## 🚀 Features

* 🌌 Dense **realistic night sky** (1000+ stars)
* ⭐ Multiple **real constellations**
* 🌞 Automatic **day/night switching**
* 🌙 Real-time **Moon position**
* 🧭 Observer-based sky (horizon → zenith)
* 🎮 Interactive controls (pause, rewind, fast-forward)
* 🏷 Constellation labels

---

## 📦 Requirements

Install dependencies:

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

| Key   | Action                    |
| ----- | ------------------------- |
| Space | Pause / Resume simulation |
| →     | Fast-forward (10 minutes) |
| ←     | Rewind (10 minutes)       |

---

## 🧭 How to Read the Sky Map

This is the **most important part** 👇

---

### 🌐 1. Map Projection (Polar View)

* The sky is drawn in a **circular (polar) format**
* You are standing at the center, looking upward

---

### 📏 2. Distance from Center = Altitude (0° → 90°)

This is one of the most important concepts in the sky map.

The circular map shows how **high an object is in the sky**, measured in **degrees (°)**.

#### 🌐 Altitude Scale

| Altitude | Meaning                                       |
| -------- | --------------------------------------------- |
| 0°       | On the horizon (edge of the map)              |
| 45°      | Halfway up the sky                            |
| 90°      | Directly overhead (zenith, center of the map) |

---

#### 🎯 How It Works in the Map

* The **center of the circle** represents **90° (zenith)**
* The **edge of the circle** represents **0° (horizon)**

So:

* Objects **near the center** → high in the sky
* Objects **near the edge** → close to the horizon

---

#### 🔄 Why It Looks "Flipped"

In the code, altitude is converted like this:

```python
r = 90 - altitude
```

This is done so that:

* Higher altitude → closer to center
* Lower altitude → closer to edge

---

#### 🌍 Real-World Intuition

Imagine standing outside:

* Looking straight ahead → **0° (horizon)**
* Looking halfway up → **~45°**
* Looking straight up → **90° (zenith)**

This map is a **top-down view of your sky**, as if you're lying on the ground looking upward.

---

#### ⚠️ Important Note

Only objects with:

```python
altitude > 0°
```

are shown.

This means:

* You only see objects **above the horizon**
* Objects below the horizon are hidden

---

#### 🌌 Quick Visual Guide

```
        90° (Zenith)
          ●
       60°   60°
     30°       30°
   0°-----------0°  (Horizon)
```

---

### 🧭 3. Direction (Azimuth)

| Label | Meaning         |
| ----- | --------------- |
| U     | Utara (North)   |
| T     | Timur (East)    |
| S     | Selatan (South) |
| B     | Barat (West)    |

Intermediate directions:

* TL = Timur Laut (NE)
* TG = Tenggara (SE)
* BD = Barat Daya (SW)
* BL = Barat Laut (NW)

➡️ Rotation is **clockwise**, like a compass.

---

### 🌞 4. Day vs Night

* 🌅 **Blue background** → daytime (Sun above horizon)
* 🌌 **Black background** → nighttime (stars visible)

---

### 🌙 5. Moon

* Appears only when above horizon
* Shown as a white point labeled `"MOON"`

---

### ⭐ 6. Stars & Constellations

There are **two types of stars**:

#### 🌌 Background Stars

* Small white dots
* Randomly distributed across the sky
* Simulate a realistic star field

#### ⭐ Constellation Stars

* Larger white dots
* Connected with cyan lines
* Labeled with constellation names

---

### ⏱️ 7. Time System

Displayed at the top:

```
Sky Map Sumbar (RUNNING)
2026-05-03 XX:XX:XX UTC
```

* Time updates continuously
* Can be controlled using arrow keys

---

## 🧠 How It Works (Behind the Scenes)

The simulation uses astronomical coordinate transformations:

### Step 1 — Fixed Sky Coordinates

* Right Ascension (RA)
* Declination (Dec)

### Step 2 — Convert to Observer View

Using `astropy`:

```python
SkyCoord → AltAz
```

This converts positions based on:

* Time
* Observer location

---

### 🌍 Observer Location

```python
lat = -0.45
lon = 100.60
```

This represents **Sumatera Barat, Indonesia**.

---

## 🔧 Customization

### 🌍 Change Location

```python
EarthLocation(lat=..., lon=...)
```

---

### 🌌 Increase Star Density

```python
num_stars = 1000
```

Try:

* 2000 → denser sky
* 5000 → very rich sky

---

### ⏱ Change Simulation Speed

```python
time_step = 1 * u.minute
```

---

## 🚀 Future Improvements

* ⭐ Real star catalog (Hipparcos / Gaia)
* 🪐 Planets (Mars, Jupiter, Venus)
* 🌌 Milky Way rendering
* 🌗 Moon phases
* 🌆 Light pollution simulation
* 🎨 Magnitude-based brightness

---

## 📁 Source Code

Main script:

```
control_time_sky_map.py
```

---

## 🌟 Summary

This project is a **mini planetarium simulation** built with Python.

It helps you understand:

* How the sky moves over time
* How celestial coordinates work
* How to read a real sky map

---

## 👨‍💻 Author

Created by **Arland**
