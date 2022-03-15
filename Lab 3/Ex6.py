#  This program prompts and reads a province and a taxable income.  Then,
#  using if-else structures, the tax rate is computed for the province
#  and the taxable income.  The tax rate and the net income are illustrated
#  using a simple bar chart 

# import javax.swing.JOptionPane;


#Input Variables
prov_id = ""               #province_id will contain the user input for the province (E.g. 'AB'). 
gross_income = 0.0               #gorss_income contains the user input for gross income (E.g. 30000). 

#Output Variables:
#You will store the result of your analysis and calculations in these variables
tax_rate = 0.0                      #Variable tax_rate will hold the tax_rate percentage. 
                                        #You will assign a value for tax_rate based on the Taxable Income (Table 1) table given in the studio project document. 
                                        #The value of tax ranges between 0 to 1 (E.g. for Alberta, income of equal or less than $40000 tax = 0.25)

net_income = 0.0                     #Net income is calculated based on tax_rate. It is the take-home income after taxes are deducted. 
                                          #i.e. net_income = gross_income * (1 - tax_rate); 
                                          
tax_amount = 0.0                    #tax amount is the amount of taxes paid based on gross income depending on the province.
                                        #i.e. tax_amount = gross_income * tax_rate;

# prompt for and read the province id 
prov_id = input("Please enter your province's two-letter abbreviation (e.g., AB for Alberta): ")
    
# prompt for and read the gross income
answer = input("Please enter your taxable income: ")

# convert user input to folat
gross_income = float(answer)
  



if(prov_id == "AB" or prov_id == "ab"):
    if(gross_income <= 40000):
        tax_rate = 0.25
    elif(gross_income > 40000 and gross_income <= 80000):
        tax_rate = 0.32
    elif(gross_income > 80000 and gross_income <= 120000):
        tax_rate = 0.36
    elif(gross_income > 120000):
        tax_rate = 0.39
elif(prov_id == "BC" or prov_id == "bc"):
    if(gross_income <= 20000):
        tax_rate = 0.20
    elif(gross_income > 20000 and gross_income <= 35000):
        tax_rate = 0.225
    elif(gross_income > 35000 and gross_income <= 50000):
        tax_rate = 0.30
    elif(gross_income > 50000 and gross_income <= 65000):
        tax_rate = 0.325
    elif(gross_income > 65000 and gross_income <= 80000):
        tax_rate = 0.365
    elif(gross_income > 80000 and gross_income <= 100000):
        tax_rate = 0.393
    elif(gross_income > 100000 and gross_income <= 120000):
        tax_rate = 0.41
    elif(gross_income > 120000):
        tax_rate = 0.44
elif(prov_id == "SK" or prov_id == "sk" or prov_id == "ON" or prov_id == "on"):
    if(gross_income <= 40000):
        tax_rate = 0.25
    elif(gross_income > 40000 and gross_income <= 60000):
        tax_rate = 0.3
    elif(gross_income > 60000 and gross_income <= 80000):
        tax_rate = 0.35
    elif(gross_income > 80000 and gross_income <= 100000):
        tax_rate = 0.4
    elif(gross_income > 100000 and gross_income <= 120000):
        tax_rate = 0.45
    elif(gross_income > 120000):
        tax_rate = 0.5

print("Gross Income:", gross_income)
print("Tax Rate:", tax_rate)
print("Tax Amount:", gross_income * tax_rate)
print("Net Income", gross_income * (1-tax_rate))
