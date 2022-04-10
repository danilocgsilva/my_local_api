# My local api

Sometimes, you will need access apis that you don't would like to allow in some public domain. So here we have an easy way to setup locally endpoints apis, with your secret key running locally.

## How to use

1. Install the utility, going to the root directory and running the following command:

`pip install .`

2. Just execute in any location:

`mylocalapi`

This will rise a local http data provider that can be consumed anytime locally. The default port is 5000, but you can set a different por with the following parameter:

`mylocalapi --port 5001`

## First usage: currency convertion

Set in your environment a variable called `EXCHANGERATE_KEY` storing your personal key from `https://app.exchangerate-api.com`, where the local api will query currency data. Then, to query data, access:

```
http://localhost:5000/currency/<CURRENCY>
```
Where the `<CURRENCY>` is the currency code (check https://pt.wikipedia.org/wiki/ISO_4217) that will be converted do Dollar (USD).


