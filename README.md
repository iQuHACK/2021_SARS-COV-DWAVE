# Team 16: DQM Maximization of COVID Vaccine  Distribution
Manjunath Rao, Vincent Pisani, Gary Sung, Anna Kristha Almazán Favela

## Introduction




## Example Sample Set
Total Vaccine Deliveries (per week)
* Delivery 1 = 50400
* Delivery 2 = 78000
* Delivery 3 = 19500
* Delivery 4 = 68400
* Delivery 5 = 1000
* Delivery 6 = 43200
* Delivery 7 = 72000
* Delivery 8 = 1900
* Delivery 9 = 132600
* Delivery 10 = 132600


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
* Vaccine Kits/Pallets: 3600, 7800, 975, 3600, 100, 3600, 3600, 100, 7800, 7800
* Kits/Pallet Count per Delivery: 14, 10, 20, 19, 10, 12, 20, 19, 17, 17
* Based on the CDC Moderna and Pfizer weekly shipment of doses data.
Shipments suggest that truckloads generally hold <50% capacity of pallets


CDC COVID [Data Tracker](https://covid.cdc.gov/covid-data-tracker/index.html#datatracker-home) - [US Lab Testing](https://covid.cdc.gov/covid-data-tracker/#testing_tests7day)

[CDC Vaccine Shipment Sizes](http://publichealth.lacounty.gov/acd/docs/COVID-19VaccineProductInfoGuide.pdf)

[Number of Pallets per Full Truckload](https://www.freightrun.com/blog/post/full-truckloads-how-many-pallets-will-fit)


![US Laboratory Testing](https://github.com/iQuHACK/2021_Team16/blob/main/images/US%20Lab%20Testing.png)
![CA, MA, OH Data](https://github.com/iQuHACK/2021_Team16/blob/main/images/CA%2C%20MA%2C%20OH.png)

## Basic Principles




## To-Do


## Installing
This project requires Python 3. To setup and install the dependencies, run the following commands:

```
python -m venv venv
source venv/bin/activate
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
