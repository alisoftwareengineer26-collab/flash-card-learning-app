# Manual Test Cases

This document contains manual test cases for the Flash Card Learning App.

**Application:** Flash Card Learning App  
**Version:** 1.0  
**Tester:** Muhammad Ali Turdiyev

---

## TC-001 – Launch Application

**Precondition:** Application files are available.

**Steps:**
1. Run `main.py`.

**Expected Result:**
- Application launches successfully.
- First question is displayed.
- Four answer buttons are visible.

**Status:** PASS

---

## TC-002 – Load Questions from CSV

**Precondition:** `questions.csv` contains valid data.

**Steps:**
1. Launch the application.

**Expected Result:**
- A question is loaded from the CSV file.
- Four answer options are displayed.

**Status:** PASS

---

## TC-003 – Select Correct Answer

**Precondition:** Quiz has started.

**Steps:**
1. Click the correct answer.

**Expected Result:**
- Selected button turns green.
- Correct score increases by one.
- Accuracy updates.
- Next question appears after approximately one second.

**Status:** PASS

---

## TC-004 – Select Incorrect Answer

**Precondition:** Quiz has started.

**Steps:**
1. Click an incorrect answer.

**Expected Result:**
- Selected button turns red.
- Correct answer is highlighted in green.
- Wrong score increases by one.
- Next question appears after approximately one second.

**Status:** PASS

---

## TC-005 – Prevent Multiple Answers

**Precondition:** Quiz has started.

**Steps:**
1. Click any answer.
2. Immediately try clicking another answer.

**Expected Result:**
- Only the first click is accepted.
- Remaining buttons are disabled.

**Status:** PASS

---

## TC-006 – Verify Question Counter

**Precondition:** Quiz has started.

**Steps:**
1. Answer several questions.

**Expected Result:**
Question counter updates correctly.

Example:
- Question 1/100
- Question 2/100
- Question 3/100

**Status:** PASS

---

## TC-007 – Verify Score Counter

**Precondition:** Quiz has started.

**Steps:**
1. Answer questions with both correct and incorrect answers.

**Expected Result:**
Correct and Wrong counters update after every question.

**Status:** PASS

---

## TC-008 – Verify Accuracy Calculation

**Precondition:** Quiz has started.

**Steps:**
1. Answer multiple questions.
2. Compare displayed accuracy with manual calculation.

**Expected Result:**
Accuracy percentage is calculated correctly.

**Status:** PASS

---

## TC-009 – Verify Question Randomization

**Precondition:** Application is closed.

**Steps:**
1. Launch the application.
2. Note the first few questions.
3. Close the application.
4. Launch again.

**Expected Result:**
Questions appear in a different order.

**Status:** PASS

---

## TC-010 – Verify Answer Randomization

**Precondition:** Quiz has started.

**Steps:**
1. Observe the position of the correct answer.
2. Restart the application several times.

**Expected Result:**
Answer positions change between runs.

**Status:** PASS

---

## TC-011 – Verify Correct Answer Highlight

**Precondition:** Quiz has started.

**Steps:**
1. Select an incorrect answer.

**Expected Result:**
Correct answer is highlighted in green.

**Status:** PASS

---

## TC-012 – Verify Button Color Reset

**Precondition:** Answer one question.

**Steps:**
1. Wait until the next question appears.

**Expected Result:**
All buttons return to their default color.

**Status:** PASS

---

## TC-013 – Verify End of Quiz

**Precondition:** Last question is displayed.

**Steps:**
1. Answer the final question.

**Expected Result:**
- "Quiz Finished!" message is displayed.
- Answer buttons disappear.

**Status:** PASS

---

## TC-014 – Verify Application Stability

**Precondition:** Quiz has started.

**Steps:**
1. Complete the entire quiz.

**Expected Result:**
Application finishes without crashing or freezing.

**Status:** PASS

---

## TC-015 – Verify CSV Data Display

**Precondition:** CSV file contains valid questions.

**Steps:**
1. Browse through multiple questions.

**Expected Result:**
Each question displays exactly four answer choices.

**Status:** PASS

---

## TC-016 – Verify Initial Statistics

**Precondition:** Launch the application.

**Steps:**
1. Observe the labels before answering any questions.

**Expected Result:**
- Correct: 0
- Wrong: 0
- Accuracy: 0%

**Status:** PASS

---

## TC-017 – Verify One-Second Delay

**Precondition:** Quiz has started.

**Steps:**
1. Select an answer.
2. Observe the application.

**Expected Result:**
- Selected answer remains visible.
- Next question appears after approximately one second.

**Status:** PASS

---



**Testing Type:** Manual Functional Testing

**Environment**
- Operating System: Windows 11
- Language: Python 3.14
- GUI Library: Tkinter
- Data Source: CSV (Pandas)
