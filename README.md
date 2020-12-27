# automato
Programa feito em python que simula o comportamento de um autômato para reconhecer uma atribuição.
Rodar o arquivo main.py e digitar uma atribuição quando aparecer a mensagem "Digite uma Atribuição"
e o programa retorna se ele é valido ou não.
A modelagem do autômato seguiu as regras de forma mais específica:
M( {q0,q1,q2,q3,q4,q5,q6,q7}, {[a-z],[0-9],"=",".","_",";"},  δ, q0, q7 )
identificador: [a-z] ( [a-z] | [0-9] | [_])*
op: ‘=’
numero: ( [0-9]([0-9])* ) | ( [0-9]([0-9])*‘.’ [0-9]([0-9])* )
pv: ‘;’
pt: ’.’
δ(transição de estados):
δ (q0,identificador)= q1
δ (q1,identificador)= q1
δ (q1,op)= q2
δ (q2,identificador)= q3
δ (q2,numero)= q4
δ (q3,identificador)= q3
δ (q3,pv)= q7
δ (q4,numero)= q4
δ (q4,pv)= q7
δ (q4,pt)= q5
δ (q5,numero)= q6
δ (q6,numero)= q6
δ (q6,pv)= q7
