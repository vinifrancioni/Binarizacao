# Programa de binarização de imanges




import cv2
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *


'''

As def's 'funcao_xxxxx' abaixo são as rotinas que tratam de cada tipo de imagem

'''

def funcao_industria():

      imagem1_process = cv2.imread('process.png')
      imagem2_process = cv2.cvtColor(imagem1_process, cv2.COLOR_BGR2GRAY)

      ret, thresh1_process = cv2.threshold(imagem2_process, 100, 255, cv2.THRESH_BINARY_INV)
      ret, thresh2_process = cv2.threshold(imagem2_process, 125, 255, cv2.THRESH_BINARY_INV)
      ret, thresh3_process = cv2.threshold(imagem2_process, 180, 255, cv2.THRESH_BINARY_INV)

      imagem3_process = np.hstack((imagem2_process, thresh1_process))
      imagem4_process = np.hstack((thresh2_process, thresh3_process))
      imagem5_process = np.vstack((imagem3_process, imagem4_process))
      cv2.imshow('Placa de Circuito Impresso', imagem5_process)
      cv2.waitKey()

def funcao_moeda():

      imagem1_moeda = cv2.imread('moeda.png')
      imagem2_moeda = cv2.cvtColor(imagem1_moeda, cv2.COLOR_BGR2GRAY)

      ret, thresh1_moeda = cv2.threshold(imagem2_moeda, 100, 255, cv2.THRESH_BINARY_INV)
      ret, thresh2_moeda = cv2.threshold(imagem2_moeda, 125, 255, cv2.THRESH_BINARY_INV)
      ret, thresh3_moeda = cv2.threshold(imagem2_moeda, 180, 255, cv2.THRESH_BINARY_INV)

      imagem3_moeda = np.hstack((imagem2_moeda, thresh1_moeda))
      imagem4_moeda = np.hstack((thresh2_moeda, thresh3_moeda))
      imagem5_moeda = np.vstack((imagem3_moeda, imagem4_moeda))
      cv2.imshow('Modeda', imagem5_moeda)
      cv2.waitKey()

def funcao_celula():

      imagem1_cell = cv2.imread('celula.png')
      imagem2_cell = cv2.cvtColor(imagem1_cell, cv2.COLOR_BGR2GRAY)

      ret, thresh1_cell = cv2.threshold(imagem2_cell, 100, 255, cv2.THRESH_BINARY_INV)
      ret, thresh2_cell = cv2.threshold(imagem2_cell, 140, 255, cv2.THRESH_BINARY_INV)
      ret, thresh3_cell = cv2.threshold(imagem2_cell, 180, 255, cv2.THRESH_BINARY_INV)

      imagem3_cell = np.hstack((imagem2_cell, thresh1_cell))
      imagem4_cell = np.hstack((thresh2_cell, thresh3_cell))
      imagem5_cell = np.vstack((imagem3_cell, imagem4_cell))
      cv2.imshow('Celula', imagem5_cell)
      cv2.waitKey()

def funcao_cafe():

      imagem1_agro = cv2.imread('cafe.png')
      imagem2_agro = cv2.cvtColor(imagem1_agro, cv2.COLOR_BGR2GRAY)

      ret, thresh1_agro = cv2.threshold(imagem2_agro, 60, 255, cv2.THRESH_BINARY)
      ret, thresh2_agro = cv2.threshold(imagem2_agro, 110, 255, cv2.THRESH_BINARY)
      ret, thresh3_agro = cv2.threshold(imagem2_agro, 180, 255, cv2.THRESH_BINARY)

      imagem3_agro = np.hstack((imagem2_agro, thresh1_agro))
      imagem4_agro = np.hstack((thresh2_agro, thresh3_agro))
      imagem5_agro = np.vstack((imagem3_agro, imagem4_agro))
      cv2.imshow('Agricultura', imagem5_agro)
      cv2.waitKey()

def funcao_placa():

# Como esse item tem sub-itens, foram criadas também sub-rotinas dentro da sua definição

      def funcao_placa_amarela():

            imagem1_car2 = cv2.imread('placa_amarela.png')
            imagem2_car2 = cv2.cvtColor(imagem1_car2, cv2.COLOR_BGR2GRAY)

            ret, thresh1_car2 = cv2.threshold(imagem2_car2, 100, 255, cv2.THRESH_BINARY)
            ret, thresh2_car2 = cv2.threshold(imagem2_car2, 125, 255, cv2.THRESH_BINARY)
            ret, thresh3_car2 = cv2.threshold(imagem2_car2, 180, 255, cv2.THRESH_BINARY)

            imagem3_car2 = np.hstack((imagem2_car2, thresh1_car2))
            imagem4_car2 = np.hstack((thresh2_car2, thresh3_car2))
            imagem5_car2 = np.vstack((imagem3_car2, imagem4_car2))
            cv2.imshow('Placa Normal', imagem5_car2)
            cv2.waitKey()

      def funcao_placa_normal():

            imagem1_car1 = cv2.imread('placa_normal.png')
            imagem2_car1 = cv2.cvtColor(imagem1_car1, cv2.COLOR_BGR2GRAY)

            ret, thresh1_car1 = cv2.threshold(imagem2_car1, 100, 255, cv2.THRESH_BINARY)
            ret, thresh2_car1 = cv2.threshold(imagem2_car1, 125, 255, cv2.THRESH_BINARY)
            ret, thresh3_car1 = cv2.threshold(imagem2_car1, 180, 255, cv2.THRESH_BINARY)

            imagem3_car1 = np.hstack((imagem2_car1, thresh1_car1))
            imagem4_car1 = np.hstack((thresh2_car1, thresh3_car1))
            imagem5_car1 = np.vstack((imagem3_car1, imagem4_car1))
            cv2.imshow('Placa Normal', imagem5_car1)

      def funcao_placa_mercosul():


            imagem1_car3 = cv2.imread('placa_mercosul.png')
            imagem2_car3 = cv2.cvtColor(imagem1_car3, cv2.COLOR_BGR2GRAY)

            ret, thresh1_car3 = cv2.threshold(imagem2_car3, 100, 255, cv2.THRESH_BINARY)
            ret, thresh2_car3 = cv2.threshold(imagem2_car3, 125, 255, cv2.THRESH_BINARY)
            ret, thresh3_car3 = cv2.threshold(imagem2_car3, 180, 255, cv2.THRESH_BINARY)

            imagem3_car3 = np.hstack((imagem2_car3, thresh1_car3))
            imagem4_car3 = np.hstack((thresh2_car3, thresh3_car3))
            imagem5_car3 = np.vstack((imagem3_car3, imagem4_car3))
            cv2.imshow('Placa Normal', imagem5_car3)
            cv2.waitKey()

      ''' 
      Da mesma maneira com que foi necessário criar "sub-def's" por que o item placa tem sub-níveis
      foi necessário criar uma nova classe para a segunda janela do menu
      '''

      class Janela2:

                  def __init__(self, lowlevel):

                        # Cria o layout da UI
                        self.frame10 = Frame(lowlevel)
                        self.frame10.pack()
                        self.frame20 = Frame(lowlevel)
                        self.frame20.pack()

                        # Cria o título que aparece na tela principal
                        self.titulo = Label(self.frame10, text='PAGINA 2', font=('Verdana', '13', 'bold'))
                        self.titulo.pack()

                        # Cria o sub-título que aparece na tela principal
                        self.msg = Label(self.frame10, width=100, height=20, text='Selecione uma das imagens abaixo')
                        self.msg.focus_force()
                        self.msg.pack()

                        # Define o botão 5.1
                        self.b051 = Button(self.frame20, text='Placa Amarela')
                        self.b051['padx'], self.b051['pady'] = 10, 5
                        self.b051['bg'] = 'yellow'
                        self.b051.bind("<Return>", self.keypress51)
                        self.b051.bind("<Any-Button>", self.button51)
                        self.b051.bind("<FocusIn>", self.fin51)
                        self.b051.bind("<FocusOut>", self.fout51)
                        self.b051['relief'] = RIDGE
                        self.b051.pack(side=LEFT)

                        # Define o botão 5.2
                        self.b052 = Button(self.frame20, text='Placa Normal')
                        self.b052['padx'], self.b052['pady'] = 10, 5
                        self.b052['bg'] = 'grey'
                        self.b052.bind("<Return>", self.keypress52)
                        self.b052.bind("<Any-Button>", self.button52)
                        self.b052.bind("<FocusIn>", self.fin52)
                        self.b052.bind("<FocusOut>", self.fout52)
                        self.b052['relief'] = RIDGE
                        self.b052.pack(side=LEFT)

                        # Define o botão 5.3
                        self.b053 = Button(self.frame20, text='Placa Mercosul')
                        self.b053['padx'], self.b053['pady'] = 10, 5
                        self.b053['bg'] = 'blue'
                        self.b053.bind("<Return>", self.keypress53)
                        self.b053.bind("<Any-Button>", self.button53)
                        self.b053.bind("<FocusIn>", self.fin53)
                        self.b053.bind("<FocusOut>", self.fout53)
                        self.b053['relief'] = RIDGE
                        self.b053.pack(side=LEFT)

                        # Define o botão 5.4
                        self.b054 = Button(self.frame20, text='SAIR')
                        self.b054['padx'], self.b054['pady'] = 10, 5
                        self.b054['bg'] = 'white'
                        self.b054.bind("<Return>", self.keypress54)
                        self.b054.bind("<Any-Button>", self.button54)
                        self.b054.bind("<FocusIn>", self.fin54)
                        self.b054.bind("<FocusOut>", self.fout54)
                        self.b054['relief'] = RIDGE
                        self.b054.pack(side=LEFT)

                  # Define os estados dos botões
                  def keypress51(self, event): self.msg
                  def keypress52(self, event): self.msg
                  def keypress53(self, event): self.msg
                  def keypress54(self, event): self.msg


                  # Chama as funções respectivas a cada botão
                  def button51(self, event):
                        funcao_placa_amarela()
                  def button52(self, event):
                        funcao_placa_normal()
                  def button53(self, event):
                        funcao_placa_mercosul()
                  def button54(self, event):
                        raiz2.destroy()

                  #Define como devem ser o estilo dos botões após pressionados
                  def fin51(self, event): self.b51['relief'] = FLAT
                  def fout51(self, event): self.b51['relief'] = RIDGE
                  def fin52(self, event): self.b52['relief'] = FLAT
                  def fout52(self, event): self.b52['relief'] = RIDGE
                  def fin53(self, event): self.b53['relief'] = FLAT
                  def fout53(self, event): self.b53['relief'] = RIDGE
                  def fin54(self, event): self.b54['relief'] = FLAT
                  def fout54(self, event): self.b54['relief'] = RIDGE


      raiz2 = Tk()
      Janela2(raiz2)
      raiz2.mainloop()


def funcao_webcam():

      cap = cv2.VideoCapture(0)
      __, imagem1_web = cap.read()
      cap.release()

      imagem1_web = cv2.resize(imagem1_web, (540, 405))
      imagem2_web = cv2.cvtColor(imagem1_web, cv2.COLOR_BGR2GRAY)

      imagem2_web_equ = cv2.equalizeHist(imagem2_web)

      ret, thresh1_web = cv2.threshold(imagem2_web_equ, 50, 255, cv2.THRESH_BINARY)
      ret, thresh2_web = cv2.threshold(imagem2_web_equ, 120, 255, cv2.THRESH_BINARY)
      ret, thresh3_web = cv2.threshold(imagem2_web_equ, 180, 255, cv2.THRESH_BINARY)

      imagem3_web = np.hstack((imagem2_web_equ, thresh1_web))
      imagem4_web = np.hstack((thresh2_web, thresh3_web))
      imagem5_web = np.vstack((imagem3_web, imagem4_web))
      cv2.imshow('Capturas da Webcam', imagem5_web)
      cv2.imshow('Imagem sem equalizacao', imagem2_web)
      cv2.waitKey()


class Janela:

      def __init__(self, toplevel):
            # Cria o layout da UI

            self.frame = Frame(toplevel)
            self.frame.pack()
            self.frame2 = Frame(toplevel)
            self.frame2.pack()

            self.titulo = Label(self.frame, text='PROGRAMA HACKERMAN 2000', font=('Verdana', '13', 'bold'))
            self.titulo.pack()

            self.msg = Label(self.frame, width=100, height=20, text='Selecione uma das imagens abaixo')
            self.msg.focus_force()
            self.msg.pack()

            # Define o botão 1
            self.b01 = Button(self.frame2, text='Industria')
            self.b01['padx'], self.b01['pady'] = 10, 5
            self.b01['bg'] = 'blue'
            self.b01.bind("<Return>", self.keypress01)
            self.b01.bind("<Any-Button>", self.button01)
            self.b01.bind("<FocusIn>", self.fin01)
            self.b01.bind("<FocusOut>", self.fout01)
            self.b01['relief'] = RIDGE
            self.b01.pack(side=LEFT)

            # Define o botão 2
            self.b02 = Button(self.frame2, text='Moeda')
            self.b02['padx'], self.b02['pady'] = 10, 5
            self.b02['bg'] = 'green'
            self.b02.bind("<Return>", self.keypress02)
            self.b02.bind("<Any-Button>", self.button02)
            self.b02.bind("<FocusIn>", self.fin02)
            self.b02.bind("<FocusOut>", self.fout02)
            self.b02['relief'] = RIDGE
            self.b02.pack(side=LEFT)

            # Define o botão 3
            self.b03 = Button(self.frame2, text='Celula')
            self.b03['padx'], self.b03['pady'] = 10, 5
            self.b03['bg'] = 'red'
            self.b03.bind("<Return>", self.keypress03)
            self.b03.bind("<Any-Button>", self.button03)
            self.b03.bind("<FocusIn>", self.fin03)
            self.b03.bind("<FocusOut>", self.fout03)
            self.b03['relief'] = RIDGE
            self.b03.pack(side=LEFT)

            # Define o botão 4
            self.b04 = Button(self.frame2, text='Agricultura')
            self.b04['padx'], self.b04['pady'] = 10, 5
            self.b04['bg'] = 'cyan'
            self.b04.bind("<Return>", self.keypress04)
            self.b04.bind("<Any-Button>", self.button04)
            self.b04.bind("<FocusIn>", self.fin04)
            self.b04.bind("<FocusOut>", self.fout04)
            self.b04['relief'] = RIDGE
            self.b04.pack(side=LEFT)

            # Define o botão 5
            self.b05 = Button(self.frame2, text='Placa de Carro')
            self.b05['padx'], self.b05['pady'] = 10, 5
            self.b05['bg'] = 'yellow'
            self.b05.bind("<Return>", self.keypress05)
            self.b05.bind("<Any-Button>", self.button05)
            self.b05.bind("<FocusIn>", self.fin05)
            self.b05.bind("<FocusOut>", self.fout05)
            self.b05['relief'] = RIDGE
            self.b05.pack(side=LEFT)

            # Define o botão 6
            self.b06 = Button(self.frame2, text='Webcam')
            self.b06['padx'], self.b06['pady'] = 10, 5
            self.b06['bg'] = 'magenta'
            self.b06.bind("<Return>", self.keypress06)
            self.b06.bind("<Any-Button>", self.button06)
            self.b06.bind("<FocusIn>", self.fin06)
            self.b06.bind("<FocusOut>", self.fout06)
            self.b06['relief'] = RIDGE
            self.b06.pack(side=LEFT)

            # Define o botão 7
            self.b07 = Button(self.frame2, text='SAIR')
            self.b07['padx'], self.b07['pady'] = 10, 5
            self.b07['bg'] = 'white'
            self.b07.bind("<Return>", self.keypress07)
            self.b07.bind("<Any-Button>", self.button07)
            self.b07.bind("<FocusIn>", self.fin07)
            self.b07.bind("<FocusOut>", self.fout07)
            self.b07['relief'] = RIDGE
            self.b07.pack(side=LEFT)

      # Define os estados dos botões
      def keypress01(self, event): self.msg
      def keypress02(self, event): self.msg
      def keypress03(self, event): self.msg
      def keypress04(self, event): self.msg
      def keypress05(self, event): self.msg
      def keypress06(self, event): self.msg
      def keypress07(self, event): self.msg

      # Chama as funções respectivas a cada botão
      def button01(self, event):
            funcao_industria()

      def button02(self, event):
            funcao_moeda()

      def button03(self, event):
            funcao_celula()

      def button04(self, event):
            funcao_cafe()

      def button05(self, event):
            funcao_placa()


      def button06(self, event):
            funcao_webcam()

      def button07(self, event):
            exit()

      # Define como devem ser o estilo dos botões após pressionados
      def fin01(self, event): self.b01['relief'] = FLAT
      def fout01(self, event): self.b01['relief'] = RIDGE
      def fin02(self, event): self.b02['relief'] = FLAT
      def fout02(self, event): self.b02['relief'] = RIDGE
      def fin03(self, event): self.b02['relief'] = FLAT
      def fout03(self, event): self.b02['relief'] = RIDGE
      def fin04(self, event): self.b01['relief'] = FLAT
      def fout04(self, event): self.b01['relief'] = RIDGE
      def fin05(self, event): self.b02['relief'] = FLAT
      def fout05(self, event): self.b02['relief'] = RIDGE
      def fin06(self, event): self.b02['relief'] = FLAT
      def fout06(self, event): self.b02['relief'] = RIDGE
      def fin07(self, event): self.b02['relief'] = FLAT
      def fout07(self, event): self.b02['relief'] = RIDGE


raiz = Tk()
Janela(raiz)
raiz.mainloop()

