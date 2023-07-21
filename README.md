# url_shortener

Using Python, I created a simple URL shortener that shortens a big website or any type of big URL. It takes a predefined user input (options) and then shortens the URL when we enter the required long website or URL.

The shortening of URL is possible due to the usage of pyshorteners library, it can be installed via this command:-

pip install pyshorteners

Additionally, I referred to the pyshorteners documentation https://pyshorteners.readthedocs.io/en/latest/ and followed https://github.com/ellisonleao/pyshorteners to get a hold on the topic of pyshorteners library.

Do note that the services used for URL shortening are TinyURL and Bitly. While TinyURL is directly integrated into the pyshorteners library, the Bitly URL shortening service is based on a subscription model and one has to open an account in order to integrate the Bitly API token into the library. (Also don't forget that Bitly's service is limited to some amount of URL shortening services in a month, so it's totally not free 🫠) 

You all can give it a try, though, for Bitly's service, you have to open a Bitly account; if you don't want to, then go for TinyURL one! :)

ALso, this is strictly restricted as of now to the CLI interface; anything related to GUI will be considered and updated in due time.
