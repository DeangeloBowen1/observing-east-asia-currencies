# US Dollar Purchasing Power in East Asia
- by Deangelo Bowen, July 1, 2022
---
## Project Description : 
The United States Dollar has never been stronger. As of today, in 2022, the USD Index has soared to an all-time high. However, domestic goods are getting any cheaper. I will be analyzing how to take advantage of the strength of the US Dollar in certain foriegn countries for profit or personal gain. The currencies I will be showcasing against the US Dollar are currencies strictly in East Asia. These currencies are the Korean Won, Japanese Yen, Chinese Yuan, Hong Kong Dollar, Taiwanese Dollar, Singapore Dollar and the Thai Baht. 

---
## Project Overview:

The purpose of this project is to identify countries in East Asia where the U.S. Dollar has, or does not have significant purchasing power. 

To fully understand the observation, when going through this notebook, understand that each currency is compared to their own national price. This, for example, means that 1 USD or dollar bill is national recognized of value as 1 dollar. 100 Yen would then be the national equivalent of the USD for Japan.

##### This national equivalent should not be confused with the global exchange rate. 

National Equivalent Prices comparable to 1 USD are as follows:
- 100 Japanese Yen
- 10 Chinese Yuan/Renminbi
- 10 HKD
- 1000 Korean Won
- 1 Singapore Dollar
- 30 Taiwanese Dollar
- 30 Thai Baht

_The information backing these calculations are assumptions of an exchange rate where the respective national equivalent of $1 per country observed equal exchange rates. The research done behind these calculations can be found here:_
- [Korean Won](https://wise.com/us/currency-converter/krw-to-usd-rate)
- [Hong Kong Dollar](https://www.scmp.com/yp/discover/advice/article/3093224/what-hong-kong-us-dollar-peg-and-how-does-it-work)
- [Singapore Dollar](https://themoneyconverter.com/USD/SGD)
- [Chinese Yuan/Renminbi](https://www.cnn.com/2021/12/09/investing/china-yuan-2021-mic-intl-hnk/index.html)
- [Thai Baht](https://www.exchangerates.org.uk/USD-THB-exchange-rate-history.html)
- [Japanese Yen](https://www.bloomberg.com/news/articles/2022-06-10/why-the-yen-is-so-weak-and-what-that-means-for-japan-quicktake)

---

## Data Dictionary
|Column | Description | Dtype|
|--------- | --------- | ----------- |
|DATE| date of observation| datetime|
|JPYEN| actual japanese yen price| float64|
|HKD| actual hong kong dollar price| float64|
|CHYUAN| actual chinese yuan/renminbi price| float64|
|KRWON| actual korean won price| float64|
|SPD| actual singapore dollar price| float64|
|TWD| actual taiwan dollar price| float64|
|THB| actual thai baht price| float64|
|USD_Index|actual usd index price|float64|
|USD_Actual| usd national equivalant price|int64|
|month| actual month |datetime|
|USD_YEN| purchase power percent for USD to YEN| float64|
|USD_HKD|purchase power percent for USD to HKD|float64|
|USD_YUAN| Purchase power percent for USD to Yuan|float64|
|USD_WON| purchase power percent for USD to Won|float64|
|USD_SPD| purchase power percent for USD to SPD| float64|
|USD_TWD| purchase power percent for USD to TWD|float64|
|USD_THB| purchase power percent for USD to thai baht |float64|

---

## Objectives :

- To conduct a Time Series Analysis observing EA Currencies vs. USD over time
- To make an informed decision based on the Analysis and showcase the current best country where the USD has more value. 
- To give recommendations on potential times to invest the USD into  the final observed country. This observation is aimed to assist potential:
    - Travelers/Backpackers
    - Goods Import/Export Businesses
    - International Shopping Enthusiasts
    - International Investing Enthusiasts (real estate, foriegn rarities, etc)
- Showcase code and techniques used for reproducable analysis to stay up-to-date in relevant data.
___

## Project Summary: 

When conducting research on the US dollar purchasing power in East Asian countries, and creating an indepth analysis on which countries as of July 2022 would be the best to expend that purchasing power, I discovered that Japan and Korea were the strongest targets, while China and Hong Kong were the weakest. 

With Chinese Yuan/Renminbi and Chinese affiliated countries such as Taiwan or Hong Kong, the USD is stagnant in negative purchasing power. This ranges from around (-17%) to (-35%)

In countries such as Singapore, Japan and Korea, the US Dollar purchasing power is continously flucuating and very volatile, however it has alwas had a consistant positive purchasing power of about 5-35%. 

My recommendations for those who are either traveling, purchasing lands or making investments in goods, or simply looking to buy enthusiast related items from foreign countries, would be to target Japan and Korea as of July, 2022. 

___

### Exploration Takeaway Summary:

- Almost immediately I was able to identify that there are many factors that influence the fluxuation of currency prices after the year 2021. I decided that these would unfortunately not be covered in this notebook, but perhaps observed as an additional at a later date.
- Overall, it looks as though each of these currencies were starting to gain some momentum against the USD in the early stages of 2021, as the Japanese Yen went from 14% to 4%, Korean Won from a high of 12.5% to 10%, and the Singapore Dollar from a high of 46% to 34%. 
- Chinese and China affiliated countries are all strong against the US Dollar.
- The Japanese Yen and Korean Won have the best prices for USD to Yen/Won on average.
- Japanese Yen and Korean Won are by far the most volatile by comparison when vs the US dollar than these other currencies. 
- Although there are some points in an autocorrelation plots that display a possible hint of seasonality, there is not a trend, thus there is no identifiable seasonailty. 

# In conclusion : 

When observing currencies against one another it's best to identify exactly what a National equivalent of one currency is to another. For this I took the USD and the national equivalent amount of currencies in East Asia, disregarding the current exchange rate. 

What I discovered was exactly how much more or less those utilizing the US Dollar would be receiving when purchasing foriegn goods, services, or making investments. 

With Chinese Yuan/Renminbi and Chinese affiliated countries such as Taiwan or Hong Kong, the USD is stagnant in negative purchasing power. This ranges from around (-17%) to (-35%)

In countries such as Singapore, Japan and Korea, the US Dollar purchasing power is continously flucuating and very volatile, however it has alwas had a consistant positive purchasing power of about 5-35%. 

### My Recommendations: 

My recommendations for those who are either traveling, purchasing lands or making investments in goods, or simply looking to buy enthusiast related items from foreign countries, would be to target Japan and Korea as of July, 2022. 

The USD to Yen is yielding over 35% more per USD than the standard ratio of 1:100 yen. Simply put, expect an immediate +30% return on investment when calculating with national equivalency. 

### With more time :

I wish to identify the causes of the massive shift in the declining of certain national currencies after 2021. 

Recent geo-political and economic events cause expentance, however this venture would take another report or two to fully expand on the what, how, and why.

## To Reproduce this project
Head to [FRED](https://fred.stlouisfed.org) to obtain each CSV
- USD to Japanese Yen
- Korean Won
- Chinese Yuan
- Hong Kong Dollar
- Thai Baht
- Singapore Dollar
- Taiwan Dollar

This data should be the most current data.

Utilize the wrangle.py to either rename the CSVs accordingly, or change the information in the .py file to match your csv naming convention. 
Finally, utilize the explore.py to explore the csvs collected and analyize the most up-to-date data. 
