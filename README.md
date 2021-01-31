# Team 16: DQM Maximization of COVID Vaccine Distribution
Manjunath Rao, Vincent Pisani, Gary Sung, Anna Kristha Almazán Favela

## Introduction
**Purpose:** To maximize state vaccination rates based on varying shipments of vaccine doses across a distribution network.
**Knapsack Problem Summary:** You need to fill a small trick-or-treat bag with the best combination of candy without breaking the bag. Each item in the knapsack has a weight and value.

**DQM:** In this model, the federal vaccine distribution center is receiving offers from states to ship a given number of vaccines. The distribution center's goal is to maximize the number of people who receive the vaccine. It must consider the rate of vaccine administration per state as well as the sizes of the shipment offers to put as many vaccines as possible to good use.



## Example Sample Set
Total Vaccine Deliveries (per week)
* Delivery 1 = 50400
* Delivery 2 = 1000
* Delivery 3 = 2000
* Delivery 4 = 68400
* Delivery 5 = 1000
* Delivery 6 = 43200
* Delivery 7 = 72000
* Delivery 8 = 1900
* Delivery 9 = 61200
* Delivery 10 = 61200


Knapsack Value: Vaccinated Count
* California      3,000,000
* Ohio              900,000
* Massachusetts     550,000

Rounded values from US Labratory Testing

Knapsack Weight: Delivery Rate
* California         54.63%
* Ohio               58.63%
* Massachusetts      51.56%

Within each state: divided total doses administered by total distributed


Total knapsack value = total doses administered (Our Goal, objective function)
Total knapsack weight = total doses distributed for CA, OH, MA (8,280,950)

## Data Collection
Centrally Distributed Vaccines and Ancillary Kits
* Moderna: kits with 100 doses or pallet with 3,600 doses
* Pfizer: kits with 975 doses or pallet with 7,800 doses

Delivery
* Vaccine Kits/Pallets: 3600, 100, 100, 3600, 100, 3600, 3600, 100, 3600, 3600
* Kits/Pallet Count per Delivery: 14, 10, 20, 19, 10, 12, 20, 19, 17, 17
* For now, delivery based on the CDC Moderna weekly shipment of doses
Shipments suggest that truckloads generally hold <50% capacity of pallets


CDC COVID [Data Tracker](https://covid.cdc.gov/covid-data-tracker/index.html#datatracker-home) - [US Lab Testing](https://covid.cdc.gov/covid-data-tracker/#testing_tests7day)

[CDC Vaccine Shipment Sizes](http://publichealth.lacounty.gov/acd/docs/COVID-19VaccineProductInfoGuide.pdf)

[Number of Pallets per Full Truckload](https://www.freightrun.com/blog/post/full-truckloads-how-many-pallets-will-fit)


![US Laboratory Testing](https://github.com/iQuHACK/2021_Team16/blob/main/images/US%20Lab%20Testing.png)
![CA, MA, OH Data](https://github.com/iQuHACK/2021_Team16/blob/main/images/CA%2C%20MA%2C%20OH.png)


## Installing
This project requires Python 3. To setup and install the dependencies, run the following commands:

```
cd (cloned git repo location here)
python -m venv venv
(for linux users) source venv/bin/activate
(for windows) .\venv\Scripts\activate
pip install -r requirements.txt
```

On subsequent visits, run `source venv/bin/activate` to reactivate the virtual environment.

## Running
You can run the project from the command line or using a Jupyter notebook.

### Command line
From the command line, run `python3 shipment_test.py`. The results are printed to standard output.

#### Jupyter notebook
To start the Jupyter notebook, run `jupyter notebook`. Wait for the browser window to open, then click on the file named `shipment_test.ipynb`.

*TODO(Turtle1331) Leap authentication instructions*


## References
1. [CDC Moderna Vaccine Distribution Allocations](https://data.cdc.gov/Vaccinations/COVID-19-Vaccine-Distribution-Allocations-by-Juris/b7pe-5nws)
2. [CDC Pfizer Vaccine Distribution Allocations](https://data.cdc.gov/Vaccinations/COVID-19-Vaccine-Distribution-Allocations-by-Juris/saz5-9hgg)
3. [ACIP's Phased Allocation of COVID-19 Vaccines](https://www.cdc.gov/vaccines/acip/meetings/downloads/slides-2020-12/slides-12-20/02-COVID-Dooling.pdf)
4. [Visualization, COVID-19 Distribution by State](https://www.usatoday.com/in-depth/graphics/2021/01/14/covid-vaccine-distribution-by-state-how-many-covid-vaccines-have-been-given-in-us-how-many-people/6599531002/)

## Academic
1. [Andrew Lucas NP-Complete NP-Hard](https://arxiv.org/pdf/1302.5843.pdf)
2. [D-Wave Knapsack Example](https://github.com/dwave-examples/knapsack/blob/master/knapsack.py#L52)
3. [D-Wave Discrete Quadratic Model (DQM)](https://docs.ocean.dwavesys.com/en/stable/concepts/dqm.html)

## New to D-Wave?
1. [D-Wave Leap Sign Up](https://cloud.dwavesys.com/leap/)
2. Leap IDE https://ide.dwavesys.io/#(github username here)
