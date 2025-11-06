# HOW TO USE THIS SYSTEM MONITOR TOOL (C++ Version)

A complete setup & usage guide for anyone who wants to run this project on their own system.

---

## ✅ 1. Install Ubuntu / WSL2 (if on Windows)

If you are using Windows:
1. Open Microsoft Store  
2. Install **Ubuntu**  
3. Launch it  
4. Update packages:

```
sudo apt update && sudo apt upgrade -y
```

---

## ✅ 2. Install Git

```
sudo apt install git -y
```

---

## ✅ 3. Clone the Project

```
git clone https://github.com/Iamsunilmishra/system-monitor-tool.git
cd system-monitor-tool
```

---

## ✅ 4. Install C++ Compiler (g++)

```
sudo apt install g++ -y
```

---

## ✅ 5. Compile the System Monitor Tool

```
g++ src/system_monitor.cpp -o monitor
```

---

## ✅ 6. Run the System Monitor

```
./monitor
```

This displays:
- ✅ CPU Usage  
- ✅ RAM Usage  
- ✅ Disk Usage  
Updated every 2 seconds.

---


## ✅ 7. View Screenshots (Optional)

Screenshots of the tool are in the `screenshots/` folder.

---

## ✅ 8. View Project Report (Optional)

Open:

```
Project_Report.pdf
```

This contains:
- System Design  
- Code Explanation  
- Screenshots  
- Conclusion  

---

## ✅ DONE ✅

You now have the System Monitor Tool running successfully on your machine.
