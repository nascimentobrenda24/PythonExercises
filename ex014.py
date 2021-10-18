# Conversor de Temperaturas( °C to °F)
# formula = tc/5 = tf-32/9 = (9c + 32) / 5


t_c = float(input('Infome a temperatura em °C:'))
t_f = ((9*t_c) / 5) + 32

print('A temperatura de {}°C é EQUIVALENTE a {}°F'.format(t_c, t_f))
