import requests
from bs4 import BeautifulSoup
from pywhatkit import sendwhatmsg_instantly
import pyautogui
import time
import keyboard as k
def get_weather(city):
    url = f"https://www.google.com/search?q=weather+{city}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    temperature = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    time_sky = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
    sky = time_sky.split('\n')[1]

    return temperature, sky

def send_whatsapp_message(to_phone, message):
    sendwhatmsg_instantly(to_phone, message)
    pyautogui.click(1050, 950)
    time.sleep(20)
    k.press_and_release('enter')


def main():
    city = input("Enter the city: ")
    to_phone = "+916363989289"  # Replace with recipient's WhatsApp number (including country code)

    try:
        temperature, sky = get_weather(city)
        rainy_conditions = ["Rainy", "Rain And Snow", "Showers", "Haze", "Cloudy"]
        if sky in rainy_conditions:
            message_body = f"Take an umbrella before leaving. Weather in {city}: {sky}, Temperature: {temperature}"
            print("Sending WhatsApp alert:", message_body)
            send_whatsapp_message(to_phone, message_body)
        else:
            print(f"No need for an umbrella. Weather in {city}: {sky}, Temperature: {temperature}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()