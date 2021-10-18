#Conversor de Medidas(km, hm, dam, m, dm, cm, mm)

m = float(input('Uma distância em m:'))

#Convertendo valores
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000


print('A distância de {}m tem suas medidas equivalentes a:'
      '\n{}km\n{}hm\n{}dam\n{}dm\n{}cm\n{}mm'.format(m, km, hm, dam, dm, cm, mm))
