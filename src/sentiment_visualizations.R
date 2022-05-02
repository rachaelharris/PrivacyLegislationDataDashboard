install.packages("ggplot2")
state.data<- read.csv(file="results/state_results.csv")
federal.data <- read.csv(file="results/federal_results.csv")
 
## Year
### Line Chart to visualize the sentiment of state-based legislation by year
state_time_chart <- ggplot() + geom_line(aes(y = score, x = year),
                                   data = state.data)
state_time_chart + labs(title = "State Legislation Sentiment by Year", x = "Year", y = "Sentiment Score")

### Line Chart to visualize the sentiment of federal legislation by year
federal_time_chart <- ggplot() + geom_line(aes(y = score, x = year),
                                         data = federal.data)
federal_time_chart + labs(title = "Federal Legislation Sentiment by Year", x = "Year", y = "Sentiment Score")

## Party
### Bar Chart to visualize the sentiment of state-based legislation by party
state_sentiment_party <- ggplot(aes(x=score, y=party, color=party, fill=party), data = state.data) + 
  geom_bar(stat = "identity")

### Bar Chart to visualize the sentiment of federal legislation by party
federal_sentiment_party <- ggplot(aes(x=score, y=party, color=party, fill=party), data = federal.data) + 
  geom_bar(stat = "identity")

## Status
### Bar Chart to visualize the sentiment of state-based legislation by bill status
state_sentiment_status <- ggplot(aes(x=type, y=score, color=party, fill=party), data = state.data) + 
  geom_bar(stat = "identity")

### Bar Chart to visualize the sentiment of federal legislation by bill status
federal_sentiment_status <- ggplot(aes(x=status, y=score, color=party, fill=party), data = federal.data) + 
  geom_bar(stat = "identity")
