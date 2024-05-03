# Test Plan for Project 3: Vadym didukh
## 1

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
| 001 | test_book_creation | Test Book, Author Name, 1234567890 |Title should be Test Book|Title is Author Name|FAIL|Titles are in wrong order|
| 002 | test_book_creation | Test Book, Author Name, 1234567890 (bugfix 001)|Title should be Test Book|Title is Test Book|Pass|N/A|


## 2

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
| 001 | test_user_return_book|user: John Doe, book: Test Book|book not in user's borrowed list|book not in borrowed list|PASS|N/A|

## 3
| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
| 001 | test_library_find_user | uder: John Doe, ID: 1 | user object retrieved successfully | user object retrieved successfully | Pass | N/A |