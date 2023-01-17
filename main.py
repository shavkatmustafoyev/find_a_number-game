from user_function import sontop
from pc_function import sontop_pc


def play(x=10):
    yana = 1
    while yana:
        taxminlar_user = sontop(x)
        taxminlar_pc = sontop_pc(x)
        if taxminlar_user > taxminlar_pc:
            print(
                f"Men yutdim! Chunki men sizdan  {taxminlar_user - taxminlar_pc} ta kam taxmin bilan topdim")
        elif taxminlar_user < taxminlar_pc:
            print(
                f"Siz yutdingiz! Chunki siz menda {taxminlar_pc - taxminlar_user} ta kam taxmin qildingiz")
        else:
            print("Durrang! Ikkovimiz bir xil taxminlar bilan topdik sonlar.")
        yana = int(input("Yana o'yin o'ynaysizmi? Ha(1)/Yo'q(0):\n"))


play()
