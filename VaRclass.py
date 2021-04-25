#Libraries
import pandas as pd
import numpy as np
from datetime import timedelta, timezone, datetime
from yahoofinancials import YahooFinancials
import matplotlib.pyplot as plt
from scipy.stats import stats
import datetime
import scipy
from datetime import datetime

def retrieve_stock_data(ticker, start, end):
    json = YahooFinancials(ticker).get_historical_price_data(start, end, "daily")
    df = pd.DataFrame(columns=["open","close","adjclose"])
    for row in json[ticker]["prices"]:
        date = datetime.fromisoformat(row["formatted_date"])
        df.loc[date] = [row["open"], row["close"], row["adjclose"]]
    df.index.name = "date"
    return df

stock = str(input("please type the stock name: "))
startdate = str(input("please type the startdate: "))
enddate = str(input("please type the enddate: "))

data = retrieve_stock_data(stock, startdate, enddate)

#You can prefer below style.
#data = pd.read_excel("sim_deneme.xlsx")
#data.head()
#data.index = dat.DATE
#data.drop(["DATE"],axis = 1,inplace = True)

class VaRCalculation:
    def __init__(self,data,days,startprice,sigma,mu):
        self.data = data
        self.days = days
        self.startprice = startprice
        self.sigma = sigma
        self.mu = mu
        self.dt = 1/float(self.days)
        self.price = np.zeros(self.days)
        self.shock = np.zeros(self.days)
        self.price[0] = self.startprice

    def firstgraph(self):
        fig = plt.figure()
        fig.set_size_inches(10,3)
        plt.plot(self.data.iloc[:,0],color = "blue")
        plt.title("{} stock in 2018".format(self.data.columns[0]), weight="bold");
        
    def secondgraph(self):
        plt.hist(self.data.iloc[:,0].pct_change(),bins=50, density=True, histtype="stepfilled", alpha=0.5)
        plt.title("Histogram of {} daily returns".format(self.data.columns[0]), weight="bold")
        
    def stdperc(self):
        print("std: {}".format(self.data.iloc[:,0].pct_change().std()))
        
    def dist_QQ(self):
        Q = self.data.iloc[:,0].pct_change().dropna()
        scipy.stats.probplot(Q, dist=scipy.stats.norm, plot=plt.figure().add_subplot(111))
        plt.title("Normal QQ-plot of {} daily returns in 2018".format(self.data.columns[0]), weight="bold");
        
    def dist_t(self):
        Q = self.data.iloc[:,0].pct_change().dropna()
        tdata, tav, tsigma = scipy.stats.t.fit(Q)
        scipy.stats.probplot(Q, dist=scipy.stats.t, sparams=(tdata, tav, tsigma), plot=plt.figure().add_subplot(111))
        plt.title("Student QQ-plot of {} daily returns in 2018".format(self.data.columns[0]), weight="bold");
        
    def historicalVaR(self):
        returns = self.data.iloc[:,0].pct_change().dropna()
        returns.hist(bins=40, density=True, histtype="stepfilled", alpha=0.5)
        #startdate = datetime.datetime.strftime(self.data.index[0],"%Y-%m-%d") 
        #enddate = datetime.datetime.strftime(self.data.index[-1],"%Y-%m-%d")
        plt.title("Daily returns on {}, 2018".format(self.data.columns[0]), weight="bold");
        quantileVaR = [returns.quantile(i) for i in [0.01,0.05,0.1]]
        print("for 0.01: {},for 0.05: {},for 0.1: {}".format(quantileVaR[0],quantileVaR[1],quantileVaR[2]))
       
    def VaR_Cov(self):
        Q = self.data.iloc[:,0].pct_change().dropna()
        tdata, tav, tsigma = scipy.stats.t.fit(Q)
        returns = self.data.iloc[:,0].pct_change().dropna()
        mean = returns.mean()
        sigma = returns.std()
        support = np.linspace(returns.min(), returns.max(), 100)
        returns.hist(bins=40, density=True, histtype="stepfilled", alpha=0.5);
        plt.plot(support, scipy.stats.t.pdf(support, loc=tav, scale=tsigma, df=tdata), "r-")
        plt.title("Daily change in HAL over 2010–2014 (%)", weight="bold");
        VaRCov = scipy.stats.norm.ppf(0.05, mean, sigma)
        print("Covariance VaR Value: {}".format(VaRCov))
        
    def mcscalc(self):
        for v in range(1,self.days):
            self.shock[v] = np.random.normal(loc = self.mu*self.dt,scale = self.sigma*np.sqrt(self.dt))
            self.price[v] = max(0,self.price[v-1]+self.shock[v]*self.price[v-1])
        return self.price
    
    def mcscalcgraph(self):
        plt.figure(figsize=(9,4))    
        for run in range(30):
            plt.plot(self.mcscalc())
            plt.xlabel("Time")
            plt.ylabel("Price")
            
    def mcsrun(self,runs):
        simulations = np.zeros(runs)
        for run in range(runs):
            simulations[run] = self.mcscalc()[self.days-1]
            q = np.percentile(simulations, 1)
            plt.hist(simulations, density=True, bins=30, histtype="stepfilled", alpha=0.5)
            plt.figtext(0.6, 0.8, "Start price: 10€")
            plt.figtext(0.6, 0.7, "Mean final price: {:.3}€".format(simulations.mean()))
            plt.figtext(0.6, 0.6, "VaR(0.99): {:.3}€".format(10 - q))
            plt.figtext(0.15, 0.6, "q(0.99): {:.3}€".format(q))
            plt.axvline(x=q, linewidth=4, color="r")
            plt.title("Final price distribution after {} days".format(self.days), weight="bold");


days = int(input("Please enter prediction days: "))
startprice = float(input("Please enter startprice:"))
sigma = float(input("Please enter sigma value: "))
mu = float(input("Please enter mu value: "))

results = VaRCalculation(data,days,startprice,sigma,mu)
        
results.firstgraph()                
results.secondgraph()        
results.stdperc()
results.dist_QQ()
results.dist_t()
results.historicalVaR()
results.VaR_Cov()
results.mcscalc()
results.mcscalcgraph()
results.mcsrun(10000)

