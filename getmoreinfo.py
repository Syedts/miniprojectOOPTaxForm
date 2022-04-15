#Author : Syed Thahirr Shahid
# This script is so the information can be retreived for the main program file by executing during the main program 

import sys
import time

# this dictionary stores all the details 
info_dict = {
    "T412": "Enter the recipient's social insurance number (SIN), as provided by the employee. If you do not have the SIN, enter nine zeros.",
    "T414": """Enter in box 14 the total employment income before deductions.
    Include the following: 
    - Salary and wages (including pay in lieu of termination notice).
    - Bonuses.
    - Vacation pay.
    - Tips and gratuities.
    """,
    "T418":"Enter the amount of EI premiums you deducted from the employee's earnings. If you did not deduct premiums, leave this box blank.",
    "T420":"Enter the total amount the employee contributed to a registered pension plan (RPP). If the employee did not contribute to a plan, leave this box blank. Do not include amounts transferred directly to an RPP from an employee's registered retirement savings plan (RRSP).",
    "T444":"Enter in box 44 the amount you deducted from employees for union dues. Include amounts you paid to a parity or advisory committee that qualify for a deduction.",
    "T446":"Enter the amount you deducted from the employee's earnings for donations to qualified donees in Canada.",
    "RRSP1":"First period - last 10 months (March to December) of the tax year (ordinarily March 2nd to December 31st of the tax year);",
    "RRSP2":"Second period - first 60 days of the following year (ordinarily January 1st to March 1st of year following the tax year). ",
    "RRSP3": "Indicate whether or not your spouse or common-law partner has ever contributed to your retirement income plan.",
    "T4A13":"If the recipient of the reported amount is a business (sole proprietor, partnership, or corporation), enter the recipient's account number.",
    "T4A16":"Enter the taxable part of annuity payments you paid to an employee, retired employee, or survivor or spouse of an employee out of, or under, a superannuation or registered pension fund or plan, including disability benefits paid as a life annuity.",
    "T4A18":'''In box 018, enter the taxable part of a single payment out of a pension fund or plan including any single payment resulting from a:

    - withdrawal from the plan, retirement from employment, or death of an employee or former employee
    - termination of, amendment to, or modification of the plan
    - reimbursement of any over-contributions to the plan

Also, enter the taxable part of any single payment out of a deferred profit sharing plan (DPSP) including a single payment due to a withdrawal from 
the plan, retirement from employment, death of an employee or former employee, or reimbursement of any over-contributions to the plan.''',
    "T4A22":'''Enter the total income tax you deducted from the recipient's remuneration during the year. This includes the federal, provincial (except Quebec), and territorial taxes that apply. Leave the box blank if you did not deduct tax.
               Do not include an amount you withheld under the authority of a garnishee or a requirement to pay that applies to the employee's previously assessed tax arrears.''',
    "T4A48":"Enter any fees or other amounts paid for services. Do not include GST/HST paid to the recipient for these services."
}
info = sys.argv[1]

def getInfo(info):
    reply = info_dict.get(info)
    print("\n")
    time.sleep(.5)
    print(reply)

getInfo(info)