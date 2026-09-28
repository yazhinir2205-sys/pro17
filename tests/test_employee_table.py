import os
import sys
from bs4 import BeautifulSoup

FILE = os.path.join(
    os.path.dirname(__file__),
    "..",
    "starter",
    "index.html"
)

TOTAL = 50
score = 0
results = []


def award(points, message):
    global score
    score += points
    results.append(f"[PASS] {message} (+{points})")


def fail(message):
    results.append(f"[FAIL] {message}")


if not os.path.exists(FILE):
    print("ERROR: starter/index.html was not found.")
    sys.exit(1)


with open(FILE, "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")


# ---------------------------------------------------------
# 1. Table and caption - 5 points
# ---------------------------------------------------------

table = soup.find("table")

if table:
    award(3, "Table element exists.")
else:
    fail("Table element is missing.")

caption = soup.find("caption")

if caption and caption.get_text(strip=True) == "Employee Table":
    award(2, "Caption is 'Employee Table'.")
else:
    fail("Caption is missing or incorrect.")


# ---------------------------------------------------------
# 2. Table header - 5 points
# ---------------------------------------------------------

thead = soup.find("thead")
headers = thead.find_all("th") if thead else []

expected_headers = [
    "Department",
    "Name",
    "E-mail",
    "Years of Service"
]

actual_headers = [
    h.get_text(" ", strip=True)
    for h in headers
]

if actual_headers == expected_headers:
    award(5, "Table header contains the correct four headings.")
else:
    fail(
        "Table headings are incorrect. "
        f"Expected {expected_headers}, got {actual_headers}"
    )


# ---------------------------------------------------------
# 3. Employee data - 10 points
# ---------------------------------------------------------

expected_employees = [
    ("Joel Murach", "joelmurach@yahoo.com", "22"),
    ("Anne Boehm", "anne@murach.com", "34"),
    ("Zak Ruvalcaba", "zak@modulemedia.com", "4"),
    ("Judy Taylor", "judy@murach.com", "39"),
    ("Cyndi Vasquez", "cyndi@murach.com", "10"),
    ("Kelly Slivkoff", "kelly@murach.com", "25"),
    ("Juliette Baylon", "juliette@murach.com", "1"),
]

tbody = soup.find("tbody")
rows = tbody.find_all("tr") if tbody else []

found_employees = []

for row in rows:
    cells = row.find_all(["td", "th"])

    # Department cells may be included in some rows.
    values = [c.get_text(" ", strip=True) for c in cells]

    if len(values) >= 4:
        values = values[-3:]

    if len(values) == 3:
        found_employees.append(tuple(values))

matched = 0

for employee in expected_employees:
    if employee in found_employees:
        matched += 1

employee_points = round((matched / len(expected_employees)) * 10)

if matched == len(expected_employees):
    award(10, "All seven employee records are correct.")
elif matched > 0:
    award(employee_points, f"{matched}/7 employee records are correct.")
else:
    fail("Employee records are missing or incorrect.")


# ---------------------------------------------------------
# 4. Department rowspans - 8 points
# ---------------------------------------------------------

department_cells = []

for row in rows:
    th = row.find("th")
    if th:
        text = th.get_text(" ", strip=True)
        if text in ["Editorial", "Marketing", "Customer Service"]:
            department_cells.append(th)

expected_departments = {
    "Editorial": "3",
    "Marketing": "2",
    "Customer Service": "2"
}

correct_departments = 0

for cell in department_cells:
    department = cell.get_text(" ", strip=True)
    rowspan = cell.get("rowspan")

    if department in expected_departments:
        if rowspan == expected_departments[department]:
            correct_departments += 1

if correct_departments == 3:
    award(8, "All department rowspan values are correct.")
elif correct_departments > 0:
    points = round((correct_departments / 3) * 8)
    award(points, f"{correct_departments}/3 department rowspans are correct.")
else:
    fail("Department rowspan values are missing or incorrect.")


# ---------------------------------------------------------
# 5. Footer and total - 7 points
# ---------------------------------------------------------

tfoot = soup.find("tfoot")

if tfoot:
    award(2, "Table footer exists.")

    footer_text = tfoot.get_text(" ", strip=True)

    if "Total Years of Service" in footer_text:
        award(2, "Footer contains the correct total label.")
    else:
        fail("Footer total label is missing.")

    if "135" in footer_text:
        award(3, "Total years of service is 135.")
    else:
        fail("Total years of service should be 135.")
else:
    fail("Table footer is missing.")


# ---------------------------------------------------------
# 6. CSS formatting - 10 points
# ---------------------------------------------------------

style = soup.find("style")

if style:
    css = style.get_text()

    css_checks = [
        ("border-collapse", 2),
        ("yellow", 2),
        ("text-align: right", 2),
        ("vertical-align: top", 2),
        ("nth-child(even)", 2),
    ]

    for keyword, points in css_checks:
        if keyword in css:
            award(points, f"CSS requirement '{keyword}' found.")
        else:
            fail(f"CSS requirement '{keyword}' is missing.")
else:
    fail("Style element is missing.")


# ---------------------------------------------------------
# 7. Semantic HTML structure - 5 points
# ---------------------------------------------------------

semantic_checks = [
    ("thead", 1),
    ("tbody", 1),
    ("tfoot", 1),
    ("th", 1),
    ("caption", 1),
]

for tag, points in semantic_checks:
    if soup.find(tag):
        award(points, f"Semantic <{tag}> element exists.")
    else:
        fail(f"Semantic <{tag}> element is missing.")


# ---------------------------------------------------------
# Final score
# ---------------------------------------------------------

score = min(score, TOTAL)

print("=" * 60)
print("EMPLOYEE TABLE - AUTOMATED GRADING")
print("=" * 60)

for result in results:
    print(result)

print("-" * 60)
print(f"FINAL SCORE: {score}/{TOTAL}")
print("-" * 60)

if score == TOTAL:
    print("STATUS: PASS")
else:
    print("STATUS: REVIEW REQUIRED")

sys.exit(0)
