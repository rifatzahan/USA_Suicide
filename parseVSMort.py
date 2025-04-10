fileObj = open("C:/Users/......../VS23MORT.DUSMCPUB_r20241030",'r')
fileOutObj = open("C:/Users/........../VS23MORT.csv","w")



fileOutObj.write('Resident_Status, Occupation_Recode, Education, Month_Of_Death, Sex, Age_Value, Age_Recode_12, Place_Of_Death, Marital_Status, DOW_of_Death, '  + \
               'Data_Year, Injured_At_Work, Manner_Of_Death, Method_Of_Disposition, Autopsy, Activity_Code, Place_Of_Causal_Injury, icd_10, ' + \
               'EA1, EA2, EA3, EA4, EA5, EA6, EA7, EA8, EA9, EA10, EA11, EA12, EA13, EA14, EA15, EA16, EA17, EA18, EA19, EA20, Race_Recode_6, Hispanic_Origin  \n')


# fileOutObj.write('Resident_Status, Occupation_Recode, Education, Month_Of_Death, Sex, Age_Value, Place_Of_Death, Marital_Status, DOW_of_Death, '  + \
#                'Data_Year, Injured_At_Work, Manner_Of_Death, Method_Of_Disposition, Autopsy, Activity_Code, Place_Of_Causal_Injury, icd_10, Race_Recode_6, Hispanic_Origin' + \
#                'EA1, EA2, EA3, EA4, EA5, EA6, EA7, EA8, EA9, EA10, EA11, EA12, EA13, EA14, EA15, EA16, EA17, EA18, EA19, EA20,' + \
#                'RA1, RA2, RA3, RA4, RA5, RA6, RA7, RA8, RA9, RA10, RA11, RA12, RA13, RA14, RA15, RA16, RA17, RA18, RA19, RA20 \n')

outStr = ""

# be careful about the position of the data in the flat file. If the data is positioned within multiple column spaces, type the exact same digit range (but add one to the first digit). but when the data is not taking range of values rather
# a particular value, then minus 1 from that particular value

for line in fileObj:

               Resident_Status = line[19].strip()
               Occupation_Recode = line[809:811].strip()
               Education = line[62].strip()
               Month_Of_Death = line[64:66].strip()
               Sex = line[68].strip()
               Age_Value = line[69:73].strip()
               Age_Recode_12 = line[78:80].strip()
               Place_Of_Death = line[82].strip()
               Marital_Status = line[83].strip()
               DOW_of_Death = line[84].strip()
               Data_Year = line[101:105].strip()
               Injured_At_Work = line[105].strip()
               Manner_Of_Death = line[106].strip()
               Method_Of_Disposition = line[107].strip()
               Autopsy = line[108].strip()
               Activity_Code = line[143].strip()
               Place_Of_Causal_Injury = line[144].strip()
               icd_10 = line[145:149].strip()
               EA1 = line[166:171].strip()
               EA2 = line[173:178].strip()
               EA3 = line[180:185].strip()
               EA4 = line[187:192].strip()
               EA5 = line[194:199].strip()
               EA6 = line[201:206].strip()
               EA7 = line[208:213].strip()
               EA8 = line[215:220].strip()
               EA9 = line[222:227].strip()
               EA10 = line[229:234].strip()
               EA11 = line[236:241].strip()
               EA12 = line[243:248].strip()
               EA13 = line[250:255].strip()
               EA14 = line[257:262].strip()
               EA15 = line[264:269].strip()
               EA16 = line[271:276].strip()
               EA17 = line[278:283].strip()
               EA18 = line[285:290].strip()
               EA19 = line[292:297].strip()
               EA20 = line[299:304].strip()
               Race_Recode_6 = line[449].strip()
               Hispanic_Origin = line[486:488].strip()
               # RA1 = line[345:348].strip()
               # RA2 = line[350:353].strip()
               # RA3 = line[355:358].strip()
               # RA4 = line[360:363].strip()
               # RA5 = line[365:368].strip()
               # RA6 = line[370:373].strip()
               # RA7 = line[375:378].strip()
               # RA8 = line[380:383].strip()
               # RA9 = line[385:388].strip()
               # RA10 = line[390:393].strip()
               # RA11 = line[395:398].strip()
               # RA12 = line[400:403].strip()
               # RA13 = line[405:408].strip()
               # RA14 = line[410:413].strip()
               # RA15 = line[415:418].strip()
               # RA16 = line[420:423].strip()
               # RA17 = line[425:428].strip()
               # RA18 = line[430:433].strip()
               # RA19 = line[435:438].strip()
               # RA20 = line[440:443].strip()


               
               
               outStr = (Resident_Status + ', ' + Occupation_Recode + ', ' + Education + ', ' + Month_Of_Death + ', ' + Sex + ', ' + Age_Value + ', ' + Age_Recode_12 + ', ' +  Place_Of_Death + ', ' + Marital_Status + ', ' + DOW_of_Death + \
                        ', ' +  Data_Year + ', ' + Injured_At_Work + ', ' + Manner_Of_Death + ', ' + Method_Of_Disposition + ', ' + Autopsy + ', ' + Activity_Code + ', ' + Place_Of_Causal_Injury + ', ' + icd_10 + \
                       ', ' + EA1 + ', ' + EA2 + ', ' + EA3 + ', ' + EA4 + ', ' + EA5 + ', ' + EA6 + ', ' + EA7 + ', ' + EA8 + ', ' + EA9 + ', ' + EA10 + ', ' + EA11 + ', ' + EA12 + ', ' + EA13 + \
                        ', ' + EA14 + ', ' + EA15 + ', ' + EA16 + ', ' + EA17 + ', ' + EA18 + ', ' + EA19 + ', ' + EA20  + ', ' + Race_Recode_6 + ', ' + Hispanic_Origin + '\n')     

               # outStr = (Resident_Status + ', ' + Occupation_Recode + ', ' + Education + ', ' + Month_Of_Death + ', ' + Sex + ', ' + Age_Value + ', ' + Place_Of_Death + ', ' + Marital_Status + ', ' + DOW_of_Death + \
               #          ', ' +  Data_Year + ', ' + Injured_At_Work + ', ' + Manner_Of_Death + ', ' + Method_Of_Disposition + ', ' + Autopsy + ', ' + Activity_Code + ', ' + Place_Of_Causal_Injury + ', ' + icd_10 + \
               #         ', ' + Race_Recode_6 + ', ' + Hispanic_Origin + ', ' + EA1 + ', ' + EA2 + ', ' + EA3 + ', ' + EA4 + ', ' + EA5 + ', ' + EA6 + ', ' + EA7 + ', ' + EA8 + ', ' + EA9 + ', ' + EA10 + ', ' + EA11 + ', ' + EA12 + ', ' + EA13 + \
               #          ', ' + EA14 + ', ' + EA15 + ', ' + EA16 + ', ' + EA17 + ', ' + EA18 + ', ' + EA19 + ', ' + EA20 + \
               #          ', '   + RA1 + ', ' + RA2 + ', ' + RA3 + ', ' + RA4 + ', ' + RA5 + ', ' + RA6 + ', ' + RA7 + ', ' + RA8 + ', ' + RA9 + ', ' + RA10 + ', ' + RA11 + ', ' + RA12 + ', ' + RA13 + \
               #          ', ' + RA14 + ', ' + RA15 + ', ' + RA16 + ', ' + RA17 + ', ' + RA18 + ', ' + RA19 + ', ' + RA20 + '\n')         

               fileOutObj.write(outStr)



print("Parse complete.")
fileOutObj.close()
fileObj.close()

