- [PMO India Website](https://www.pmindia.gov.in/ory/%e0%ac%b8%e0%ac%a6%e0%ad%8d%e0%ad%9f%e0%ac%a4%e0%ac%ae-%e0%ac%96%e0%ac%ac%e0%ac%b0/)

- I scrapped 2M tokens from PMO website, using the code given here.

- The task is divided into two parts : -
  - Loading the links from PMO website.
  - Scrapping a given link.

- Most of the time was spent in loading all the links, since the website is dynamically loaded. So I used Selenium library to continiously scroll down for a full-night.

- This has its limit. The older links (before 2019) do not scrapped easily. They throw plenty of errors. 

- Of the collected links, 2/3rd part was successfully scrapped.
