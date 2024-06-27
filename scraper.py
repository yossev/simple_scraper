from bs4 import BeautifulSoup
import requests

def scrape(newsurl):
    response =  requests.get(newsurl)
    # 200 is the code for a sucessful scrape
    if(response.status_code != 200):
        if(response.status_code == 404):
            print("Error getting news, status code is: " +
                  str(response.status_code))
            raise Exception(
                'looks like this page dont exists! Check if your URL is valid')
        else:
            print("Error getting news, status code is: " +
                  str(response.status_code))
            raise Exception(
                'Check if the URL is valid, if you have an internet connection or try later!')
        
    soupContent = BeautifulSoup(response.content, 'html.parser')

    # Fetch the headline of the scraped object and write it in a txt file
    headlineDiv = soupContent.find(class_="headline__text")
    headline = headlineDiv.text.strip()
    f = open(f"{headline}"+".txt", "a")
    f.write(f"{headline}" +"\n")
    f.write("- - - - - - - - - - - - - - - - - - \n")


    # find all the divs that have class paragraph, loop through them and then add them to the body
    AllDivParagraphs = soupContent.find_all(
        'p', class_='paragraph'
    )
    body = ''

    for paragraph in AllDivParagraphs:
        body += paragraph.text.strip() + "\n"

    f.write(body)
    
    # find the timestamp for the article and write it 

    timeStampTag = soupContent.find(
        class_='timestamp'
    )

    timeStamp = timeStampTag.text
    f.write("- - - - - - - - - - - - - - - - - -")
    f.write(timeStamp)

def main():
    newsurl = None

    newsurl = str(input("Enter the URL of the CNN Post you would like to scrape, or exit to exit : \n"))

    # Exit the function if requested
    if(newsurl == "exit"):
        exit() 
    else:
        print("Now Scraping "+f"{newsurl}"+"...")
        scrape(newsurl)

if __name__ == "__main__":
    main()