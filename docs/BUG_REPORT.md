# Bug Reports

This document contains bugs and known issues identified during manual testing of the Flash Card Learning App.

**Application:** Flash Card Learning App  
**Version:** 1.0  
**Tester:** Muhammad Ali Turdiyev

---

# BUG-001 – Application crashes when questions.csv is missing

**Severity:** High  
**Priority:** High  
**Status:** Open

### Preconditions
- Delete or rename `questions.csv`.

### Steps to Reproduce
1. Run `main.py`.

### Expected Result
The application should display a user-friendly error message explaining that the CSV file could not be found.

### Actual Result
The application terminates with a Python traceback (`FileNotFoundError`).

---

# BUG-002 – Application crashes if CSV format is invalid

**Severity:** High  
**Priority:** High  
**Status:** Open

### Preconditions
- Modify `questions.csv`.
- Remove one required column (A, B, C, D or Correct).

### Steps to Reproduce
1. Save the modified CSV.
2. Run the application.

### Expected Result
The application should notify the user that the CSV format is invalid.

### Actual Result
The application crashes with an exception.

---

# BUG-003 – Fixed total question count

**Severity:** Medium  
**Priority:** Medium  
**Status:** Open

### Steps to Reproduce
1. Create a CSV file containing fewer or more than 100 questions.
2. Launch the application.

### Expected Result
The question counter should display:

Question X / Total Questions

Example:

Question 4 / 25

### Actual Result
The application always displays:

Question X / 100

---

# BUG-004 – No restart option after quiz completion

**Severity:** Medium  
**Priority:** Medium  
**Status:** Open

### Steps to Reproduce
1. Complete all quiz questions.

### Expected Result
The user should be able to restart the quiz without restarting the application.

### Actual Result
Only "Quiz Finished!" is displayed and answer buttons disappear.

---

# BUG-005 – Application does not support empty CSV file

**Severity:** High  
**Priority:** Medium  
**Status:** Open

### Preconditions
Replace `questions.csv` with an empty file.

### Steps to Reproduce
1. Run the application.

### Expected Result
Display a message such as:

"No questions available."

### Actual Result
Application crashes while attempting to load the first question.

---

# BUG-006 – No confirmation before closing application

**Severity:** Low  
**Priority:** Low  
**Status:** Open

### Steps to Reproduce
1. Start the quiz.
2. Close the application window.

### Expected Result
Application asks:

"Are you sure you want to exit?"

### Actual Result
Application closes immediately.

---

# BUG-007 – Quiz progress is not saved

**Severity:** Low  
**Priority:** Low  
**Status:** Open

### Steps to Reproduce
1. Answer several questions.
2. Close the application.
3. Launch it again.

### Expected Result
Application resumes previous progress or provides an option to continue.

### Actual Result
Quiz always starts from the beginning.

---

# BUG-008 – Duplicate answers may confuse users

**Severity:** Low  
**Priority:** Medium  
**Status:** Open

### Preconditions
Create a question where two answer options contain identical text.

### Steps to Reproduce
1. Launch the application.
2. Open the duplicated question.

### Expected Result
Application should uniquely identify answers.

### Actual Result
Duplicate answer text may confuse users.

---

# BUG-009 – No validation of CSV content

**Severity:** Medium  
**Priority:** Medium  
**Status:** Open

### Steps to Reproduce
1. Insert blank cells into the CSV.
2. Launch the application.

### Expected Result
Application should report invalid question data.

### Actual Result
Blank buttons or unexpected behavior may occur.

---

# BUG-010 – Accuracy value updates only after answering

**Severity:** Low  
**Priority:** Low  
**Status:** Closed

### Steps to Reproduce
1. Launch the application.

### Expected Result
Accuracy starts at 0%.

### Actual Result
Works correctly.

### Resolution
Verified during testing. No defect found.

---

# Bug Summary

| ID | Title | Severity | Status |
|----|----------|----------|--------|
| BUG-001 | Missing CSV crashes application | High | Open |
| BUG-002 | Invalid CSV format crashes application | High | Open |
| BUG-003 | Fixed question count (100) | Medium | Open |
| BUG-004 | No restart feature | Medium | Open |
| BUG-005 | Empty CSV crashes application | High | Open |
| BUG-006 | No exit confirmation | Low | Open |
| BUG-007 | Quiz progress is not saved | Low | Open |
| BUG-008 | Duplicate answer text issue | Low | Open |
| BUG-009 | No CSV validation | Medium | Open |
| BUG-010 | Initial accuracy display | Low | Closed |

---

**Testing Type:** Manual Functional Testing

**Environment**
- Windows 11
- Python 3.14
- Tkinter
- Pandas
- CSV data source