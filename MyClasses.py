# Author : Syed Thahirr Shahid 400421993
# imports 
from fpdf import FPDF
# My parent Class 
class TaxForm:
    T_Form = []
    name = " "
    sin_number = 0
    def __init__(self,name,sinno):
        self.__name = name
        self.__sinno = sinno
    
    def addtoform(self):
        TaxForm.T_Form.append("Name: " + self.__name)
        TaxForm.T_Form.append("Sin Number: " + self.__sinno)

    def showform(self):
        for content in TaxForm.T_Form:
            print(content)
        return
    
    def printtopdf(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Times", size= 18)

        fd = open("form_summary.txt","r")

        for i in fd:
            pdf.cell(200,10 , txt = i , ln=1, align="L")
        pdf.output("Tax_Form_Summary.pdf")
        return
# This print the Tax summary into a txt file 
    def printtofile(self):
        with open("form_summary.txt","w") as summaryfile:
            for lines in TaxForm.T_Form:
                summaryfile.write(lines)
                summaryfile.write("\n")
        summaryfile.close()
        return
    

# T4 is a Child class of the TaxForm with custom constructor and functions. 
class T4(TaxForm):
    def __init__(self, name, sinno,year,box14,box18,box20,box44,box46):
        TaxForm.__init__(self,name,sinno)
        self.__box14 = box14
        self.__name = name
        self.__sinno = sinno
        self.__year = year
        self.__box18 = box18
        self.__box20 = box20
        self.__box44 = box44
        self.__box46 = box46
        TaxForm.sin_number = self.__sinno

#########################################################################################################################################
####################  This is appended to the T_form list so That I can print it whenever the use wants to see the whole Tax Form summary
    def addtoform(self):
        title  = "T4 Summary"
        TaxForm.T_Form.append(title)
        info = '''\
Employer Name: {name}
Sin Number: {sinno}
Year:{year}
Employment Income: ${b14}
Employee's EI premiums: ${b18}
RPP Contributions: ${b20}
Union Dues: ${b44}
Charitable Donations: ${b46}

            \
            '''.format(name = self.__name,sinno = self.__sinno,year = self.__year,b14=self.__box14,b18=self.__box18,b20=self.__box20,b44=self.__box44,b46=self.__box46)
        TaxForm.T_Form.append( str(info) )


#########################################################################################
################# THIS IS WHAT PRINTS OUT WHEN THE OBJECT IS PRINTED  ######################

    def __str__(self):
        output = '''\
Employer Name: {name}.
Sin Number: {sinno}
Year: {year}
Employment Income: ${b14}
Employee's EI premiums: ${b18}
RPP Contributions: ${b20}
Union Dues: ${b44}
Charitable Donations: ${b46}
            \
            '''.format(name = self.__name,sinno = self.__sinno,year = self.__year,b14=self.__box14,b18=self.__box18,b20=self.__box20,b44=self.__box44,b46=self.__box46)


        return output



class RRSP(TaxForm):

    def __init__(self, name,sinno,taxyear,first_period_amount, second_period_amount,CS_indicator):
        TaxForm.__init__(self,name,sinno)
        self.__sinno = sinno
        self.__name = name
        self.__taxyear = taxyear
        self.__first_period_amount = first_period_amount
        self.__second_period_amount = second_period_amount
        self.__CS_indicator = CS_indicator


    def addtoform(self):
        title  = "RRSP Summary"
        TaxForm.T_Form.append(title)
        info = '''\
Name: {name}
Year:{year}
First Period Amount: {fpa}
Second Period Amount: {spa}
Contributor spouse or common-law partner indicator: {CS_in}

            \
            '''.format(name = self.__name,year = self.__taxyear,fpa=self.__first_period_amount,spa=self.__second_period_amount,CS_in=self.__CS_indicator)
        TaxForm.T_Form.append( str(info) )


    #########################################################################################
################# THIS IS WHAT PRINTS OUT WHEN THE OBJECT IS PRINTED  ######################

    def __str__(self):
        output = '''\
Name: {name}
Year:{year}
First Period Amount: {fpa}
Second Period Amount: {spa}
Contributor spouse or common-law partner indicator: {CS_in}

            \
            '''.format(name = self.__name,year = self.__taxyear,fpa=self.__first_period_amount,spa=self.__second_period_amount,CS_in=self.__CS_indicator)


        return output
##########################################
## This is the T4A Form ######

class T4A(TaxForm):

    def __init__(self, name, sinno,year,b13,b16,b18,b22,b48):
        TaxForm.__init__(self,name,sinno)
        self.__name = name
        self.__sinno = sinno
        self.__year = year
        self.__b13 = b13
        self.__b16 = b16
        self.__b18 = b18
        self.__b22 = b22
        self.__b48 = b48

    def addtoform(self):
        title  = "T4A Summary"
        TaxForm.T_Form.append(title)
        info = '''\
Payer's Name: {name}
Year of payment name:{year}
Sin Number: {sinno}
Recipient's program account number: {b13} 
Pension or superannuation: ${b16} 
Lump-sum Payments: ${b18} 
Income Tax Deducted: ${b22} 
Fees for services: ${b48} 

            \
            '''.format(name = self.__name,year = self.__year,sinno = self.__sinno,b13 = self.__b13,b16 = self.__b16,b18 = self.__b18, b22 = self.__b22, b48 = self.__b48)
        TaxForm.T_Form.append( str(info) )


    #########################################################################################
################# THIS IS WHAT PRINTS OUT WHEN THE OBJECT IS PRINTED  ######################

    def __str__(self):
        output = '''\
Payer's Name: {name}
Year of payment name:{year}
Sin Number: {sinno}
Recipient's program account number: {b13} 
Pension or superannuation: ${b16} 
Lump-sum Payments: ${b18} 
Income Tax Deducted: ${b22} 
Fees for services: ${b48} 

            \
            '''.format(name = self.__name,year = self.__year,sinno = self.__sinno,b13 = self.__b13,b16 = self.__b16,b18 = self.__b18, b22 = self.__b22, b48 = self.__b48)


        return output