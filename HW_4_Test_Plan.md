# Test Plan for HW4 
## 1. 'add' Function

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
| 001 | add - Test with positive numbers | 3, 2 | 5 | 1 | FAIL | Have to add instead of subtract |
| 002 | add - Test with positive numbers (bugfix 001)| 3, 2 | 5 | 5 | PASS | N/A |
| 003 | add - Test with zero and positive number | 0, 5 | 5 | 5 | PASS | N/A |

## 2. 'subtract' Function

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
| 001 | subtract - Test with positive numbers | 5, 3 | 2 | 8 | FAIL | Have to subtract instead of add |
| 002 | subtract - Test with positive numbers (bugfix001) | 5, 3 | 2 | 2 | PASS | N/A |
| 003 | subtract - Test with positive numbers | 3, 5 | -2 | -2 | PASS | N/A |

## 3. 'divide' Function

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
| 001 | divide - Test with positive numbers | 6, 2 | 3 | 12 | FAIL | Have to divide instead of multiply |
| 002 | divide - Test with positive numbers (bugfix001) | 6, 2 | 3 | 3 | PASS | N/A |
| 003 | divide - Test with positive number and zero | 1, 0 | Error | Error | PASS | N/A |

## 4. 'multiply' Function

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
| 001 | multiply - Test with positive numbers | 4, 3 | 12 | 1.3333333333333333 | FAIL | Have to multiply instead of divide |
| 002 | multiply - Test with positive numbers (bugfix001)| 4, 3 | 12 | 12 | PASS | N/A |
| 003 | multiply - Test with positive number and zero | 4, 0 | 0 | 0 | PASS | N/A |

## 5. 'greet' Function

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
| 001 | greet - Test with string | "John" | "Hello, John!" | "Heloo, John" | FAIL | typo error in word "Heloo" |
| 002 | greet - Test with string (bugfix001)| "John" | "Hello, John!" | "Hello, John!" | PASS | N/A |
| 003 | greet - Test with string | "Doe" | "Hello, Doe!" | "Heloo, Doe!" | PASS | N/A |

## 6. 'square' Function

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
| 001 | square - Test with positive number | 4 | 16 | 8 | FAIL | num + num is causing an incorrect calculation |
| 002 | squre - Test with positive number (bugfix001)| 4 | 16 | 16 | PASS | N/A |
| 003 | square - Test with zero | 0 | 0 | 0 | PASS | N/A |

## 7. 'is_even' Function
| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
| 001 | is_even - Test with positive number | 4 | True | False | FAIL | Remainder = 1 instead of 0 |
| 002 | is_even - Test with positive number (bugfix001)| 4 | True | True | PASS | N/A |
| 003 | is_even - Test with positive number | 3 | False | False | PASS | N/A |


## 8. 'grade_calc' Function

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
| 001 | grade_calc - Test with positive number | 95 | A | A | FAIL | missing "and score" in if statement and should be <=79 instead of <79 |
| 002 | grade_calc - Test with positive number (bugfix001)| 95 | A | A | PASS | N/A |
| 003 | grade_calc - Test with positive number | 85 | B | B | PASS | N/A |
| 004 | grade_calc - Test with positive number | 75 | C | C | PASS | N/A |
| 005 | grade_calc - Test with positive number | 79 | C | C | PASS | N/A |
| 006 | grade_calc - Test with positive number | 65 | D | D | PASS | N/A |
| 007 | grade_calc - Test with positive number | 50 | F | F | PASS | N/A |
| 008 | grade_calc - Test with positive number | 105 | Invalid Score | Invaild Score | PASS | N/A |
| 009 | grade_calc - Test with negative number | -5 | Invalid Score | Invaild Score | PASS | N/A |

## 9. 'speed_check' Function

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
| 001 | speed_check - Test with positive number | 10 | Too slow | Too slow | FAIL |  Failed for upper end of within limit need to change max speed limit 60 to 70 |
| 002 | speed_check - Test with positive number (bugfix001)| 10 | Too slow | Too slow | PASS | N/A |
| 003 | speed_check - Test with positive number | 50 | Within limit | Within limit | PASS | N/A |
| 004 | speed_check - Test with positive number | 80 | Over speed limit | Over speed limit | PASS | N/A |
| 005 | speed_check - Test with positive number | 65 | Within limit | Within limit | PASS | N/A |

## 10. 'is_leap_year' Function

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
| 001 | is_leap_year - Test with positive number | 2020 | True | True | PASS | N/A |
| 002 | is_leap_year - Test with positive number | 2021 | False | False | PASS | N/A |
| 003 | is_leap_year - Test with positive number | 2000 | True | True | PASS | N/A |
| 004 | is_leap_year - Test with positive number | 1900 | False | True | FAIL | The year 1900 is divisible by 4 and 100 but not by 400 |
| 005 | is_leap_year - Test with positive number (bugfix004)| 1900 | False | False | PASS | N/A |
