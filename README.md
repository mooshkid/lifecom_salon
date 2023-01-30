# Python Selenium - Hair Salon

The purpose of this project is to extract all salon details from [https://hair-chiba.or.jp/category/salon](https://hair-chiba.or.jp/category/salon/).

## Description

The script first creates a list of all the salon page urls. Then it will scrape the details table found on each page into a pandas data frame to be output as a excel/csv file format. 

## Getting Started

### Prerequisites
Python enviroment with the following dependencies installed.

### Dependencies

-   Selenium
-   ChromeDriver
-   Pandas


## Usage

-  run `main.py`

```
py main.py
```


## Authors

Masa Yamanaka - [yamanaka@lcom-group.jp](yamanaka@lcom-group.jp)

## Version History

-   2.0
    -   Combined `salon_url.py` and `salon_details.py` into one `main.py` script.
-   1.1
    -   Various bug fixes and optimizations
    -   See [commit change]() or See [release history]()
    -   Stuff
-   1.0
    -   Initial Release

## License


## References

-   [https://stackoverflow.com/questions/51176690/looping-over-pages-until-it-cant-find-the-next-link](https://stackoverflow.com/questions/51176690/looping-over-pages-until-it-cant-find-the-next-link)
-   [https://stackoverflow.com/questions/54862426/python-selenium-get-href-value](https://stackoverflow.com/questions/54862426/python-selenium-get-href-value)
-   [https://sparkbyexamples.com/pandas/how-to-append-row-to-pandas-dataframe/](https://sparkbyexamples.com/pandas/how-to-append-row-to-pandas-dataframe/)
