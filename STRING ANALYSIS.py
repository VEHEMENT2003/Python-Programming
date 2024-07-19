# PROGRAM TO INPUT A STRING AND DISPLAY ITS ANALYSIS
Str1=input("Please tell the String : ")      # ENTER THE VALUE OF STRING 
for x in Str1:          # USING FOR LOOP 
      if(x.isdigit()):                     # x.isdigit REPRESENTS NUMERIC VALUES
            print(x,"It is a numerical value  ")
      elif(x.isalpha()):                # x.isalpha REPRESENTS LITERAL VALUES
            print(x,"It is an alphabet ")
      elif(x.isalnum()):              # x.isalnum REPRESENTS LITERAL AND NUMERIC VALUES
            print(x,"It is a Special Character ")
      elif(not(x.isalpha()) and not(x.isdigit())):
            print(x,"It is a Special Character ")
      elif(x.isalpha()) and (x.iscapitalize()): # x.iscapitalize CONVERTS SMALL LETTERS INTO CAPITAL LETTERS
            print(x,"It is a Capital Letter ")
