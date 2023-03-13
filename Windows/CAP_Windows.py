from selenium import webfriver
from selenium.webdriver.common.by import By
from time import sleep
import random

browser = webdriver.Chrome('Location of Chrome Driver')

login_id = 'Login ID'
login_pass = 'Password'

url = 'https://sas.benesse.ne.jp/classi/s/'
browser.get(url)

user_name_form = browser.find_element(By.XPATH,'//*[@id="student_form"]/div/div[1]/input')
user_name_form.send_keys(login_id)

user_password_form = browser.find_element(By.XPATH,'//*[@id="usr_password"]')
user_password_form.send_keys(login_pass)

login_button = browser.find_element(By.XPATH,'//*[@id="student_form"]/div/button')
login_button.click()

sleep(2)

input_element = ['楽しい一日だった！', '今日は少し疲れた。', 'たくさんのことをやり遂げることができた。','家でのんびり過ごした。','部活で楽しいことがあった','部活で嬉しいことがあった','友達を作ることができました','今日は忙しい1日でした','面白いニュースを聞いてほんわかとした気持ちになった','外で運動する時間があった','1日寝ないで集中することができた','今日は暑かった','いい出会いがあった','ずっと前から楽しみにしていたことが実現しました！','新しいことを学べた','今日1日、忙しすぎた','今日は、大切な人と過ごすことができた','ずっと食べたかったアイスを食べることができた','理想と現実が合わなかった','アレルギーだったピーナッツを克服することができた','おじいちゃんにMacBookを買ってもらった','おばあちゃんにiPhoneを買ってもらった','ひいおじいちゃんにApple Watchを買ってもらった','ひいおばあちゃんにiPadを買ってもらった','ひいひいおじいちゃんにAirPods Proを買ってもらった','ひいひいおばあちゃんにAirTagをつけた','1000円無くした','今日はとても天気が良かった','久しぶりに部屋の片付けをした','駅のホームで、ｳｰﾀﾝ､ｹﾞﾞﾝｷ! ｹﾞﾝｷ!と叫んでいる男がいた']

year = '2023'
month = '03'
day = 31

days_processed = day - 9

for number_of_repetitions in range(9):
    
    ordinary_number = len(input_element)
    number_processed = ordinary_number - 1
    random_number = random.randint(0,number_processed)

    sleep(2)

    created_url = ('https://study.classi.jp/reports/form/'+ year + '-' + month + '-0' + str(number_of_repetitions + 1))
    browser.get(created_url)

    sleep(2)

    text_to_enter = browser.find_element(By.XPATH,'/html/body/study-root/spen-single-column/div/main/study-my-report-form/form/div[2]/div[2]/study-student-message/div/div[2]/div/textarea')
    text_to_enter.clear()
    text_to_enter.send_keys((input_element[random_number]))

    sleep(2)

    confirm_contents_button = browser.find_element(By.XPATH,'/html/body/study-root/spen-single-column/div/main/study-my-report-form/form/div[2]/div[3]/button')
    confirm_contents_button.click()

    sleep(2)

for number_of_repetitions in range(days_processed):
    
    ordinary_number = len(input_element)
    number_processed = ordinary_number - 1
    random_number = random.randint(0,number_processed)

    sleep(2)

    created_url = ('https://study.classi.jp/reports/form/'+ year + '-' + month + '-' + str(number_of_repetitions + 10))
    browser.get(created_url)

    sleep(2)

    text_to_enter = browser.find_element(By.XPATH,'/html/body/study-root/spen-single-column/div/main/study-my-report-form/form/div[2]/div[2]/study-student-message/div/div[2]/div/textarea')
    text_to_enter.clear()
    text_to_enter.send_keys((input_element[random_number]))

    sleep(2)

    confirm_contents_button = browser.find_element(By.XPATH,'/html/body/study-root/spen-single-column/div/main/study-my-report-form/form/div[2]/div[3]/button')
    confirm_contents_button.click()

    sleep(2)

# © 2023 RK inc.
