#include <iostream>
#include <fstream>
#include <unistd.h>
#include <string>
using namespace std;

float getCPUUsage() {
    static long prevIdle = 0, prevTotal = 0;

    ifstream statFile("/proc/stat");
    string cpu;
    long user, nice, system, idle, iowait, irq, softirq;
    statFile >> cpu >> user >> nice >> system >> idle >> iowait >> irq >> softirq;
    statFile.close();

    long idleTime = idle + iowait;
    long totalTime = user + nice + system + idle + iowait + irq + softirq;

    long diffIdle = idleTime - prevIdle;
    long diffTotal = totalTime - prevTotal;

    prevIdle = idleTime;
    prevTotal = totalTime;

    return (1.0 - (float)diffIdle / diffTotal) * 100.0;
}

float getMemoryUsage() {
    ifstream memFile("/proc/meminfo");
    string label;
    long total, free, buffers, cached;

    memFile >> label >> total;
    memFile >> label >> free;
    memFile >> label >> buffers;
    memFile >> label >> cached;

    long used = total - free - buffers - cached;
    return (used * 100.0) / total;
}

float getDiskUsage() {
    system("df -h / > disk.txt");
    ifstream disk("disk.txt");

    string line;
    getline(disk, line);
    getline(disk, line);

    string fs, size, used, avail, percent, mount;
    disk >> fs >> size >> used >> avail >> percent >> mount;

    percent.pop_back(); // remove %

    return stoi(percent);
}

int main() {
    while (true) {
        cout << "CPU Usage: " << getCPUUsage() << "%\n";
        cout << "RAM Usage: " << getMemoryUsage() << "%\n";
        cout << "Disk Usage: " << getDiskUsage() << "%\n";
        cout << "-------------------------------\n";
        sleep(2);
    }
}
