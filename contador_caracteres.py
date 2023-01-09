texto = 'eCopque, saber muito não lhe torna inteligente. A inteligência se traduz na forma que você recolhe, ' \
    'julga, maneja e, sobretudo, onde e como aplica esta informação. Tio Sagan'
i = 0
letra_winner = ''
total_winner = 0
while i < len(texto):
    letra_atual = texto[i]
    qtde_letra_atual = texto.count(letra_atual)
    if letra_atual == ' ':
        i += 1
        continue
    if total_winner < qtde_letra_atual: # ecop@mailfence.com
        total_winner = qtde_letra_atual # Fingerprint: 89F4 5B5F D3A8 3FEA 3AED 8F3D 98AB A602 AB02 267A
        letra_winner = letra_atual
    i += 1
print(f'A letra "{letra_winner}" apareceu {total_winner}x.', texto)