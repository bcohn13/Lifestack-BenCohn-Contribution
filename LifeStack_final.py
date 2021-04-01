import random
import requests
from bs4 import BeautifulSoup
import time

#This is an example Python Script that I wrote.
class User:
    """A class that simulates an app user"""
    
    def __init__(self,age,sex,weight,height):
        """Initializes the user.
        
        Raises:
            ValueError: Raised if an invalid sex is 
            entered, the age entered is below 18 or
            if the height or weight values entered
            are not numbers.
        """
        self.age=age
        self.sex=sex
        self.weight=weight
        self.height=height
        
        if int(self.age) < 18:
            raise ValueError("There is an age restriction for this app.")
        
        if self.sex !="male" and self.sex !="female":
            raise ValueError("Please enter a valid sex.")
        
        if not self.weight.isnumeric():
            raise ValueError("Please enter a valid weight.")
        
        if not self.height.isnumeric():
            raise ValueError("Please enter a valid height.")
        
def find_url(sex,age,weight,height):
    """Finds urls that contain information about a User's health.
    
    Args:
        sex (str): The physical sex of a User.
        age (int): The age of a User.
        weight (float): The weight of a User.
        height (float): The height of a User.
        
    Returns:
        url (str): A url to use for a websearch.
    """
    
    browser=["www.google","search.yahoo","duckduckgo"]
    url=requests.get("https://"+random.choice(browser)+
    ".com/search?q=health+advice "
    +str(sex)+" "+str(age)+" "+str(weight)+" "+str(height)+
    "&oq=health+advice+for&aqs=chrome."+
    ".69i57.20598j0j9&sourceid=chrome&ie=UTF-8")
    return url
        
def find_advice(user):
    """Uses the url link and the data from the User to find urls with releveant
    advice.
    
    Args:
        user (User): A User object with features that will be examined.
    """
    req = find_url(user.sex,user.age,user.weight,user.height)
    cont=req.content
    soup = BeautifulSoup(cont, features="html.parser")
    #found on 
    #https://stackoverflow.com/questions/5815747/beautifulsoup-getting-href
    for a in soup.find_all('a', href=True):
        time.sleep(1)
        if "/search?" in a["href"]:
            if "https:" not in a["href"]:
                print("https:"+a["href"])
            else:
                print(a["href"])

def main():
    """Runs the program using input values.
    """
    
    age=input("Enter your age: ")
    sex=input("Enter male or female: ")
    weight=input("Enter your weight: ")
    height=input("Enter your height: ")
    user=User(age,sex,weight,height)
    find_advice(user)
    
main()