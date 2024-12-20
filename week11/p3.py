import p2
from scipy.interpolate import lagrange

num_shares = 4
threshold = 3

# 1: Gerar o polinómio f para o segredo 100 e com as partes x1, x2, x3, x4
secret_f = 100
coefficients_f, shares_f = p2.secret_sharing(secret_f, num_shares, threshold)
print("Partes f:", shares_f)
print("-------------------------------------")

# 2: Gerar o polinómio g para o segredo 550 e com as partes y1, y2, y3, y4
secret_g = 550
coefficients_g, shares_g = p2.secret_sharing(secret_g, num_shares, threshold)
print("Partes g:", shares_g)
print("-------------------------------------")

# 3: Calcular z1 = x1 + y1, z2 = x2 + y2, z3 = x3 + y3
z_shares = [(x[0], x[1] + y[1]) for x, y in zip(shares_f[:3], shares_g[:3])]
print("Partes z (soma de f e g):", z_shares)

# 4: Reconstruir o segredo usando z1, z2, z3
reconstructed_polynomial = p2.recover_polynomial_with_lagrange(z_shares)
reconstructed_secret = reconstructed_polynomial(0)
print("Segredo reconstruído a partir de z:", reconstructed_secret)
