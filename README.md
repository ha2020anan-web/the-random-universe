# 🌌 CosmicRNG

> A chaotic, educational, and semi-scientific random number generator powered by the cosmos.

![Banner](https://upload.wikimedia.org/wikipedia/commons/9/9c/ESO_-_Milky_Way.jpg)

---

## 🚀 Overview

**CosmicRNG** is a Python-based experimental random number generator that derives entropy from astronomical data such as:

- 🌙 Moon position & distance  
- ☀️ Sun position  
- 🪐 Planetary distances (Mars, Venus, Mercury, Pluto…)  
- 🌌 Celestial mechanics via Skyfield  
- ⚡ Bitwise transformations of space-time data  

It is designed for **educational purposes, experimentation, and fun**, not cryptographic security.

---

## ⚠️ Disclaimer

> This project is NOT cryptographically secure.

CosmicRNG should NOT be used for:
- OTP systems 🔐  
- Password generation 🔑  
- Security tokens  
- Financial or production systems  

This is purely a **cosmic experiment + learning project**.

---

## 🧠 How It Works

CosmicRNG collects real astronomical data using:

:contentReference[oaicite:0]{index=0}

Then transforms it into numerical entropy.

### Pipeline:

1. Fetch celestial positions
2. Compute distances between Earth and bodies
3. Normalize values into integers
4. Combine using bitwise operations
5. Hash or mix final entropy

---

## 🌍 Data Sources

CosmicRNG uses real astronomical computations:

- Planet ephemeris (NASA JPL data)
- Moon orbital position
- Solar reference frame
- Pluto barycenter approximation

---

## 🪐 Example Output

```text
Cosmic Entropy Seed: 83910293810293
Random Value: 7
