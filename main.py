import csv
import sys
import venn

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn3, venn2_circles
import matplotlib.image as mpimg  # for img reading


def print_menu(file_name):  # print option to start the program.
    print("\nPan genome data analysis and visualization program.")
    print(f"Data file Name: {file_name}")
    print("Option 1 - Print Pan genome data")
    print("Option 2 - Output Venn diagram from all data")
    print("Option 3 - Output Venn diagram from first four person (sort by number of gene from each person)")
    print("Option 4 - Output Venn diagram from second four person (sort by number of gene from each person)")
    print("Option 5 - Output Venn diagram from Third four person (sort by number of gene from each person)")
    print("Option 6 - Output Venn diagram from fourth four person (sort by number of gene from each person)")
    print("Option 7 - Exit program")


def menu():
    choice = input("\nPlease enter your choice (1-7): ")

    print("")
    valid_choices = ['1', '2', '3', '4', '5', '6', '7']

    while 1:
        if choice not in valid_choices:
            print("Please Enter the right choice ! (1,2,3,4,5,6,7)")
            choice = input("\nPlease enter your choice (1-7): ")

        if choice != '7':
            if choice == '1':
                print("Option 1 - Print Pan genome data\n")
                # print(df)
            elif choice == '2':
                print("Option 2 - Output Venn diagram from all data\n")
            elif choice == '3':
                print("Option 3 - Output Venn diagram from first four person (sort by number of gene from each "
                      "person)\n")
            elif choice == '4':
                print("Option 4 - Output Venn diagram from second four person (sort by number of gene from each "
                      "person)\n")
            elif choice == '5':
                print("Option 5 - Output Venn diagram from Third four person (sort by number of gene from each "
                      "person)\n")
            elif choice == '6':
                print("Option 6 - Output Venn diagram from fourth four person (sort by number of gene from each "
                      "person)\n")

            print_menu(FileName)
            choice = input("\nPlease enter your choice (1-7): ")
        elif choice == '7':
            print("Option 7 - Exit program\n")
            sys.exit()


def get_label_dict(col_name: list):
    # generate dataFrame specified by column name
    p_df = pd.read_csv(f"./{FileName}", usecols=col_name)
    text = ""
    g_dict = {}
    for gen_num in range(len(df)):
        for i in p_df.iloc[gen_num]:
            text += f"{i}"

        if g_dict.__contains__(text):
            g_dict[text] += f", g{gen_num + 1}"
        else:
            g_dict[text] = f"g{gen_num + 1}"
        text = ""
    return g_dict


def draw_venn4_by_group(p_cols: list, **opts):
    fig, ax = venn.venn4(get_label_dict(p_cols), names=p_cols)
    fig_name = f"venn_group{opts.get('groupNum', '')}"
    fig.savefig(fig_name, bbox_inches='tight')
    plt.clf()
    # venn_fig = mpimg.imread(fig_name)

    # plt.imshow(venn_fig)  # 显示图片
    plt.axis('off')  # 不显示坐标轴
    # plt.show()


# 从外面传的labelDict是一个[[], [], [], []]，每一个[]是column name，作为一个子图ax，坐标分别是221 222 223 224
def draw_4venn4_together(p_2dlst, **options):
    colors = options.get('colors', [venn.default_colors[i] for i in range(4)])
    figsize = options.get('figsize', (14, 14))
    dpi = options.get('dpi', 96)
    fontsize = options.get('fontsize', 12)

    fig = plt.figure(0, figsize=figsize, dpi=dpi)

    for i in range(len(p_2dlst)):
        # 每一个的idx
        labels = get_label_dict(p_2dlst[i])
        names = p_2dlst[i]

        p_idx = 220 + i + 1

        ax = fig.add_subplot(p_idx, aspect='equal')
        ax.set_axis_off()
        ax.set_ylim(bottom=0.0, top=1.0)
        ax.set_xlim(left=0.0, right=1.0)

        # body
        venn.draw_ellipse(fig, ax, 0.350, 0.400, 0.72, 0.45, 140.0, colors[0])
        venn.draw_ellipse(fig, ax, 0.450, 0.500, 0.72, 0.45, 140.0, colors[1])
        venn.draw_ellipse(fig, ax, 0.544, 0.500, 0.72, 0.45, 40.0, colors[2])
        venn.draw_ellipse(fig, ax, 0.644, 0.400, 0.72, 0.45, 40.0, colors[3])
        venn.draw_text(fig, ax, 0.85, 0.42, labels.get('0001', ''), fontsize=fontsize)
        venn.draw_text(fig, ax, 0.68, 0.72, labels.get('0010', ''), fontsize=fontsize)
        venn.draw_text(fig, ax, 0.77, 0.59, labels.get('0011', ''), fontsize=fontsize)
        venn.draw_text(fig, ax, 0.32, 0.72, labels.get('0100', ''), fontsize=fontsize)
        venn.draw_text(fig, ax, 0.71, 0.30, labels.get('0101', ''), fontsize=fontsize)
        venn.draw_text(fig, ax, 0.50, 0.66, labels.get('0110', ''), fontsize=fontsize)
        venn.draw_text(fig, ax, 0.65, 0.50, labels.get('0111', ''), fontsize=fontsize)
        venn.draw_text(fig, ax, 0.14, 0.42, labels.get('1000', ''), fontsize=fontsize)
        venn.draw_text(fig, ax, 0.50, 0.17, labels.get('1001', ''), fontsize=fontsize)
        venn.draw_text(fig, ax, 0.29, 0.30, labels.get('1010', ''), fontsize=fontsize)
        venn.draw_text(fig, ax, 0.39, 0.24, labels.get('1011', ''), fontsize=fontsize)
        venn.draw_text(fig, ax, 0.23, 0.59, labels.get('1100', ''), fontsize=fontsize)
        venn.draw_text(fig, ax, 0.61, 0.24, labels.get('1101', ''), fontsize=fontsize)
        venn.draw_text(fig, ax, 0.35, 0.50, labels.get('1110', ''), fontsize=fontsize)
        venn.draw_text(fig, ax, 0.50, 0.38, labels.get('1111', ''), fontsize=fontsize)

        # legend
        venn.draw_text(fig, ax, 0.13, 0.18, names[0], colors[0], fontsize=fontsize, ha="right")
        venn.draw_text(fig, ax, 0.18, 0.83, names[1], colors[1], fontsize=fontsize, ha="right", va="bottom")
        venn.draw_text(fig, ax, 0.82, 0.83, names[2], colors[2], fontsize=fontsize, ha="left", va="bottom")
        venn.draw_text(fig, ax, 0.87, 0.18, names[3], colors[3], fontsize=fontsize, ha="left", va="top")
        leg = ax.legend(names, loc='center left', bbox_to_anchor=(1.0, 0.5), fancybox=True)
        leg.get_frame().set_alpha(0.5)

    return fig


if __name__ == '__main__':
    FileName = "p16-G30.csv"
    df = pd.read_csv(f"./{FileName}")

    p_g_lst = []  # [[person#, 携带gene总数],...]
    for idx, person in enumerate(df):
        # 不要gene_name那一列
        if idx == 0:
            continue
        p_lst = [i for i in df[person]]
        p_g_lst.append([person, sum(p_lst)])

    # sort person by gene_num in ↑ order
    p_g_lst.sort(key=lambda x: x[1], reverse=True)

    # 只要column, 每组4个，一共len(p_g_lst)/4组
    p_groups = [[p_g_lst[i + j * 4][0] for i in range(0, 4)] for j in range(0, int(len(p_g_lst) / 4))]
    print("after sorting:")
    print(p_groups)

    # get_label_dict(p_groups[0])
    # testing
    # draw_venn4_by_group(p_groups[0], groupNum=1)
    # draw_venn4_by_group(p_groups[1], groupNum=2)
    # draw_venn4_by_group(p_groups[2], groupNum=3)

    fig_all = draw_4venn4_together(p_groups)

    fig_all.savefig('venn_all.png', bbox_inches='tight')
    venn_fig_all = mpimg.imread('venn_all.png')

    plt.imshow(venn_fig_all)  # 显示图片
    plt.axis('off')  # 不显示坐标轴
