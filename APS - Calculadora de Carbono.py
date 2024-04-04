import tkinter as tk
from tkinter import *

def calculo_emissao_carbono():
    consumo = float(consumo_entry.get())
    taxa_emissao_carb = consumo * 0.125
    compens_carb = taxa_emissao_carb * 0.023
    ton_carb = compens_carb / 0.023
    quantidade_árvores = taxa_emissao_carb * 0.88

    emissao_mensal.set(f"Considerando que a taxa de emissão de carbono por consumo de energia no Brasil é de 125g por kWh,")
    emissao_mensal2.set(f"sua emissão mensal de carbono é de {taxa_emissao_carb} Kg de CO2.")
    compensacao_carb.set(f"A compensação de carbono necessária é de US$ {compens_carb}, ou, {ton_carb} kg de carbono.")
    árvores_necessarias.set(f"Dica: para uma rápida compensação desse carbono (1 mês), será necessário plantar {quantidade_árvores} árvores!")
    

def calculo_lucro_potencial():
    quantidade_venda_credito = float(quantidade_venda_entry.get())
    
    lucro_potencial = quantidade_venda_credito * 23
    resultado_lucro.set(f"Considerando as flutuações dos valores dos créditos em 2023,")
    resultado_lucro2.set(f"os lucros potenciais da empresa vendendo {quantidade_venda_credito} créditos de carbono serão de US${lucro_potencial}.")

janela = tk.Tk()
janela.title("Atividades Práticas Supervisionadas")
janela.geometry('1920x1080')
janela.config(bg = '#d8ccc0')
logo = PhotoImage(file='C:/Users/Tera/OneDrive/Área de Trabalho/co2.png')
label = Label(janela, image = logo, width= 190, height= 190)
label.place(x= 587,  y= 80)


título = Label(janela, text= "Calculadora de Carbono - APS",
               fg = 'black',
               font = 'Arial 14',
               bg = '#d8ccc0')
título.place(x= 555, y= 30)


consumo_entry = tk.StringVar()
quantidade_venda_entry = tk.StringVar()
emissao_mensal = tk.StringVar()
emissao_mensal2 = tk.StringVar()
resultado_lucro = tk.StringVar()
resultado_lucro2 = tk.StringVar()
compensacao_carb = tk.StringVar()
árvores_necessarias = tk.StringVar()


consumo_text = tk.Label(janela, text="Entre com o consumo de energia (em kWh) da sua empresa / indústria:",
         fg = 'black',
         font = 'Arial 11',
         bg = '#d8ccc0')
consumo_text.place(x= 100, y= 305)

kwh_info = tk.Label(janela, text = "(Pequena / média indústria: 1.000 - 90.000 kWh mensal  |  Grandes indústrias: 100.000+ kWh mensal)",
                    fg = 'black',
                    font = 'Arial 8',
                    bg = '#d8ccc0')
kwh_info.place(x= 90, y= 346)


consumo_box = tk.Entry(janela, textvariable = consumo_entry, width= 40)
consumo_box.place(x= 215, y= 390)


botao_emissao = tk.Button(janela, text = "Calcular Emissão de Carbono", command = calculo_emissao_carbono)
botao_emissao.place(x= 255, y= 430)


emissao_resultado = tk.Label(janela, textvariable = emissao_mensal,
                            fg = 'black',
                            font = 'Verdana 9',
                            bg = '#d8ccc0')
emissao_resultado.place(x= 30, y= 480)


emissao_resultado2 = tk.Label(janela, textvariable = emissao_mensal2,
                              fg = 'black',
                              font = 'Verdana 9',
                              bg = '#d8ccc0')
emissao_resultado2.place(x= 160, y= 500)


compensacao_resultado = tk.Label(janela, textvariable = compensacao_carb,
                                fg = 'Black',
                                font = 'Verdana 9',
                                bg = '#d8ccc0')
compensacao_resultado.place(x= 60, y= 540)


árvores_resultado = tk.Label(janela, textvariable = árvores_necessarias,
                             fg = 'Black',
                             font = 'Verdana 9',
                             bg = '#d8ccc0')
árvores_resultado.place(x= 30, y= 570)


creditos_text = tk.Label(janela, text = "Quantos créditos você deseja vender?",
                        fg = 'black',
                        font = 'Arial 11',
                        bg = '#d8ccc0')
creditos_text.place(x= 920, y= 305)


dica_vendas = tk.Label(janela, text = "(Uma tonelada de carbono não emitida = um crédito de carbono).",
                       fg = 'black',
                       font = 'Arial 8',
                       bg = '#d8ccc0')
dica_vendas.place(x= 890, y= 330)


dica_vendas2 = tk.Label(janela, text = "Comprar e vender créditos de carbono pode ser uma estratégia inteligente para a sua empresa, não apenas do ponto de vista financeiro",
                        fg = 'black',
                        font = 'Arival 8',
                        bg = '#d8ccc0')
dica_vendas2.place(x= 700, y= 350)


dica_vendas3 = tk.Label(janela, text = "mas também como uma maneira de mostrar o seu compromisso com a sustentabilidade e a responsabilidade social.",
                        fg = 'black',
                        font = 'Arial 8',
                        bg = '#d8ccc0')
dica_vendas3.place(x= 760, y= 370)


venda_box = tk.Entry(janela, textvariable = quantidade_venda_entry, width= 40)
venda_box.place(x= 910, y= 405)


botao_lucro = tk.Button(janela, text = "Calcular Lucro Potencial", command = calculo_lucro_potencial)
botao_lucro.place(x= 965, y= 440)


lucro_resultado = tk.Label(janela, textvariable = resultado_lucro,
                           fg = 'black',
                           font= 'Verdana 9',
                           bg = '#d8ccc0')
lucro_resultado.place(x= 820, y= 490)


lucro_resultado2 = tk.Label(janela, textvariable = resultado_lucro2,
                            fg = 'black',
                            font = 'Verdana 9',
                            bg = '#d8ccc0')
lucro_resultado2.place(x= 740, y= 520)



janela.mainloop()