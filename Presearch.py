import time
import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.by import By

window = tk.Tk()
window.geometry("550x350")
window.resizable(False, False)
window.title("PresearchBot")
window.iconbitmap('./files./icon.ico')

def getWords():
    with open('./files/words.txt') as f:
        return f.readlines()

def saveWords():
    words = wordsTextBox.get(index1=1.0, index2=tk.END).splitlines()
    with open('./files/words.txt', 'w') as f:
        for i in range(len(words)):
            if(i != len(words)-1):
                f.write(words[i])
                f.write('\n')
            else:
                f.write(words[i])
    setStatus('Kaydedildi')

def setStatus(text):
    statusLabel.config(text="Durum : " + text)

def bot():
    #Opera
    options = webdriver.ChromeOptions()
    options.add_experimental_option('w3c', True)
    driver = webdriver.Opera(options=options, executable_path='./files/operadriver.exe')

    #Chrome
    # driver = webdriver.Chrome(executable_path='./files/chromedriver.exe')
    
    if waitForVpn.get():
        driver.set_window_size(1200,500)
        driver.get("opera://settings/vpnWithDisclaimer")
        time.sleep(5)

    driver.set_window_size(500,500)
    second = int(secondTextBox.get())

    for i in range(5):
        try:
            setStatus("Presearch'a giriliyor'")
            driver.get("https://presearch.com/")
            time.sleep(1)
            break
        except:
            setStatus('Adres Başlatılamadı ! Deneme ', i+1)
            if(i == 4):
                setStatus("Başarısız !")
                driver.close()
                return
        

    for i in range(5):
        setStatus("Giriş deneniyor")

        driver.find_element(by=By.XPATH, value='/html/body/div/div[4]/div[1]/div[2]/div/div[2]/div').click()
        # opera
        #/html/body/div/div[4]/div[1]/div[2]/div/div[2]/div => register or login btn
        #/html/body/div[1]/div[3]/div[1]/form/div[1]/input email input

        # chrome
        #/html/body/div[1]/div[2]/div/div[2]/div[3]/div[1]/form/div[1]/input => register or login btn
        #time.sleep(5)
        #driver.switch_to.window(driver.window_handles[1])

        while (len(driver.window_handles) != 2): #for opera != 2 // for chrome != 1
            time.sleep(1)

        setStatus("Giriş yapıldı")
        break

    kelimeler = wordsTextBox.get(index1=1.0, index2=tk.END).splitlines()
    driver.get("https://engine.presearch.org/search?q=" + kelimeler[0])

    time.sleep(second)
    for i in range(1,len(kelimeler)):
        setStatus("Arama yapılıyor")

        searchinput = driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div[3]/div[1]/dic/div[2]/div[1]/div/form/div/input')
        searchbutton = driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div[3]/div[1]/dic/div[2]/div[1]/div/form/div/div/button')

        time.sleep(1)

        searchinput.clear()
        searchinput.send_keys(kelimeler[i])
        searchbutton.click()

        setStatus("Arama Yapıldı")

        time.sleep(second)
        
    setStatus("Başarılı !")

startButton = tk.Button(window, text="Başlat", bg="gray", fg="white", border="0", activebackground="#A9A9A9", command=bot)
startButton.pack()
startButton.place(anchor="n", height=75, width=250, x=150, y=50)

statusLabel = tk.Label(window, text="Durum : Boşta")
statusLabel.pack()
statusLabel.place(anchor="n", x=150, y=135)

wordsLabel = tk.Label(window, text="Aranacak Kelimeler")
wordsLabel.pack()
wordsLabel.place(anchor="n", height=25, width=250, x=425, y=25)

wordsTextBox = tk.Text(window, wrap='none')
wordsTextBox.pack()
wordsTextBox.place(anchor="n", height=200, width=200, x=425, y=50)

loadedWords = getWords()
for word in loadedWords:
    wordsTextBox.insert(tk.END, word)

secondLabel = tk.Label(window, text="Bekleme süresi (sn) : ")
secondLabel.pack()
secondLabel.place(anchor="n", x=90, y=200)

secondTextBox = tk.Entry(window)
secondTextBox.pack()
secondTextBox.place(anchor="n", x=210, y=200, width=75, height=23)
secondTextBox.insert(string="7", index=tk.END)

waitForVpn = tk.BooleanVar()
vpnLabel = tk.Label(window, text="Vpn Açmak İçin Bekle (5 sn)")
vpnLabel.pack() 
vpnLabel.place(anchor="n", x=110, y=225)

vpnCheckBox = tk.Checkbutton(window, variable=waitForVpn, onvalue=True, offvalue=False)
vpnCheckBox.pack()
vpnCheckBox.place(anchor="n", x=210, y=225, width=25, height=23)

saveWordsButton = tk.Button(window, text="Kaydet", bg="gray", fg="white", border="0", activebackground="#A9A9A9", command=saveWords)
saveWordsButton.pack()
saveWordsButton.place(anchor="n", height=30, width=100, x=425, y=275)

# Start the GUI
window.mainloop()