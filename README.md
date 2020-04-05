# Octopus Agile Price Display

A simple node-red flow and Python script to display the current Octopus Agile
electricity price on a RaspberryPi equipped with a Pimoroni Micro Dot pHAT display:

![overview](docs/display.jpg)

TODO: take a better picture - the display looks better than this in real life!

It also provides a web interface using a node-red dashboard:

![overview](docs/dashboard.png)

The main functionality is provided by the node-red flow, with the Python script just
used to drive the LED display.

The node-red flow queries the Octopus Agile tariff API to fetch the half hourly rates
once per day and caches the prices in a simple SQLite file based database.

## Install





### Create the empty SQLite database

Create the data basefile file and enter SQLite command prompt:

```bash
sqlite3 agile_rates.sqlite
```

Create the table:

```
sqlite> create table rates(start_time unsigned integer primary key, cost unsigned smallint);
```

### Configure the node-red flow



### Run

```
npm start
```

