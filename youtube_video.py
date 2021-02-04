from pafy import new
import youtube_dl
import requests
import time
r = requests.session()
fil = r.get('https://pastebin.com/raw/WEScHrWH').text

print("""
██╗   ██╗ ██████╗ ██╗   ██╗
╚██╗ ██╔╝██╔═══██╗██║   ██║
 ╚████╔╝ ██║   ██║██║   ██║ ╔╦╗┬ ┬ ┌┐  ┌─┐
  ╚██╔╝  ██║   ██║██║   ██║  ║ │ │ ├┴┐ ├┤
   ██║   ╚██████╔╝╚██████╔╝  ╩ └─┘ └─┘ └─┘
   ╚═╝    ╚═════╝  ╚═════╝ Download Video""")
print(''+fil+'━━━━━━━━━━━━━━━━━━━━')
time.sleep(1.2)
filza = input("""
[1]>> تحميل مقطع واحد 
[2]>> تحميل اكثر من مقطع 
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Here : """)

print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
print(' ')



if filza == '1':
	url = input('Enter URL vedio --> :\n')
	
	try:
		print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
	
		vedio = new(url)
		
		vedi = vedio.getbest()
		
		vedi.download()
		
		print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
		print("        \nDone vedio ..")
	
	except ValueError:
		print(' Error url ..!')
	
	except OSError:
		print(' Error url ..!')
		
	except:
		print(' Error url ..!')



elif filza == '2':
	url2 = input('[1] Enter URL vedio --> :\n')

	url3 = input('[2] Enter URL vedio --> :\n')
	url4 = input('[3] Enter URL vedio --> :\n')
	url5 = input('[4] Enter URL vedio --> :\n')
	print('+++++++++++++++++++++++++\n')
	
	try:
	
		vedio2 = new(url2)
		
		vedi2 = vedio2.getbest()
		
		vedi2.download()
		print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
	except ValueError:
		print(' Error url ..!')
	
	except OSError:
		print(' Error url ..!')
		
	except:
		print(' Error url ..!') 
	
	
	
	
	try:
		
		vedio3 = new(url3)
		
		vedi3 = vedio3.getbest()
		
		vedi3.download()
		print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
	except ValueError:
		print(' Error url ..!')
	
	except OSError:
		print(' Error url ..!')
		
	except:
		print(' Error url ..!') 
	
	
	
	try:
		
		vedio4 = new(url4)
		
		vedi4 = vedio4.getbest()
		
		vedi4.download()
		print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
	except ValueError:
		print(' Error url ..!')
	
	except OSError:
		print(' Error url ..!')
		
	except:
		print(' Error url ..!') 
		
	
	
	
	try:
		vedio5 = new(url5)
		
		vedi5 = vedio5.getbest()
		
		vedi5.download()
		print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
		
		print("        \nDone vedio ..")
	
	except ValueError:
		print(' Error url ..!')
	
	except OSError:
		print(' Error url ..!')
		
	except:
		print(' Error url ..!') 




else:
	print('             [ Error ..! ]')
