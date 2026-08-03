# 📈 CAF Capstone: Stock Price Viewer

Build and deploy an interactive web application that compares the historical stock prices of two publicly traded companies.

In this Capstone, you'll use **Streamlit** to create a simple web app where a user enters two stock ticker symbols, selects a date range, and instantly sees both stocks plotted on the same chart using real market data.

The finished project is small enough to complete in a single sitting, but introduces several important skills you'll use again throughout the course.
---
# 🚀 Live Deployment

One of the most important parts of this Capstone is learning how to deploy your application.

A finished project should not only run locally.

It should be accessible to other people.

You will learn how to deploy your Streamlit application using **Streamlit Community Cloud**, creating your own public link that you can share in:

- your portfolio;
- your CV;
- LinkedIn;
- job applications.

The course video walks through the complete deployment process step by step.


---

# What You'll Build

Your application will allow a user to:

- Enter two stock ticker symbols (for example, `AAPL` and `MSFT`)
- Select a date range
- Download historical stock prices
- Compare both stocks on a single chart

Instead of producing output in the terminal, you'll build an application that anyone can open in a web browser and interact with.

---

# Why This Project?

This Capstone introduces the complete workflow of building a small Python application from start to finish.

While building it, you'll practice:

- building a web interface with `Streamlit`;
- collecting real-world data using `yfinance`;
- visualizing data with `Matplotlib`;
- creating a project that can be shared with other people.

Although the application is simple, it follows the same development process used for much larger projects.

---

# Repository

```text
CAF-stock-price-viewer/
│
├── app.py
├── requirements.txt
└── README.md
```


---

This application makes it easy to analyze and compare stock performance over time with a user-friendly interface.

![Screenshot 2024-05-21 at 14 26 10](https://github.com/Foxfix/stock_viewer/assets/16303236/cbe57b57-c535-486c-b7bf-8adaffece1f7)

---

# Running the Project

Install the required packages:

```bash
pip install -r requirements.txt
```

Start the application:

```bash
streamlit run app.py
```

Your browser should open automatically.

Enter two valid stock ticker symbols, choose a date range, and the comparison chart will be displayed.

---

# Your Assignment

Your goal is to understand how the application works, not just run it.

Before moving on, make sure you can explain:

- where the stock data comes from;
- how the user inputs are collected;
- how the chart is generated;
- how Streamlit turns a Python script into a web application.

Being able to explain the project is just as important as getting it to run.

---

# Challenge Yourself

Once the base application is working, try extending it.

Some ideas include:

- Compare three or more companies.
- Display percentage returns instead of raw prices.
- Add moving averages.
- Show trading volume.
- Display basic summary statistics.
- Allow users to choose different chart styles.

Try implementing one improvement without following a tutorial.

That's where the real learning happens.

---

## 🎥 Video Course

<p align="center">
  <a href="https://youtu.be/XQaUNNLNqHU">
    <img src="https://img.youtube.com/vi/XQaUNNLNqHU/maxresdefault.jpg" alt="Python Course" width="800">
  </a>
</p>

<p align="center">
  <strong>Streamlit Full Course for Beginners | Build & Deploy a Stock Dashboard with Python</strong><br>
  Follow the YouTube course and practice with the assignments in this repository.
</p>

<p align="center">
  <a href="https://youtu.be/XQaUNNLNqHU">
    <img src="https://img.shields.io/badge/▶%20Watch%20on-YouTube-red?style=for-the-badge&logo=youtube" alt="Watch on YouTube">
  </a>
</p>
