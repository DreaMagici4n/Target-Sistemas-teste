######################################################### - QUESTÃO 2 - ################################################
# user_num = int(input("Informe um numero: "))
# fibonacci_num = 0
# fibonacci_list = []
#
# for num in range(0, user_num + 1):
#     fibonacci_num += num
#     fibonacci_list.append(fibonacci_num)
#
# print(fibonacci_list)
# if user_num in fibonacci_list:
#     print("O numero informado pertence a sequencia")
# else:
#     print("O numero informado não pertence a sequencia")

######################################################### - QUESTÃO 3 - ################################################
# import json
#
# with open("dados.json") as file:
#     faturamento_mes_json= json.load(file)
#     list_faturamento_diario = [dia["valor"] for dia in faturamento_mes_json if dia["valor"] > 0]
#     menor_valor_faturamento = round(min(list_faturamento_diario), 2)
#     maior_valor_faturamento = round(max(list_faturamento_diario), 2)
#     media_mensal = round(sum(list_faturamento_diario)/len(list_faturamento_diario), 2)
#     faturamento_maior_que_media_dias = len([dia["dia"] for dia in faturamento_mes_json
#                                             if dia["valor"] > media_mensal])
#
# print(menor_valor_faturamento)
# print(maior_valor_faturamento)
# print(media_mensal)
# print(faturamento_maior_que_media_dias)
######################################################### - QUESTÃO 4 - ################################################

# FATURAMENTO_ESTADO_MES = {
#     "SP": 67836.43,
#     "RJ": 36678.66,
#     "MG": 29229.88,
#     "ES": 27165.48,
#     "OUTROS": 19849.53,
# }
# faturamento_mes_total = sum([FATURAMENTO_ESTADO_MES[estado] for estado in FATURAMENTO_ESTADO_MES])
#
# for estado in FATURAMENTO_ESTADO_MES:
#     faturamento = FATURAMENTO_ESTADO_MES[estado]
#     porcentagem = round(faturamento/faturamento_mes_total * 100, 2)
#     if estado == "OUTROS":
#         print(f"{estado.title()} Estados representam {porcentagem}% do valor total da distribuidora.")
#     else:
#         print(f"{estado} representa {porcentagem}% do valor total da distribuidora.")
######################################################### - QUESTÃO 5 - ################################################

# string = input("Informe a palavra que deseja inverter: ")
# string_reversa = ""
#
# caracteres = [caracter for caracter in string]
#
# for caracter in caracteres[::-1]:
#     string_reversa += caracter
#
# print(string_reversa)
