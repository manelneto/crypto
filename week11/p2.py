import p1
import random
from scipy.interpolate import lagrange

def secret_sharing(secret, num_shares, threshold):
    degree = threshold - 1
    coefficients = p1.generate_polynomial(secret, degree)
    
    print(f"O polinómio gerado é: {coefficients}")
    shares = []
    for i in range(1, num_shares + 1):
        x = i
        y = p1.evaluate_polynomial(coefficients, x)
        shares.append((x, y))
    
    return coefficients, shares

def recover_polynomial_with_lagrange(shares):
    """
    Reconstrói o segredo usando a função lagrange do scipy.
    """
    x_coords, y_coords = zip(*shares)  # Extrai os x e y 
    polynomial = lagrange(x_coords, y_coords)
    return polynomial

if __name__ == "__main__":
    # Inputs
    secret = 1001
    num_shares = 5 # número de partes geradas
    threshold = 3 # número de partes necessárias para reconstruir o segredo

    coefficients, shares = secret_sharing(secret, num_shares, threshold)
    print("Partes:", shares)

    selected_shares = random.sample(shares, threshold)
    print("Partes selecionadas:", selected_shares)

    # f'
    reconstructed_polynomial = recover_polynomial_with_lagrange(selected_shares)

    # Verifica f'(0)
    reconstructed_secret = reconstructed_polynomial(0)
    print("Segredo reconstruído f'(0):", reconstructed_secret)
