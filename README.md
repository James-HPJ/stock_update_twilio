# Tesla Stock Tracker

This Python project tracks the stock prices of Tesla using the Alpha Vantage API and retrieves news articles about the company from the NewsAPI. It then utilizes the Twilio WhatsApp service to send a WhatsApp message to a specified mobile phone number. The message includes the percentage change in stock price from yesterday's closing to the day before yesterday's closing, along with three news articles related to Tesla.

## Prerequisites

Before running the project, ensure you have the following:

- Python 3 installed
- Required Python packages listed in `requirements.txt`
- Alpha Vantage API key (Get it from [Alpha Vantage](https://www.alphavantage.co/))
- NewsAPI key (Get it from [NewsAPI](https://newsapi.org/))
- Twilio account SID, auth token, and verified phone number (Get them from [Twilio](https://www.twilio.com/))

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/tesla-stock-tracker.git
   ```
2. Navigate to the project directory:
   ```
   cd tesla-stock-tracker
   ```
3. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```
4. Set up the necessary environment variables:

- A_VANTAGE_APIKEY - Your Alpha Vantage API key
- NEWSAPI_APIKEY - Your NewsAPI key
- TWILIO_ACC_SID - Your Twilio account SID
- TWILIO_AUTH_TOKEN - Your Twilio auth token
- TWILIO_NO - Your verified Twilio phone number
- YOUR_WHATSAPP_NO - Your whatsapp no to recieve the notification

  5.Run the Python script:

  ```
  python main.py
  ```

## Usage

Customize the script as needed to choose your own stock to monitor, the treshold of percentage difference in the stock price to activate notifications, or the body and format of the message sent.
