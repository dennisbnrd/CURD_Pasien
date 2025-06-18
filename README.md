# Sistem Reservasi CRUD Pasien Rumah Sakit
This system is a simple Python-based application used to manage patient data, reservations, and doctor schedules. It runs on a terminal/command-line interface (CLI) and uses list and dictionary-based data structures.

## Business Understanding
Managing patient records, doctor schedules, and medical appointments is critical for ensuring efficient operations in hospitals and clinics. Many small- to medium-sized healthcare providers still rely on manual systems, which are prone to human error, delays, and data inconsistency. This project aims to simulate a basic hospital information system using Python, designed to improve operational workflows by digitizing:
- Patient Data Management: Storing and updating patient personal information in a structured format, with input validation to maintain data integrity.
- Reservation System: Allowing patients to book, view, or cancel reservations based on available doctors and schedules, reducing miscommunication and overlapping appointments.
- Doctor Scheduling: Letting administrators easily manage doctor availability by day and specialization, making it easier to match patients with the right doctors.

This system is especially useful for:
- Demonstrating CRUD (Create, Read, Update, Delete) logic in a real-world context
- Training or prototyping before implementing a full-stack hospital information system
- Educational purposes to understand how health records and scheduling work together
By streamlining core hospital functions with this CLI system, healthcare facilities can reduce clerical workload, minimize errors, and deliver a more organized service to patients.

## Features
The Hospital Information System includes the following core features:
### Patient Management
- Add new patient records with ID, name, gender, age, address, and phone number
- Update existing patient details with input validation
- Delete patient records (with confirmation prompt)
- Automatically removes related reservations when a patient is deleted
- Display patient data in a clear tabular format

### Reservation Management
- Patients can create new reservations by selecting:
  - Symptoms/complaints
  - Date of appointment
  - Doctor and treatment type (Inpatient/Outpatient)
- Automatically assigns room for inpatients and placeholder for outpatients
- Modify reservation details (symptoms, date, doctor, room)
- Delete reservations (individually or all at once with confirmation)
- Show reservation data in tabulated format

###  Doctor Schedule Management
- Add new doctors with their specialization and working days
- Prevent duplicate doctor entries
- Delete doctor schedules with confirmation
- View all current doctor schedules in a tabular list

## Installation
Follow these steps to set up and run the Hospital Information System on your local machine:
### 1. Requirements
Python 3.6 or above must be installed
