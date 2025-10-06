import numpy as np
import matplotlib.pyplot as plt
import warnings
import subprocess
warnings.filterwarnings("ignore", category=RuntimeWarning)

def sqrd(num):
    return num**2

def cubd(num):
    return num**3

RED = "\033[31m"
GRAY = "\033[90m"
RESET = "\033[0m"
BOLD = "\033[1m"
FUNC_FAMILYS = ["Linear", "Absolute", "Quadratic", "Cubic", "Square Root", "Cube Root", "Reciprocal"]
TRANS_LIST = ["Vertical Translation", "Horizontal Translation", "Reflection X-Axis", "Reflection Y-Axis", "Vertical Stretch/Compression", "Horizontal Stretch/Compression"]
transformationsIncluded = {}

func_family = "quadratic"
transformations = True
h_translation = 0 # left-right
v_translation = 0 # up-down
reflection_x = 1 # flip vertically
reflection_y = 1 # flip horizontally
vertical_sc = 1
horizontal_sc = 1

print(f"{GRAY}Function Familys: ")
for func in FUNC_FAMILYS:
    print(f"  {FUNC_FAMILYS.index(func) + 1}. {func}")
print(RESET, end="")
print(f"{BOLD}Enter the number corresponding to your function family: {RESET}", end="")
funcFamChoice = input()
match funcFamChoice:
    case "1":
        func_family = "linear"
    case "2":
        func_family = "absolute"
    case "3":
        func_family = "quadratic"
    case "4":
        func_family = "cubic"
    case "5":
        func_family = "sqrt"
    case "6":
        func_family = "cbrt"
    case "7":
        func_family = "reciprocal"
    case _:
        print("\033[2J\033[H", end="")
        print(f"{RED}Invalid Input, {funcFamChoice} is not a number corresponding to a Function Family")
        exit()

print("\033[2J\033[H", end="")
print(f"{BOLD}Function Family: {FUNC_FAMILYS[int(funcFamChoice) - 1]}{RESET}\n")

print(f"{BOLD}Add Transformation(s)? (y/n): {RESET}", end="")
incTrans = input().lower()
if incTrans == "y":
    transformations = True
    looping = True

    while looping:
        print("\033[2J\033[H", end="")
        print(f"{BOLD}Function Family: {FUNC_FAMILYS[int(funcFamChoice) - 1]}{RESET}")
        print(f"{BOLD}Transformations Added: ")
        for tran in transformationsIncluded:
            print(f"  - {tran}: {transformationsIncluded[tran]}")
        print(RESET + "\n", end="")

        print(f"{GRAY}Example")
        print("f(x) = -2(-1/2(x + 2)) - 5")
        print("  - Vertical Translation: -5")
        print("  - Horizontal Translation: 2")
        print("  - Reflection X-Axis: True")
        print("  - Reflection Y-Axis: True")
        print("  - Vertical Stretch/Compression: 2")
        print(f"  - Horizontal Stretch/Compression: 1/2{RESET}\n")

        print(f"{GRAY}Transformations: ")
        for tran in TRANS_LIST:
            if tran in transformationsIncluded:
                print(f"{RED}  X. {tran} (Already Added){RESET}{GRAY}")
            else:
                print(f"  {TRANS_LIST.index(tran) + 1}. {tran}")
        print(RESET, end="")
        print(f"{BOLD}Enter the number corresponding to your transformation: {RESET}", end="")
        tranChoice = input()

        match tranChoice:
            case "1":
                if "Vertical Translation" in list(transformationsIncluded.keys()):
                    print("\033[2J\033[H", end="")
                    print(f"{RED}Invalid Input, Vertical Translation already added.")
                    exit()
                print(f"{BOLD}  - Enter Vertical Translation Number: {RESET}", end="")
                tranNum = input()
                tranNum = eval(tranNum)
                v_translation = tranNum
                transformationsIncluded["Vertical Translation"] = tranNum
            case "2":
                if "Horizontal Translation" in list(transformationsIncluded.keys()):
                    print("\033[2J\033[H", end="")
                    print(f"{RED}Invalid Input, Horizontal Translation already added.")
                    exit()
                print(f"{BOLD}  - Enter Horizontal Translation Number: {RESET}", end="")
                tranNum = input()
                tranNum = eval(tranNum)
                h_translation = tranNum * -1
                transformationsIncluded["Horizontal Translation"] = tranNum
            case "3":
                if "Reflection X-Axis" in list(transformationsIncluded.keys()):
                    print("\033[2J\033[H", end="")
                    print(f"{RED}Invalid Input, Reflection X-Axis already added.")
                    exit()
                reflection_x = -1
                transformationsIncluded["Reflection X-Axis"] = "Added"
            case "4":
                if "Reflection Y-Axis" in list(transformationsIncluded.keys()):
                    print("\033[2J\033[H", end="")
                    print(f"{RED}Invalid Input, Reflection Y-Axis already added.")
                    exit()
                reflection_y = -1
                transformationsIncluded["Reflection Y-Axis"] = "Added"
            case "5":
                if "Vertical Stretch/Compression" in list(transformationsIncluded.keys()):
                    print("\033[2J\033[H", end="")
                    print(f"{RED}Invalid Input, Vertical Stretch/Compression already added.")
                    exit()
                print(f"{BOLD}  - Enter Vertical Stretch/Compression Number: {RESET}", end="")
                tranNum = input()
                tranNum = eval(tranNum)
                vertical_sc = tranNum
                transformationsIncluded["Vertical Stretch/Compression"] = f"{float(tranNum):.2f}"
            case "6":
                if "Horizontal Stretch/Compression" in list(transformationsIncluded.keys()):
                    print("\033[2J\033[H", end="")
                    print(f"{RED}Invalid Input, Horizontal Stretch/Compression already added.")
                    exit()
                print(f"{BOLD}  - Enter Horizontal Stretch/Compression Number: {RESET}", end="")
                tranNum = input()
                tranNum = eval(tranNum)
                horizontal_sc = tranNum
                transformationsIncluded["Horizontal Stretch/Compression"] = f"{float(tranNum):.2f}"
            case _:
                print("\033[2J\033[H", end="")
                print(f"{RED}Invalid Input, {tranChoice} is not a number corresponding to a transformation.")
                exit()

        print(f"\n{BOLD}Would you like to add more translation(s)? (y/n): {RESET}", end="")
        contLoop = input().lower()
        if contLoop == "y":
            continue
        elif contLoop == "n":
            break
        else:
            print("\033[2J\033[H", end="")
            print(f"{RED}Invalid Input, {contLoop} is not \"y\" or \"n\".")
            exit()

elif incTrans == "n":
    transformations = False
else:
    print("\033[2J\033[H", end="")
    print(f"{RED}Invalid Input, {incTrans} is not an answer. \"y\" or \"n\" only.")
    exit()

print("\033[2J\033[H", end="")
print(f"{BOLD}Enter Line Color (Rainbow Only): {RESET}", end="")
lnColor = input()

x_left = np.linspace(-10, -0, 400)
x_right = np.linspace(0, 10, 400)

fig, ax = plt.subplots(figsize=(6, 6))

match func_family:
    case "linear":
        ax.plot(x_left + h_translation, reflection_x * vertical_sc * (reflection_y * (x_left * horizontal_sc)) + v_translation, lnColor)
        ax.plot(x_right + h_translation, reflection_x * vertical_sc * (reflection_y * (x_right * horizontal_sc)) + v_translation, lnColor)
    case "absolute":
        ax.plot(x_left + h_translation, reflection_x * vertical_sc * (np.abs(reflection_y * (x_left * horizontal_sc))) + v_translation, lnColor)
        ax.plot(x_right + h_translation, reflection_x * vertical_sc * (np.abs(reflection_y * (x_right * horizontal_sc))) + v_translation, lnColor)
    case "quadratic":
        ax.plot(x_left + h_translation, reflection_x * vertical_sc * (sqrd(reflection_y * (x_left * horizontal_sc))) + v_translation, lnColor)
        ax.plot(x_right + h_translation, reflection_x * vertical_sc * (sqrd(reflection_y * (x_right * horizontal_sc))) + v_translation, lnColor)
    case "cubic":
        ax.plot(x_left + h_translation, reflection_x * vertical_sc * (cubd(reflection_y * (x_left * horizontal_sc))) + v_translation, lnColor)
        ax.plot(x_right + h_translation, reflection_x * vertical_sc * (cubd(reflection_y * (x_right * horizontal_sc))) + v_translation, lnColor)
    case "sqrt":
        ax.plot(x_left + h_translation, reflection_x * vertical_sc * (np.sqrt(reflection_y * (x_left * horizontal_sc))) + v_translation, lnColor)
        ax.plot(x_right + h_translation, reflection_x * vertical_sc * (np.sqrt(reflection_y * (x_right * horizontal_sc))) + v_translation, lnColor)
    case "cbrt":
        ax.plot(x_left + h_translation, reflection_x * vertical_sc * (np.cbrt(reflection_y * (x_left * horizontal_sc))) + v_translation, lnColor)
        ax.plot(x_right + h_translation, reflection_x * vertical_sc * (np.cbrt(reflection_y * (x_right * horizontal_sc))) + v_translation, lnColor)
    case "reciprocal":
        x_left = np.linspace(-10, -0.1, 400)
        x_right = np.linspace(0.1, 10, 400)
        ax.plot(x_left + h_translation, reflection_x * vertical_sc * (1/(reflection_y * (x_left * horizontal_sc))) + v_translation, lnColor)
        ax.plot(x_right + h_translation, reflection_x * vertical_sc * (1/(reflection_y * (x_right * horizontal_sc))) + v_translation, lnColor)
        plt.axvline(x=h_translation, color="gray", linestyle="--")
        plt.axhline(y=v_translation, color="gray", linestyle="--")
    
print("\033[2J\033[H", end="")

plt.axvline(x=0, color="black")
plt.axhline(y=0, color="black")

plt.xlim(-10 + h_translation, 10 + h_translation)
plt.ylim(-10 + v_translation, 10 + v_translation)
plt.xticks(np.arange(-10 + h_translation, 11 + h_translation, 1))
plt.yticks(np.arange(-10 + v_translation, 11 + v_translation, 1))

plt.grid(True)

plt.savefig("plot.png")