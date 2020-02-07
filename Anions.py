import random
from colorama import Fore, Style, init

# ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻₀₁₂₃₄₅₆₇₈₉
# anions = {"F⁻": "Fluoreto", "Cl⁻": "Cloreto", "Br⁻": "Brometo", "I⁻": "Iodeto",
# 		  "CN⁻": "Cianeto", "S²⁻": "Sulfeto", "CO²⁻": "Carbonato", "SO₄²⁻": "Sulfato",
# 		  "SO₃²⁻": "Sulfito", "ClO⁻": "Hipoclorito", "ClO₂⁻": "Clorito", "ClO₃⁻": "Clorato",
# 		  "ClO₄⁻": "Perclorato", "BO₃⁵⁻": "Borato", "PO₄³⁻": "Fosfato", "PO₃³⁻": "Fosfito",
# 		  "P₂O₇⁴⁻": "Pirofosfato", "OH⁻": "Hidroxido", "CH₃COO⁻": "Acetato", "PbO₂²⁻": "Plumbito",
# 		  "PbO₃²⁻": "Plumbato", "IO⁻": "Hipoiodito", "IO₂⁻": "Iodito", "IO₃⁻": "Iodato",
# 		  "IO₄⁻": "Periodato", "BrO₃⁻": "Bromato", "BrO⁻": "Hipobromato", "NO₂⁻": "Nitrito",
# 		  "NO₃⁻": "Nitrato", "SCN⁻": "Tiocianato", "CNO⁻": "Cianato", "CrO₄²⁻": "Cromato",
# 		  "Cr₂O₇²⁻": "Dicromato", "MnO₄⁻": "Permanganato", "MnO₄²⁻": "Manganato"}

anions = {"F-": "Fluoreto", "Cl-": "Cloreto", "Br-": "Brometo", "I-": "Iodeto",
		  "CN-": "Cianeto", "S2-": "Sulfeto", "CO2-3": "Carbonato", "SO2-4": "Sulfato",
		  "SO2-3": "Sulfito", "ClO-": "Hipoclorito", "ClO-2": "Clorito", "ClO-3": "Clorato",
		  "ClO-4": "Perclorato", "BO5-3": "Borato", "PO3-4": "Fosfato", "PO3-3": "Fosfito",
		  "P2O4-7": "Pirofosfato", "OH-": "Hidroxido", "CH3COO-": "Acetato", "PbO2-2": "Plumbito",
		  "PbO2-3": "Plumbato", "IO-": "Hipoiodito", "IO-2": "Iodito", "IO-3": "Iodato",
		  "IO-4": "Periodato", "BrO-3": "Bromato", "BrO-": "Hipobromato", "NO-2": "Nitrito",
		  "NO-3": "Nitrato", "SCN-": "Tiocianato", "CNO-": "Cianato", "CrO2-4": "Cromato",
		  "Cr2O2-7": "Dicromato", "MnO-4": "Permanganato", "MnO2-4": "Manganato"}

init()
print(f"{Fore.MAGENTA}Tabela de Anions. Feito por Everton Colombo em 29/05/2019{Style.RESET_ALL}\n\n")


def formulatoname():
	corrects = 0
	while True:
		try:
			formula = random.choice(list(anions.keys()))
		except:
			break
		name = anions[formula]
		anions.pop(formula)
		print(f"{Fore.CYAN}Qual o anion cuja formula é", Fore.YELLOW + "{}".format(formula) + Style.RESET_ALL + "?", sep=' ')
		answer = input("R: ")
		print()
		if answer.upper() == name.upper():
			corrects += 1
			print(f"{Fore.GREEN}Correto!{Style.RESET_ALL}")
		else:
			print(f"{Fore.RED}Errado!{Style.RESET_ALL}" + "\nO correto seria" + Fore.YELLOW + " {}".format(name) + Style.RESET_ALL)
		print("\n-------\n")

	print("\n\n" + "=" * 40 + "\n\n")
	result = Style.BRIGHT + Fore.MAGENTA + str(corrects) + Style.RESET_ALL
	if corrects <= 17:
		print(Fore.RED + "Voce acertou apenas {}/35".format(result + Fore.YELLOW))
	else:
		print(Fore.GREEN + "Voce acertou {}/35".format(result + Fore.YELLOW))
	print(Style.RESET_ALL)
	input("Pressione ENTER para fechar...")


def nametoformula():
	corrects = 0
	while True:
		try:
			name = random.choice(list(anions.values()))
		except:
			break
		formula = list(anions.keys())[list(anions.values()).index(name)]
		anions.pop(formula)
		print(f"{Fore.CYAN}Qual a formula do anion", Fore.YELLOW + "{}".format(name) + Style.RESET_ALL + "?", sep=' ')
		answer = input("R: ")
		print()
		if answer == formula:
			corrects += 1
			print(f"{Fore.GREEN}Correto!{Style.RESET_ALL}")
		else:
			print(f"{Fore.RED}Errado!{Style.RESET_ALL}" + "\nO correto seria" + Fore.YELLOW + " {}".format(formula) + Style.RESET_ALL)
		print("\n-------\n")

	print("\n\n" + "=" * 40 + "\n\n")
	result = Style.BRIGHT + Fore.MAGENTA + str(corrects) + Style.RESET_ALL
	if corrects <= 17:
		print(Fore.RED + "Voce acertou apenas {}/35".format(result + Fore.YELLOW))
	else:
		print(Fore.GREEN + "Voce acertou {}/35".format(result + Fore.YELLOW))
	print(Style.RESET_ALL)
	input("Pressione ENTER para fechar...")

if __name__ == "__main__":
	mode = input("'formulas' ou 'nomes'? ")
	print()
	formulatoname() if mode == 'nomes' else nametoformula() if mode == 'formulas' else print(f"{Fore.RED}Erro")
