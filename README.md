# Overview

In this project, we will examine the Value at Risk calculations and results of a stock withdrawn from the yahoo site at the desired date intervals.

## Introduction

## What is Value at Risk ?

Belirli bir zaman dilimi boyunca bir firma, portföy veya pozisyondaki finansal risk seviyesini ölçen ve nicelendiren bir istatistik türüdür. Bu ölçüt, en çok yatırım bankaları ve ticari bankalar tarafından kurumsal portföylerindeki potansiyel zararların kapsamını ve gerçekleşme oranını belirlemek için kullanılmaktadır.
Bu çalışmada VaR hesaplanmasının 3 methodunu ve kullanılma aşamalarını göreceğiz. Bu çalışmada Value at Risk ölçümü *Historical Method*, *The Variance-Covariance Method* ve *Monte Carlo Simulation* teknikleri kullanılarak hesaplanmıştır. 

## Some Assumptions

- *The Variance-Covariance Method* için Value at Risk hesaplanması hisse senedi getirilerinin normal olarak dağıtıldığını varsaymaktadır. 
- Monte Carlo simülasyonu, rastgele denemeler oluşturan herhangi bir yöntemi ifade etmektedir.

## Approach

In order for the Value at Risk model to work, initially the desired stockname, startdate and enddate variables must be defined. 
Later, the days, startprice, sigma and mu values can be defined and the desired results can be achieved by running the VaRclass.py file after reaching the location.

## Results

- The results.firstgraph () output draws us the historical distribution graph for the stock for which we calculate VaR.

![Stock Trading Dist](./Extra/HistDist.png)

- The results.secondgraph () output draws us the histogram of the open daily returns distribution graph for the stock for which we calculate VaR.

![Stock Trading Dist_2](./Extra/DailyReturn.png)

- results.stdperc() output give us the standard deviation value for the stock for which we calculate VaR.
- results.dist_QQ() output draws us the normal QQ plot graph for the stock for which we calculate VaR.

![Stock Trading Dist_3](./Extra/NormalQQ.png)

- results.dist_t() output draws us the student t plot graph for the stock for which we calculate VaR.

![Stock Trading Dist_4](./Extra/student_t.png)

- results.historicalVaR() output gives us the 0.99, 0.95 and 0.9 confidence interval VaR value and historical VaR graph for the stock for which we calculate VaR.

![Stock Trading Dist_5](./Extra/historicvar.png)

- results.VaR_Cov() output gives us the covariance VaR value and Covariance VaR graph for the stock for which we calculate VaR.

![Stock Trading Dist_6](./Extra/Cov.png)

- results.mcscalcgraph() output draws us the monte carlo sim plot graph for the stock for which we calculate VaR.

![Stock Trading Dist_7](./Extra/MonteCarloSim.png)

- results.mcsrun(10000) gives us the monte carlo simulation results for which we calculate VaR.

In order to use this project, you'll need to install the required python packages:

You can download requirements via "pip install -r requirements"

```bash
pip3 install -r requirements.txt
```

Also you can visit my [Linkedin page](https://www.linkedin.com/in/taylan-polat/) or [Github Page](https://github.com/taylan95?tab=repositories)

## References

- [What is Value at Risk ?](https://www.investopedia.com/terms/v/var.asp)
- [Value at Risk with Python](https://risk-engineering.org/VaR/) 