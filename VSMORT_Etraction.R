file.remove("VSMORT.csv")

directory <- "/Users/rifat/Library/CloudStorage/OneDrive-UniversityofSaskatchewan/PhD CS USASK/Research/Suicide USA data 2004-2023/data"

files <- list.files(directory, full.names = TRUE)

# Specify the file paths for output
output_file <- "VSMORT.csv"

for (file in files) {
  # Open the input and output files
  fileObj <- file(file, "r")
  fileOutObj <- file(output_file, "a")
  
  # Write the header to the output file if it's the first file
  if (file == files[1]) {
    header <- "Month_Of_Death,DOW_of_Death,Data_Year,Manner_Of_Death,ICD10,Sex\n"
    writeLines(header, fileOutObj)
  }
  
  # Read each line of the input file, extract the desired fields, and write them to the output file
  while (length(line <- readLines(fileObj, n = 1, warn = FALSE)) > 0) {
    Month_Of_Death <- substr(line, 65, 66)
    DOW_of_Death <- substr(line, 85, 85)
    Data_Year <- substr(line, 102, 105)
    Manner_Of_Death <- substr(line, 107, 107)
    ICD10 <- substr(line, 146, 149)
    Sex <- substr(line, 69, 69)
    
    if (Manner_Of_Death == "2") {
      outStr <- paste(Month_Of_Death, DOW_of_Death, Data_Year, Manner_Of_Death, ICD10, Sex, sep = ", ")
      write(outStr, file = fileOutObj, append = TRUE)
    }
  }
  
  print("Parse complete.")
  close(fileOutObj)
  close(fileObj)
}


VSMORT <- read.csv("VSMORT.csv", header = T)

