install.packages("dplyr")
library(dplyr)

all_authors_info_2020 <- do.call("rbind",list( authors_info_2020_sep, authors_info_2020_1_sep,authors_info_2020_2.sep, authors_info_2020_3.sep, authors_info_2020_4.sep))
all_authors_info_2020 <- subset(all_authors_info_2020, !is.na(Author.ID) & Author.ID != "")
View(all_authors_info_2020)

all_authors_info_2021<-do.call("rbind",list( authors_info_2021_sep, authors_info_2021_sep,authors_info_2021_2.sep, authors_info_2021_3.sep, authors_info_2021_4.sep))
all_authors_info_2021<- subset(all_authors_info_2021, !is.na(Author.ID) & Author.ID != "")
View(all_authors_info_2021)

all_authors_info_2022 <- do.call("rbind",list( authors_info_2022_sep, authors_info_2022_sep,authors_info_2022_sep, authors_info_2022_3.sep, authors_info_2022_4.sep))
all_authors_info_2022<- subset(all_authors_info_2022, !is.na(Author.ID) & Author.ID != "")
View(all_authors_info_2022)

During_Covid<- do.call("rbind", list(all_authors_info_2020, all_authors_info_2021, all_authors_info_2022))
rownames(During_Covid) <- NULL
View(During_Covid)

all_authors_info_2023<- do.call("rbind",list( authors_info_2023_sep, authors_info_2023_sep,authors_info_2023_2.sep, authors_info_2023_3.sep, authors_info_2023_4.sep))
After_Covid<- subset(all_authors_info_2023, !is.na(Author.ID) & Author.ID != "")
rownames(After_Covid) <- NULL
View(After_Covid)

# Save During_Covid dataframe to a CSV file
write.csv(During_Covid, "During_Covid.csv", row.names = FALSE)

# Save After_Covid dataframe to a CSV file
write.csv(After_Covid, "After_Covid.csv", row.names = FALSE)
