import pyshorteners

print("URL SHORTENER" "\n""BITLY API AND TINYURL")

x=input("Type which option do you want? \na.TinyURL\nble .Bitly\n")

if(x=="a"):
	url=input("Enter the URL: ") #TinyURL shortener service
  	def short_url():
		t=pyshorteners.Shortener()
		print("The Shortened URL is: " + t.tinyurl.short(url))
	short_url()

elif(x=="b"):
	long_url = input("Enter the URL: ") #Bitly shortener service
  	b = pyshorteners.Shortener(api_key='344d2a038314910ed941d314fd8736777322abd9')
	short_url = b.bitly.short(long_url)
	print("The Shortened URL is: " + short_url)
	
else:
	print("Invalid Request, Exiting!")

#API key given in line 14 is completely based on my Bitly account and is limited to some tokens for a given time
#you will have to change the API key with any other one
