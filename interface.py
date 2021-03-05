import tkinter as tk
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ReportBot:

    def __init__(self):
        self.root = tk.Tk()
        self.frame_id_jogadores = tk.LabelFrame(self.root, text="Elementos para Reportar", padx=40, pady=15)
        self.report1_entry = tk.Entry(self.frame_id_jogadores, width=70)
        self.report2_entry = tk.Entry(self.frame_id_jogadores, width=70)
        self.report3_entry = tk.Entry(self.frame_id_jogadores, width=70)
        self.driver = None
        self.community = tk.StringVar()
        self.a, self.b, self.c, self.d, self.e = tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar(), \
                                                 tk.BooleanVar(), tk.BooleanVar()
        self.jogadores = []
        self.lista = []

    def criar_interface(self):
        self.root.title("Report CSGO Players")

        self.frame_id_jogadores.grid(row=0, column=0, sticky=tk.E + tk.N + tk.S + tk.W, ipadx=5, ipady=5, padx=5,
                                     pady=5)

        label_explicacao = tk.Label(self.frame_id_jogadores, text="Abaixo coloque os perfis que deseja denunciar:")
        label_explicacao.config(font=(20))
        label_explicacao.grid(row=0, column=0, columnspan=2, pady=20, padx=20)

        # REPORTSSSSS PLAYERS
        self.frame_id_jogadores.columnconfigure(0, weight=1)
        self.frame_id_jogadores.columnconfigure(1, weight=2)

        # PERFIL 1
        report1_label = tk.Label(self.frame_id_jogadores, text="Perfil 1:")
        report1_label.grid(row=1, column=0, sticky=tk.E, padx=20)

        self.report1_entry.grid(row=1, column=1, padx=20, pady=20, sticky=tk.W + tk.E)

        # PERFIL 2
        report2_label = tk.Label(self.frame_id_jogadores, text="Perfil 2:")
        report2_label.grid(row=2, column=0, sticky=tk.E, padx=20, pady=(0, 20))

        self.report2_entry.grid(row=2, column=1, padx=20, pady=(0, 20), sticky=tk.W + tk.E)

        # PERFIL 3
        report3_label = tk.Label(self.frame_id_jogadores, text="Perfil 3:")
        report3_label.grid(row=3, column=0, sticky=tk.E, padx=20, pady=(0, 20))

        self.report3_entry.grid(row=3, column=1, padx=20, pady=(0, 20), sticky=tk.W + tk.E)

        # FRAME TIPOS DE REPORT ----------------------------------------------------------------------------------------
        frame_report = tk.LabelFrame(self.root, text="Formas de Denúnica", padx=40, pady=15)
        frame_report.grid(row=1, column=0, sticky=tk.E + tk.N + tk.S + tk.W, ipadx=5, ipady=5, padx=5, pady=5)

        # REPORT CS:GO - TYPE: CHECKBUTTONS ----------------------------------------------------------------------------
        # CHECKSBUTTON
        frame_CSGO_report = tk.LabelFrame(frame_report, text="CS:GO REPORT", padx=40, pady=15)
        frame_CSGO_report.grid(row=0, column=0, sticky=tk.E + tk.N + tk.S + tk.W, ipadx=5, ipady=5, padx=5, pady=5)

        aa = tk.Checkbutton(frame_CSGO_report, text="Abusive Communications or Profile", anchor='w', variable=self.a)
        aa.pack(fil='both')

        bb = tk.Checkbutton(frame_CSGO_report, text="Griefing", anchor='w', variable=self.b)
        bb.pack(fil='both')

        cc = tk.Checkbutton(frame_CSGO_report, text="Wall Hacking", anchor='w', variable=self.c)
        cc.pack(fil='both')

        dd = tk.Checkbutton(frame_CSGO_report, text="Aim Hacking", anchor='w', variable=self.d)
        dd.pack(fil='both')

        ee = tk.Checkbutton(frame_CSGO_report, text="Other Hacking", anchor='w', variable=self.e)
        ee.pack(fil='both')

        self.lista.extend((self.a, self.b, self.c, self.d, self.e))

        # REPORT COMMUNITY - TYPE: RADIOBUTTONS ------------------------------------------------------------------------
        MODES = [
            ('Inappropiate or Offensive Content', '542'),
            ('Spamming, Annoying or Harassment', '643'),
            ('Theft, Scamming, Fraud or Malicious', '144'),
            ('Cheating in a Game', '541'),
            ('Random', 'random')
        ]

        frame_COMMUNITY_report = tk.LabelFrame(frame_report, text="COMMUNITY REPORT", padx=40, pady=15)
        frame_COMMUNITY_report.grid(row=0, column=1, sticky=tk.E + tk.N + tk.S + tk.W, ipadx=5, ipady=5, padx=5, pady=5)

        self.community.set('541')

        for text, value in MODES:
            tk.Radiobutton(frame_COMMUNITY_report, variable=self.community, text=text, value=value).pack(anchor=tk.W)

        # BUTTON REPORT ------------------------------------------------------------------------------------------------
        iniciar_programa = tk.Button(self.root, text="REPORTAR!", fg="white", bg="gray", command=self.iniciar_selenium)
        iniciar_programa.config(font=('Helvetica 15 bold'))
        iniciar_programa.grid(row=10, column=0, columnspan=2, padx=20, pady=(0, 20), sticky=tk.W + tk.E)

        self.root.mainloop()

    def iniciar_selenium(self):
        options = webdriver.ChromeOptions()
        options.add_argument('start-maximized')
        options.add_argument('disable-infobars')
        options.add_argument('--disable-extensions')

        self.driver = webdriver.Chrome(chrome_options=options, executable_path='chromedriver.exe')
        self.driver.get('https://extremereportbot.com/home/')
        self.pegar_jogadores()

        continuar = True
        contador = 0
        while continuar:
            for steamplayer in self.jogadores:
                try:
                    WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'steamuser'))).send_keys(
                        steamplayer)
                    WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'finduser'))).click()
                    WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'user_confirm'))).click()
                    WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, '//label[@for="csgo"]'))).click()
                    WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, '//label[@for="community"]'))).click()

                    self.marcar_checkboxs(self.driver)
                    WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'report_confirm'))).click()
                    time.sleep(40)
                    self.driver.refresh()
                    contador += 1
                    print(f'Quantidade de vezes reportados: {contador / len(self.jogadores)}')
                except:
                    self.driver.refresh()

    def marcar_checkboxs(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f'//label[@for="{self.community.get()}"]'))).click()

        fors_label = [46, 48, 43, 47, 42]
        new_list = []
        for elemento in self.lista:
            new_list.append(elemento.get())

        zip_iterator = zip(fors_label, new_list)
        dictconjugado = dict(zip_iterator)

        for key, value in dictconjugado.items():
            if value:
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, f'//label[@for="{key}"]'))).click()

    def pegar_jogadores(self):
        for perfil in [self.report1_entry.get(), self.report2_entry.get(), self.report3_entry.get()]:
            if perfil != '':
                self.jogadores.append(perfil)


meubot = ReportBot()
meubot.criar_interface()
