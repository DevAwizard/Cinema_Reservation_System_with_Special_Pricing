[![Progress](https://img.shields.io/badge/Progress-In%20Progress-yellow)](https://github.com/DevAwizard/Exams_42) 

![cinema reservation system](https://github.com/user-attachments/assets/596af58a-814e-4756-a4a9-61e3c9f79bb6)


<div align="center">
<h1>🎬 Cinema Seat Reservation System Documentation</h1>
<img src="https://img.shields.io/badge/python-%233776AB.svg?&style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/markdown-%23000000.svg?&style=for-the-badge&logo=markdown&logoColor=white" />
<img src="https://img.shields.io/badge/visual%20studio%20code-%23007ACC.svg?&style=for-the-badge&logo=visual%20studio%20code&logoColor=white" />
</div>

Welcome to my **first Python project**! 🎉 This project simulates a cinema seat reservation system, with the goal of applying the basics of Python programming. It combines object-oriented principles with a user-friendly interface for managing seat reservations, pricing, and discounts. Through this project, I aim to reinforce fundamental Python concepts like classes, objects, and basic operations.



### 📑 **Table of Contents**
1. [Project Overview](#project-overview)
2. [Core Components](#core-components)
   - [Seat Management](#seat-management)
   - [Pricing Structure](#pricing-structure)
   - [Validation & Exception Handling](#validation-exception-handling)
   - [Code Organization](#code-organization)


### 🎬 **Project Overview**
<a name="project-overview"></a>

This project simulates a digital cinema seat management system that allows users to reserve seats, manage prices, and apply discounts. The system is built using object-oriented programming principles for scalability and flexibility. As my **first Python project**, I focused on applying the basics of Python, including classes, methods, and attributes, while adhering to good programming practices.


### 🪑 **Core Components**
<a name="core-components"></a>

#### 1. **Seat Management**:
<a name="seat-management"></a>

- The **Seat** class 🛋️ represents individual cinema seats with attributes such as:
  - `numero`: Seat number.
  - `fila`: Seat row.
  - `reservado`: Reservation status (True/False).
  - `precio`: Seat price, which varies based on the day and viewer's age.

- The **CinemaHall** class 🎥 manages a collection of seats and supports the following actions:
  - **Add a Seat** ➕: Add a new seat to the hall, ensuring no duplicates.
  - **Reserve a Seat** 📅: Change a seat’s status to reserved and assign the appropriate price.
  - **Cancel a Reservation** ❌: Reset a seat to available status when a reservation is canceled.
  - **Display Seats** 👀: List all seats with their reservation status and applied prices (including discounts).
  - **Search for a Seat** 🔍: Find a seat based on its number or row.



#### 2. **💲 Pricing Structure**:
<a name="pricing-structure"></a>

- **Base Price**: Set a standard ticket price for general viewers. 🎟️
- **Discounted Wednesday Pricing**: Apply a 20% discount on Wednesdays to celebrate the moviegoer’s day! 🤑
- **Senior Citizen Discount**: Offer a 30% discount for viewers aged 65 or older. 👵👴

#### 3. **⚙️ Validation & Exception Handling**:
<a name="validation-exception-handling"></a>

- **Seat Validation** ✅: Ensure valid seat numbers and rows for smooth seat management.
- **Discount Eligibility** 🎉: Validate viewer age and the current day to apply discounts correctly.
- **Error Prevention** 🚫: Prevent duplicate bookings and ensure cancellations are only allowed for reserved seats.


#### 4. **📚 Code Organization**:
<a name="code-organization"></a>

- All attributes are **private** and accessed through getters and setters to ensure encapsulation. 🔒
- Methods are designed to be **modular**, promoting clean, organized, and reusable code. 🔄
- The system follows best practices by **avoiding global variables**. 🛡️










---
