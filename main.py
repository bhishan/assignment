import kivy
import mechanize
from bs4 import BeautifulSoup
from kivy.app import App
from kivy.uix.label import Label
class MyApp(App):
    def build(self):

        br = mechanize.Browser()
        br.set_handle_robots(False)
        br.addheaders = [("User-agent","Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.13) Gecko/20101206 Ubuntu/10.10 (maverick) Firefox/3.6.13")]

        sign_in = br.open("http://school.dwit.edu.np/login/index.php")  #the login url

        br.select_form(nr = 0) #accessing form by their index. Since we have only one form in this example, nr =0.
#br.select_form(name = "form name") Alternatively you may use this instead of the above line if your form has name attribute available.

        br["username"] = "bhishan_0306" #the key "username" is the variable that takes the username/email value 

        br["password"] = "Lenovo!1"    #the key "password" is the variable that takes the password value

        logged_in = br.submit()   #submitting the login credentials
        logincheck = logged_in.read()
        initial_soup = BeautifulSoup(logincheck)
        url_checker = "http://school.dwit.edu.np/mod/assign/view.php?id="
        assignment_details = ""
        for link in initial_soup.find_all('a'):
            if link.get('href')[:49] == url_checker:


                req = br.open(link.get('href')).read() 
                soup = BeautifulSoup(req)
                counter = 0
                for p in soup.find_all("p"):
                    if counter>=2:
                        break
                    assignment_details += p.get_text() + "\n" 
                    counter+=1
        return Label(text=assignment_details)


if __name__ == '__main__':
    MyApp().run()
