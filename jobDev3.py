import json

def main():
    dados = json.load(open("jobDev3\dados.json"))
    menor = float('inf')
    maior = 0
    media = mediaDias(dados)
    fatZero = ''
    diasMaiores = ''
    for dia in dados:
        if(dia['valor']!=0 and dia['valor']<menor): 
            menorDia = dia
            menor = dia['valor']
        if(dia['valor']==0):
            fatZero += str(dia['dia'])+', '
        if(dia['valor']>maior): 
            maiorDia = dia
            maior = dia['valor']
        if(dia['valor']>media): diasMaiores = diasMaiores+str(dia['dia'])+', '

    print('O dia com maior faturamento foi dia '+str(maiorDia['dia'])+' com $'+str(maiorDia['valor'])+'\nO dia com menor faturamento (diferente de 0) foi dia '+str(menorDia['dia'])+' com $'+str(menorDia['valor']))
    print('O(s) dia(s) com faturamento nulo (zero) foi(oram) o(s) dia(s) '+fatZero[:-2])
    print('Os dias com faturamento acima da média de '+str(media)+' foram os dias '+diasMaiores[:-2])
        

def mediaDias(dados):
    dindin=0
    dias=0
    for dia in dados:
        if(dia['valor']==0): continue
        else:
            dindin+=dia['valor']
            dias+=1
    return (dindin/dias)
    
    

if __name__ == "__main__":
    main()