from selenium import webdriver
#todo: import BY
#todo: import pandas

def web_driver():
  options = webdriver.ChromeOptions()
  options.add_argument('--verbose')
  options.add_argument('--no-sandbox')
  options.add_argument('--headless')
  options.add_argument('--disabled-gpu')
  options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome(options=options)
  return driver

driver = web_driver()

for i, cpf in enumerate(tabela["CPF"]):
    email = tabela.loc[i, "Email"]
    descricao = tabela.loc[i, "Descricao"]
    valor = tabela.loc[i, "Valor"]

    driver.get('https://docs.google.com/spreadsheets/d/1I8z2hVLoX7dkgWfDhc17ez17o67YRrRVMtLuXZEg9As/edit?gid=0#gid=0')

    #todo: implement xpath form field
    driver.find_element(By.XPATH, '//p[@class="price_color"]').send_keys(cpf)
    driver.find_element(By.XPATH, '//p[@class="price_color"]').send_keys(email)
    driver.find_element(By.XPATH, '//p[@class="price_color"]').send_keys(descricao)
    driver.find_element(By.XPATH, '//p[@class="price_color"]').send_keys(valor)
