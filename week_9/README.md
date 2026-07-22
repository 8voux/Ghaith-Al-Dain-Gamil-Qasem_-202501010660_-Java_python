# IT Helpdesk Ticket Registration System

## Purpose of the Application

This application is a simple IT Helpdesk Ticket Registration System developed using Python modules. It allows users to register an IT support ticket by entering their information, issue details, location, and priority level. The system automatically assigns a technician based on the selected priority and displays the completed helpdesk ticket.

---

## Tech Stack

- Programming Language: Python 3
- IDE: Visual Studio Code / GitHub Codespaces
- Modules:
  - main.py
  - ticket.py
  - display.py

---

## How to Use

1. Open the project in Visual Studio Code or GitHub Codespaces.
2. Run the `main.py` file.
3. Enter:
   - Student Name
   - Student ID
   - Issue
   - Location
   - Priority (High/Medium/Low)
4. The program will:
   - Assign a technician automatically.
   - Display the completed helpdesk ticket.

Technician Assignment:
- High → Ahmad
- Medium → Siti
- Low → Ali

---

## Demonstration

Example Input

```
Student Name: Ghaith
Student ID: 202501010660
Issue: Blue screen PC
Location: Lab 101 Level 1
Priority: High
```

Example Output

```
========== HELPDESK TICKET ==========
Student Name : Ghaith
Student ID   : 202501010660
Issue        : Blue screen PC
Location     : Lab 101 Level 1
Priority     : High
Technician   : Ahmad
Status       : Pending
====================================
```

---

![all text .](demo.gif)